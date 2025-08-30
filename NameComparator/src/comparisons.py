import re
import numpy as np
from fuzzywuzzy import fuzz

import NameComparator.src.usefulTools as usefulToolsMod

def spelling_comparison(name_a : str, name_b : str) -> tuple[bool, list]:
    """Identifies if two names are a match according to a comparison based soley on spelling.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        tuple[bool, list]: whether the names are a match, and the resulting word combo
    """        
    word_combo = usefulToolsMod.find_which_words_match_and_how_well(name_a, name_b)
    count = sum(1 for tup in word_combo if tup[2] > 80)
    min_length = min(len(name_a.split()), len(name_b.split()))
    if (count >= 3) or (count == min_length):
        return True, word_combo
    if _consonant_comparison(name_a, name_b):
        return True, word_combo
    return False, word_combo

def _consonant_comparison(name_a : str, name_b : str) -> bool:
    """Identifies if two names are a match according to consonant comparison.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        bool: whether the two names are a match according to consonant comparison
    """        
    # Setup
    word_combo = usefulToolsMod.find_which_words_match_and_how_well(name_a, name_b)
    min_required_matches = len(word_combo)
    num_word_consonant_matches = 0

    # Loop through every word match in the combo
    for tup in word_combo:
        # Get the matching word data
        wordA = name_a.split()[int(tup[0])]
        wordB = name_b.split()[int(tup[1])]
        original_score_for_words:int = int(tup[2])

        # Get the words as consonants
        consonants_name_a = _reduce_to_simple_consonants(wordA)
        consonants_name_b = _reduce_to_simple_consonants(wordB)
        consonants_ratio = fuzz.ratio(consonants_name_a, consonants_name_b)

        # Continue if bad match
        if original_score_for_words <= 30:
            continue
        if (len(wordA) != 1) and (len(wordB) != 1): #if neither word is initial
            lowest_syllable_count = min(consonants_name_a.count("*"), consonants_name_b.count("*"))
            if lowest_syllable_count < 2:
                continue
        if (consonants_ratio <= 80 or original_score_for_words <= 60) and consonants_ratio != 100:
            continue

        # If not rejected, increment the number of matches
        num_word_consonant_matches += 1

    # If enough matches, return true. Otherwise return false.
    if (num_word_consonant_matches > min_required_matches) or (num_word_consonant_matches >= 3):
        return True
    return False
    
def _reduce_to_simple_consonants(string : str) -> str:
    """Reduces a string to the simple consonant componants.

    Args:
        string: a string

    Returns:
        the consonant componants
    """            
    string = re.sub("a|e|i|o|u|y", "*", string)
    string = string.replace("**", "*")
    string = re.sub(r'(.)\1+', r'\1', string)
    return string

def pronunciation_comparison(ipa_of_name_a : str, ipa_of_name_b : str, nameA : str, nameB : str) -> tuple[bool, list]:
    """Identifies whether two names are a match according to a pronunciation comparison.

    Args:
        ipa_of_name_a: the ipa of a name
        ipa_of_name_b: the ipa of a name
        name_a: the name of a person
        name_b: the name of a person
        
    Returns:
        whether the name was a match, and the word combo
    """        
    # Initialize empty list to store scores
    ipa_words_a = ipa_of_name_a.split()
    ipa_words_b = ipa_of_name_b.split()
    if len(ipa_words_a) < len(ipa_words_b):
        ipa_words_a += [None] * (len(ipa_words_b) - len(ipa_words_a))
    elif len(ipa_words_a) > len(ipa_words_b):
        ipa_words_b += [None] * (len(ipa_words_a) - len(ipa_words_b))
    scores = np.zeros((len(ipa_words_a), len(ipa_words_b)))

    # Score each matchup
    word_combo = usefulToolsMod.find_which_words_match_and_how_well(nameA, nameB)
    for index_a, word_a in enumerate(ipa_words_a):
        for index_b, word_b in enumerate(ipa_words_b):
            # Assign a default very low score for dummy pairings
            scores[index_a, index_b] = -1e9 
            if (word_a is None) or (word_b is None):
                continue
            # Reassign the default score to all real pairings
            score = fuzz.ratio(word_a, word_b)
            for item in range(len(word_combo)):
                index_x, index_y, initial_score = word_combo[item]
                # Use initial score for initials (bad pun)
                if index_a == int(index_x) and index_b == int(index_y) and (initial_score == 100 or initial_score == 0):
                    score = initial_score
            scores[index_a, index_b] = score

    # Identify the best matchups
    ipa_words_a = [str(i) if word is not None else None for i, word in enumerate(ipa_words_a)]
    ipa_words_b = [str(i) if word is not None else None for i, word in enumerate(ipa_words_b)]
    word_combo = usefulToolsMod.identify_best_matchups(scores=scores, list_a=ipa_words_a, list_b=ipa_words_b)
    lowest_score = min(word_combo, key=lambda tuple: tuple[2])[2]
    
    # Return whether pronunciaion match or not
    min_length = min(len(ipa_of_name_a.split()), len(ipa_of_name_b.split()))
    if min_length <= 2:
        if lowest_score >= 80:
            return True, word_combo
        return False, word_combo
    if min_length > 2:
        if lowest_score > 75:
            return True, word_combo
        return False, word_combo