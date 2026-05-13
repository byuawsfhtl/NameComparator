from re import sub as re_sub
from re import search as re_search
from json import loads as json_loads
from importlib.resources import files

from rapidfuzz.fuzz import ratio as fuzz_ratio
from NameComparator.src.usefulTools import find_word_matches_and_quality, get_matching_words_and_indices, NameEditor

# This is required to make sure that it reads in the characters correctly
unparsed_spelling_rules = files('data').joinpath('rules/rulesSpelling.json').read_text(encoding='utf-8')
unparsed_ipa_rules = files('data').joinpath('rules/rulesIpa.json').read_text(encoding='utf-8')

def modify_names_together(name_one:str, name_two:str) -> tuple[str,str]:
    """Modifies the name together, changing them in a way that is much more intense than simply cleaning together.

    Args:
        name_one: The first name to modify
        name_two: The second name to modify

    Returns:
        A tuple containing the modified names
    """        
    name_one = re_sub(r'ie\b', 'y', name_one)
    name_two = re_sub(r'ie\b', 'y', name_two)
    name_one, name_two = remove_word_or_from_names(name_one, name_two)
    name_one, name_two = _fix_vowel_mistakes(name_one, name_two)
    name_one, name_two = _fix_swapped_characters(name_one, name_two)
    name_one, name_two = _deal_with_wrong_first_char(name_one, name_two)
    for middle_substring_option_one, middle_substring_option_two, substring_beginnings, substring_endings, minimum_letters in json_loads(unparsed_spelling_rules):
        name_one, name_two = _replace_substring_centers_if_names_are_similar(name_one, name_two, middle_substring_option_one, middle_substring_option_two, substring_beginnings, substring_endings, minimum_letters)
    name_one = re_sub(r'\s+', ' ', name_one)
    name_two = re_sub(r'\s+', ' ', name_two)
    name_one = name_one.strip()
    name_two = name_two.strip()
    return name_one, name_two

def remove_word_or_from_names(name_one:str, name_two:str) -> tuple[str, str]:
    """Removes the word 'or' from a name. This might happen when a name has been poorly indexed,
    which makes the indexer's guesses for a specific word of the name sta in the string, causing
    the 'or'.

    Args:
        name_one: The first name to remove the word 'or' from
        name_two: The second name to remove the word 'or' from

    Returns:
        A tuple containing the modified names with a consistent use of 'or' (or lack thereof)
    """        
    if (not name_one) or (not name_two):
        return name_one, name_two
    name_one = name_one.strip()
    name_two = name_two.strip()
    name_one, name_two = name_one.lower(), name_two.lower()

    # if 'or' in neither
    if (" or " not in name_one) and (" or " not in name_two):
        return name_one, name_two
    
    # if 'or' in both
    elif (" or " in name_one) and (" or " in name_two):
        return name_one, name_two

    # if 'or' in name_one and not name_two
    elif " or " in name_one:
        # Gets the score for if the word before 'or' is removed
        right_name_one = re_sub("[a-z]+ or ", " ", name_one)

        if not right_name_one:
            right_name_one = '_'
        right_word_combos, possible_right_prefix_count = find_word_matches_and_quality(right_name_one, name_two)
        right_average_score = sum(tup[2] for tup in right_word_combos) / len(right_word_combos)

        # Gets the score for if the word after 'or' is removed
        left_name_one = re_sub(" or [a-z]+", " ", name_one)

        if not left_name_one:
            left_name_one = '_'
        left_word_combos, possible_left_prefix_count =  find_word_matches_and_quality(left_name_one, name_two)
        left_average_score = sum(tup[2] for tup in left_word_combos) / len(left_word_combos)

        # Return the higher one
        if right_average_score >= left_average_score:
            return right_name_one, name_two
        return left_name_one, name_two
    
    # if 'or' in name_two and not name_one
    elif " or " in name_two:
        right_name_two = re_sub("[a-z]+ or ", " ", name_two)

        if not right_name_two:
            right_name_two = '_'
        right_word_combos, possible_right_prefix_count = find_word_matches_and_quality(right_name_two, name_one)
        right_average_score = sum(tup[2] for tup in right_word_combos) / len(right_word_combos)

        # Gets the score for if the word after 'or' is removed
        left_name_two = re_sub(" or [a-z]+", " ", name_two)
        if not left_name_two:
            left_name_two = '_'
        left_word_combos, possible_left_prefix_count =  find_word_matches_and_quality(left_name_two, name_one)
        left_average_score = sum(tup[2] for tup in left_word_combos) / len(left_word_combos)

        # Return the higher one
        if right_average_score >= left_average_score:
            return name_one, right_name_two
        return name_one, left_name_two
    
    return name_one, name_two

def _fix_vowel_mistakes(name_one:str, name_two:str) -> tuple[str, str]:
    """Modifies two matching words in a name so that they are the same if 
    they are only different by one vowel and are 5 letters or longer.

    Args:
        name_one: The first name to check for vowel differences in
        name_two: The second name to check for vowel differences in

    Returns:
        A tuple containing the two modified names
    """        
    name_editor_instance = NameEditor(name_one, name_two)
    for index_one, _, word_one, word_two in get_matching_words_and_indices(name_one, name_two):
        # Continue if either word is less than 5 chars or not same length
        length_one = len(word_one)
        length_two = len(word_two)
        if length_one < 5:
            continue
        elif length_two < 5:
            continue
        elif length_one != length_two:
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
            name_editor_instance.update_name_one(index_one, word_two)
    
    # Return the modified (or not) names
    return name_editor_instance.get_modified_names()

def _fix_swapped_characters(name_one:str, name_two:str) -> tuple[str, str]:
    """If two matching words (of 5 letters of more) for the two names are the same 
    barring swapped letters (such as a typo), this function makes the words the same.

    Args:
        name_one: The first name to check for swapped letters
        name_two: The second name to check for swapped letters

    Returns:
        A tuple containing the names, modified to remove any swapped letters
    """        
    name_editor_instance = NameEditor(name_one, name_two)
    for index_one, _, word_one, word_two in get_matching_words_and_indices(name_one, name_two):
        # Skip if the words are not 5 long, are different length, or not fuzzy 80
        if len(word_one) != 5:
            continue
        elif len(word_one) != len(word_two):
            continue
        elif fuzz_ratio(word_two, word_one) != 80:
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
        name_editor_instance.update_name_one(index_one, word_two)
    
    # Return the modified (or not) names
    return name_editor_instance.get_modified_names()

def _deal_with_wrong_first_char(name_one:str, name_two:str) -> tuple[str, str]:
    """If two matching words (of 5 letters or more) are the same barring the first letter, 
    this function makes them the same.

    Args:
        name_one: The first name to check for an incorrect first character
        name_two: The second name to check for an incorrect first character

    Returns:
        A tuple containing the names, modified to have a matching first character
    """        
    name_editor_instance = NameEditor(name_one, name_two)
    for index_one, _, word_one, word_two in get_matching_words_and_indices(name_one, name_two):
        if word_one == word_two:
            continue
        if (word_one[1:] == word_two[1:]) and (len(word_one) > 4) and (len(word_two) > 4):
            name_editor_instance.update_name_one(index_one, word_two)

    return name_editor_instance.get_modified_names()

def _replace_substring_centers_if_names_are_similar(name_one:str, name_two:str, middle_substring_option_one:str, middle_substring_option_two:str, possible_substring_beginnings:list[str], possible_substring_endings:list[str], minimum_required_letters:int) -> tuple[str,str]:
    """For any given matching word pair, replaces a specific substring in one of the words with a similar substring found in the other word.
    It checks this by comparing the beginnings and ends of words, then determining similarities of everything in between those and replacing
    them if they seem like they indicate similar words. This could be compared to a 'word sandwich' of sorts where the beginnings and endings
    are sort of like bread on the ends and the center substrings are like the fillings.

    Args:
        name_one: The first name to check for similar substrings
        name_two: The second name to check for similar substrings
        middle_substring_option_one: The first possible middle of the substring
        middle_substring_option_two: The second possible middle of the substring
        possible_substring_beginnings: A list of possible beginnings to the substring. Whichever beginning is found in the one must be found 
            in the other in order for the replacement to be considered valid
        possible_substring_endings: A list of possible endings to the substring. Whichever ending is found in the one must be found in the 
            other in order for the replacement to be considered valid
        minimum_required_letters: The minimum required letters to be found in both words in order for the replacement to be considered valid

    Returns:
        A tuple containing the names, modified to have the same substrings in the center (if applicable)
    """        

    print(f"Determining if the centers should be replaced for the following variables in Python: name_one - {name_one} name_two - {name_two} middle_substring_option_one - {middle_substring_option_one} middle_substring_option_two - {middle_substring_option_two} possible_substring_beginnings - {possible_substring_beginnings} possible_substring_endings - {possible_substring_endings} minimum_required_letters - {minimum_required_letters}")

    # Return if both middles not in different words
    if (middle_substring_option_one not in name_one and middle_substring_option_two not in name_one) or (middle_substring_option_one not in name_two and middle_substring_option_two not in name_two):
        print("No replacements made in Python due to substrings that are already the same")
        return name_one, name_two

    name_editor_instance = NameEditor(name_one, name_two)
    for index_one, index_two, word_one, word_two in get_matching_words_and_indices(name_one, name_two):
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
        name_editor_instance.update_name_one(index_one, word_one)
        name_editor_instance.update_name_two(index_two, word_two)
        print(f"Updated name_one with {word_one} in Python")
        print(f"Updated name_two with {word_two} in Python")

    # concatonates the two lists together back into strings
    name_one, name_two = name_editor_instance.get_modified_names()
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
        middle_substring_option_one: The first possible middle of the substring
        middle_substring_option_two: The second possible middle of the substring
        possible_substring_endings: A list of all possible endings to a substring
        
    Returns:
        A tuple containing the modified versions of word_one and word_two if any
        changes were made, or just word_one and word_two if none were made
    """
    
    for substring_beginning in possible_substring_beginnings:
        if substring_beginning not in word_one or substring_beginning not in word_two:
            continue

        for substring_ending in possible_substring_endings:
            if substring_ending not in word_one or substring_ending not in word_two:
                continue

            # Skip the beginnings and ends if the pattern is not found in both, 
            # if the middles are the same, or if the patterns are too far appart
            pattern = f"{substring_beginning}({middle_substring_option_one}|{middle_substring_option_two}){substring_ending}"
            result_list_one = re_search(pattern, word_one)
            result_list_two = re_search(pattern, word_two)

            if not result_list_one or not result_list_two:
                continue
            if result_list_one.group(0) == result_list_two.group(0):
                continue

            start_index_of_list_one_span, end_index_of_list_one_span = result_list_one.span()
            start_index_of_list_two_span, end_index_of_list_two_span = result_list_two.span()

            if (abs(start_index_of_list_one_span - start_index_of_list_two_span) > 2 and abs(end_index_of_list_one_span - end_index_of_list_two_span) > 2):
                continue

            # Update the words by replacing matching (different) middles with the second middle substring option
            start_index_string_one, end_index_string_one = start_index_of_list_one_span, end_index_of_list_one_span
            start_index_string_two, end_index_string_two = start_index_of_list_two_span, end_index_of_list_two_span
            middle_coordinate_string_one = start_index_string_one + len(substring_beginning), end_index_string_one - len(substring_ending)
            middle_coordinate_string_two = start_index_string_two + len(substring_beginning), end_index_string_two - len(substring_ending)
            word_one = _overwrite_with_substring(word_one, middle_substring_option_two, middle_coordinate_string_one[0], middle_coordinate_string_one[1])
            word_two = _overwrite_with_substring(word_two, middle_substring_option_two, middle_coordinate_string_two[0], middle_coordinate_string_two[1])

    return word_one, word_two

def _overwrite_with_substring(string:str, replacement:str, start_index:int, end_index:int) -> str:
    """Overwrites a specific index range of a string with the replacement string.

    Args:
        string: The string to replace
        replacement: The replacement string
        start_index: The start index for the replacement
        end_index: The end index for the replacement

    Returns:
        A new string, with the specified indices replaced by the replacement string
    """
    return string[:start_index] + replacement + string[(end_index):]

def modify_ipas_by_comparison(ipa_one:str, ipa_two:str) -> tuple[str,str]:
    """Modifies two ipas by comparing them to each other.

    Args:
        ipa_one: The first ipa of a name
        ipa_two: The second ipa of a name

    Returns:
        A tuple containing the modified ipas of two words or names
    """
    for middle_substring_option_one, middle_substring_option_two, substring_beginnings, substring_endings, minimum_letters in json_loads(unparsed_ipa_rules):
        ipa_one, ipa_two = _replace_substring_centers_if_names_are_similar(ipa_one, ipa_two, middle_substring_option_one, middle_substring_option_two, substring_beginnings, substring_endings, minimum_letters)
    return ipa_one, ipa_two