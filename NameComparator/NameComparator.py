from dataclasses import dataclass
from typing import NamedTuple
from json import loads as json_loads
from importlib.resources import files
from pydantic import BaseModel
from re import split as re_split

from NameComparator.src.clean import clean_name, clean_names_by_comparison, clean_ipa
from NameComparator.src.nicknames import remove_nicknames
from NameComparator.src.insights import is_worth_continuing, either_name_too_short
from NameComparator.src.comparisons import compare_spelling, pronunciation_comparison
from NameComparator.src.modify import modify_names_together, modify_ipas_by_comparison
from NameComparator.src.ipa import get_ipa
from NameComparator.src.uniqueness import score_uniqueness
from NameComparator.src.uniqueness import FrequencyData

unparsed_usa_to_1950_surnames = files('NameComparator').joinpath('data/frequency/surnamesUsaTo1950.json').read_text()
unparsed_usa_to_1950_first_names = files('NameComparator').joinpath('data/frequency/firstNamesUsaTo1950.json').read_text()

class Attempt(NamedTuple):
    """Represents an attempt at name comparison (often used for debugging).

    Attributes:
        name_one: The version of the first name to be used in this attempt
        name_two: The version of the second name to be used in this attempt
        word_combos: A list of tuples describing the word matchups and quality
        score_of_attempt: The score associated with the percent confidence 
            returned from this attempt
    """
    name_one: str
    name_two: str
    word_combos: list[tuple[str, str, int]]
    score_of_attempt: float

@dataclass
class ResultsOfNameComparison:
    """Represents the results of a name comparison.

    Attributes:
        name_one: The original name_one
        name_two: The original name_two
        match: Whether or not the names are a match. Defaults to False
        uniqueness: How unique the names were in comparison to the chosen population. Defaults to 0.0
        too_short: Whether or not either of the names are one word or less. Defaults to True
        attempt_one: Debugging data about the first attempt to compare the names. Defaults to None
        attempt_two: Debugging data about the second attempt to compare the names. Defaults to None
        attempt_three: Debugging data about the third attempt to compare the names. Defaults to None
        attempt_four: Debugging data about the fourth attempt to compare the names. Defaults to None
        most_recent_attempt_score: The percent confidence score associated with the most recent attempt
            that was made while comparing the names
        average_score_of_combined_attempts: The average percent confidence score from all of the
            attempts that were made while comparing the names
    """
    name_one: str
    name_two: str
    match: bool = False
    uniqueness: float = 0.0
    too_short: bool = True
    attempt_one: Attempt | None = None
    attempt_two: Attempt | None = None
    attempt_three: Attempt | None = None
    attempt_four: Attempt | None = None
    most_recent_attempt_score: float = 0
    average_score_of_combined_attempts: float = 0

class FlexibleName(BaseModel):
    """ This class represents a name in a way that allows for more
    flexible comparison and for determining the most complete and full
    version of a name when given a list of possible name inputs.

    Attributes:
        original_name_list: The list of possible name variations as
            originally input into the class
        cleaned_name_list: The original name list with irrelevant or
            unlikely names removed from it
        best_name_from_list: The best name that is retrieved from the
            list
        extrapolated_name: The complete name as extrapolated from
            all of the name variations in the name list
    """

    def __init__(self, name_list_input: list[str]):
        self.original_name_list = name_list_input
        self.cleaned_name_list = clean_name_list(name_list_input)
    # TODO: Build functions to allow for all of these different variables and
    # outputs to be determined, probably when the class is constructed. Also
    # allow for different constructor variants if that feels appropriate

def compare_two_names(name_one:str, name_two:str, frequency_data:FrequencyData|None = None) -> ResultsOfNameComparison:
    """Compares two names to identify whether or not they are a match.

    Args:
        name_one: The first name to compare
        name_two: The second name to compare
        frequency_data: The first name and surname frequencies in a chosen 
            population - Defaults to None

    Returns:
        The data gleaned from the comparison: whether or not they are a match, 
        whether or not one or both names is too generic, whether or not one or 
        both names is too short, and the attempt data for each different 
        comparison method used
    """        
    # Deal with the optional frequency_data argument
    if not frequency_data:
        frequency_data = FrequencyData(json_loads(unparsed_usa_to_1950_first_names), json_loads(unparsed_usa_to_1950_surnames))

    # Data validation
    if not isinstance(name_one, str) or not isinstance(name_two, str):
        raise TypeError(f'name_one was {type(name_one)}. Must be a str. name_two was {type(name_two)}. Must be a str.')
    if not isinstance(frequency_data, FrequencyData):
        raise TypeError(f'frequency_data was the type {type(frequency_data)}. Must be a FrequencyData object.')

    # Create the return object to edit later
    results = ResultsOfNameComparison(name_one=name_one, name_two=name_two)

    # Clean the names
    name_one = clean_name(name_one)
    name_two = clean_name(name_two)
    name_one, name_two = clean_names_by_comparison(name_one, name_two)

    # Deal with names that are too short
    results.too_short = either_name_too_short(name_one, name_two)
    if not name_one:
        name_one = '_'
    if not name_two:
        name_two = '_'
    if (name_one == '_') or (name_two == '_'):
        return results
    
    # Find the uniqueness of this name matchup (ie. hopefully not 'John Smith' and 'J Smith')
    results.uniqueness = score_uniqueness(name_one, name_two, frequency_data)

    # Remove nicknames before the actual comparison
    name_one, name_two = remove_nicknames(name_one, name_two)

    # 1st attempt: Checks if names are a match according to string comparison alone
    match, word_combos, attempt_one_score = compare_spelling(name_one, name_two)
    results.attempt_one = Attempt(name_one, name_two, word_combos, attempt_one_score)
    if match:
        results.match = True
        results.most_recent_attempt_score = attempt_one_score
        results.average_score_of_combined_attempts = attempt_one_score
        return results

    # Failed first attempt. Check if names are even worth continuing
    if is_worth_continuing(name_one, name_two) is False:
        return results

    # 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
    modified_name_one, modified_name_two = modify_names_together(name_one, name_two)
    match, word_combos, attempt_two_score = compare_spelling(modified_name_one, modified_name_two)
    results.attempt_two = Attempt(modified_name_one, modified_name_two, word_combos, attempt_two_score)
    if match:
        results.match = True
        results.most_recent_attempt_score = attempt_two_score
        results.average_score_of_combined_attempts = ((attempt_two_score + attempt_one_score) / 2)
        return results
        
    # 3rd attempt: Checks if modified names are a match according to pronunciation
    ipa_of_modified_name_one = clean_ipa(get_ipa(modified_name_one))
    ipa_of_modified_name_two = clean_ipa(get_ipa(modified_name_two))
    ipa_of_modified_name_one, ipa_of_modified_name_two = modify_ipas_by_comparison(ipa_of_modified_name_one, ipa_of_modified_name_two)
    match, word_combos, attempt_three_score = pronunciation_comparison(ipa_of_modified_name_one, ipa_of_modified_name_two, modified_name_one, modified_name_two)
    results.attempt_three = Attempt(ipa_of_modified_name_one, ipa_of_modified_name_two, word_combos, attempt_three_score)
    if match:
        results.match = True
        results.most_recent_attempt_score = attempt_three_score
        results.average_score_of_combined_attempts = ((attempt_three_score + attempt_two_score + attempt_one_score) / 3)
        return results

    # 4th attempt: Check if original names are a match according to pronunciation
    ipa_of_name_one = clean_ipa(get_ipa(name_one))
    ipa_of_name_two = clean_ipa(get_ipa(name_two))
    ipa_of_name_one, ipa_of_name_two = modify_ipas_by_comparison(ipa_of_name_one, ipa_of_name_two)
    match, word_combos, attempt_four_score = pronunciation_comparison(ipa_of_name_one, ipa_of_name_two, name_one, name_two)
    results.attempt_four = Attempt(ipa_of_name_one, ipa_of_name_two, word_combos, attempt_four_score)
    if match:
        results.match = True
        results.most_recent_attempt_score = attempt_four_score
        results.average_score_of_combined_attempts = ((attempt_four_score + attempt_three_score + attempt_two_score + attempt_one_score) / 4)
    return results


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
            length_of_fragment = len(list(edited_name_fragment))

            # Add the fragment to the list of fragments in the name
            fragment_to_add = {
                'unedited_fragment': initial_fragment,
                'edited_fragment': edited_name_fragment,
                'edited_fragment_length': length_of_fragment
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
    # to determine if there is a better possible name
    



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


