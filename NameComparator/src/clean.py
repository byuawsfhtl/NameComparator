import re
from unidecode import unidecode
from fuzzywuzzy import fuzz

import NameComparator.src.usefulTools as usefulTools
import NameComparator.src.comparisons as comparisonsMod

def clean_name(name:str) -> str:
    """Cleans a singular name to get rid of extra or unhelpful data, and to standardize surnames.

    Args:
        name (str): the name being cleaned

    Returns:
        str: the cleaned name
    """        
    # Deal with blank names
    if (name == "") or (not isinstance(name, str)):
        return "_"

    # Deal with whitespace
    name = re.sub(r'[^\S ]', ' ', name)
    name = re.sub(r" +", " ", name)
    name = name.strip()

    # Standardize name into ascii
    name = unidecode(name)
    name = name.lower()

    # Deal with blank names again
    if name == "":
        return "_"

    # Remove Punctiation
    name = re.sub(r"[.,?;\"*()]", "", name)

    # Remove spaces after apostrophe
    name = re.sub("' +", "'", name)

    # Remove jr and sr
    name = re.sub(r"\bjr\b", "", name).replace(r"\bjunior\b", "")
    name = re.sub(r"\bsr\b", "", name).replace(r"\bsenior\b", "")

    # Remove titles
    name = re.sub(r"\bprof\b", "", name).replace(r"\bprofessor\b", "")
    name = re.sub(r"\bmr\b", "", name).replace(r"\bmister\b", "")
    name = re.sub(r"\bmrs\b", "", name).replace(r"\bmissus\b", "")
    name = re.sub(r"\bms\b", "", name).replace(r"\bmiss\b", "")
    name = re.sub(r"\bdr\b", "", name).replace(r"\bdoctor\b", "")
    name = re.sub(r"\bstudent\b", "", name)
    name = re.sub(r"\brev\b", "", name)
    name = name.replace("reverend", "")

    # Remove family relations
    name = re.sub(r"\bsister\b", "", name)
    name = re.sub(r"\bbrother\b", "", name)
    name = re.sub(r"\bmother\b", "", name)
    name = re.sub(r"\bfather\b", "", name)
    name = re.sub(r" in law", " ", name)

    # Removes "head of household"
    name = name.replace("head of household", "")

    # Remove Common Abbreviations
    common_abbreviations = {
        'wm': 'william',
        'geo': 'george',
        'chas': 'charles',
        'thos': 'thomas',
        'jas': 'james',
        'jno': 'john',
        'robt': 'robert',
        'jos': 'joseph',
        'benj': 'benjamin'
    }
    name_as_list = []
    for word in name.split():
        name_as_list.append(common_abbreviations.get(word, word))
    name = ' '.join(name_as_list)

    # Remove stuff like 'the 3rd'
    name = re.sub(r"[1-9][a-z]2,6", "", name).replace(" the ", "")

    # Remove Roman numerals
    name = ' '.join(re.sub(r'\b(ii|iii|iv)\b', '', word) for word in name.split())
    name = re.sub(r" +", " ", name)
    name = name.strip()

    # Remove 'no suffix'
    name = name.replace("no suffix", "")

    # Deal with Dutch names
    name = re.sub(r"\bvan de", "vande", name)
    name = re.sub(r"\bvan den", "vanden", name)
    name = re.sub(r"\bvan der", "vander", name)
    
    # Deal with whitespace one last time, then return
    name = re.sub(r" +", " ", name)
    name = name.strip()
    if not name:
        name = '_'
    return name

def clean_names_by_comparison(name_one:str = '_', name_two:str = '_') -> tuple[str, str]:
    """Cleans names by comparing them to one another, fixing common errors to standardize.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the two cleaned names
    """        
    # Return if either name is blank
    if (name_one == '_') or (name_two == '_'):
        return name_one, name_two
    
    # Deal with dashes
    name_one, name_two = _deal_with_dashes(name_one, name_two)
    
    # Deal with Scottish and Irish names
    name_one, name_two = _fix_related_prefixes(name_one, name_two, 'mac', 'mc')
    name_one, name_two = _fix_mc_and_mac_names(name_one, name_two)

    # Deal with just Irish names
    irish_names_starting_with_o = [
        'beirne', 'berry', 'boyle', 'bryant', 'brian', 'brien', 'bryan', 'ceallaigh', 'conner',
        'connor', 'conor', 'daniel', 'day', 'dean', 'dea', 'doherty', 'donnell', 'donnel', 'donoghue',
        'donohue', 'donovan', 'dowd', 'driscoll', 'fallon', 'farrell', 'flaherty', 'flanagan', 'flynn',
        'gara', 'gorman', 'grady', 'guinn', 'guin', 'hagan', 'haire', 'hair', 'halloran', 'hanlon',
        'hara', 'hare', 'harra', 'harrow', 'haver', 'hearn', 'hern', 'herron', 'higgins', 'hora',
        'kane', 'keefe', 'keeffe', 'kelley', 'kelly', 'laughlin', 'leary', 'loughlin', 'mahoney',
        'mahony', 'maley', 'malley', 'mara', 'mary', 'meara', 'melia', 'moore', 'more', 'muir',
        'murchu', 'mure', 'murphy', 'neall', 'neal', 'neill', 'neil', 'ney', 'niall', 'quinn', 'regan',
        'reilly', 'riley', 'riordan', 'roark', 'rorke', 'rourke', 'ryan', 'shaughnessy', 'shea',
        'shields', 'sullivan', 'toole', 'tool',
    ]

    if (' o ' in name_one) or (" o" in name_one) or (" o" in name_two) or (' o ' in name_two):
        for surname in irish_names_starting_with_o:
            if (surname in name_one) or (surname in name_two):
                name_one, name_two = _remove_irish_o(name_one, name_two, surname)

    # Figure out what needs to be done with prefixes in the names and make needed changes
    name_one, name_two = _handle_prefixes_in_names(name_one, name_two)

    # Combine words that are one word in the other name
    while True:
        combined, name_one, name_two = _combine_split_words(name_one, name_two)
        if not combined:
            break
    while True:
        combined, name_two, name_one = _combine_split_words(name_two, name_one)
        if not combined:
            break

    # Remove extra spaces
    name_one = re.sub(r'\s+', ' ', name_one)
    name_two = re.sub(r'\s+', ' ', name_two)
    name_one = name_one.strip()
    name_two = name_two.strip()

    # Return the cleaned names
    return name_one, name_two

def _handle_prefixes_in_names(name_one: str, name_two: str) -> tuple[str, str]:
    """This is a helper function for clean_names_by_comparison that helps manage its
    cyclomatic complexity. It takes in two names that are going to be compared later
    on and figures out what needs to be done with prefixes that might be on them to
    ensure that later standardization goes smoothly.
    
    Args:
        name_one: The first name to run prefix checks and handling on
        name_two: The second name to run prefix checks and handling on
        
    Returns:
        A tuple containing the input names, with prefixes modified in a way that lets
        them be standardized later on"""
    
    # Create a list of prefixes to check
    possible_prefixes = [
        "d'", "de", "fi", "santa", "san", "de la", "de los", "del", "la", "le", "du", "dela", "los", 
        "der", "den", "vanden", "vander", "vande", "van", "von", 'di', 'dil'
    ]

    # Deal with any prefixes and optional intros that make the match worse
    name_one = re.sub(r"\s+", " ", name_one)
    name_one = name_one.strip()
    name_two = re.sub(r"\s+", " ", name_two)
    name_two = name_two.strip()

    for prefix in possible_prefixes:
        if (f" {prefix}" in name_one) or (f" {prefix}" in name_two):
            if (prefix == 'de') or (prefix == 'di'):
                name_one, name_two = _fix_related_prefixes(name_one, name_two, 'de', 'di')
                name_one, name_two = _remove_unnecessary_prefixes("de", name_one, name_two)
                name_one, name_two = _combine_prefix_with_surname_if_in_both(name_one, name_two, "de")
            elif (prefix == 'del') or (prefix == 'dil'):
                name_one, name_two = _fix_related_prefixes(name_one, name_two, 'del', 'dil')
                name_one, name_two = _remove_unnecessary_prefixes("del", name_one, name_two)
            elif prefix == 'van':
                name_one, name_two = _remove_unnecessary_prefixes("van", name_one, name_two)
                name_one, name_two = _combine_prefix_with_surname_if_in_both(name_one, name_two, "van")
            else:
                name_one, name_two = _remove_unnecessary_prefixes(prefix, name_one, name_two)

    return name_one, name_two

def _deal_with_dashes(name_one:str, name_two:str) -> tuple[str, str]:
    """Cleans both names in order to deal with dashes in names.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the cleaned names
    """        
    # Return old if no dash in either
    if ('-' not in name_one) and ('-' not in name_two):
        return name_one, name_two

    # Return old if dash in both
    if ('-' in name_one) and ('-' in name_two):
        return name_one, name_two
    
    # Try replacing the dash with a space, and combine words if necessary
    name_one_edited = name_one.replace('-', ' ')
    name_two_edited = name_two.replace('-', ' ')
    if not name_one_edited:
        name_one_edited = '_'
    if not name_two_edited:
        name_two_edited = '_'
    _, name_one_edited, name_two_edited = _combine_split_words(name_one_edited, name_two_edited)

    # Return old if the score did not improve
    diff, _, _ = usefulTools.calculate_edit_improvement(name_one, name_two, name_one_edited, name_two_edited)
    if diff <= 0:
        return name_one, name_two
    
    # Return the edited names
    return name_one_edited, name_two_edited

def _combine_split_words(name_one:str, name_two:str) -> tuple[str, str]:
    """Combines words within one of the names if that combination is one word in the other name.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    words_in_name_one = name_one.split()

    # Do not combine words that are only two in length
    if len(words_in_name_one) < 3:
        return False, name_one, name_two
    
    # Do not combine words that are already a good spelling match
    if comparisonsMod.compare_spelling(name_one, name_two)[0]:
        return False, name_one, name_two
    
    for index_one, _, word_one, word_two in usefulTools.get_matching_words_and_indices(name_one, name_two):
        # Skip if word_one and word_two are not a good match
        if (fuzz.partial_ratio(word_one, word_two) < 75):
            continue

        # Skip if either word is only an initial
        if (len(word_one) == 1) or (len(word_two) == 1):
            continue

        # Find the left and right neighbors
        left_neighbor = words_in_name_one[index_one - 1] if index_one - 1 >= 0 else ''
        right_neighbor = words_in_name_one[index_one + 1] if index_one + 1 < len(words_in_name_one) else ''

        # Skip neighbors if they are initials
        left_neighbor = left_neighbor if len(left_neighbor) > 1 else ''
        right_neighbor = right_neighbor if len(right_neighbor) > 1 else ''
        if (not left_neighbor) and (not right_neighbor):
            return False, name_one, name_two

        # Choose the neighbor that best matches word_one's match and return needed variables related to it
        chosen_neighbor, compound, neighbor_index = _choose_best_neighbor_word(word_one, index_one, word_two, left_neighbor, right_neighbor)

        # Skip if the neighbor is a bad partial match to word_two's match
        if fuzz.partial_ratio(chosen_neighbor, word_two) < 65:
            continue

        # Check if the compound is significantly better than the original
        original_score = fuzz.ratio(word_one, word_two)
        compound_score = fuzz.ratio(compound, word_two)
        if compound_score < original_score + 20:
            continue
        difference_of_original_lengths = abs(len(word_two) - len(word_one))
        difference_of_compound_lengths = abs(len(word_two) - len(compound))
        if difference_of_original_lengths < difference_of_compound_lengths:
            continue

        # If the compound was a better match, use a name editor to create an edited name_one where the words are combined
        ne = usefulTools.NameEditor(name_one, name_two)
        ne.update_name_one(index_one, compound)
        ne.update_name_one(neighbor_index, '')
        name_one_edited, _ = ne.get_modified_names()

        # If the edited name_one is better (or only slightly worse), go with the edited version
        improvement = usefulTools.calculate_edit_improvement(name_one, name_two, name_one_edited, name_two)[0]
        if improvement > -1:
            return True, name_one_edited, name_two

    # If no edits were beneficial, just return the original words
    return False, name_one, name_two

def _fix_related_prefixes(name_one:str, name_two:str, prefix_variant_one:str, prefix_variant_two:str) -> tuple[str, str]:
    """Cleans names to deal with prefixes that are different by spelling, but functionally the same.

    Args:
        name_one (str): a name
        name_two (str): a name
        prefix_variant_one (str): the first related prefix
        prefix_variant_two (str): the second related prefix

    Returns:
        tuple[str, str]: the two modified names
    """        
    # Return if prefix_variant_one in neither or prefix_variant_two in neither
    if (f' {prefix_variant_one}' not in name_one) and (f' {prefix_variant_one}' not in name_two):
        return name_one, name_two
    if (f' {prefix_variant_two}' not in name_one) and (f' {prefix_variant_two}' not in name_two):
        return name_one, name_two

    # Return if prefix_variant_one or prefix_variant_two is found in both
    if (f' {prefix_variant_one}' in name_one) and (f' {prefix_variant_one}' in name_two):
        return name_one, name_two
    if (f' {prefix_variant_two}' in name_one) and (f' {prefix_variant_two}' in name_two):
        return name_one, name_two
    
    # Replace prefix_variant_two with prefix_variant_one
    if f' {prefix_variant_two}' in name_one:
        name_one = name_one.replace(f' {prefix_variant_two}', f' {prefix_variant_one}')
    else:
        name_two = name_two.replace(f' {prefix_variant_two}', f' {prefix_variant_one}')
    return name_one, name_two

def _choose_best_neighbor_word(word_one: str, index_one: int, word_two: str, left_neighbor: str, right_neighbor: str) -> tuple[str, str, int]:
    """This function looks at the words that are directly to the right and left of a specific word and then
    performs a partial ratio to figure out which word is a better match for the specific word. It then
    returns the compund.
    
    Args:
        word_one: The word that is being checked for matches
        index_one: The index of the word that is being checked for matches
        word_two: A word used as a reference point in comparison to the selected word
        left_neighbor: The word to the left of a selected word
        right_neighbor: The word to the right of a selected word

    Returns:
        Three items as a tuple, containing the better neighbor word choice, the compuond of the selected
        word and the better neighbor, and the index of the word that is selected as a better neighbor
    """

    # Choose the neighbor that best matches word_one's match
    if not left_neighbor:
        was_left_chosen = False
    elif not right_neighbor:
        was_left_chosen = True
    else:
        left_score = fuzz.partial_ratio(left_neighbor, word_two)
        right_score = fuzz.partial_ratio(right_neighbor, word_two)
        if left_score > right_score:
            was_left_chosen = True
        else:
            was_left_chosen = False

    # Initialize the chosen neighbor, compound, and neighbor index
    if was_left_chosen:
        chosen_neighbor = left_neighbor
        compound = f'{left_neighbor}{word_one}'
        neighbor_index = index_one - 1
    else:
        chosen_neighbor = right_neighbor
        compound = f'{word_one}{right_neighbor}'
        neighbor_index = index_one + 1

    return chosen_neighbor, compound, neighbor_index

def _fix_mc_and_mac_names(name_one:str, name_two:str) -> tuple[str, str]:
    """Modified names to fix problems where mc or mac are in either names and don't match when they should.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the two modified names 
    """        
    # Return names if no prefixes are in them
    if _determine_if_skip_names_in_fix_mc_and_mac_names(name_one, name_two):
        return name_one, name_two
    
    # Combine split words (if any)
    _, name_one, name_two = _combine_split_words(name_one, name_two)
    
    # Edit the names, if necessary
    ne = usefulTools.NameEditor(name_one, name_two)
    for prefix in ['mc', 'mac']:
        for index_one, index_two, word_one, word_two in usefulTools.get_matching_words_and_indices(name_one, name_two):
            # Skip pair if the prefix is in both words
            if (word_one.startswith(prefix)) and (word_two.startswith(prefix)):
                continue

            # Skip pair if the prefix is not in either of them
            if (not word_one.startswith(prefix)) and (not word_two.startswith(prefix)):
                continue

            # Skip pair if either word is a firstname
            if (index_one < 1) or (index_two < 1):
                continue

            # Skip pair if the shortest word is only 4 long
            if min(len(word_one), len(word_two)) < 3:
                continue

            # Skip pair if they are already a solid match
            if fuzz.ratio(word_one, word_two) > 80:
                continue

            # Skip pair if the prefix is removed and not a good fuzzy match
            if word_one.startswith(prefix):
                updated_word_one = word_one.replace(prefix, '', 1)
                updated_word_two = word_two
            else:
                updated_word_one = word_one
                updated_word_two = word_two.replace(prefix, '', 1)
            if fuzz.ratio(updated_word_one, updated_word_two) < 75:
                continue

            # Update the words
            ne.update_name_one(index_one, updated_word_one)
            ne.update_name_two(index_two, updated_word_two)

    # Return the edited (or not) names
    return ne.get_modified_names()

def _determine_if_skip_names_in_fix_mc_and_mac_names(name_one: str, name_two: str) -> bool:
    """A simple function to determine if the prefixes 'mc' or 'mac' are in two selected names to
    decide if names should be skipped in the _fix_mc_and_mac_names function.
    
    Args:
        name_one: The first name to be checked
        name_two: The second name to be checked
        
    Returns:
        True if 'mc' and 'mac' are absent from all of the names, indicating that the function can
        skip them. Otherwise, returns false indicating that they need further checks"""

    if ("mc" not in name_one) and ("mac" not in name_one) and ("mc" not in name_two) and ("mac" not in name_two):
        return True
    else:
        return False

def _remove_irish_o(name_one:str, name_two:str, surname:str) -> tuple[str, str]:
    """Removes the irish O if needed for easier name comparison.

    Args:
        name_one (str): a name
        name_two (str): a name
        surname (str): one of the irish surnames that often starts with O'

    Returns:
        tuple[str, str]: the modified names
    """        
    # Edit the names
    surname_one = name_one.split()[-1]
    if fuzz.ratio(surname_one, surname) > 75:
        if surname_one[0] == 'o':
            name_one = name_one.replace(f'{surname_one}', surname)
        else:
            name_one = name_one.replace(f'o {surname_one}', surname)
    surname_two = name_two.split()[-1]
    if fuzz.ratio(surname_two, surname) > 75:
        if surname_two[0] == 'o':
            name_two = name_two.replace(f'{surname_two}', surname)
        else:
            name_two = name_two.replace(f'o {surname_two}', surname)
    return name_one, name_two


def _remove_unnecessary_prefixes(prefix:str, name_one:str = "_", name_two:str = "_") -> tuple[str,str]:
    """Removes an unnecessary prefix from either or both of the names if
    it would make it harder to detect a name match.

    Args:
        prefix (str): the prefix to (probably) remove
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str,str]: the modified names
    """        
    # If the prefix is not in either names, return the names
    if (f" {prefix}" not in name_one) and (f" {prefix}" not in name_two):
        return name_one, name_two
    
    # If the names are already a good match, return the names
    if comparisonsMod.compare_spelling(name_one, name_two)[0]:
        return name_one, name_two

    # Setup
    name_one_edited = name_one
    name_two_edited = name_two
    space_then_prefix_then_space = f" {prefix} "
    space_then_prefix = f" {prefix}"

    # Make the edited names different
    if (space_then_prefix_then_space in name_one) and (space_then_prefix_then_space in name_two):
        pass
    elif (space_then_prefix_then_space in name_one) and (space_then_prefix in name_two):
        name_one_edited = name_one_edited.replace(space_then_prefix_then_space, space_then_prefix)
    elif (space_then_prefix in name_one) and (space_then_prefix_then_space in name_two):
        name_two_edited = name_two_edited.replace(space_then_prefix_then_space, space_then_prefix)
    name_one_edited = name_one_edited.replace(space_then_prefix_then_space, " ")
    name_two_edited = name_two_edited.replace(space_then_prefix_then_space, " ")
    name_one_edited = re.sub(r"\s+", " ", name_one_edited)
    name_two_edited = re.sub(r"\s+", " ", name_two_edited)
    no_edits_made = (name_one == name_one_edited) and (name_two == name_two_edited) 

    # If no edits were made, try removing space_then_prefix if only in name_one and it's a long word
    if no_edits_made:
        name_one, no_edits_made = _remove_space_then_prefix_from_unedited_name(prefix, space_then_prefix, name_one, name_two)

    # If no edits were made, try removing space_then_prefix if only in name_two and it's a long word
    if no_edits_made:
        name_two, no_edits_made = _remove_space_then_prefix_from_unedited_name(prefix, space_then_prefix, name_two, name_one)

    # If the edits were significantly beneficial (or pass spell), return the edited versions
    improvement, _, _= usefulTools.calculate_edit_improvement(name_one, name_two, name_one_edited, name_two_edited)
    if (improvement >= 10) or comparisonsMod.compare_spelling(name_one_edited, name_two_edited)[0]:
        return name_one_edited, name_two_edited
    
    # Finally, if the names are identical other than the prefix, remove the prefix
    name_one, name_two = _remove_prefix_if_prefix_is_only_difference_in_names(prefix, name_one, name_two)
    return name_one, name_two

def _remove_prefix_if_prefix_is_only_difference_in_names(prefix: str, name_one: str, name_two: str) -> tuple[str, str]:
    """This is a helper function for _remove_unnecessary_prefixes that is intended to help
    resolve its cyclomatic complexity. This function will remove a prefix from two names 
    that are identical outside of the prefix.
    
    Args:
        prefix: The prefix to check to see if it is the only difference
        name_one: The first name to compare and possibly remove a prefix from
        name_two: The second name to compare and possibly remove a prefix from
        
    Returns:
        A tuple containing two names, modified to remove the prefix if they are identical, 
        or the names as input if they aren't identical outside of the prefix"""
    
    ne = usefulTools.NameEditor(name_one, name_two)
    for index_one, index_two, word_one, word_two in usefulTools.get_matching_words_and_indices(name_one, name_two):
        if (word_one.startswith(prefix)) and (word_one[len(prefix):] == word_two) and (len(word_two) > 2):
            ne.update_name_one(index_one, word_one[len(prefix):])
        elif (word_two.startswith(prefix)) and (word_two[len(prefix):] == word_one) and (len(word_one) > 2):
            ne.update_name_two(index_two, word_two[len(prefix):])
    name_one, name_two = ne.get_modified_names()

def _remove_space_then_prefix_from_unedited_name(prefix: str, space_then_prefix: str, name_to_possibly_change: str, other_name: str) -> tuple[str, bool]:
    """This is a helper function for _remove_unnecessary_prefixes that is intended to remove
    the " prefix" pattern from words that may or may not have it, if the same pattern is not
    present in a second word. The utility of this is to create parity between different name
    parts so they can be accurately compared later.
    
    Args:
        prefix: The possible prefix that needs to be removed
        space_then_prefix: A string containing a space before the prefix, used for boolean
            comparisons and regex matching
        name_to_possibly_change: The name to check for needed changes
        other_name: The name to compare the target name to, to check for needed changes 
        
    Returns:
        This returns a tuple containing the end result of the name changes if there were any,
        or the unchanged name, and a boolean variable indicating if any changes were made to
        name_to_possibly_change during this function call
    """

    edit_happened = False
    pattern = r'\b{}\w*\b'.format(space_then_prefix)
    space_then_prefix_only_in_name_to_change = (space_then_prefix in name_to_possibly_change) and (space_then_prefix not in other_name)
    match_in_name_to_change = re.search(pattern, name_to_possibly_change)
    if (space_then_prefix_only_in_name_to_change) and (match_in_name_to_change is not None):
        matched_word = match_in_name_to_change.group()
        if len(matched_word) > len(prefix) + 4:
            name_to_possibly_change = name_to_possibly_change.replace(space_then_prefix, " ")
            edit_happened = True
    
    return name_to_possibly_change, edit_happened

def _combine_prefix_with_surname_if_in_both(name_one:str, name_two:str, prefix:str) -> tuple[str, str]:
    """Combines the prefix with the surname in both of the names if the prefix exists in both.

    Args:
        name_one (str): a name
        name_two (str): a name
        prefix (str): the prefix to combine with the surname

    Returns:
        tuple[str, str]: the modified names
    """        
    # Return if ' prefix ' in neither
    if (not re.search(f' {prefix} .', name_one)) or (not re.search(f' {prefix} .', name_two)):
        return name_one, name_two
    
    # Get the letter after ' prefix '
    letter_one = name_one[name_one.index(f' {prefix} ') + 4]
    letter_two = name_two[name_two.index(f' {prefix} ') + 4]

    # If the letter after matches, replace ' prefix ' with ' prefix'
    if letter_one == letter_two:
        name_one = name_one.replace(f' {prefix} ', f' {prefix}')
        name_two = name_two.replace(f' {prefix} ', f' {prefix}')
    return name_one, name_two

def clean_ipa(ipa:str) -> str:
    """Cleans ipa to get rid of double ipa-consonants and other mistakes.

    Args:
        ipa (str): the ipa of a word

    Returns:
        str: the cleaned ipa
    """        
    all_ipa_consonants = ['l', 'd', 'z', 'b', 't', 'k', 'n', 's', 'w', 'v', 'ð', 'ʒ', 'ʧ', 'θ', 'h', 'g', 'ʤ', 'ŋ', 'p', 'm', 'ʃ', 'f', 'j', 'r']
    for consonant in all_ipa_consonants:
        double_consonant = consonant + consonant
        if double_consonant in ipa:
            ipa = ipa.replace(double_consonant, consonant)
    ipa = ipa.replace("ɛɛ", "i")
    ipa = ipa.replace("ɪɪ", "ɪ")
    ipa = ipa.replace("iɪ", "i")
    ipa = ipa.replace("ŋg", "ŋ")
    ipa = ipa.replace(",", "")
    if not ipa:
        ipa = '_'
    return ipa