import re
import numpy as np
from fuzzywuzzy import fuzz

import NameComparator.src.usefulTools as usefulToolsMod

def compare_spelling(name_one:str, name_two:str) -> tuple[bool, list]:
    """Identifies if two names are a match according to a comparison based soley on spelling.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[bool, list]: whether the names are a match, and the resulting word combo
    """        
    word_combo = usefulToolsMod.find_word_matches_and_quality(name_one, name_two)
    count = sum(1 for tup in word_combo if tup[2] > 80)
    minimum_length = min(len(name_one.split()), len(name_two.split()))
    if (count >= 3) or (count == minimum_length):
        return True, word_combo
    if _consonant_comparison(name_one, name_two):
        return True, word_combo
    return False, word_combo

def _consonant_comparison(name_one:str, name_two:str) -> bool:
    """Identifies if two names are a match according to consonant comparison.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        bool: whether the two names are a match according to consonant comparison
    """        
    # Setup
    word_combo = usefulToolsMod.find_word_matches_and_quality(name_one, name_two)
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
        consonant_ratio = fuzz.ratio(consonants_in_name_one, consonants_in_name_two)

        # Continue if bad match
        if original_score_for_words <= 30:
            continue
        if (len(word_one) != 1) and (len(word_two) != 1): #if neither word is initial
            lowest_syllable_count = min(consonants_in_name_one.count("*"), consonants_in_name_two.count("*"))
            if lowest_syllable_count < 2:
                continue
        if (consonant_ratio <= 80 or original_score_for_words <= 60) and consonant_ratio != 100:
            continue

        # If not rejected, increment the number of matches
        number_of_consonant_matches += 1

    # If enough matches, return true. Otherwise return false.
    if (number_of_consonant_matches > minimum_required_matches) or (number_of_consonant_matches >= 3):
        return True
    return False
    
def _reduce_to_simple_consonants(string:str) -> str:
    """Reduces a string to the simple consonant componants.

    Args:
        string (str): a string

    Returns:
        str: the consonant componants
    """            
    string = re.sub("a|e|i|o|u|y", "*", string)
    string = string.replace("**", "*")
    string = re.sub(r'(.)\1+', r'\1', string)
    return string

def pronunciation_comparison(ipa_of_name_one:str, ipa_of_name_two:str, name_one:str, name_two:str) -> tuple[bool, list]:
    """Identifies whether two names are a match according to a pronunciation comparison.

    Args:
        ipa_of_name_one (str): the ipa of a name
        ipa_of_name_two (str): the ipa of a name
        name_one (str): a name
        name_two (str): a name
        
    Returns:
        tuple[bool, list]: whether the name was a match, and the word combo
    """        
    # Initialize empty list to store scores
    words_from_ipa_one = ipa_of_name_one.split()
    words_from_ipa_two = ipa_of_name_two.split()
    if len(words_from_ipa_one) < len(words_from_ipa_two):
        words_from_ipa_one += [None] * (len(words_from_ipa_two) - len(words_from_ipa_one))
    elif len(words_from_ipa_one) > len(words_from_ipa_two):
        words_from_ipa_two += [None] * (len(words_from_ipa_one) - len(words_from_ipa_two))
    scores = np.zeros((len(words_from_ipa_one), len(words_from_ipa_two)))

    # Score each matchup
    word_combo = usefulToolsMod.find_word_matches_and_quality(name_one, name_two)
    for index_one, word_one in enumerate(words_from_ipa_one):
        for index_two, word_two in enumerate(words_from_ipa_two):
            # Assign a default very low score for dummy pairings
            scores[index_one, index_two] = -1e9 
            if (word_one is None) or (word_two is None):
                continue
            # Reassign the default score to all real pairings
            score = fuzz.ratio(word_one, word_two)
            for item in range(len(word_combo)):
                word_combo_index_one, word_combo_index_two, initial_score = word_combo[item]
                # Use initial score for initials (bad pun)
                if index_one == int(word_combo_index_one) and index_two == int(word_combo_index_two) and (initial_score == 100 or initial_score == 0):
                    score = initial_score
            scores[index_one, index_two] = score

    # Identify the best matchups
    words_from_ipa_one = [str(i) if word is not None else None for i, word in enumerate(words_from_ipa_one)]
    words_from_ipa_two = [str(i) if word is not None else None for i, word in enumerate(words_from_ipa_two)]
    word_combo = usefulToolsMod.identify_best_matches(scores=scores, list_one=words_from_ipa_one, list_two=words_from_ipa_two)
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