import re
from functools import lru_cache
from fuzzywuzzy import fuzz

import NameComparator.src.usefulTools as usefulToolsMod
import NameComparator.data.rules.rulesSpelling as rulesSpelling
import NameComparator.data.rules.rulesIpa as rulesIpa

def modify_names_together(name_a: str, name_b: str) -> tuple[str,str]:
    """Modifies the name together (changing them in a way that is much more intense than simply cleaning together).

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        the modified names
    """        
    name_a = re.sub(r'ie\b', 'y', name_a)
    name_b = re.sub(r'ie\b', 'y', name_b)
    name_a, name_b = _remove_or_in_names(name_a, name_b)
    name_a, name_b = _fix_vowel_mistakes(name_a, name_b)
    name_a, name_b = _fix_swapped_chars(name_a, name_b)
    name_a, name_b = _deal_with_wrong_first_char(name_a, name_b)
    for meat_option_1, meat_option_2, bottom_breads, top_breads, min_letters in rulesSpelling.data:
        name_a, name_b = use_sandwhich_patterns_on_all_words(name_a, name_b, meat_option_1, meat_option_2, bottom_breads, top_breads, min_letters)
    name_a = re.sub(r'\s+', ' ', name_a)
    name_b = re.sub(r'\s+', ' ', name_b)
    name_a = name_a.strip()
    name_b = name_b.strip()
    return name_a, name_b

def _remove_or_in_names(name_a: str, name_b: str) -> tuple[str, str]:
    """Removes the word 'or' from a name (assuming that the name could have been 
    poorly indexed so that the indexer's guesses for a specific word of the name is still within the string).

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        the modified names
    """        
    if (not name_a) or (not name_b):
        return name_a, name_b
    name_a = name_a.strip()
    name_b = name_b.strip()
    name_a, name_b = name_a.lower(), name_b.lower()

    # if or in neither
    if (not " or " in name_a) and (not " or " in name_b):
        return name_a, name_b
    
    # if or in both
    elif (" or " in name_a) and (" or " in name_b):
        return name_a, name_b

    # if or in nameA and not nameB
    elif " or " in name_a:
        # Gets the score for if the word before 'or' is removed
        right_name_a = re.sub("[a-z]+ or ", " ", name_a)
        if not right_name_a:
            right_name_a = '_'
        right_word_combo = usefulToolsMod.find_which_words_match_and_how_well(right_name_a, name_b)
        right_average_score = sum(matchup.score for matchup in right_word_combo) / len(right_word_combo)
        # Gets the score for if the word after 'or' is removed
        left_name_a = re.sub(" or [a-z]+", " ", name_a)
        if not left_name_a:
            left_name_a = '_'
        left_word_combo =  usefulToolsMod.find_which_words_match_and_how_well(left_name_a, name_b)
        left_average_score = sum(matchup.score for matchup in left_word_combo) / len(left_word_combo)
        # Return the higher one
        if right_average_score >= left_average_score:
            return right_name_a, name_b
        return left_name_a, name_b
    
    # if or in nameB and not nameA
    elif " or " in name_b:
        right_name_b = re.sub("[a-z]+ or ", " ", name_b)
        if not right_name_b:
            right_name_b = '_'
        right_word_combo = usefulToolsMod.find_which_words_match_and_how_well(right_name_b, name_a)
        right_average_score = sum(matchup.score for matchup in right_word_combo) / len(right_word_combo)
        # Gets the score for if the word after 'or' is removed
        left_name_b = re.sub(" or [a-z]+", " ", name_b)
        if not left_name_b:
            left_name_b = '_'
        left_word_combo =  usefulToolsMod.find_which_words_match_and_how_well(left_name_b, name_a)
        left_average_score = sum(matchup.score for matchup in left_word_combo) / len(left_word_combo)
        # Return the higher one
        if right_average_score >= left_average_score:
            return name_a, right_name_b
        return name_a, left_name_b

def _fix_vowel_mistakes(name_a: str, name_b: str) -> tuple[str, str]:
    """Modifies two matching words in a name so that they are the same if 
    they are only different by one vowel and 5 letters or more.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        the two modified names
    """        
    ne = usefulToolsMod.NameEditor(name_a, name_b)
    for matchup in usefulToolsMod.find_which_words_match_and_how_well(name_a, name_b):
        # Unpack
        index_a = matchup.word_in_name_a.index
        word_a = matchup.word_in_name_a.string
        word_b = matchup.word_in_name_b.string

        # Continue if either word is less than 5 chars or not same length
        len_a = len(word_a)
        len_b = len(word_b)
        if len_a < 5:
            continue
        if len_b < 5:
            continue
        if len_a != len_b:
            continue

        # Check if there is only one difference
        mismatched_index = None
        too_many_diffs = False
        for i in range(len_a):
            if word_a[i] == word_b[i]:
                continue
            if mismatched_index:
                too_many_diffs = True
                break
            mismatched_index = i
        
        # Continue if there was not exactly one difference
        if (too_many_diffs) or (mismatched_index is None):
            continue

        # Replace one of the letters to be the other if they are cooresponding
        char_word_a = word_a[mismatched_index]
        char_word_b = word_b[mismatched_index]
        cooresponding = ['ao', 'ea', 'iy']
        if (f'{char_word_a}{char_word_b}' in cooresponding) or (f'{char_word_b}{char_word_a}' in cooresponding):
            ne.update_name_a(index_a, word_b)
    
    # Return the modified (or not) names
    return ne.get_modified_names()

def _fix_swapped_chars(name_a: str, name_b: str) -> tuple[str, str]:
    """If two matching words (of 5 letters of more) for the two names are the same barring swapped letters (typo), makes the words the same.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        the modified names
    """        
    ne = usefulToolsMod.NameEditor(name_a, name_b)
    for matchup in usefulToolsMod.find_which_words_match_and_how_well(name_a, name_b):
        # Unpack
        index_a = matchup.word_in_name_a.index
        word_a = matchup.word_in_name_a.string
        word_b = matchup.word_in_name_b.string

        # Skip if the words are not 5 long, are different length, or not fuzzy 80
        if len(word_a) != 5:
            continue
        if len(word_a) != len(word_b):
            continue
        if fuzz.ratio(word_b, word_a) != 80:
            continue

        # Find how many differences and where
        diff_count = 0
        diff_positions = []
        for i in range(len(word_a)):
            if word_a[i] != word_b[i]:
                diff_count += 1
                diff_positions.append(i)
        
        # Skip if there are not two differences, differences are not sequential, or not swappable
        if diff_count != 2:
            continue
        pos_i, pos_j = diff_positions
        if abs(pos_i - pos_j) != 1:
            continue
        if (word_a[pos_i] != word_b[pos_j]) or (word_a[pos_i] != word_b[pos_j]):
            continue

        # This is the scenerio we are looking for. Make the words identical
        ne.update_name_a(index_a, word_b)
    
    # Return the modified (or not) names
    return ne.get_modified_names()

def _deal_with_wrong_first_char(name_a: str, name_b: str) -> tuple[str, str]:
    """If two matching words (of 5 letters or more) are the same barring the first letter, makes the same.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        the modified names
    """        
    ne = usefulToolsMod.NameEditor(name_a, name_b)
    for matchup in usefulToolsMod.find_which_words_match_and_how_well(name_a, name_b):
        index_a = matchup.word_in_name_a.index
        word_a = matchup.word_in_name_a.string
        word_b = matchup.word_in_name_b.string
        if word_a == word_b:
            continue
        if (word_a[1:] == word_b[1:]) and (len(word_a) > 4) and (len(word_b) > 4):
            ne.update_name_a(index_a, word_b)
    name_a, name_b = ne.get_modified_names()
    return name_a, name_b

def use_sandwhich_patterns_on_all_words(name_a: str, name_b: str, meat_option_x: str, meat_option_y: str, bottom_bread_options: frozenset[str], top_bread_options: frozenset[str], min_required_letters:int) -> tuple[str,str]:
    """For any given matching word pair, replaces a specific substring in one of the words, with a similar substring found in the other word.

    Args:
        name_a: the name of a person
        name_b: the name of a person
        meat_option_x: the first possible middle of the substring
        meat_option_y: the second possible middle of the substring
        bottom_bread_options (list[str]): a list of possible beginnings to the substring. Whichever beginning is found in the one must be found in the other in order for the replacement to work
        top_bread_options (list[str]): a list of possible endings to the substring. Whichever ending is found in the one must be found in the other in order for the replacement to work
        min_required_letters (int): the minimum required letters to be found in both words in order for the replacement to work

    Returns:
        the modified names
    """        
    # Return if both middles not in different words
    if (meat_option_x not in name_a and meat_option_y not in name_a) or (meat_option_x not in name_b and meat_option_y not in name_b):
        return name_a, name_b

    ne = usefulToolsMod.NameEditor(name_a, name_b)
    for matchup in usefulToolsMod.find_which_words_match_and_how_well(name_a, name_b):
        # Unpack
        index_a = matchup.word_in_name_a.index
        index_b = matchup.word_in_name_b.index
        word_a = matchup.word_in_name_a.string
        word_b = matchup.word_in_name_b.string

        # Skip words that are not long enough for the given rule
        if len(word_a) < min_required_letters or len(word_b) < min_required_letters:
            continue

        # Update the words according to spelling rules
        updated_word_a, updated_word_b = _sandwich_pattern(word_a, word_b, meat_option_x, meat_option_y, bottom_bread_options, top_bread_options)

        # Skip if there weren't any changes if there was any change
        if (updated_word_a == word_a) and (updated_word_b == word_b):
            continue

        # Update the words for that match
        ne.update_name_a(index_a, updated_word_a)
        ne.update_name_b(index_b, updated_word_b)

    # concatonates the two lists together back into strings
    name_a, name_b = ne.get_modified_names()
    return name_a, name_b

@lru_cache(maxsize=10_000)
def _sandwich_pattern(word_a: str, word_b: str, meat_option_x: str, meat_option_y: str, bottom_bread_options: frozenset[str], top_bread_options: frozenset[str]) -> tuple[str, str]:
    """Modifies two words based on the pattern. Takes a list of potential starts and a list of potential ends (the breads),
    that a substring within could begin or end with, within two words. The same beginning and ends must be present in each word,
    even though many beginnings or ends may be in the list. Each word must have one of two middle that matches, one of which
    will be replaced. If this pattern does not match, or the words are too short or too far apart, then the changes don't happen.

    Args:
        word_a: a word in a name
        word_b: a word in a name
        meat_option_x: one substring middle variant
        meat_option_y: the other substring middle variant
        bottom_bread_options: the list of potential starts of the substring. The potential start must be consistent for both
        top_bread_options: the list of potential ends to the substring. The potential ends must be consistent for both

    Returns:
        _description_
    """    
    
    # Early exit if neither word contains any meat options
    if not any(meat in word_a for meat in [meat_option_x, meat_option_y]) or \
       not any(meat in word_b for meat in [meat_option_x, meat_option_y]):
        return word_a, word_b
    
    # Add word breaks once
    padded_a = f"-{word_a}-"
    padded_b = f"-{word_b}-"
    
    # Pre-filter bread options that exist in both words to reduce search space
    valid_bottom_breads = [b for b in bottom_bread_options if b in padded_a and b in padded_b]
    valid_top_breads = [t for t in top_bread_options if t in padded_a and t in padded_b]
    
    # Early exit if no valid bread combinations
    if not valid_bottom_breads or not valid_top_breads:
        return word_a, word_b
    
    # Search for patterns more efficiently
    for bottom_bread in valid_bottom_breads:
        for top_bread in valid_top_breads:
            # Use cached compiled pattern
            compiled_pattern = _get_compiled_regex_pattern(bottom_bread, meat_option_x, meat_option_y, top_bread)
            
            # Find matches
            match_a = compiled_pattern.search(padded_a)
            match_b = compiled_pattern.search(padded_b)
            
            if not match_a or not match_b:
                continue
                
            # Quick check if patterns are identical (skip if so)
            if match_a.group(0) == match_b.group(0):
                continue
            
            # Check span proximity efficiently
            span_a = match_a.span()
            span_b = match_b.span()
            if abs(span_a[0] - span_b[0]) > 2 or abs(span_a[1] - span_b[1]) > 2:
                continue
            
            # Calculate middle coordinates
            bottom_len = len(bottom_bread)
            top_len = len(top_bread)
            
            middle_start_a = span_a[0] + bottom_len
            middle_end_a = span_a[1] - top_len
            middle_start_b = span_b[0] + bottom_len  
            middle_end_b = span_b[1] - top_len
            
            # Replace middles with meat_option_y and remove dashes in one operation
            result_a = (padded_a[:middle_start_a] + meat_option_y + padded_a[middle_end_a:]).replace('-', '')
            result_b = (padded_b[:middle_start_b] + meat_option_y + padded_b[middle_end_b:]).replace('-', '')
            
            return result_a, result_b
    
    # No matches found, return original words
    return word_a, word_b


@lru_cache(maxsize=10_000)
def _get_compiled_regex_pattern(bottom_bread: str, meat_x: str, meat_y: str, top_bread: str) -> re.Pattern[str]:
    """Cache compiled regex patterns to avoid recompilation.

    Args:
        bottom_bread: the start of the substring
        meat_x: a possible middle of the substring
        meat_y: a different possible middle of the substring
        top_bread: the end of the substring

    Returns:
        the pattern for identifying modification possibilities
    """    
    pattern = f"{re.escape(bottom_bread)}({re.escape(meat_x)}|{re.escape(meat_y)}){re.escape(top_bread)}"
    return re.compile(pattern)


@lru_cache(maxsize=10_000)
def modify_ipas_together(ipa_a: str, ipa_b: str) -> tuple[str,str]:
    """Modifies two ipas by comparing each to one another.

    Args:
        ipa_a: the ipa of a name
        ipa_b: the ipa of a name

    Returns:
        the two modified names
    """
    for meat_option_x, meat_option_y, bottom_breads, top_breads, min_letters in rulesIpa.data:
        ipa_a, ipa_b = use_sandwhich_patterns_on_all_words(ipa_a, ipa_b, meat_option_x, meat_option_y, bottom_breads, top_breads, min_letters)
    return ipa_a, ipa_b