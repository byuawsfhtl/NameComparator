from NameComparator.NameComparator import compare_two_names
from re import split as re_split

def extrapolate_best_full_name(cleaned_list_of_names) -> str:
    
    # If there is nothing left in the cleaned names, we can't
    # determine the best name so return an empty string
    if not cleaned_list_of_names:
        return ''
    
    # If there is only one name in the cleaned names, we can
    # safely say that's the best name in the list. Just
    # return it
    if len(cleaned_list_of_names) == 1:
        return cleaned_list_of_names[0]
    
    broken_name_list = []
    current_index_in_name_list = 0
    index_of_name_with_most_fragments = 0
    fragments_in_name_with_most_fragments = 0
    for name in cleaned_list_of_names:

        # Split the name by likely indicators of different names (eg, surname, first name, etc)
        split_name = re_split(r'[. ,]\s*', name)

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
            dictionary_to_add_to_broken_name_list['fragment_list'].append[fragment_to_add]

        # Add the fully constructed dictionary to the list of broken up names
        broken_name_list.append(dictionary_to_add_to_broken_name_list)

        # Update this so we know where we are in the cleaned list of names    
        current_index_in_name_list = current_index_in_name_list + 1

    # Populate an initial array of strings equal to the length of the name with the most
    # fragments, using the fragments from that name as the starting point
    best_name_as_fragments = []
    for initial_name_fragment in broken_name_list[index_of_name_with_most_fragments]['fragment_list']:
        best_name_as_fragments.append(initial_name_fragment['unedited_fragment'])

    # Go through each of the name fragments and compare them to the current list of best fragments
    # to determine if there is a better possible name. Store unknown data to parse through later
    multiple_possible_matches_dictionary = {}
    for broken_name in broken_name_list:
        
        # If the number of fragments matches the max number of fragments, we can probably safely assume that
        # the names have similar positions as long as their first letters match.
        if len(broken_name['fragment_list']) == fragments_in_name_with_most_fragments:
            fragment_index = 0
            for specific_fragment in broken_name['fragment_list']:
                # Probably turn this into a helper function eventually but for now I'm just going to let it be gross
                if list(specific_fragment)[0] == list(best_name_as_fragments[fragment_index])[0]:
                    if specific_fragment['length_of_unedited_fragment'] > best_name_as_fragments[fragment_index]:
                        # TODO: NOTE: WARNING: Will this return true for an initial? If not, it may cause issues
                        if compare_two_names(specific_fragment, best_name_as_fragments[fragment_index]).match:
                            best_name_as_fragments[fragment_index] = specific_fragment
                            # TODO: NOTE: It would probably be best to add this to a list of 'potential names' or
                            # something like that so that later on if there is a conflict and it's unclear which
                            # name should 'win' in a space we can detect if it should just be an initial or not

        # If the number of fragments doesn't match the max number of fragments, we'll need to handle the logic
        # a little bit differently
        else:
            for specific_fragment in broken_name['fragment_list']:
                index_of_fragment_in_best_name_list = 0
                possible_name_matches_for_specific_fragment = []
                for fragment_of_best_name in best_name_as_fragments:
                    # If the first letter of the fragment matches the first letter of a fragment from the best
                    # name option, list it as a possible match. If it doesn't match any, list it as an
                    # unknown location
                    if list(specific_fragment)[0] == list(fragment_of_best_name)[0]:
                        possible_name_matches_for_specific_fragment.append(index_of_fragment_in_best_name_list) # Note that this only tracks the possible fragment location matches (thier indices)
                    index_of_fragment_in_best_name_list = index_of_fragment_in_best_name_list + 1
                
                # If there's only one possible matching slot, we're just going to take that one given that the new fragment is better
                if len(possible_name_matches_for_specific_fragment) == 1:
                    if len(specific_fragment) > len(best_name_as_fragments[possible_name_matches_for_specific_fragment[0]]):
                        # TODO: NOTE: WARNING: Will this return true for an initial? If not, it may cause issues
                        if compare_two_names(specific_fragment, best_name_as_fragments[possible_name_matches_for_specific_fragment[0]]).match:
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
                for index_key in multiple_possible_matches_dictionary:

                    # NOTE: TODO: I feel like the above things should be helper functions that we just run again
                    # in this segment, actually

                    apple = 0 # NOTE: TODO: This is dummy filler code to temporarily remove an error. Remove it 
                              # once you have real code here





    # After everything else is done, recompile the name fragments into one complete name and return it as a string
    complete_extrapolated_name = ''
    add_spaces_index_checker = 1
    for best_fragment in best_name_as_fragments:
        complete_extrapolated_name = complete_extrapolated_name + best_fragment
        if add_spaces_index_checker < len(best_name_as_fragments):
            complete_extrapolated_name = complete_extrapolated_name + ' '

    return complete_extrapolated_name
                            







def clean_name_list(input_list_of_names) -> list[str]:

    list_of_matches = []
    list_of_non_matches = []
    index_count = 0

    # If the list is 2 items long or less, it will be inconclusive since we can't determine
    # which names are going to be the most significant using this method so return an empty
    # list of matches. This also establishes a base case for recursion, which is important
    if input_list_of_names.length <= 2:
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


