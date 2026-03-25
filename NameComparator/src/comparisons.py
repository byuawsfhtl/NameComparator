from re import sub as re_sub
from numpy import ndarray
from numpy import zeros as numpy_zeros
from fuzzywuzzy.fuzz import ratio as fuzz_ratio

from NameComparator.src.usefulTools import identify_best_matches, find_word_matches_and_quality

def compare_spelling(name_one:str, name_two:str) -> tuple[bool, list]:
    """Identifies if two names are a match according to a comparison based soley on spelling.

    Args:
        name_one: The first name used in the spelling comparison
        name_two: The second name used in the spelling comparison

    Returns:
        A tuple containing whether the names are a match and the resulting word combo
    """        
    word_combo = find_word_matches_and_quality(name_one, name_two)
    count = sum(1 for tup in word_combo if tup[2] > 80)
    minimum_length = min(len(name_one.split(' ')), len(name_two.split(' ')))
    if (count >= 3) or (count == minimum_length):
        return True, word_combo
    if _consonant_comparison(name_one, name_two):
        return True, word_combo
    return False, word_combo

def _consonant_comparison(name_one:str, name_two:str) -> bool:
    """Identifies if two names are a match according to consonant comparison.

    Args:
        name_one: The first name used in the consonant comparison
        name_two: The second name used in the consonant comparison

    Returns:
        A boolean representing whether the two names are a match, according 
        to consonant comparison
    """        
    # Setup
    word_combo = find_word_matches_and_quality(name_one, name_two)
    minimum_required_matches = len(word_combo)
    number_of_consonant_matches = 0

    # Loop through every word match in the combo
    for tup in word_combo:
        # Get the matching word data
        word_one = name_one.split()[int(tup[0])]
        word_two = name_two.split()[int(tup[1])]
        original_score_for_words:int = int(tup[2])

        # Get the words as consonants
        consonants_in_name_one = _reduce_to_simple_consonants(word_one)
        consonants_in_name_two = _reduce_to_simple_consonants(word_two)
        consonant_ratio = fuzz_ratio(consonants_in_name_one, consonants_in_name_two)

        # Continue if bad match
        if original_score_for_words <= 30:
            continue
        if (len(word_one) != 1) and (len(word_two) != 1): # If neither word is an initial
            lowest_syllable_count = min(consonants_in_name_one.count("*"), consonants_in_name_two.count("*"))
            if lowest_syllable_count < 2:
                continue
        if (consonant_ratio <= 80 or original_score_for_words <= 60) and consonant_ratio != 100:
            continue

        # If not rejected, increment the number of matches
        number_of_consonant_matches += 1

    # If enough matches, return true. Otherwise return false.
    return (number_of_consonant_matches > minimum_required_matches) or (number_of_consonant_matches >= 3)
    
def _reduce_to_simple_consonants(string:str) -> str:
    """Reduces a string to its simple consonant componants.

    Args:
        string: The string we want to reduce

    Returns:
        A string containing only the consonants of the original string, separated
        by asterisks
    """            
    string = re_sub("a|e|i|o|u|y", "*", string)
    string = re_sub(r'\*{2,}', "*", string)
    string = re_sub(r'(.)\1+', r'\1', string)
    return string

def pronunciation_comparison(ipa_of_name_one:str, ipa_of_name_two:str, name_one:str, name_two:str) -> tuple[bool, list]:
    """Identifies whether two names are a match according to a pronunciation comparison.

    Args:
        ipa_of_name_one: The ipa of the first name to compare the pronuncation of
        ipa_of_name_two: The ipa of the second name to compare the pronuncation of
        name_one: The first name to compare the pronuncation of
        name_two: The second name to compare the pronuncation of
        
    Returns:
        A tuple containing whether or not the name was a match and the word combo
    """        
    # Initialize empty list to store scores
    words_from_ipa_one = ipa_of_name_one.split()
    words_from_ipa_two = ipa_of_name_two.split()
    if len(words_from_ipa_one) < len(words_from_ipa_two):
        words_from_ipa_one += [None] * (len(words_from_ipa_two) - len(words_from_ipa_one))
    elif len(words_from_ipa_one) > len(words_from_ipa_two):
        words_from_ipa_two += [None] * (len(words_from_ipa_one) - len(words_from_ipa_two))

    # Create a matrix of zeros using numpy
    scores = numpy_zeros((len(words_from_ipa_one), len(words_from_ipa_two)))

    # Score each matchup
    word_combo_for_scores = find_word_matches_and_quality(name_one, name_two)
    _matchup_scores(word_combo_for_scores, scores, words_from_ipa_one, words_from_ipa_two)

    # Identify the best matchups
    words_from_ipa_one = [str(i) if word is not None else None for i, word in enumerate(words_from_ipa_one)]
    words_from_ipa_two = [str(i) if word is not None else None for i, word in enumerate(words_from_ipa_two)]
    word_combo = identify_best_matches(scores=scores, list_one=words_from_ipa_one, list_two=words_from_ipa_two)
    lowest_score = min(word_combo, key=lambda tuple: tuple[2])[2]
    
    # Return whether pronunciaion match or not
    minimum_length = min(len(ipa_of_name_one.split()), len(ipa_of_name_two.split()))
    if minimum_length <= 2:
        if lowest_score >= 80:
            return True, word_combo
        return False, word_combo
    if minimum_length > 2:
        if lowest_score > 75:
            return True, word_combo
        return False, word_combo
    
    # Default return just in case something gets here
    return False, word_combo

def _matchup_scores(word_combo_for_scores: list[tuple[str, str, int]], scores: ndarray, words_from_ipa_one: list, words_from_ipa_two: list) -> None:
    """Finds the score for the quality of each matchup of words that are potential matches, in terms of ipa
    pronunciations. It then updates a list of scores to reflect this for later processing in the
    pronunciation_comparison function.
    
    Args:
        word_combo_for_scores: A list of word combinations that need to be scored
        scores: A list of scores for all of the different word combinations
        words_from_ipa_one: A list of words that could match the ipa pronuncation of the first checked word
        words_from_ipa_two: A list of words that could match the ipa pronuncation of the second checked word
    """
    for index_one, word_one in enumerate(words_from_ipa_one):
        for index_two, word_two in enumerate(words_from_ipa_two):
            # Assign a default very low score for dummy pairings
            scores[index_one, index_two] = -1e9 
            
            if (word_one is None) or (word_two is None):
                continue
            # Reassign the default score to all real pairings
            score = _score_word_combos_helper(word_one, word_two, index_one, index_two, word_combo_for_scores)
            scores[index_one, index_two] = score

def _score_word_combos_helper(word_one: str, word_two: str, index_one: int, index_two: int, word_combo_for_scores: list[tuple[str, str, int]]) -> int:
    """This function is a helper function to reduce the nesting depth of _matchup_scores.
    What it does is it compares all of the scores for a word combo and then finds a score
    that is going to be more accurate for them, as opposed to a default score.
    
    Args:
        word_one: The first word that needs a scoring comparison
        word_two: The second word, that needs to be compared to the first word for a score
        index_one: The index of the first word
        index_two: The index of the second word
        word_combo_for_scores: A list of word combinations that need to be scored

    Returns:
        An int representing the score that should be set for a particular word combo
    """

    score = fuzz_ratio(word_one, word_two)
    for item in range(len(word_combo_for_scores)):
        word_combo_for_scores_index_one, word_combo_for_scores_index_two, initial_score = word_combo_for_scores[item]
        # Use initial score for initials (bad pun)
        if index_one == int(word_combo_for_scores_index_one) and index_two == int(word_combo_for_scores_index_two) and (initial_score == 100 or initial_score == 0):
            score = initial_score

    return score