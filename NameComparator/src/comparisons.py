from re import sub as re_sub
from numpy import ndarray
from numpy import zeros as numpy_zeros
from rapidfuzz.fuzz import ratio as fuzz_ratio
from importlib.resources import files
from json import loads as json_loads

from NameComparator.src.usefulTools import identify_best_matches, find_word_matches_and_quality, round_in_a_normal_way

# Read the various variables from a file
prefix_list = json_loads(files('data').joinpath('possiblePrefixList.json').read_text(encoding='utf-8'))
comparison_variables_as_dict = json_loads(files('data').joinpath('variablesForComparisons.json').read_text(encoding='utf-8'))

max_score: int = comparison_variables_as_dict.get("maxScore")
guaranteed_passing_score: int = comparison_variables_as_dict.get("guaranteedPassingScore")
conditionally_passing_score: int = comparison_variables_as_dict.get("conditionallyPassingScore")
further_checks_needed_score: int = comparison_variables_as_dict.get("furtherChecksNeededScore")
guaranteed_fail_score: int = comparison_variables_as_dict.get("guaranteedFailScore")

fuzzy_comparison_weight: float = comparison_variables_as_dict.get("fuzzyComparisonWeight")
consonant_comparison_weight: float = comparison_variables_as_dict.get("consonantComparisonWeight")

number_of_valid_combos_to_skip_further_checks: int = comparison_variables_as_dict.get("numberOfValidCombosToSkipFurtherChecks")
length_needed_for_conditionally_passing_pronunciation_comparison: int = comparison_variables_as_dict.get("lengthNeededForConditionallyPassingPronunciationComparison")

def compare_spelling(name_one:str, name_two:str) -> tuple[bool, list, float]:
    """Identifies if two names are a match according to a comparison based soley on spelling.

    Args:
        name_one: The first name used in the spelling comparison
        name_two: The second name used in the spelling comparison

    Returns:
        A tuple containing whether or not the names are a match, the resulting word combos, and
        a score representing the average percentage match of the word combos that are considered 
        valid
    """        

    print(f"Comparing spelling for {name_one} and {name_two} in Python")

    word_combos, possible_prefix_count = find_word_matches_and_quality(name_one, name_two)

    print(f"Word combos for compare spelling in Python: {word_combos}")

    count = 0 # Or should this be the number of exceptions? We'll have to find out here soon hahaha
    combined_scores = 0
    averaged_scores = 0

    for tuple in word_combos:
        if tuple[2] >= guaranteed_passing_score:
            count = count + 1
        combined_scores = combined_scores + tuple[2]

    minimum_length = min(len(name_one.split(' ')), len(name_two.split(' ')))

    if len(word_combos) >= 1:
        averaged_scores = combined_scores / len(word_combos)

    if (count >= number_of_valid_combos_to_skip_further_checks) and ((count >= minimum_length - possible_prefix_count)):
        print(f"Determined to return true in Python. Current variables: count - {count} number_of_valid_combos_to_skip_further_checks - {number_of_valid_combos_to_skip_further_checks} minimum_length - {minimum_length} possible_prefix_count - {possible_prefix_count}")
        return True, word_combos, averaged_scores
    
    # Determine if it matches on consonants or not if the whole fuzzy string comparison is unclear
    is_consonant_match, consonant_match_score = _consonant_comparison(name_one, name_two, word_combos, possible_prefix_count)

    # Return the values, averaging the score and slightly favoring the initial fuzzy string match ones
    return is_consonant_match, word_combos, ((averaged_scores * fuzzy_comparison_weight) + (consonant_match_score * consonant_comparison_weight))

def _consonant_comparison(name_one:str, name_two:str, word_combos: list[tuple[str, str, float]], possible_prefix_count: int) -> tuple[bool, float]:
    """Identifies if two names are a match according to consonant comparison and
    determines a score representing how closely the contonants line up according
    to a fuzzy match comparison for all of the accepted word combos.

    Args:
        name_one: The first name used in the consonant comparison
        name_two: The second name used in the consonant comparison
        word_combos: The word combos of the names, as found in compare_spelling
        possible_prefix_count: A count of possible prefixes that we need to consider
            when determining whether or not the names will pass

    Returns:
        A tuple containing a boolean representing whether or not the two names 
        are a match according to consonant comparison and a score representing
        the quality of the matches on average
    """        

    print(f"Comparing consonants for {name_one} and {name_two} in Python")

    # Setup
    minimum_required_matches = len(word_combos) - possible_prefix_count
    number_of_consonant_matches = 0
    combined_scores_based_on_consonant_fuzzy_matches = 0
    average_score = 0
    increase_to_valid_checks_needed_for_skip = 0

    name_one_fragments = name_one.split()
    name_two_fragments = name_two.split()

    print(f"Determined the minimum number of required matches is {minimum_required_matches} in Python")

    # Loop through every word match in the combo
    for tup in word_combos:
        # Get the matching word data
        word_one = name_one_fragments[int(tup[0])]
        word_two = name_two_fragments[int(tup[1])]
        original_score_for_words:int = int(tup[2])

        # Get the words as consonants
        consonants_in_name_one = _reduce_to_simple_consonants(word_one)
        consonants_in_name_two = _reduce_to_simple_consonants(word_two)
        consonant_ratio = round_in_a_normal_way(fuzz_ratio(consonants_in_name_one, consonants_in_name_two))

        print(f"Consonants in each name in Python - name_one: {consonants_in_name_one}  name_two: {consonants_in_name_two}")
        print(f"Consonant ratio in Python: {consonant_ratio}")

        # Continue if bad match or update to be a proper score in certain cases with initials
        if original_score_for_words <= guaranteed_fail_score:
            print("Below guaranteed fail score in Python")
            continue
        elif (len(word_one) == 1 and word_one == word_two[0]) or (len(word_two) == 1 and word_two == word_one[0]):
                print("Updated consonant ratio due to initials in Python")
                consonant_ratio = 80
        if (((consonant_ratio < guaranteed_passing_score) or (original_score_for_words < further_checks_needed_score)) and (consonant_ratio != max_score)):
            print(f"Failed big check in Python where consonant_ratio = {consonant_ratio}, guaranteed_passing_score = {guaranteed_passing_score}, original_score_for_words = {original_score_for_words}, further_checks_needed_score = {further_checks_needed_score}, and max_score = {max_score}")
            continue

        # If not rejected, increment the number of matches and increase the total score
        number_of_consonant_matches += 1
        combined_scores_based_on_consonant_fuzzy_matches = combined_scores_based_on_consonant_fuzzy_matches + consonant_ratio

        increase_to_valid_checks_needed_for_skip = _increment_valid_checks_needed_for_skip_if_appropriate(word_one, word_two, increase_to_valid_checks_needed_for_skip)

    # Find the average score of all of the matches, if relevant
    if number_of_consonant_matches > 0:
        average_score = combined_scores_based_on_consonant_fuzzy_matches / number_of_consonant_matches

    # If there are enough matches, return true and a score. Otherwise return false and a score
    print(f"Number of consonant matches in Python: {number_of_consonant_matches}")
    print(f"Result of consonant comparison in Python {((number_of_consonant_matches >= minimum_required_matches) or ((number_of_consonant_matches >= number_of_valid_combos_to_skip_further_checks) and (name_one_fragments[0] == name_two_fragments[0]))), average_score}")
    return (((number_of_consonant_matches >= minimum_required_matches) or ((number_of_consonant_matches >= number_of_valid_combos_to_skip_further_checks + increase_to_valid_checks_needed_for_skip) and (name_one_fragments[0] == name_two_fragments[0]))), average_score)
    
def _increment_valid_checks_needed_for_skip_if_appropriate(word_one: str, word_two: str, increase_to_valid_checks_needed_for_skip: int) -> int:
    """This is a helper function that's designed to modify the number of valid segments needed to skip a few checks.
    If the name is a prefix that's floating AND is in both names, we want to note that and increase the number of
    valid combos to skip further checks. This ensures that what's supposed to be one complete name or surname is 
    not considered several when we're determining if the names are a match.

    Args:
        word_one: The first word (or name segment) to check for a prefix in
        word_two: The second word (or name segment) to check for a prefix in
        increase_to_valid_checks_needed_for_skip: The current value that needs to be applied to the number of
            valid segments that are needed to skip some checks later on

    Returns:
        A number that's incremented to be larger if both word one and word two contain the same prefix
    """
    if (word_one in prefix_list) and (word_one == word_two):
        increase_to_valid_checks_needed_for_skip = increase_to_valid_checks_needed_for_skip + 1

    return increase_to_valid_checks_needed_for_skip

def _reduce_to_simple_consonants(string:str) -> str:
    """Reduces a string to its simple consonant componants.

    Args:
        string: The string we want to reduce

    Returns:
        A string containing only the consonants of the original string, separated
        by asterisks
    """            
    string = re_sub(r"a|e|i|o|u|y", "*", string)
    string = re_sub(r'\*{2,}', "*", string)
    string = re_sub(r'(.)\1+', r'\1', string)
    return string

def pronunciation_comparison(ipa_of_name_one:str, ipa_of_name_two:str, name_one:str, name_two:str) -> tuple[bool, list, float]:
    """Identifies whether two names are a match according to a pronunciation comparison.

    Args:
        ipa_of_name_one: The ipa of the first name to compare the pronuncation of
        ipa_of_name_two: The ipa of the second name to compare the pronuncation of
        name_one: The first name to compare the pronuncation of
        name_two: The second name to compare the pronuncation of
        
    Returns:
        A tuple containing whether or not the name was a match, the word combos for the
        names, and the score of the item used to determine if it was a match or not
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
    word_combos_for_scores, possible_prefix_count = find_word_matches_and_quality(name_one, name_two)
    _matchup_scores(word_combos_for_scores, scores, words_from_ipa_one, words_from_ipa_two)

    # Identify the best matchups
    words_from_ipa_one = [str(i) if word is not None else None for i, word in enumerate(words_from_ipa_one)]
    words_from_ipa_two = [str(i) if word is not None else None for i, word in enumerate(words_from_ipa_two)]
    word_combos = identify_best_matches(scores=scores, list_one=words_from_ipa_one, list_two=words_from_ipa_two)
    # This defaults the minimum score to 0 if there is no real minimum score, or sets it to the smalles one otherwise
    lowest_score = min(word_combos, key=lambda tuple: tuple[2])[2] if min(word_combos, key=lambda tuple: tuple[2])[2] else 0
    
    # Return whether pronunciaion match or not
    minimum_length = min(len(ipa_of_name_one.split()), len(ipa_of_name_two.split()))
    if minimum_length < length_needed_for_conditionally_passing_pronunciation_comparison:
        if lowest_score >= guaranteed_passing_score:
            return True, word_combos, lowest_score
        return False, word_combos, lowest_score
    if minimum_length >= length_needed_for_conditionally_passing_pronunciation_comparison:
        if lowest_score >= conditionally_passing_score:
            return True, word_combos, lowest_score
        return False, word_combos, lowest_score
    
    # Default return just in case something gets here
    return False, word_combos, lowest_score

def _matchup_scores(word_combos_for_scores: list[tuple[str, str, float]], scores: ndarray, words_from_ipa_one: list, words_from_ipa_two: list) -> None:
    """Finds the score for the quality of each matchup of words that are potential matches, in terms of ipa
    pronunciations. It then updates a list of scores to reflect this for later processing in the
    pronunciation_comparison function.
    
    Args:
        word_combos_for_scores: A list of word combinations that need to be scored
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
            score = _score_word_combos_helper(word_one, word_two, index_one, index_two, word_combos_for_scores)
            scores[index_one, index_two] = score

def _score_word_combos_helper(word_one: str, word_two: str, index_one: int, index_two: int, word_combos_for_scores: list[tuple[str, str, float]]) -> float:
    """This function is a helper function to reduce the nesting depth of _matchup_scores.
    What it does is it compares all of the scores for a word combo and then finds a score
    that is going to be more accurate for them, as opposed to a default score.
    
    Args:
        word_one: The first word that needs a scoring comparison
        word_two: The second word, that needs to be compared to the first word for a score
        index_one: The index of the first word
        index_two: The index of the second word
        word_combos_for_scores: A list of word combinations that need to be scored

    Returns:
        An int representing the score that should be set for a particular word combo
    """

    score = fuzz_ratio(word_one, word_two)
    for item in range(len(word_combos_for_scores)):
        word_combos_for_scores_index_one, word_combos_for_scores_index_two, initial_score = word_combos_for_scores[item]
        # Use initial score for initials (bad pun)
        if index_one == int(word_combos_for_scores_index_one) and index_two == int(word_combos_for_scores_index_two) and (initial_score == 100 or initial_score == 0):
            score = initial_score

    return score