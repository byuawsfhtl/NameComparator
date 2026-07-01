from NameComparator.NameComparator import compare_two_names
from re import split as re_split

# TODO: Consider coming up with logic that can use the list of nicknames
# to determine possible full names for a person when a nickname or
# shorthand version is used

# TODO: It may be worth also having this return a list of all of the
# possible names for different segments that haven't been accepted
# or rejected yet due to uncertainty. This will help with the 
# FlexibleName stuff later on

def extrapolate_best_full_name(cleaned_list_of_names) -> str:
    """This function takes in a list of cleaned names for a single person
    and then determines what the most likely best full name is based on 
    that list, favoring having full names instead of initials or 
    abbreviations when possible.

    Args:
        cleaned_list_of_names: A list of names, cleaned by using one of the
            cleaning functions, that contains variations of a name for a 
            particular person
    
    Returns:
        A string representing the best or most complete version of a name,
        based on all of the input names
    """
    
    # If there is nothing left in the cleaned names, we can't
    # determine the best name so return an empty string
    if not cleaned_list_of_names:
        return ''
    
    # If there is only one name in the cleaned names, we can
    # safely say that's the best name in the list. Just
    # return it
    if len(cleaned_list_of_names) == 1:
        return cleaned_list_of_names[0]
    
    # Break all of the names into a collection of pieces I'm calling fragments
    broken_name_list, index_of_name_with_most_fragments = _break_names_into_fragments(cleaned_list_of_names)

    # Populate an initial array of strings equal to the length of the name with the most
    # fragments, using the fragments from that name as the starting point
    fragments_count_of_name_with_most_fragments = len(broken_name_list[index_of_name_with_most_fragments]['fragment_list'])
    best_name_as_fragments = []
    for initial_name_fragment in broken_name_list[index_of_name_with_most_fragments]['fragment_list']:
        best_name_as_fragments.append(initial_name_fragment)

    # Go through each of the name fragments and compare them to the current list of best fragments
    # to determine if there is a better possible name. Store unknown data to parse through later
    multiple_possible_matches_dictionary: dict = {}
    for broken_name in broken_name_list:
        
        # If the number of fragments matches the max number of fragments, we can probably safely assume that
        # the names have similar positions as long as their first letters match.
        if len(broken_name['fragment_list']) == fragments_count_of_name_with_most_fragments:
            best_name_as_fragments = _extrapolate_names_from_equal_length_fragments(broken_name, best_name_as_fragments)

        # If the number of fragments doesn't match the max number of fragments, we'll need to handle the logic
        # a little bit differently
        else:
            for specific_fragment in broken_name['fragment_list']:
                print(f"Handling logic for the fragment {specific_fragment} from the list {broken_name['fragment_list']}")
                index_of_fragment_in_best_name_list = 0
                possible_name_matches_for_specific_fragment = []
                print(f"Note that the current best name fragment list looks as follows: {best_name_as_fragments}")
                for fragment_of_best_name in best_name_as_fragments:
                    # If the first letter of the fragment matches the first letter of a fragment from the best
                    # name option, list it as a possible match. If it doesn't match any, list it as an
                    # unknown location
                    print(f"Comparing the fragment {specific_fragment} to the fragment {fragment_of_best_name} from the current best name")
                    if specific_fragment['edited_fragment'][0] == fragment_of_best_name['edited_fragment'][0]:
                        possible_name_matches_for_specific_fragment.append(index_of_fragment_in_best_name_list) # Note that this only tracks the possible fragment location matches (thier indices)
                        print(f"Updated possible name matches for the specific fragment with the index {index_of_fragment_in_best_name_list}")
                    index_of_fragment_in_best_name_list = index_of_fragment_in_best_name_list + 1

                
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
                for index_key in list(multiple_possible_matches_dictionary):

                    # If the item in the name fragments is still an initial, we should definitely look at it
                    print(f"Quick check on the best_name_as_fragments list: {best_name_as_fragments}")
                    check_for_initial_in_name_fragment = best_name_as_fragments[index_key]["edited_fragment"]
                    if len(check_for_initial_in_name_fragment) > 1:

                        # We need to make sure there are no other names that are an initial that matches the letter
                        # that the index key names start with
                        index_of_other_name_fragment = 0
                        two_or_more_fragments_are_the_same_initial = False
                        for other_name_fragment in best_name_as_fragments:
                            # Make sure that we aren't accidentally reading in the same fragment a second time
                            if index_of_other_name_fragment == index_key:
                                index_of_other_name_fragment = index_of_other_name_fragment + 1
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
                            else:
                                check_for_initial_in_other_name_fragment = other_name_fragment['edited_fragment']
                                if len(check_for_initial_in_other_name_fragment) > 1:
                                    index_of_other_name_fragment = index_of_other_name_fragment + 1
                                    continue
                                else:
                                    if check_for_initial_in_other_name_fragment == check_for_initial_in_name_fragment:
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
                                if fragments_are_likely_the_same:
                                    found_matching_fragment_in_other_location = True
                                    break
                            # If there is another matching fragment, we don't really want to put it here since it's
                            # unlikely to belong in this slot
                            if found_matching_fragment_in_other_location:
                                multiple_possible_matches_dictionary[index_key].remove(fragment_to_test_for_belonging)
                                continue
                            # If it doesn't match anything else, it probably does go in that slot NOTE: (unless there's 
                            # a more frequent alternative maybe?)
                            else:
                                best_name_as_fragments[index_key] = fragment_to_test_for_belonging
                                found_an_initial_replacement = True
                                multiple_possible_matches_dictionary[index_key].remove(fragment_to_test_for_belonging)
                                break  

                        # If we found any replacements in the previous step, we need to iterate through the remaining
                        # possible matches in the dictionary to determine if any of them are a more complete version
                        # of the name than the one we took in as a replacement for the initial
                        if found_an_initial_replacement:
                            for fragment_to_test_as_better_option in multiple_possible_matches_dictionary[index_key]:
                                if len(fragment_to_test_as_better_option) > len(best_name_as_fragments[index_key]):
                                    if compare_two_names(fragment_to_test_as_better_option, best_name_as_fragments[index_key]).match:
                                        best_name_as_fragments[index_key] = fragment_to_test_as_better_option
                                    multiple_possible_matches_dictionary[index_key].remove(fragment_to_test_as_better_option)

                        # TODO: NOTE: There will be an exception to this if the name in the list isn't inside of another
                        # key, inside of another name fragment, AND doesn't match the name inside of the particular index
                        # that it's assigned to. In this case, we want to keep it inside of the dictionary and later compare
                        # it for frequency. Otherwise we'll just leave the initial in it's place (wait, do we actually want
                        # to do this???) (Actually, maybe we do since it will handle conflicting info if we get new name
                        # information added. It will definitely require upgrading the step right above this one though)

                    # At the end of this, if there is nothing left in the key, we want to completely remove the key
                    if not multiple_possible_matches_dictionary[index_key]:
                        multiple_possible_matches_dictionary.pop(index_key, None)


                    # NOTE: TODO: I feel like a *lot* of the things inside of this code should really be helper functions. This would
                    # likely both improve efficiency and reduce a meaningful amount of redundancy that is currently in the code

    # After everything else is done, recompile the name fragments into one complete name and return it as a string
    complete_extrapolated_name = ''
    add_spaces_index_checker = 1
    for best_fragment in best_name_as_fragments:
        complete_extrapolated_name = complete_extrapolated_name + best_fragment['edited_fragment']
        if add_spaces_index_checker < len(best_name_as_fragments):
            complete_extrapolated_name = complete_extrapolated_name + ' '

    return complete_extrapolated_name


def _break_names_into_fragments(cleaned_list_of_names: list) -> tuple[list[dict], int]:
    """This function takes in a list of cleaned names and breaks them
    up based on spaces and punctuation into their various parts, which
    are being labelled as fragments. It also determines which of those
    names has the most total fragments.
    
    Args:
        cleaned_list_of_names: A list of names, cleaned by using one of 
            the cleaning functions, that contains variations of a name 
            for a particular person

    Returns:
        A list of dictionaries where each entry is a name and the
        dictionary within it contains all of the info on the name
        fragments. It also returns an integer representing the
        index of the name inside of the list that has the most
        total fragments in it
    """

    broken_name_list = []
    current_index_in_name_list = 0
    index_of_name_with_most_fragments = 0
    fragments_in_name_with_most_fragments = 0
    for name in cleaned_list_of_names:

        print(f"Name before split: {name}")

        # Split the name by likely indicators of different names (eg, surname, first name, etc)
        unfiltered_split_name = re_split(r'[. ,]\s*', name.strip())
        split_name = list(filter(None, unfiltered_split_name))

        print(f"Name after split: {split_name}")

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
                'edited_fragment_length': length_of_edited_fragment
            }
            dictionary_to_add_to_broken_name_list['fragment_list'].append(fragment_to_add)
            print(f"Added the fragment {fragment_to_add}")

        # Add the fully constructed dictionary to the list of broken up names
        broken_name_list.append(dictionary_to_add_to_broken_name_list)

        # Update this so we know where we are in the cleaned list of names    
        current_index_in_name_list = current_index_in_name_list + 1

    return broken_name_list, index_of_name_with_most_fragments


def _extrapolate_names_from_equal_length_fragments(broken_name: dict, best_name_as_fragments: list[dict]) -> list[dict]:
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

    Returns:
        A list of name fragments (which are dictionaries) representing the newly updated
        calculation for the best final name result
    """

    # TODO: This currently won't update anything to fall under the multiple possible name matches
    # variable when maybe it should. Look into this and consider implementing it as a part of
    # the check

    fragment_index = 0
    for specific_fragment in broken_name['fragment_list']:
        # Probably turn this into a helper function eventually but for now I'm just going to let it be gross
        if (specific_fragment['edited_fragment'][0] == best_name_as_fragments[fragment_index]['edited_fragment'][0]) and (specific_fragment['edited_fragment_length'] > best_name_as_fragments[fragment_index]['edited_fragment_length']):
            # TODO: NOTE: WARNING: Will this return true for an initial? If not, it may cause issues
            if compare_two_names(specific_fragment['edited_fragment'], best_name_as_fragments[fragment_index]['edited_fragment']).match:
                best_name_as_fragments[fragment_index] = specific_fragment
                # TODO: NOTE: It would probably be best to add this to a list of 'potential names' or
                # something like that so that later on if there is a conflict and it's unclear which
                # name should 'win' in a space we can detect if it should just be an initial or not

    return best_name_as_fragments
                            

def clean_name_list(input_list_of_names) -> list[str]:

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


