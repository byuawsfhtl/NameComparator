import re
from HungarianScorer.HungarianScorer import HungarianScorer
from fuzzywuzzy import fuzz

import NameComparator.src.modify as modifyMod
import NameComparator.src.ipa as ipaMod
import NameComparator.src.usefulTools as usefulToolsMod

def spelling_comparison(name_a: str, name_b: str) -> tuple[bool, list]:
    """Identifies if two names are a match according to a comparison based soley on spelling.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        tuple[bool, list]: whether the names are a match, and the resulting word combo
    """        
    all_matchups = usefulToolsMod.find_which_words_match_and_how_well(name_a, name_b)
    count = sum(1 for matchup in all_matchups if matchup.score > 80)
    min_length = min(len(name_a.split()), len(name_b.split()))
    if (count >= 3) or (count == min_length):
        return True, all_matchups
    if _consonant_comparison(name_a, name_b):
        return True, all_matchups
    return False, all_matchups

def _consonant_comparison(name_a: str, name_b: str) -> bool:
    """Identifies if two names are a match according to consonant comparison.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        bool: whether the two names are a match according to consonant comparison
    """        
    # Setup
    all_matchups = usefulToolsMod.find_which_words_match_and_how_well(name_a, name_b)
    min_required_matches = len(all_matchups)
    num_word_consonant_matches = 0

    # Loop through every word match in the combo
    for matchup in all_matchups:
        # Get the matching word data
        word_a = matchup.word_in_name_a.string
        word_b = matchup.word_in_name_b.string
        original_matchup_score = matchup.score

        # Get the words as consonants
        consonants_name_a = _reduce_to_simple_consonants(word_a)
        consonants_name_b = _reduce_to_simple_consonants(word_b)
        consonants_ratio = fuzz.ratio(consonants_name_a, consonants_name_b)

        # Continue if bad match
        if original_matchup_score <= 30:
            continue
        if (len(word_a) != 1) and (len(word_b) != 1): #if neither word is initial
            lowest_syllable_count = min(consonants_name_a.count("*"), consonants_name_b.count("*"))
            if lowest_syllable_count < 2:
                continue
        if (consonants_ratio <= 80 or original_matchup_score <= 60) and consonants_ratio != 100:
            continue

        # If not rejected, increment the number of matches
        num_word_consonant_matches += 1

    # If enough matches, return true. Otherwise return false.
    if (num_word_consonant_matches > min_required_matches) or (num_word_consonant_matches >= 3):
        return True
    return False
    
def _reduce_to_simple_consonants(string: str) -> str:
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


def score_words(word_a: str, word_b: str):
    if len(word_a) == 1:
        return 100 if word_b.startswith(word_a) else 0
    if len(word_b) == 1:
        return 100 if word_a.startswith(word_b) else 0
    ipa_word_a = ipaMod.get_ipa_of_one_word(word_a)
    ipa_word_b = ipaMod.get_ipa_of_one_word(word_b)
    ipa_word_a, ipa_word_b = modifyMod.modify_ipas_together(ipa_word_a, ipa_word_b)
    return fuzz.ratio(ipa_word_a, ipa_word_b)


def pronunciation_comparison(name_a: str, name_b: str) -> tuple[bool, list]:
    """Identifies whether two names are a match according to a pronunciation comparison.
     
    Args:
        ipa_of_name_a: the ipa of a name
        ipa_of_name_b: the ipa of a name
        name_a: the name of a person
        name_b: the name of a person
             
    Returns:
        whether the name was a match, and the word combo
    """
    # Use HungarianScorer to find optimal assignment
    optimal_combo = HungarianScorer.getBestComboAsIndices(name_a.split(), name_b.split(), score_words)
    if not optimal_combo:
        return False, []
    
    # Find the lowest score from the optimal assignment
    lowest_score = min(optimal_combo, key=lambda tuple: tuple[2])[2]

    # Determine if it's a match based on thresholds
    min_length = min(len(name_a.split()), len(name_b.split()))
    
    if min_length <= 2:
        is_match = lowest_score >= 80
    else:
        is_match = lowest_score > 75
        
    return is_match, optimal_combo