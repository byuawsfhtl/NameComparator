from re import sub as re_sub, search as re_search
from unidecode import unidecode
from rapidfuzz.fuzz import ratio as fuzz_ratio, partial_ratio as fuzz_partial_ratio

from NameComparator.src.comparisons import compare_spelling
from NameComparator.src.useful_tools import calculate_edit_improvement, get_matching_words_and_indices, NameEditor

from json import loads as json_loads
from pathlib import Path
prefix_list = json_loads((Path(__file__).parent.parent.parent / 'data/possiblePrefixList.json').read_text(encoding='utf-8'))


def clean_name(name:str) -> str:
    """Cleans a singular name to get rid of extra or unhelpful data, and to standardize surnames.

    Args:
        name: the name to clean

    Returns:
        A string containing the cleaned name
    """        
    # Deal with blank names
    if (name == "") or (not isinstance(name, str)):
        return "_"

    # Deal with whitespace
    name = re_sub(r'[^\S ]', ' ', name)
    name = re_sub(r" +", " ", name)
    name = name.strip()

    # Standardize name into ascii
    name = unidecode(name)
    name = name.lower()

    # Deal with blank names again
    if name == "":
        return "_"

    # Remove Punctuation
    name = re_sub(r"[.,?;\"*()]", "", name)

    # Remove spaces after apostrophe
    name = re_sub("' +", "'", name)

    # Remove jr and sr
    name = re_sub(r"\bjr\b", "", name).replace(r"\bjunior\b", "")
    name = re_sub(r"\bsr\b", "", name).replace(r"\bsenior\b", "")

    # Remove titles
    name = re_sub(r"\bprof\b", "", name).replace(r"\bprofessor\b", "")
    name = re_sub(r"\bmr\b", "", name).replace(r"\bmister\b", "")
    name = re_sub(r"\bmrs\b", "", name).replace(r"\bmissus\b", "")
    name = re_sub(r"\bms\b", "", name).replace(r"\bmiss\b", "")
    name = re_sub(r"\bdr\b", "", name).replace(r"\bdoctor\b", "")
    name = re_sub(r"\bstudent\b", "", name)
    name = re_sub(r"\brev\b", "", name)
    name = name.replace("reverend", "")

    # Remove family relations
    name = re_sub(r"\bsister\b", "", name)
    name = re_sub(r"\bbrother\b", "", name)
    name = re_sub(r"\bmother\b", "", name)
    name = re_sub(r"\bfather\b", "", name)
    name = re_sub(r" in law", " ", name)

    # Removes "head of household"
    name = name.replace("head of household", "")

    # Remove common abbreviations
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
    name = re_sub(r"[1-9][a-z]2,6", "", name).replace(" the ", "")

    # Remove Roman numerals
    name = ' '.join(re_sub(r'\b(ii|iii|iv)\b', '', word) for word in name.split()) # Remove Roman numerals ii, iii, iv
    name = re_sub(r" +", " ", name)
    name = name.strip()

    # Remove 'no suffix'
    name = name.replace("no suffix", "")

    # Deal with Dutch names
    # name = re_sub(r"\bvan de", "vande", name)
    # name = re_sub(r"\bvan den", "vanden", name)
    # name = re_sub(r"\bvan der", "vander", name)
    
    # Deal with whitespace one last time, then return
    name = re_sub(r" +", " ", name)
    name = name.strip()
    if not name:
        name = '_'

    return name

def clean_names_by_comparison(name_one:str = '_', name_two:str = '_') -> tuple[str, str, bool]:
    """Cleans names by comparing them to one another, fixing common errors to standardize.

    Args:
        name_one: The first name to clean
        name_two: The second name to clean

    Returns:
        A tuple containing the two cleaned names and a boolean noting whether or not
        to perform a confidence penalty based on if a prefix was removed
    """        

    should_penalty_apply = False
    was_prefix_modified = False
    was_irish_o_removed = False

    # Return if either name is blank
    if (name_one == '_') or (name_two == '_'):
        return name_one, name_two, False
    
    # Deal with dashes
    name_one, name_two = _deal_with_dashes(name_one, name_two)

    # Deal with just Irish 'O' names
    name_one, name_two, was_irish_o_removed = _handle_irish_o_in_names(name_one, name_two)

    # Determine if there is a floating prefix that should be removed before making any other changes
    name_one_segments = name_one.split()
    name_two_segments = name_two.split()

    # Compare the first letters. If something looks like a prefix, see if it matches the first letters of 
    # anything else in the other name. If it doesn't, we can just delete it
    name_one = _remove_floating_prefix_if_unnecessary(name_one_segments, name_two_segments)
    name_two = _remove_floating_prefix_if_unnecessary(name_two_segments, name_one_segments) 

    # Figure out what else needs to be done with prefixes in the names and make needed changes
    name_one, name_two, was_prefix_modified = _handle_prefixes_in_names(name_one, name_two)

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
    name_one = re_sub(r'\s+', ' ', name_one)
    name_one = name_one.strip()
    name_two = re_sub(r'\s+', ' ', name_two)
    name_two = name_two.strip()

    if was_prefix_modified or was_irish_o_removed:
        should_penalty_apply = True

    # Return the cleaned names
    return name_one, name_two, should_penalty_apply

def _handle_irish_o_in_names(name_one: str, name_two: str) -> tuple[str, str, bool]:
    """Removes irish 'o's from a name if it's appropriate as part of the name 
    cleaning process.
    
    Args:
        name_one: The first name to check for irish 'o's in
        name_two: The second name to check for irish 'o's in
        
    Returns:
        A tuple containing the two names after handling the irish 'o's and a boolean
        representing whether or not an o was removed
    """

    was_irish_o_removed = False

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
            removed_o_this_run = False
            if (surname in name_one) or (surname in name_two):
                name_one, name_two, removed_o_this_run = _remove_irish_o(name_one, name_two, surname)
            if removed_o_this_run:
                was_irish_o_removed = True

    return name_one, name_two, was_irish_o_removed

def _handle_prefixes_in_names(name_one: str, name_two: str) -> tuple[str, str, bool]:
    """This is a helper function for clean_names_by_comparison that helps manage its
    cyclomatic complexity. It takes in two names that are going to be compared later
    on and figures out what needs to be done with prefixes that might be on them to
    ensure that later standardization goes smoothly.
    
    Args:
        name_one: The first name to run prefix checks and handling on
        name_two: The second name to run prefix checks and handling on
        
    Returns:
        A tuple containing the input names, with prefixes modified in a way that lets
        them be standardized later on. After this contains a boolean describing whether
        or not a prefix was removed from a name
    """

    # Deal with any prefixes and optional intros that make the match worse
    name_one = re_sub(r"\s+", " ", name_one)
    name_one = name_one.strip()
    name_two = re_sub(r"\s+", " ", name_two)
    name_two = name_two.strip()
    was_a_prefix_modified = False

    for prefix in prefix_list:
        if (f" {prefix}" in name_one) or (f" {prefix}" in name_two):

            did_we_fix_prefixes = False
            did_we_remove_prefixes = False

            if (prefix == 'de') or (prefix == 'di'):
                name_one, name_two, did_we_fix_prefixes = _fix_related_prefixes(name_one, name_two, 'de', 'di')
                name_one, name_two, did_we_remove_prefixes = _remove_unnecessary_prefixes("de", name_one, name_two)
                # name_one, name_two = _combine_prefix_with_surname_if_in_both(name_one, name_two, "de")
            elif (prefix == 'del') or (prefix == 'dil'):
                name_one, name_two, did_we_fix_prefixes = _fix_related_prefixes(name_one, name_two, 'del', 'dil')
                name_one, name_two, did_we_remove_prefixes = _remove_unnecessary_prefixes("del", name_one, name_two)
            elif prefix == 'van':
                name_one, name_two, did_we_remove_prefixes = _remove_unnecessary_prefixes("van", name_one, name_two)
                # name_one, name_two = _combine_prefix_with_surname_if_in_both(name_one, name_two, "van")
            elif (prefix == 'mc') or (prefix == 'mac'):
                name_one, name_two, did_we_fix_prefixes = _fix_related_prefixes(name_one, name_two, 'mac', 'mc')
                name_one, name_two, did_we_remove_prefixes = _fix_mc_and_mac_names(name_one, name_two)
            else:
                name_one, name_two, did_we_remove_prefixes = _remove_unnecessary_prefixes(prefix, name_one, name_two)

            if did_we_fix_prefixes or did_we_remove_prefixes:
                was_a_prefix_modified = True

    return name_one, name_two, was_a_prefix_modified

def _deal_with_dashes(name_one:str, name_two:str) -> tuple[str, str]:
    """Cleans both names in order to deal with dashes in names.

    Args:
        name_one: a name
        name_two: a name

    Returns:
        A tuple containing the modified names with consistency in dashes
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
    diff, _, _ = calculate_edit_improvement(name_one, name_two, name_one_edited, name_two_edited)
    if diff <= 0:
        return name_one, name_two
    
    # Return the edited names
    return name_one_edited, name_two_edited

def _combine_split_words(name_one:str, name_two:str, optional_name_one_for_comparisons: str|None = None) -> tuple[bool, str, str]:
    """Combines words within one of the names if that combination is one word in the other name.

    Args:
        name_one: The first name to clean
        name_two: The second name to clean
        optional_name_one_for_comparisons: An optional field that will compare recursive runs
            of this function to this name rather than whatever is put into the 'name one'
            variable. Defaults to None

    Returns:
        A tuple containing whether or not the names were modified and the modified names
    """        

    words_in_name_one = name_one.split()

    # Do not combine words that are only two in length
    if len(words_in_name_one) < 3:
        return False, name_one, name_two
    
    for index_one, index_two, word_one, word_two in get_matching_words_and_indices(name_one, name_two):

        # Skip if word_one and word_two are not a good match
        if (fuzz_partial_ratio(word_one, word_two) < 75):
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
        if fuzz_partial_ratio(chosen_neighbor, word_two) < 65:
            continue

        # Check if the compound is significantly better than the original
        original_score = fuzz_ratio(word_one, word_two)
        compound_score = fuzz_ratio(compound, word_two)
        if compound_score < original_score + 20:
            continue
        difference_of_original_lengths = abs(len(word_two) - len(word_one))
        difference_of_compound_lengths = abs(len(word_two) - len(compound))
        if difference_of_original_lengths < difference_of_compound_lengths:
            continue

        # If the compound was a better match, use a name editor to create an edited name_one where the words are combined
        name_editor_instance = NameEditor(name_one, name_two)
        name_editor_instance.update_name_one(index_one, compound)
        name_editor_instance.update_name_one(neighbor_index, '')
        name_one_edited, not_used = name_editor_instance.get_modified_names()

        # If we get to this point, it's worth checking for another neighbor word that may match situationally
        did_another_pass_improve_it_more, updated_name_result, ignore = _combine_split_words(name_one_edited, name_two, name_one)
        if did_another_pass_improve_it_more:
            name_one_edited = updated_name_result

        # If the edited name_one is better, go with the edited version
        if optional_name_one_for_comparisons:
            improvement, useless, useless_two = calculate_edit_improvement(optional_name_one_for_comparisons, name_two, name_one_edited, name_two)
        else:
            improvement, useless, useless_two = calculate_edit_improvement(name_one, name_two, name_one_edited, name_two)
        if improvement > 0:
            return True, name_one_edited, name_two

    # If no edits were beneficial, just return the original words
    return False, name_one, name_two

def _fix_related_prefixes(name_one:str, name_two:str, prefix_variant_one:str, prefix_variant_two:str) -> tuple[str, str, bool]:
    """Cleans names to deal with prefixes that are different by spelling, but functionally the same.

    Args:
        name_one: The first name to clean
        name_two: The second name to clean
        prefix_variant_one: The first related prefix to check
        prefix_variant_two: The second related prefix to check

    Returns:
        A tuple containing the two names, cleaned to have consistent prefixes, and a boolean
        representing if changes were made to either of the names
    """        


    # Return if prefix_variant_one in neither or prefix_variant_two in neither
    if (f' {prefix_variant_one}' not in name_one) and (f' {prefix_variant_one}' not in name_two):
        return name_one, name_two, False
    if (f' {prefix_variant_two}' not in name_one) and (f' {prefix_variant_two}' not in name_two):
        return name_one, name_two, False

    # Return if prefix_variant_one or prefix_variant_two is found in both
    if (f' {prefix_variant_one}' in name_one) and (f' {prefix_variant_one}' in name_two):
        return name_one, name_two, False
    if (f' {prefix_variant_two}' in name_one) and (f' {prefix_variant_two}' in name_two):
        return name_one, name_two, False
    
    # Replace prefix_variant_two with prefix_variant_one
    if f' {prefix_variant_two}' in name_one:
        name_one = name_one.replace(f' {prefix_variant_two}', f' {prefix_variant_one}')
    else:
        name_two = name_two.replace(f' {prefix_variant_two}', f' {prefix_variant_one}')

    return name_one, name_two, True

def _remove_floating_prefix_if_unnecessary(target_name_segments: list[str], other_name_segments: list[str]) -> str:
    """This function deteremines if there is a prefix in the name that is on it's own 
    (is floating) and then determines if it thinks it will be best to keep the prefix 
    or to remove it.
    
    Args:
        target_name_segments: All of the words / segments inside of the name that's going to 
            be modified
        other_name_segments: All of the words / segments inside of the name that's going to
            be compared against to see if the target name is going to be modified
            
    Returns:
        The updated target name as a string, updated to have removed any standalone 
        (floating) prefixes, if necessary
    """

    improved_name_segment_list = []
    previous_segment_was_merged = False

    for segment_index, name_segment in enumerate(target_name_segments):
        if previous_segment_was_merged:
            previous_segment_was_merged = False
            continue

        elif name_segment in prefix_list:
            add_to_improved_segment_list, previous_segment_was_merged = _iterate_through_and_compare_to_other_name_segments(target_name_segments, other_name_segments, segment_index, name_segment)
            improved_name_segment_list.extend(add_to_improved_segment_list)

        else:
            improved_name_segment_list.append(name_segment)

    return ' '.join(improved_name_segment_list)

def _iterate_through_and_compare_to_other_name_segments(target_name_segments: list[str], other_name_segments: list[str], segment_index: int, name_segment: str) -> tuple[list[str], bool]:
    """This is a helper function for _remove_floating_prefix_if_unnecessary that
    iterates through all of the name segments of the non-target word and then
    compares them to possible combinations of segments in the target word to see
    if one name is a combination of the others.
    
    Args:
        target_name_segments: The name segments of the word that we want to modify
        other_name_segments: The name segments to compare the target word's segments to
        segment_index: The index of the current segment that's being checked
        name_segment: The current name segment that's being checked
    
    Returns:
        A tuple containing a list of name segments to append to the final list
        of improved name segments and a boolean representing whether or not the
        previous segmetn was merged
    """
    improved_name_segment_list = []
    previous_segment_was_merged = False

    for segment_from_other_name in other_name_segments:
        if (segment_index + 2 <= len(target_name_segments)) and ((name_segment + target_name_segments[segment_index + 1]) == segment_from_other_name):
            improved_name_segment_list.append((name_segment + target_name_segments[segment_index + 1]))
            previous_segment_was_merged = True
            break
        elif name_segment[0] == segment_from_other_name[0]:
            improved_name_segment_list.append(name_segment)
            break

    return improved_name_segment_list, previous_segment_was_merged

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
        Three items as a tuple, containing the better neighbor word choice, the compound of the selected
        word and the better neighbor, and the index of the word that is selected as a better neighbor
    """

    # Choose the neighbor that best matches word_one's match
    if not left_neighbor:
        was_left_chosen = False
    elif not right_neighbor:
        was_left_chosen = True
    else:
        left_score = fuzz_partial_ratio(left_neighbor, word_two)
        right_score = fuzz_partial_ratio(right_neighbor, word_two)
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

def _fix_mc_and_mac_names(name_one:str, name_two:str) -> tuple[str, str, bool]:
    """Modifies names to fix problems where mc or mac are in either names and don't match when they should.

    Args:
        name_one: The first name to clean
        name_two: The second name to clean

    Returns:
        A tuple with the two names, modified to have matching 'mc' or 'mac' uses, and 
        a boolean representing whether or not the names were modified
    """        
    # Return names if mc and mac aren't in either of them
    if _determine_if_skip_names_in_fix_mc_and_mac_names(name_one, name_two):
        return name_one, name_two, False
    
    # Combine split words (if any)
    _, name_one, name_two = _combine_split_words(name_one, name_two)
    
    # Edit the names, if necessary
    name_editor_instance = NameEditor(name_one, name_two)
    was_mc_or_mac_removed = False
    for prefix in ['mc', 'mac']:
        for index_one, index_two, word_one, word_two in get_matching_words_and_indices(name_one, name_two):

            temp_flag_for_changes = False

            if _check_skip_cases_for_specific_word_pair_while_fixing_mc_and_mac_names(word_one, word_two, prefix, index_one, index_two):
                continue

            # Skip pair if the prefix is removed and not a good fuzzy match
            updated_word_one = word_one
            updated_word_two = word_two

            if word_one.startswith(prefix):
                updated_word_one = word_one.replace(prefix, '', 1)
                updated_word_two = word_two
                temp_flag_for_changes = True
            elif word_two.startswith(prefix):
                updated_word_one = word_one
                updated_word_two = word_two.replace(prefix, '', 1)
                temp_flag_for_changes = True

            if temp_flag_for_changes and (fuzz_ratio(updated_word_one, updated_word_two) < 75):
                continue

            # Update the words
            name_editor_instance.update_name_one(index_one, updated_word_one)
            name_editor_instance.update_name_two(index_two, updated_word_two)
            was_mc_or_mac_removed = temp_flag_for_changes
            temp_name_one, temp_name_two = name_editor_instance.get_modified_names()

    # Return the edited (or not) names
    edited_name_one, edited_name_two = name_editor_instance.get_modified_names()

    return edited_name_one, edited_name_two, was_mc_or_mac_removed

def _check_skip_cases_for_specific_word_pair_while_fixing_mc_and_mac_names(word_one: str, word_two: str, prefix: str, index_one: int, index_two: int) -> bool:
    """This is a helper function for fix_mc_and_mac_names that fixes cyclomatic
    complexity by moving all of the initial skip checks at the beginning of
    each for loop iteration into its own function.
    
    Args:
        word_one: The first word (name segment) in the for loop iteration
        word_two: The second word (name segment) in the for loop iteration
        prefix: The prefix to look for in the words
        index_one: The index of the first word in the for loop iteration
        index_two: The index of the second word in the for loop iteration
        
    Returns:
        A boolean representing if the current for loop iteration should be
        skipped
    """

    # Skip pair if the prefix is in both words
    if (word_one.startswith(prefix)) and (word_two.startswith(prefix)):
        return True

    # Skip pair if the prefix is not in either of them
    if (not word_one.startswith(prefix)) and (not word_two.startswith(prefix)):
        return True

    # Skip pair if either word is a firstname
    if (index_one < 1) or (index_two < 1):
        return True

    # Skip pair if the shortest word is less than 4 characters long
    if min(len(word_one), len(word_two)) < 4:
        return True

    # Skip pair if they are already a solid match
    if fuzz_ratio(word_one, word_two) > 80:
        return True
    
    return False

def _determine_if_skip_names_in_fix_mc_and_mac_names(name_one: str, name_two: str) -> bool:
    """A simple function to determine if the prefixes 'mc' or 'mac' are in two selected names to
    decide if names should be skipped in the _fix_mc_and_mac_names function.
    
    Args:
        name_one: The first name to check
        name_two: The second name to check
        
    Returns:
        True if 'mc' and 'mac' are absent from all of the names, indicating that the function can
        skip them. Otherwise, returns false indicating that they need further checks"""

    return ("mc" not in name_one) and ("mac" not in name_one) and ("mc" not in name_two) and ("mac" not in name_two)

def _remove_irish_o(name_one:str, name_two:str, surname:str) -> tuple[str, str, bool]:
    """Removes the irish O if needed for easier name comparison.

    Args:
        name_one: The first name to remove a possible Irish o from
        name_two: The second name to remove a possible Irish o from
        surname: One of the irish surnames that often starts with O'

    Returns:
        A tuple containing the two modified names with the Irish o removed
        if appropriate and a boolean representing whether an o was removed
    """      

    old_name_one = name_one
    old_name_two = name_two
    was_o_removed = False

    # Edit the names
    surname_one = name_one.split()[-1]
    if fuzz_ratio(surname_one, surname) > 75:
        if surname_one[0] == 'o':
            name_one = name_one.replace(f'{surname_one}', surname)
            if (old_name_one != name_one):
                was_o_removed = True
        else:
            name_one = name_one.replace(f'o {surname_one}', surname)
            if (old_name_one != name_one):
                was_o_removed = True
    surname_two = name_two.split()[-1]
    if fuzz_ratio(surname_two, surname) > 75:
        if surname_two[0] == 'o':
            name_two = name_two.replace(f'{surname_two}', surname)
            if (old_name_two != name_two):
                was_o_removed = True
        else:
            name_two = name_two.replace(f'o {surname_two}', surname)
            if (old_name_two != name_two):
                was_o_removed = True

    return name_one, name_two, was_o_removed

def _remove_unnecessary_prefixes(prefix:str, name_one:str = "_", name_two:str = "_") -> tuple[str, str, bool]:
    """Removes an unnecessary prefix from either or both of the names if
    it would make it harder to detect a name match.

    Args:
        prefix: The prefix to (probably) remove from the names
        name_one: The first name to remove a possible prefix from
        name_two: The second name to remove a possible prefix from

    Returns:
        A tuple containing the two names, modified to have their prefixes removed
        if it's easier to find a name match without them. After this it has a
        boolean representing whether or not a prefix was removed
    """        

    if not _check_for_early_return_in_remove_unnecessary_prefixes(prefix, name_one, name_two):
        return name_one, name_two, False

    # Setup
    name_one_edited = name_one
    name_two_edited = name_two
    space_then_prefix_then_space = f" {prefix} "
    space_then_prefix = f" {prefix}"

    edits_made = False

    # If the names have different prefix patterns, make them match the same one
    if (space_then_prefix_then_space in name_one_edited) and (space_then_prefix in name_two_edited) and (space_then_prefix_then_space not in name_two_edited):
        name_one_edited = name_one_edited.replace(space_then_prefix_then_space, space_then_prefix)
        edits_made = True
    elif (space_then_prefix in name_one_edited) and (space_then_prefix_then_space in name_two_edited) and (space_then_prefix_then_space not in name_one_edited):
        name_two_edited = name_two_edited.replace(space_then_prefix_then_space, space_then_prefix)
        edits_made = True

    # If no edits were made, try removing space_then_prefix if only in name_one and it's a long word
    if not edits_made:
        name_one_edited, edits_made = _remove_space_then_prefix_from_unedited_names(prefix, space_then_prefix, name_one_edited, name_two_edited)

    # If no edits were made, try removing space_then_prefix if only in name_two and it's a long word
    if not edits_made:
        name_two_edited, edits_made = _remove_space_then_prefix_from_unedited_names(prefix, space_then_prefix, name_two_edited, name_one_edited)

    # If the edits were significantly beneficial (or pass spell), return the edited versions
    improvement, _, _= calculate_edit_improvement(name_one, name_two, name_one_edited, name_two_edited)
    if (improvement >= 10) and compare_spelling(name_one_edited, name_two_edited)[0]:
        return name_one_edited, name_two_edited, edits_made
    
    # Finally, if the names are identical other than the prefix, remove the prefix
    name_one_edited, name_two_edited, prefix_removed = _remove_prefix_if_prefix_is_only_difference_in_names(prefix, name_one_edited, name_two_edited)

    if prefix_removed or edits_made:
        edits_made = True
    else:
        edits_made = False

    # At the end of the function, check for improvments. If it's actually better, return the edits otherwise
    # return the original one
    final_improvement_check, _, _= calculate_edit_improvement(name_one, name_two, name_one_edited, name_two_edited)
    if final_improvement_check > 0:
        return name_one_edited, name_two_edited, edits_made
    else:
        return name_one, name_two, False
    
def _check_for_early_return_in_remove_unnecessary_prefixes(prefix: str, name_one: str, name_two: str) -> bool:
    """This is a helper function designed to reduce cyclomatic complexity in
    _remove_unnecessary_prefixes by figuring out the early return cases for it
    in a separate function.
    
    Args:
        prefix: The prefix to check for in the names
        name_one: The first name to check for a prefix that needs to be removed
        name_two: The second name to check for a prefix that needs to be removed
        
    Returns:
        A boolean representing whether or not the _remove_unnecessary_prefixes
        call would accomplish anything
    """
    # If the prefix is not in either names, return the names
    if (f" {prefix}" not in name_one) and (f" {prefix}" not in name_two):
        return False
    
    # If the names are already a good match, return the names
    if compare_spelling(name_one, name_two)[0]:
        return False
    
    return True

def _remove_prefix_if_prefix_is_only_difference_in_names(prefix: str, name_one: str, name_two: str) -> tuple[str, str, bool]:
    """This is a helper function for _remove_unnecessary_prefixes that is intended to help
    resolve its cyclomatic complexity. This function will remove a prefix from two names 
    that are identical outside of the prefix.
    
    Args:
        prefix: The prefix to check to see if it is the only difference
        name_one: The first name to compare and possibly remove a prefix from
        name_two: The second name to compare and possibly remove a prefix from
        
    Returns:
        A tuple containing two names, modified to remove the prefix if they are identical, 
        or the names as input if they aren't identical outside of the prefix. It also has
        a boolean after this, representing whether or not a prefix was removed
    """
    
    name_editor_instance = NameEditor(name_one, name_two)
    name_edited = False

    for index_one, index_two, word_one, word_two in get_matching_words_and_indices(name_one, name_two):
        if (word_one.startswith(prefix)) and (word_one[len(prefix):] == word_two) and (len(word_two) > 2):
            name_editor_instance.update_name_one(index_one, word_one[len(prefix):])
            name_edited = True
        elif (word_two.startswith(prefix)) and (word_two[len(prefix):] == word_one) and (len(word_one) > 2):
            name_editor_instance.update_name_two(index_two, word_two[len(prefix):])
            name_edited = True

    name_one, name_two = name_editor_instance.get_modified_names()

    return name_one, name_two, name_edited

def _remove_space_then_prefix_from_unedited_names(prefix: str, space_then_prefix: str, name_to_possibly_change: str, other_name: str) -> tuple[str, bool]:
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
        This returns a tuple containing the end result of the name changes if there were any
        (or the unchanged name) and a boolean variable indicating if any changes were made to
        name_to_possibly_change during this function call
    """

    edit_happened = False
    pattern = r'\b{}\w*\b'.format(space_then_prefix)
    is_space_then_prefix_only_in_name_to_change = (space_then_prefix in name_to_possibly_change) and (space_then_prefix not in other_name)
    match_in_name_to_possibly_change = re_search(pattern, name_to_possibly_change)
    if ((is_space_then_prefix_only_in_name_to_change) and (match_in_name_to_possibly_change is not None)):
        matched_word = match_in_name_to_possibly_change.group()
        if (len(matched_word) > len(prefix) + 4):
            name_to_possibly_change = name_to_possibly_change.replace(space_then_prefix, " ")
            edit_happened = True
    
    return name_to_possibly_change, edit_happened

def _combine_prefix_with_surname_if_in_both(name_one:str, name_two:str, prefix:str) -> tuple[str, str]:
    """Combines the prefix with the surname in both of the names if the prefix exists in both.

    Args:
        name_one: The first name to possibly modify
        name_two: The second name to possibly modify
        prefix: The prefix to combine with the surname

    Returns:
        A tuple containing the names with any changes that were made to them or the unchanged
        names
    """        
    # Return if ' prefix ' in neither
    if (not re_search(f' {prefix} .', name_one)) or (not re_search(f' {prefix} .', name_two)):
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