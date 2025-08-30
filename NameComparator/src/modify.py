import re
from fuzzywuzzy import fuzz

import NameComparator.src.usefulTools as usefulToolsMod
import NameComparator.data.rules.rulesSpelling as rulesSpelling
import NameComparator.data.rules.rulesIpa as rulesIpa

def modify_names_together(name_a : str, name_b : str) -> tuple[str,str]:
    """Modifies the name together (changing them in a way that is much more intense than simply cleaning together).

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        the modified names
    """        
    name_a = re.sub(r'ie\b', 'y', name_a)
    name_b = re.sub(r'ie\b', 'y', name_b)
    name_a, name_b = _removeOrInNames(name_a, name_b)
    name_a, name_b = _fixVowelMistakes(name_a, name_b)
    name_a, name_b = _fixSwappedChars(name_a, name_b)
    name_a, name_b = _dealWithWrongFirstChar(name_a, name_b)
    for meatOption1, meatOption2, bottomBreads, topBreads, minLetters in rulesSpelling.data:
        name_a, name_b = _replace_substring_sandwich_meat_if_matching_bread(name_a, name_b, meatOption1, meatOption2, bottomBreads, topBreads, minLetters)
    name_a = re.sub(r'\s+', ' ', name_a)
    name_b = re.sub(r'\s+', ' ', name_b)
    name_a = name_a.strip()
    name_b = name_b.strip()
    return name_a, name_b

def _removeOrInNames(name_a : str, name_b : str) -> tuple[str, str]:
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
        right_average_score = sum(tup[2] for tup in right_word_combo) / len(right_word_combo)
        # Gets the score for if the word after 'or' is removed
        left_name_a = re.sub(" or [a-z]+", " ", name_a)
        if not left_name_a:
            left_name_a = '_'
        left_word_combo =  usefulToolsMod.find_which_words_match_and_how_well(left_name_a, name_b)
        left_average_score = sum(tup[2] for tup in left_word_combo) / len(left_word_combo)
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
        right_average_score = sum(tup[2] for tup in right_word_combo) / len(right_word_combo)
        # Gets the score for if the word after 'or' is removed
        left_name_b = re.sub(" or [a-z]+", " ", name_b)
        if not left_name_b:
            left_name_b = '_'
        left_word_combo =  usefulToolsMod.find_which_words_match_and_how_well(left_name_b, name_a)
        left_average_score = sum(tup[2] for tup in left_word_combo) / len(left_word_combo)
        # Return the higher one
        if right_average_score >= left_average_score:
            return name_a, right_name_b
        return name_a, left_name_b

def _fixVowelMistakes(name_a : str, name_b : str) -> tuple[str, str]:
    """Modifies two matching words in a name so that they are the same if 
    they are only different by one vowel and 5 letters or more.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        the two modified names
    """        
    ne = usefulToolsMod.NameEditor(name_a, name_b)
    for index_a, _, word_a, word_b in usefulToolsMod.get_pair_indices_and_words(name_a, name_b):
        # Continue if either word is less than 5 chars or not same length
        lenA = len(word_a)
        lenB = len(word_b)
        if lenA < 5:
            continue
        if lenB < 5:
            continue
        if lenA != lenB:
            continue

        # Check if there is only one difference
        mismatched_index = None
        too_many_diffs = False
        for i in range(lenA):
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

def _fixSwappedChars(name_a : str, name_b : str) -> tuple[str, str]:
    """If two matching words (of 5 letters of more) for the two names are the same barring swapped letters (typo), makes the words the same.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        tuple[str, str]: the modified names
    """        
    ne = usefulToolsMod.NameEditor(name_a, name_b)
    for index_a, _, word_a, word_b in usefulToolsMod.get_pair_indices_and_words(name_a, name_b):
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

def _dealWithWrongFirstChar(name_a : str, name_b : str) -> tuple[str, str]:
    """If two matching words (of 5 letters or more) are the same barring the first letter, makes the same.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        tuple[str, str]: the modified names
    """        
    ne = usefulToolsMod.NameEditor(name_a, name_b)
    for index_a, _, word_a, word_b in usefulToolsMod.get_pair_indices_and_words(name_a, name_b):
        if word_a == word_b:
            continue
        if (word_a[1:] == word_b[1:]) and (len(word_a) > 4) and (len(word_b) > 4):
            ne.update_name_a(index_a, word_b)
    name_a, name_b = ne.get_modified_names()
    return name_a, name_b

def _replace_substring_sandwich_meat_if_matching_bread(name_a : str, name_b : str, meat_option_x : str, meat_option_y : str, bottom_bread_options:list[str], top_bread_options:list[str], min_required_letters:int) -> tuple[str,str]:
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
    for index_a, index_b, word_a, word_b in usefulToolsMod.get_pair_indices_and_words(name_a, name_b):
        # Skip words that are not long enough for the given rule
        if len(word_a) < min_required_letters or len(word_b) < min_required_letters:
            continue

        # Add clear word breaks
        word_a = f"-{word_a}-"
        word_b = f"-{word_b}-"

        for bottom_bread in bottom_bread_options:
            if bottom_bread not in word_a or bottom_bread not in word_b:
                continue

            for top_bread in top_bread_options:
                if top_bread not in word_a or top_bread not in word_b:
                    continue

                # Skip the bread if the pattern is not found in both, if the middles (meats) are the same, or if the patterns are too far appart
                pattern = f"{bottom_bread}({meat_option_x}|{meat_option_y}){top_bread}"
                results_a = re.search(pattern, word_a)
                results_b = re.search(pattern, word_b)
                if not results_a or not results_b:
                    continue
                if results_a.group(0) == results_b.group(0):
                    continue
                spanA1, spanB1 = results_a.span()
                spanA2, spanB2 = results_b.span()
                if not (abs(spanA1 - spanA2) <= 2 and abs(spanB1 - spanB2) <= 2):
                    continue

                # Update the words by replacing matching (different) middles with the meat option 2
                startIndexStringA, endIndexStringA = results_a.span()
                startIndexStringB, endIndexStringB = results_b.span()
                middleCoordsStringA = startIndexStringA + len(bottom_bread), endIndexStringA - len(top_bread)
                middleCoordsStringB = startIndexStringB + len(bottom_bread), endIndexStringB - len(top_bread)
                word_a = _overwriteWithSubstring(word_a, meat_option_y, middleCoordsStringA[0], middleCoordsStringA[1])
                word_b = _overwriteWithSubstring(word_b, meat_option_y, middleCoordsStringB[0], middleCoordsStringB[1])

        # Update the words for that match (though a change may not have occured)
        word_a = word_a.replace("-", "")
        word_b = word_b.replace("-", "")
        ne.update_name_a(index_a, word_a)
        ne.update_name_b(index_b, word_b)

    # concatonates the two lists together back into strings
    name_a, name_b = ne.get_modified_names()
    return name_a, name_b

def _overwriteWithSubstring(string : str, replacement : str, startIndex:int, endIndex:int) -> str:
    """Overwrites a specific index range of a string with the replacement string.

    Args:
        string (str): the string to replace
        replacement (str): the replacement string
        startIndex (int): the start index for the replacement
        endIndex (int): the end index for the replacement

    Returns:
        _type_: _description_
    """
    stringList = list(string)
    stringList[startIndex:endIndex] = replacement
    newString = ''.join(stringList)
    return newString

def modify_ipas_together(ipaA : str, ipaB : str) -> tuple[str,str]:
    """Modifies two ipas by comparing each to one another.

    Args:
        ipaA (str): the ipa of a name
        ipaB (str): the ipa of a name

    Returns:
        tuple[str,str]: the two modified names
    """
    for meatOption1, meatOption2, bottomBreads, topBreads, minLetters in rulesIpa.data:
        ipaA, ipaB = _replace_substring_sandwich_meat_if_matching_bread(ipaA, ipaB, meatOption1, meatOption2, bottomBreads, topBreads, minLetters)
    return ipaA, ipaB