from NameComparator.NameComparator import compare_two_names
from re import split as re_split

# TODO: Consider coming up with logic that can use the list of nicknames
# to determine possible full names for a person when a nickname or
# shorthand version is used

def extrapolate_best_full_name(input_list_of_names: list, multiple_possible_matches_dictionary: dict | None = None, name_fragments_and_frequency: list | None = None) -> tuple[str, dict, list]:
    """This function takes in a list of names for a single person
    and then determines what the most likely best full name is based on 
    that list, favoring having full names instead of initials or 
    abbreviations when possible.

    Args:
        input_list_of_names: A list of names that contains variations of a 
            name for a particular person
        multiple_possible_matches_dictionary: A dictionary of all of the
            possible name fragment matches and positions that are undetermined 
            for a particular name at the time of the start of this function
        name_fragments_and_frequency: A list of all of the name fragments
            that have been used for the name so far, their positions, and their
            frequencies
    
    Returns:
        A string representing the best or most complete version of a name,
        based on all of the input names and a dictionary containing all of
        the name fragments that haven't been used yet. Then a dictionary of
        all of the unused possible matches for name fragments. Then a list
        of all the name fragments and how frequently they appear
    """
    # If variables are None at the start of the function, set them to
    # a more appropriate empty dictionary or list
    if not multiple_possible_matches_dictionary:
        multiple_possible_matches_dictionary = {}

    if not name_fragments_and_frequency:
        name_fragments_and_frequency = []
    
    # If there is nothing in the list of names, we can't
    # determine the best name so return an empty string
    if not input_list_of_names:
        return '', {}, []
    
    cleaned_list_of_names = clean_name_list(input_list_of_names)
    
    # If there is only one name in the cleaned names, we can
    # safely say that's the best name in the list. Just
    # return it
    if len(cleaned_list_of_names) == 1:
        return cleaned_list_of_names[0], {}, []
    
    # Break all of the names into a collection of pieces I'm calling fragments
    broken_name_list, index_of_name_with_most_fragments, name_fragments_and_frequency = _break_names_into_fragments(cleaned_list_of_names, name_fragments_and_frequency)

    # Order the list of names according to the number of fragments in each name (from
    # largest to smalles) to ensure that the names are sorted as expected
    broken_name_list.sort(key = lambda item: item['total_fragments'], reverse = True)

    # Populate an initial array of strings equal to the length of the name with the most
    # fragments, using the fragments from that name as the starting point
    fragment_count_of_name_with_most_fragments = len(broken_name_list[index_of_name_with_most_fragments]['fragment_list'])
    best_name_as_fragments: list[dict] = []
    for initial_name_fragment in broken_name_list[index_of_name_with_most_fragments]['fragment_list']:
        best_name_as_fragments.append(initial_name_fragment)

    # Go through each of the name fragments and compare them to the current list of best fragments
    # to determine if there is a better possible name. Store unknown data to parse through later
    for broken_name in broken_name_list:
        # If the number of fragments matches the max number of fragments, we can probably safely assume that
        # the names have similar positions as long as their first letters match
        if len(broken_name['fragment_list']) == fragment_count_of_name_with_most_fragments:
            best_name_as_fragments, multiple_possible_matches_dictionary = _extrapolate_names_from_equal_length_fragments(broken_name, best_name_as_fragments, multiple_possible_matches_dictionary, name_fragments_and_frequency)
            print(f"Best name as fragments after extrapolating from equal length segments: {best_name_as_fragments}")

        # If the number of fragments doesn't match the max number of fragments, we'll need to handle the logic
        # a little bit differently
        else:
            best_name_as_fragments, multiple_possible_matches_dictionary = _extrapolate_names_from_different_length_fragments(broken_name, best_name_as_fragments, multiple_possible_matches_dictionary)
            print(f"Best name as fragments after extrapolating from different length segments: {best_name_as_fragments}")

    # After everything else is done, recompile the name fragments into one complete name and return it as a string
    complete_extrapolated_name = ''
    add_spaces_index_checker = 1
    for best_fragment in best_name_as_fragments:
        complete_extrapolated_name = complete_extrapolated_name + best_fragment['edited_fragment']
        if add_spaces_index_checker < len(best_name_as_fragments):
            complete_extrapolated_name = complete_extrapolated_name + ' '

    return complete_extrapolated_name.strip(), multiple_possible_matches_dictionary, name_fragments_and_frequency


def _break_names_into_fragments(cleaned_list_of_names: list, name_fragments_and_frequency: list) -> tuple[list[dict], int, list]:
    """This function takes in a list of cleaned names and breaks them
    up based on spaces and punctuation into their various parts, which
    are being labelled as fragments. It also determines which of those
    names has the most total fragments.
    
    Args:
        cleaned_list_of_names: A list of names, cleaned by using one of 
            the cleaning functions, that contains variations of a name 
            for a particular person
        name_fragments_and_frequency: A list of all of the name fragments
            that have been used for the name so far, their positions, and 
            their frequencies

    Returns:
        A list of dictionaries where each entry is a name and the
        dictionary within it contains all of the info on the name
        fragments. It also returns an integer representing the
        index of the name inside of the list that has the most
        total fragments in it and a list of all the name fragments 
        and how frequently they appear
    """
    broken_name_list = []
    current_index_in_name_list = 0
    index_of_name_with_most_fragments = 0
    fragments_in_name_with_most_fragments = 0
    for name in cleaned_list_of_names:
        # Split the name by likely indicators of different names (eg, surname, first name, etc)
        unfiltered_split_name = re_split(r'[. ,]\s*', name.strip())
        split_name = list(filter(None, unfiltered_split_name))
        total_name_fragments = len(split_name)

        if fragments_in_name_with_most_fragments < total_name_fragments:
            fragments_in_name_with_most_fragments = total_name_fragments
            index_of_name_with_most_fragments = current_index_in_name_list

        # Create a dictionary to add to a list for later comparison of fragments
        dictionary_to_add_to_broken_name_list = {
            'complete_name': name,
            'complete_name_position_in_list': current_index_in_name_list,
            'total_fragments': total_name_fragments,
            'fragment_list': []
        }

        # Remove spaces, commas, and periods from name fragments to get accurate info on them
        for name_fragment in split_name:
            initial_fragment = name_fragment
            edited_name_fragment = name_fragment.strip()
            edited_name_fragment = edited_name_fragment.replace('.', '')
            edited_name_fragment = edited_name_fragment.replace(',', '')
            length_of_fragment = len(name_fragment)
            length_of_edited_fragment = len(list(edited_name_fragment))

            # Add the fragment to the list of fragments in the name
            fragment_to_add = {
                'unedited_fragment': initial_fragment,
                'edited_fragment': edited_name_fragment,
                'length_of_unedited_fragment': length_of_fragment,
                'edited_fragment_length': length_of_edited_fragment,
                'fragment_frequency': 1
            }
            dictionary_to_add_to_broken_name_list['fragment_list'].append(fragment_to_add)

            found_frequency_fragment = False
            for frequency_fragment in name_fragments_and_frequency:
                if fragment_to_add['edited_fragment'] == frequency_fragment['edited_fragment']:
                    frequency_fragment['fragment_frequency'] = frequency_fragment['fragment_frequency'] + 1
                    found_frequency_fragment = True

            if not found_frequency_fragment:
                name_fragments_and_frequency.append(fragment_to_add)

        # Add the fully constructed dictionary to the list of broken up names
        broken_name_list.append(dictionary_to_add_to_broken_name_list)

        # Update this so we know where we are in the cleaned list of names
        current_index_in_name_list = current_index_in_name_list + 1

    return broken_name_list, index_of_name_with_most_fragments, name_fragments_and_frequency


def _extrapolate_names_from_equal_length_fragments(broken_name: dict, best_name_as_fragments: list[dict], multiple_possible_matches_dictionary: dict, name_fragments_and_frequency: list) -> tuple[list[dict], dict]:
    """This function is a helper function for extrapolate_best_full_name that will take in a 
    name that's been broken into it's name fragments and the currently determined best name,
    also broken into it's fragments. Then it compares the fragments to each other to determine
    if the fragment from the broken name is a better match than the currently known best
    fragment.

    Args:
        broken_name: A dictionary containing all of the info on a specific name and all of
            it's fragments
        best_name_as_fragments: A list of name fragments (which are dictionaries) for the
            best final name result as calculated so far
        multiple_possible_matches_dictionary: A dictionary containing all of the name 
            fragments that have multiple possible locations that they could fit in. It's 
            used to help determine locations of names later on
        name_fragments_and_frequency: A dictionary of all of the name fragments
            that have been used for the name so far, their positions, and their
            frequencies

    Returns:
        A list of name fragments (which are dictionaries) representing the newly updated
        calculation for the best final name result. It also returns a list of all of the 
        fragments that have multiple possible locations or matches as updated during this 
        call of the function
    """
    for fragment_index, specific_fragment in enumerate(broken_name['fragment_list']):
        # Probably turn this into a helper function eventually but for now I'm just going to let it be gross
        if (specific_fragment['edited_fragment'][0] == best_name_as_fragments[fragment_index]['edited_fragment'][0]) and (specific_fragment['edited_fragment_length'] > best_name_as_fragments[fragment_index]['edited_fragment_length'] and compare_two_names(specific_fragment['edited_fragment'], best_name_as_fragments[fragment_index]['edited_fragment']).match):
            # TODO: NOTE: WARNING: Will the match in this if statement return true for an initial? If not, it may cause issues
            best_name_as_fragments[fragment_index] = specific_fragment
            for current_index in multiple_possible_matches_dictionary:
                if specific_fragment in multiple_possible_matches_dictionary[current_index]:
                    multiple_possible_matches_dictionary[current_index].remove(specific_fragment)
        # In the event that it isn't a great match but has the same positioning, it might be good to look
        # at it's occurence count in the name_fragments_and_frequency list. If another name has a higher
        # frequency, it's more likely to be correct so we'll take that one
        else:
            # Find the frequency of both names
            best_name_fragment_frequency = 0
            broken_name_fragment_frequency = 0
            for frequency_fragment in name_fragments_and_frequency:
                if frequency_fragment['edited_fragment'] == specific_fragment['edited_fragment']:
                    broken_name_fragment_frequency = frequency_fragment['fragment_frequency']
                if frequency_fragment['edited_fragment'] == best_name_as_fragments[fragment_index]['edited_fragment']:
                    best_name_fragment_frequency = frequency_fragment['fragment_frequency']
            # If the new fragment is an initial, we'll just ignore it since we'd want a better name than an initial anyways
            if len(specific_fragment['edited_fragment']) == 1 or specific_fragment['edited_fragment'] == best_name_as_fragments[fragment_index]['edited_fragment']:
                continue
            # If the new fragment option has more versions, take that
            if broken_name_fragment_frequency > best_name_fragment_frequency:
                best_name_as_fragments[fragment_index] = specific_fragment
                for current_index in multiple_possible_matches_dictionary:
                    if specific_fragment in multiple_possible_matches_dictionary[current_index]:
                        multiple_possible_matches_dictionary[current_index].remove(specific_fragment)
            # If they have an equal number and the same initial, just leave an empty intial
            # fragment and add them both to the multiple possible matches dictionary
            elif broken_name_fragment_frequency == best_name_fragment_frequency and specific_fragment['edited_fragment'][0] == best_name_as_fragments[fragment_index]['edited_fragment'][0]:
                if multiple_possible_matches_dictionary.get(fragment_index, ''):
                    multiple_possible_matches_dictionary[fragment_index].append(specific_fragment)
                else:
                    multiple_possible_matches_dictionary[fragment_index] = [specific_fragment]
                    
                multiple_possible_matches_dictionary[fragment_index].append(best_name_as_fragments[fragment_index])
                best_name_as_fragments[fragment_index] = {
                    'unedited_fragment': specific_fragment['edited_fragment'][0],
                    'edited_fragment': specific_fragment['edited_fragment'][0],
                    'length_of_unedited_fragment': 1,
                    'edited_fragment_length': 1,
                    'fragment_frequency': 0
                }
            # If the best name one has more versions do nothing and leave the best name as is


    return best_name_as_fragments, multiple_possible_matches_dictionary


# TODO: WARNING: The name extrapolation for different length fragments doesn't yet consider the 
# frequency of fragments in the event that there is a conflict of names this should be
# updated for better accuracy
def _extrapolate_names_from_different_length_fragments(broken_name: dict, best_name_as_fragments: list[dict], multiple_possible_matches_dictionary: dict) -> tuple[list[dict], dict]:
    """This is a helper function for extrapolate_best_full_name that's used to determine which name
    fragments belong in the best final name conclusion when the fragments have a different length.
    It uses a collection of logic to determine if a name fragment is better than a currently accepted
    one, if there's a conflict, and to determine the order of fragments. This is all used to return
    an updated list of the best fragments to be included in the conclusion for the final full name.
    
    Args:
        multiple_possible_matches_dictionary: A dictionary containing all of the name fragments that
            have multiple possible locations that they could fit in. It's used to help determine
            locations of names later on
        broken_name: The specific collection of name fragments from a particular name that's being
            compared to find possible name fragment matches or improvements in the final name
        best_name_as_fragments: A list of name fragments (which are dictionaries) for the best final 
            name result as calculated so far

    Returns:
        A list of name fragments (which are dictionaries) representing the newly updated calculation 
        for the best final name result. It also returns a list of all of the fragments that have 
        multiple possible locations or matches as updated during this call of the function
    """

    first_accepted_index_of_previous_fragment = -1
    for specific_fragment in broken_name['fragment_list']:
        possible_name_matches_for_specific_fragment = []
        found_first_accepted_index = False

        if specific_fragment in best_name_as_fragments:
            continue

        # If the first letter of the fragment matches the first letter of a fragment from the best
        # name option, list it as a possible match. If it doesn't match any, list it as an
        # unknown location
        for index_of_fragment_in_best_name_list, fragment_of_best_name in enumerate(best_name_as_fragments):
            accepted_a_fragment_this_iteration = False
            if (index_of_fragment_in_best_name_list > first_accepted_index_of_previous_fragment) and (specific_fragment['edited_fragment'][0] == fragment_of_best_name['edited_fragment'][0]) and (len(specific_fragment['edited_fragment']) != 1) and (specific_fragment['edited_fragment'] != fragment_of_best_name['edited_fragment']) and (compare_two_names(specific_fragment['edited_fragment'], fragment_of_best_name['edited_fragment']).match) and (specific_fragment not in multiple_possible_matches_dictionary[index_of_fragment_in_best_name_list] if multiple_possible_matches_dictionary.get(index_of_fragment_in_best_name_list, '') else True):
                possible_name_matches_for_specific_fragment.append(index_of_fragment_in_best_name_list) # Note that this only tracks the possible fragment location matches (by thier indices)
                accepted_a_fragment_this_iteration = True
            if not found_first_accepted_index and accepted_a_fragment_this_iteration:
                first_accepted_index_of_previous_fragment = index_of_fragment_in_best_name_list
                found_first_accepted_index = True

        # If there's only one possible matching slot, we're just going to take that one given that the new fragment is better
        if len(possible_name_matches_for_specific_fragment) == 1:
            if len(specific_fragment['edited_fragment']) > len(best_name_as_fragments[possible_name_matches_for_specific_fragment[0]]['edited_fragment']):
                # TODO: NOTE: WARNING: Will this return true for an initial? If not, it may cause issues
                if compare_two_names(specific_fragment['edited_fragment'], best_name_as_fragments[possible_name_matches_for_specific_fragment[0]]['edited_fragment']).match:
                    best_name_as_fragments[possible_name_matches_for_specific_fragment[0]] = specific_fragment

        # If there are several possible matching slots, we need to store that info for later use
        elif len(possible_name_matches_for_specific_fragment) > 1:
            for index in possible_name_matches_for_specific_fragment:
                if multiple_possible_matches_dictionary.get(index, ''):
                    multiple_possible_matches_dictionary[index].append(specific_fragment)
                else:
                    multiple_possible_matches_dictionary[index] = [specific_fragment]

        # Now that we have more info, we need to go through each name fragment with an unknown slot
        # and determine if any of them have a more clear location or if they have something equivalent
        # that's been figured out
        best_name_as_fragments, multiple_possible_matches_dictionary = _check_for_newly_discovered_matches(best_name_as_fragments, multiple_possible_matches_dictionary)

    return best_name_as_fragments, multiple_possible_matches_dictionary


def _check_for_newly_discovered_matches(best_name_as_fragments: list[dict], multiple_possible_matches_dictionary: dict) -> tuple[list[dict], dict]:
    """This is a helper function for _extrapolate_names_from_different_length_fragments
    that takes in a list of all of the matches with more than one possible location for
    a name and deteremines if we have the information to place them in a proper
    place in the final name yet or not.

    Args:
        best_name_as_fragments: A list of name fragments (which are dictionaries) for the best final 
            name result as calculated so far
        multiple_possible_matches_dictionary: A dictionary containing all of the name fragments that
            have multiple possible locations that they could fit in

    Returns:
        A list of name fragments (which are dictionaries) representing the newly updated calculation 
        for the best final name result. It also returns a dictionary containing all the possible
        remaining name fragments (if any) with an unkown location in the final name calculation
    
    """
    for index_key in list(multiple_possible_matches_dictionary):
        # If the item in the name fragments is still an initial, we should definitely look at it
        check_for_initial_in_name_fragment = best_name_as_fragments[index_key]["edited_fragment"]
        if len(check_for_initial_in_name_fragment) == 1:
            # We need to make sure there are no other names that are an initial that matches the letter
            # that the index key names start with
            two_or_more_fragments_are_the_same_initial = False
            for index_of_other_name_fragment, other_name_fragment in enumerate(best_name_as_fragments):
                # Make sure that we aren't accidentally reading in the same fragment a second time
                if index_of_other_name_fragment == index_key:
                    continue
                # If it's not, find out if the other name fragment in an initial. If it's not, we can move on. If it is
                # we need to note that there's another name that could possibly have this one as a match that's just an
                # initial, so we'll need to move on and skip this particular name fragment check for now.

                # NOTE: TODO: This logic as it currently is could be slightly wrong if there's a frequency mismatch between
                # the two names with the same initial, in which case we should probably put the more frequent name into
                # each fragment. But we also probably want to do that check at the end after running all of the other comparison
                # stuff that we can. Rather than doing it here. This will also introduce a need for more weirdness at the end though
                # to make sure that the frequencies haven't changed and demoted a particular name's status / confidence in it's
                # match to be incomplete and result in an initial again
                check_for_initial_in_other_name_fragment = other_name_fragment['edited_fragment']
                if len(check_for_initial_in_other_name_fragment) > 1:
                    continue
                if check_for_initial_in_other_name_fragment[0] == check_for_initial_in_name_fragment[0]:
                    two_or_more_fragments_are_the_same_initial = True
                    break

            # If there are two or more fragments with the same initial, we'll want to shelve the rest of the
            # efforts to determine this segment of the name for now
            if two_or_more_fragments_are_the_same_initial:
                continue

            # If there are no others that are just an initial, we can check each item inside of the index
            # key to see if it matches the other name fragments that are currently accepted
            # NOTE: This segment is likely to cause weird issues if there is a person with two of the
            # same name in their full name, so it's worth having this in the back of your mind if one of
            # the test cases is acting funky
            # NOTE: Another thing that could definitely go wrong here is that we're permutating a list
            # as we're going through it, which could result in certain items being skipped when they
            # shouldn't be. You should probably clean this up so that it isn't a risk once you've
            # gotten the core of the code and the test cases written out
            found_an_initial_replacement = False
            for fragment_to_test_for_belonging in multiple_possible_matches_dictionary[index_key]:
                # Search to see if there's another fragment that matches this particular name
                found_matching_fragment_in_other_location = False
                for currently_accepted_name_fragment in best_name_as_fragments:
                    fragments_are_likely_the_same = compare_two_names(fragment_to_test_for_belonging['edited_fragment'], currently_accepted_name_fragment['edited_fragment']).match
                    if fragments_are_likely_the_same and len(currently_accepted_name_fragment['edited_fragment']) > 1:
                        found_matching_fragment_in_other_location = True
                        break
                # If there is another matching fragment, we don't really want to put it here since it's
                # unlikely to belong in this slot
                if found_matching_fragment_in_other_location:
                    for current_index in multiple_possible_matches_dictionary:
                        if fragment_to_test_for_belonging in multiple_possible_matches_dictionary[current_index]:
                            multiple_possible_matches_dictionary[current_index].remove(fragment_to_test_for_belonging)
                    continue
                # If it doesn't match anything else, it probably does go in that slot NOTE: (unless there's 
                # a more frequent alternative maybe?)
                else:
                    best_name_as_fragments[index_key] = fragment_to_test_for_belonging
                    found_an_initial_replacement = True
                    for current_index in multiple_possible_matches_dictionary:
                        if fragment_to_test_for_belonging in multiple_possible_matches_dictionary[current_index]:
                            multiple_possible_matches_dictionary[current_index].remove(fragment_to_test_for_belonging)
                    break  

            # If we found any replacements in the previous step, we need to iterate through the remaining
            # possible matches in the dictionary to determine if any of them are a more complete version
            # of the name than the one we took in as a replacement for the initial
            if found_an_initial_replacement:
                for fragment_to_test_as_better_option in multiple_possible_matches_dictionary[index_key]:
                    if len(fragment_to_test_as_better_option['edited_fragment']) > len(best_name_as_fragments[index_key]['edited_fragment']):
                        if compare_two_names(fragment_to_test_as_better_option['edited_fragment'], best_name_as_fragments[index_key]['edited_fragment']).match:
                            best_name_as_fragments[index_key] = fragment_to_test_as_better_option
                        for current_index in multiple_possible_matches_dictionary:
                            if fragment_to_test_as_better_option in multiple_possible_matches_dictionary[current_index]:
                                multiple_possible_matches_dictionary[current_index].remove(fragment_to_test_as_better_option)

            # TODO: NOTE: There will be an exception to this if the name in the list isn't inside of another
            # key, inside of another name fragment, AND doesn't match the name inside of the particular index
            # that it's assigned to. In this case, we want to keep it inside of the dictionary and later compare
            # it for frequency. Otherwise we'll just leave the initial in it's place (wait, do we actually want
            # to do this???) (Actually, maybe we do since it will handle conflicting info if we get new name
            # information added. It will definitely require upgrading the step right above this one though)

        # At the end of this, if there is nothing left in the key, we want to completely remove the key
        if not multiple_possible_matches_dictionary[index_key]:
            multiple_possible_matches_dictionary.pop(index_key, None)


    # TODO: NOTE: You want to create a case where if a name matches a certain location well isn't a possible match
    # for any other fragment slot, and the current fragment slot is only an initial, it should be assumed that that
    # fragment should be placed into the currently undetermined slot

    return best_name_as_fragments, multiple_possible_matches_dictionary


def clean_name_list(input_list_of_names: list[str]) -> list[str]:
    """This function takes in a list of names to prepare for name extrapolation,
    then standardizes them by doing a few initial comparisons to each other and
    removing any unusual punctuation that's in them.
    
    Args:
        input_list_of_names: A list of names that need to be cleaned
        
    Returns:
        A list of all of the names, now cleaned and ready to be used for
        name extrapolation
    """

    list_of_matches = []
    list_of_non_matches = []
    index_count = 0

    # If the list is 2 items long or less, it will be inconclusive since we can't determine
    # which names are going to be the most significant using this method so return an empty
    # list of matches. This also establishes a base case for recursion, which is important
    if len(input_list_of_names) <= 2:
        return []

    for item in input_list_of_names:
        # Skip the first name because there isn't anything to compare to yet
        if index_count == 0:
            index_count = index_count + 1
            continue

        # For the second name, compare it to the first name
        elif index_count == 1:
            result_of_comparison = compare_two_names(input_list_of_names[0], item).match
            # If they're a match, start building a list of matches
            if result_of_comparison:
                list_of_matches.append(input_list_of_names[0])
                list_of_matches.append(item)
            # If they're not a match, start building a list of non-matches
            else:
                list_of_non_matches.append(input_list_of_names[0])
                list_of_matches.append(item)
            index_count = index_count + 1

        # After the second name we can apply this logic repeatedly
        else:
            # If there haven't been any matches, compare to the list of non-matches
            # to see if this name matches any of them
            if not list_of_matches:
                got_an_initial_match = False

                for not_a_match in list_of_non_matches:
                    # If we already found a basis from which to create a match list, we don't need to run this anymore
                    if got_an_initial_match:
                        break

                    result_of_comparison_with_non_match = compare_two_names(item, not_a_match).match
                    # If the name matches something in the list of non-matches so far, add them to the
                    # list of matches
                    if result_of_comparison_with_non_match:
                        got_an_initial_match = True
                        list_of_matches.append(not_a_match)
                        list_of_matches.append(item)
                        list_of_non_matches.remove(not_a_match)

                # If there are still no more matches, add the name to the list of non-matches since it didn't match anything
                if not got_an_initial_match:
                    list_of_non_matches.append(item)

            # Otherwise, compare the new name to the list of matches to see if it
            # matches any of the ones there
            else:
                matches_another_match = False

                for already_a_match in list_of_matches:
                    # If it already matches something, we can just skip the rest of the cycle
                    if matches_another_match:
                        break

                    result_of_comparison_with_match = compare_two_names(item, already_a_match).match

                    # If the name matches another match, add it into the list of matches
                    if result_of_comparison_with_match:
                        matches_another_match = True
                        list_of_matches.append(item)

                # If the name doesn't match any of the other matches, add it to the list of non-matches
                if not matches_another_match:
                    list_of_non_matches.append(item)

    # Run this function again on the list of non-matches to make sure that there isn't a better list
    # of matches that could be returned
    check_for_better_match_list = clean_name_list(list_of_non_matches)

    # If the returned match list has more matches than the initial match list, determine that one
    # is the better match between the two since it matches more things. Return that one instead
    if (len(check_for_better_match_list) > len(list_of_matches)):
        list_of_matches = check_for_better_match_list

    return list_of_matches


# NOTE: TODO: This isn't finished yet, but you wanted it here to make sure that you are aware
# it's a specific upgrade that *will* be needed for the FlexibleName information later on
def extrapolate_name_based_on_new_information(new_name_information: list, ):

    return


# NOTE: TODO: The name extrapolation will only handle name discrepancies if the issue happens
# when the name fragments have the same length. There are situations where a discrepancy could
# occur during handling of names with a different number of fragments. This could possibly be
# upgraded to handle that better