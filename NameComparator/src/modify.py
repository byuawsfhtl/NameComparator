import re
from fuzzywuzzy import fuzz

import NameComparator.src.usefulTools as usefulToolsMod
import NameComparator.data.rules.rulesSpelling as rulesSpelling
import NameComparator.data.rules.rulesIpa as rulesIpa

def modify_names_together(name_one:str, name_two:str) -> tuple[str,str]:
    """Modifies the name together (changing them in a way that is much more intense than simply cleaning together).

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str,str]: the modified names
    """        
    name_one = re.sub(r'ie\b', 'y', name_one)
    name_two = re.sub(r'ie\b', 'y', name_two)
    name_one, name_two = remove_word_or_from_names(name_one, name_two)
    name_one, name_two = _fix_vowel_mistakes(name_one, name_two)
    name_one, name_two = _fix_swapped_characters(name_one, name_two)
    name_one, name_two = _deal_with_wrong_first_char(name_one, name_two)
    for middle_substring_option_one, middle_substring_option_two, substring_beginnings, substring_endings, minimum_letters in rulesSpelling.data:
        name_one, name_two = _replace_substring_centers_if_names_are_similar(name_one, name_two, middle_substring_option_one, middle_substring_option_two, substring_beginnings, substring_endings, minimum_letters)
    name_one = re.sub(r'\s+', ' ', name_one)
    name_two = re.sub(r'\s+', ' ', name_two)
    name_one = name_one.strip()
    name_two = name_two.strip()
    return name_one, name_two

def remove_word_or_from_names(name_one:str, name_two:str) -> tuple[str, str]:
    """Removes the word 'or' from a name (assuming that the name could have been 
    poorly indexed so that the indexer's guesses for a specific word of the name is still within the string).

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    if (not name_one) or (not name_two):
        return name_one, name_two
    name_one = name_one.strip()
    name_two = name_two.strip()
    name_one, name_two = name_one.lower(), name_two.lower()

    # if or in neither
    if (not " or " in name_one) and (not " or " in name_two):
        return name_one, name_two
    
    # if or in both
    elif (" or " in name_one) and (" or " in name_two):
        return name_one, name_two

    # if or in name_one and not name_two
    elif " or " in name_one:
        # Gets the score for if the word before 'or' is removed
        right_name_one = re.sub("[a-z]+ or ", " ", name_one)
        if not right_name_one:
            right_name_one = '_'
        right_word_combo = usefulToolsMod.find_word_matches_and_quality(right_name_one, name_two)
        right_average_score = sum(tup[2] for tup in right_word_combo) / len(right_word_combo)
        # Gets the score for if the word after 'or' is removed
        left_name_one = re.sub(" or [a-z]+", " ", name_one)
        if not left_name_one:
            left_name_one = '_'
        left_word_combo =  usefulToolsMod.find_word_matches_and_quality(left_name_one, name_two)
        left_average_score = sum(tup[2] for tup in left_word_combo) / len(left_word_combo)
        # Return the higher one
        if right_average_score >= left_average_score:
            return right_name_one, name_two
        return left_name_one, name_two
    
    # if or in name_two and not name_one
    elif " or " in name_two:
        right_name_two = re.sub("[a-z]+ or ", " ", name_two)
        if not right_name_two:
            right_name_two = '_'
        right_word_combo = usefulToolsMod.find_word_matches_and_quality(right_name_two, name_one)
        right_average_score = sum(tup[2] for tup in right_word_combo) / len(right_word_combo)
        # Gets the score for if the word after 'or' is removed
        left_name_two = re.sub(" or [a-z]+", " ", name_two)
        if not left_name_two:
            left_name_two = '_'
        left_word_combo =  usefulToolsMod.find_word_matches_and_quality(left_name_two, name_one)
        left_average_score = sum(tup[2] for tup in left_word_combo) / len(left_word_combo)
        # Return the higher one
        if right_average_score >= left_average_score:
            return name_one, right_name_two
        return name_one, left_name_two

def _fix_vowel_mistakes(name_one:str, name_two:str) -> tuple[str, str]:
    """Modifies two matching words in a name so that they are the same if 
    they are only different by one vowel and 5 letters or more.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the two modified names
    """        
    ne = usefulToolsMod.NameEditor(name_one, name_two)
    for index_one, _, word_one, word_two in usefulToolsMod.get_matching_words_and_indices(name_one, name_two):
        # Continue if either word is less than 5 chars or not same length
        length_one = len(word_one)
        length_two = len(word_two)
        if length_one < 5:
            continue
        if length_two < 5:
            continue
        if length_one != length_two:
            continue

        # Check if there is only one difference
        mismatched_index = None
        too_many_differences = False
        for i in range(length_one):
            if word_one[i] == word_two[i]:
                continue
            if mismatched_index:
                too_many_differences = True
                break
            mismatched_index = i
        
        # Continue if there was not exactly one difference
        if (too_many_differences) or (mismatched_index is None):
            continue

        # Replace one of the letters to be the other if they are cooresponding
        char_word_one = word_one[mismatched_index]
        char_word_two = word_two[mismatched_index]
        cooresponding = ['ao', 'ea', 'iy']
        if (f'{char_word_one}{char_word_two}' in cooresponding) or (f'{char_word_two}{char_word_one}' in cooresponding):
            ne.update_name_one(index_one, word_two)
    
    # Return the modified (or not) names
    return ne.get_modified_names()

def _fix_swapped_characters(name_one:str, name_two:str) -> tuple[str, str]:
    """If two matching words (of 5 letters of more) for the two names are the same barring swapped letters (typo), makes the words the same.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    ne = usefulToolsMod.NameEditor(name_one, name_two)
    for index_one, _, word_one, word_two in usefulToolsMod.get_matching_words_and_indices(name_one, name_two):
        # Skip if the words are not 5 long, are different length, or not fuzzy 80
        if len(word_one) != 5:
            continue
        if len(word_one) != len(word_two):
            continue
        if fuzz.ratio(word_two, word_one) != 80:
            continue

        # Find how many differences and where
        difference_count = 0
        difference_positions = []
        for i in range(len(word_one)):
            if word_one[i] != word_two[i]:
                difference_count += 1
                difference_positions.append(i)
        
        # Skip if there are not two differences, differences are not sequential, or not swappable
        if difference_count != 2:
            continue
        position_one, position_two = difference_positions
        if abs(position_one - position_two) != 1:
            continue
        if (word_one[position_one] != word_two[position_two]) or (word_one[position_one] != word_two[position_two]):
            continue

        # This is the scenerio we are looking for. Make the words identical
        ne.update_name_one(index_one, word_two)
    
    # Return the modified (or not) names
    return ne.get_modified_names()

def _deal_with_wrong_first_char(name_one:str, name_two:str) -> tuple[str, str]:
    """If two matching words (of 5 letters or more) are the same barring the first letter, makes the same.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    ne = usefulToolsMod.NameEditor(name_one, name_two)
    for index_one, _, word_one, word_two in usefulToolsMod.get_matching_words_and_indices(name_one, name_two):
        if word_one == word_two:
            continue
        if (word_one[1:] == word_two[1:]) and (len(word_one) > 4) and (len(word_two) > 4):
            ne.update_name_one(index_one, word_two)
    name_one, name_two = ne.get_modified_names()
    return name_one, name_two

def _replace_substring_centers_if_names_are_similar(name_one:str, name_two:str, middle_substring_option_one:str, middle_substring_option_two:str, possible_substring_beginnings:list[str], possible_substring_endings:list[str], minimum_required_letters:int) -> tuple[str,str]:
    """For any given matching word pair, replaces a specific substring in one of the words with a similar substring found in the other word.
    It checks this by comparing the beginnings and ends of words, then determining similarities of everything in between those and replacing
    them if they seem like they indicate similar words. This could be compared to a 'word sandwich' of sorts where the beginnings and endings
    are sort of like bread on the ends and the center substrings are like the fillings.

    Args:
        name_one (str): a name
        name_two (str): a name
        middle_substring_option_one (str): the first possible middle of the substring
        middle_substring_option_two (str): the second possible middle of the substring
        possible_substring_beginnings (list[str]): a list of possible beginnings to the substring. Whichever beginning is found in the one must be found in the other in order for the replacement to work
        possible_substring_endings (list[str]): a list of possible endings to the substring. Whichever ending is found in the one must be found in the other in order for the replacement to work
        minimum_required_letters (int): the minimum required letters to be found in both words in order for the replacement to work

    Returns:
        tuple[str,str]: the modified names
    """        
    # Return if both middles not in different words
    if (middle_substring_option_one not in name_one and middle_substring_option_two not in name_one) or (middle_substring_option_one not in name_two and middle_substring_option_two not in name_two):
        return name_one, name_two

    ne = usefulToolsMod.NameEditor(name_one, name_two)
    for index_one, index_two, word_one, word_two in usefulToolsMod.get_matching_words_and_indices(name_one, name_two):
        # Skip words that are not long enough for the given rule
        if len(word_one) < minimum_required_letters or len(word_two) < minimum_required_letters:
            continue

        # Add clear word breaks
        word_one = f"-{word_one}-"
        word_two = f"-{word_two}-"

        # Check words for substring matches and make appropriate replacements and edits
        word_one, word_two = _handle_substring_replacements_and_checks(word_one, word_two, possible_substring_beginnings, middle_substring_option_one, middle_substring_option_two, possible_substring_endings)

        # Update the words for that match (though a change may not have occured)
        word_one = word_one.replace("-", "")
        word_two = word_two.replace("-", "")
        ne.update_name_one(index_one, word_one)
        ne.update_name_two(index_two, word_two)

    # concatonates the two lists together back into strings
    name_one, name_two = ne.get_modified_names()
    return name_one, name_two

def _handle_substring_replacements_and_checks(word_one: str, word_two: str, possible_substring_beginnings: list[str], middle_substring_option_one: str, middle_substring_option_two: str, possible_substring_endings: list[str]) -> tuple[str, str]:
    """This is a helper function for _replace_substring_centers_if_names_are_similar
    that helps with its cyclomatic complexity. It's actual function is to see if
    substring patterns exist within word_one or word_two and then replace them to
    be the same if they are close enough to what's in *both* word_one and word_two.
    
    Args:
        word_one: The first word or name to look for substring matches in
        word_two: The second word or name to look for substring matches in
        possible_substring_beginnings: A list of all possible beginnings to a substring
        middle_substring_option_one: the first possible middle of the substring
        middle_substring_option_two: the second possible middle of the substring
        possible_substring_endings: A list of all possible endings to a substring
        
    Returns:
        A tuple containing the modified versions of word_one and word_two if any
        changes were made, or just word_one and word_two if none were made"""
    
    for substring_beginning in possible_substring_beginnings:
        if substring_beginning not in word_one or substring_beginning not in word_two:
            continue

        for substring_ending in possible_substring_endings:
            if substring_ending not in word_one or substring_ending not in word_two:
                continue

            # Skip the bread if the pattern is not found in both, if the middles (meats) are the same, or if the patterns are too far appart
            pattern = f"{substring_beginning}({middle_substring_option_one}|{middle_substring_option_two}){substring_ending}"
            result_list_one = re.search(pattern, word_one)
            result_list_two = re.search(pattern, word_two)
            if not result_list_one or not result_list_two:
                continue
            if result_list_one.group(0) == result_list_two.group(0):
                continue
            start_index_of_list_one_span, end_index_of_list_one_span = result_list_one.span()
            start_index_of_list_two_span, end_index_of_list_two_span = result_list_two.span()
            if not (abs(start_index_of_list_one_span - start_index_of_list_two_span) <= 2 and abs(end_index_of_list_one_span - end_index_of_list_two_span) <= 2):
                continue

            # Update the words by replacing matching (different) middles with the meat option 2
            start_index_string_one, end_index_string_one = result_list_one.span()
            start_index_string_two, end_index_string_two = result_list_two.span()
            middle_coordinate_string_one = start_index_string_one + len(substring_beginning), end_index_string_one - len(substring_ending)
            middle_coordinate_string_two = start_index_string_two + len(substring_beginning), end_index_string_two - len(substring_ending)
            word_one = _overwrite_with_substring(word_one, middle_substring_option_two, middle_coordinate_string_one[0], middle_coordinate_string_one[1])
            word_two = _overwrite_with_substring(word_two, middle_substring_option_two, middle_coordinate_string_two[0], middle_coordinate_string_two[1])

    return word_one, word_two

def _overwrite_with_substring(string:str, replacement:str, start_index:int, end_index:int) -> str:
    """Overwrites a specific index range of a string with the replacement string.

    Args:
        string (str): the string to replace
        replacement (str): the replacement string
        start_index (int): the start index for the replacement
        end_index (int): the end index for the replacement

    Returns:
        _type_: _description_
    """
    string_list = list(string)
    string_list[start_index:end_index] = replacement
    new_string = ''.join(string_list)
    return new_string

def modify_ipas_by_comparison(ipa_one:str, ipa_two:str) -> tuple[str,str]:
    """Modifies two ipas by comparing each to one another.

    Args:
        ipa_one (str): the ipa of a name
        ipa_two (str): the ipa of a name

    Returns:
        tuple[str,str]: the two modified names
    """
    for middle_substring_option_one, middle_substring_option_two, substring_beginnings, substring_endings, minimum_letters in rulesIpa.data:
        ipa_one, ipa_two = _replace_substring_centers_if_names_are_similar(ipa_one, ipa_two, middle_substring_option_one, middle_substring_option_two, substring_beginnings, substring_endings, minimum_letters)
    return ipa_one, ipa_two