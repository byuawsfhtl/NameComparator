from pyscripttestutils import PyScriptTestRunner
import pytest
from pathlib import Path
from tests.test_data._ai_generated_unextrapolated_names import ai_generated_name_lists_for_extrapolation

from NameComparator.src.name_extrapolation import clean_name_list, extrapolate_best_full_name

# TODO: NOTE: This file is not yet finished. It is mostly created thus far
# to track a specific test case that will likely be very insightful. This
# will be updated later to be comprehensive and actually include meaningful
# test cases

full_final_name = 'John Jacob Jingleheimer Schmidtt'

list_of_input_names = ['J J J S', 'John Schmidtt', 'J. Jingleheimer', 'John J. J. S.', 'Jacob Jingleheimer Schmidtt']

returned_still_unknown_names: list = [] # Empty because there should be no unknowns left

cleaned_list_of_names = clean_name_list(list_of_input_names)
print("Extrapolating name for the first test case:")
name_result, leftover_fragments, ignored_fragment_frequency_list = extrapolate_best_full_name(cleaned_list_of_names)
print(f"leftover_fragments - {leftover_fragments}")
print(f"frequency list at end: {ignored_fragment_frequency_list}")
print(f"Final result of name extrapolation: name - {name_result}")
print("\n\n")

# TODO: NOTE: What do we want to do with this next one? It won't be possible 
# to get the full final name and it will be difficult to determine where
# the extra J should go. You'll need to think through this. It might have
# overlap with the test case after this one, at least in terms of figuring
# out the logic

another_full_final_name = 'John J J Schmidtt'

returned_still_unknown_names = ['Jingleheimer']

list_of_input_names = ['J J J S', 'John Schmidtt', 'J. Jingleheimer', 'John J. J. S.']

cleaned_list_of_names = clean_name_list(list_of_input_names)
print("Extrapolating name for the second test case:")
name_result, leftover_fragments, ignored_fragment_frequency_list = extrapolate_best_full_name(cleaned_list_of_names)
print(f"leftover_fragments - {leftover_fragments}")
print(f"frequency list at end: {ignored_fragment_frequency_list}")
print(f"Final result of name extrapolation: name - {name_result}")
print("\n\n")

# TODO: NOTE: For this next one if there are two possible names with an unclear 'winner',
# we should probably just take the initial of the name and use that for now

# TODO: NOTE: This next test case would also be a *GREAT* one to use for the add another
# name function to help clarify more information as part of the flexible name
# yet_another_full_final_name = 'John Jacob Jingleheimer Schmidtt'

intended_final_result_if_no_new_info = 'J J Jingleheimer Schmidtt' # This works since we know that Jingleheimer has to be after both John and Jacob to work

returned_still_unknown_names = ['John', 'Jacob'] # We would hold on to these as having an unknown position in case we get more information later, in something
                                                 # like an add name function for FlexibleName

list_of_input_names = ['J J J S', 'John Jingleheimer Schmidtt', 'Jacob Jingleheimer Schmidtt']

cleaned_list_of_names = clean_name_list(list_of_input_names)
print("Extrapolating name for the third test case:")
name_result, leftover_fragments, ignored_fragment_frequency_list = extrapolate_best_full_name(cleaned_list_of_names)
print(f"leftover_fragments - {leftover_fragments}")
print(f"frequency list at end: {ignored_fragment_frequency_list}")
print(f"Final result of name extrapolation: name - {name_result}")
print("\n\n")

# TODO: NOTE: None of these cases figure out what we should do with abbreviations or titles
# you will need to figure out how to handle those. I think we should probably just have a list
# of titles such as ms., mr., mrs., lt., etc. that we should just note to throw at the beginning
# or end based on where they were before. But for abbreviations things will be a little bit
# trickier. Can I borrow some code from what is already inside of NameComparator somewhere else
# that factors that in?


# NOTE: This particular case is used to determine uncertainty when a new name is introduced to a seemingly solved situation.
# This could also be incredibly helpful as a test case for if a new name is introduced. It's worth considering how we want
# this handled, especially if there are multiple occurences of one of the names (which we would want to prioritize over
# a single anomolous occurence, of course)

unusual_situation_full_name = 'John Jacob Jingleheimer Schmidtt'

intended_final_result_of_unusual_situation = 'J J J Schmidtt'

returned_unkown_names_for_unusual_situation = ['Jacob', 'Jangle'] # Do we want to include an expected index for all of these to help with this process? This would probably be
                                                                  # fairly situational to something odd like this though

list_of_input_names = ['J J J S', 'John Jacob Jingleheimer Schmidtt', 'John Jangle Jingleheimer Schmidtt']

cleaned_list_of_names = clean_name_list(list_of_input_names)
print("Extrapolating name for the fourth test case:")
name_result, leftover_fragments, ignored_fragment_frequency_list = extrapolate_best_full_name(cleaned_list_of_names)
print(f"leftover_fragments - {leftover_fragments}")
print(f"frequency list at end: {ignored_fragment_frequency_list}")
print(f"Final result of name extrapolation: name - {name_result}")
print("\n\n")

# NOTE: Fortunately, I think that it would be best to not factor the above test case when it comes to a new name being
# added to an already finished FlexibleName. The only exception to that woud be if it would slot into an unkown space in the
# same spot as something else that is unkown, based on the new info from the added name


# TODO: NOTE: Would this handle a case where the guy's name is something odd like "Jacob John John Joshua"? Or would it be
# super confusing to the name extrapolator? It's definitely going to be worth testing this to make sure that it handles
# that alright, especially if it's not clear that the names are right next to each other at first. Here's an example test
# case: [J J J J, Jacob John John, Jacob J John, Jacob John Joshua, Jacob John, Jacob Joshua, Jacob J John Joshua]
# In this test case, we want the function to assume that Joshua must come after the Johns and that Jacob must come before
# the Johns, since that is the best assumption based on the data that is given and their positionality to each other.
# It might be helpful to note in this case that Jacob *can't* be in the third or fourth position, logically speaking due to
# it being in front of at least 2 other names in one of the test cases. This same logic can also be used to know that Joshua
# *can't* be in the first two names.



# NOTE: This next test case is probably better implemented *after* you get the rest of this working, so prioritize that
# and then come back to this with more info and an otherwise working application first

# TODO: NOTE: None of these factor in the possibility of a Spanish last name like Maria-Sanchez, which could
# be represented as Maria Sanchez, Maria, Sanchez, or Maria-Sanchez. Ideally there would be some kind of logic
# that looks for hypenated names and either breaks them up (but notes they have the same possible position)
# or checks names against the hyphenated name to see if it's contained within that surname and then determine
# that the hyphenated name is going to be more accurate. Or something like that

# NOTE: For the case above, it's probably worth having some sort of check for hypens across names. If a hypen
# is found between two name fragments, create some sort of flag to factor in that it's now a hypenated name and
# then run through the name fragments to determine which ones can likely be collapsed into the hypenated one.
# This should definitely factor in proximity of the fragment to the combined one though, so that if the name is
# something like "Juanita Maria Maria-Sanchez", it doesn't also collapse the middle name into the hypenated
# last name. A good test case for this might be something like [Juanita M Sanchez, Juanita M Maria, Juanita Maria M,
# Juanita Maria S, Juanita Maria Maria Sanchez, Juanita M M-S, Juanita Maria-Sanchez] or something similar. Possibly
# reorder that to make it cleaner though

path_for_typescript_version = Path(__file__).resolve().parent.parent / "NameComparatorTS" / "dist" / "NameComparatorTS" / "bridge_for_tests.js"

test_runner = PyScriptTestRunner(path_for_typescript_version)

test_runner.add_method(extrapolate_best_full_name, "extrapolateBestFullName", executor = lambda args: extrapolate_best_full_name(args[0], args[1]))

def test_simple_solveable_name_case():
    full_final_name = 'John Jacob Jingleheimer Schmidtt'

    test_case = {"input": ['J J J S', 'John Schmidtt', 'J Jingleheimer', 'John J J S', 'Jacob Jingleheimer Schmidtt']}
    python_result, typescript_result = test_runner.run("extrapolate_best_full_name", "extrapolateBestFullName", test_case)

    test_runner.assert_strict_parity(python_result, typescript_result)
    assert python_result[0] == full_final_name
    assert typescript_result[0] == full_final_name
    assert python_result[1] == {}
    assert typescript_result[1] == {}
    assert python_result[2] == [{'unedited_fragment': 'J', 'edited_fragment': 'J', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 6}, 
                                {'unedited_fragment': 'S', 'edited_fragment': 'S', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 2}, 
                                {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 2}, 
                                {'unedited_fragment': 'Schmidtt', 'edited_fragment': 'Schmidtt', 'length_of_unedited_fragment': 8, 'edited_fragment_length': 8, 'fragment_frequency': 2}, 
                                {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 2}, 
                                {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1}]
    assert typescript_result[2] == [{'unedited_fragment': 'J', 'edited_fragment': 'J', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 6}, 
                                    {'unedited_fragment': 'S', 'edited_fragment': 'S', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 2}, 
                                    {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 2}, 
                                    {'unedited_fragment': 'Schmidtt', 'edited_fragment': 'Schmidtt', 'length_of_unedited_fragment': 8, 'edited_fragment_length': 8, 'fragment_frequency': 2}, 
                                    {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 2}, 
                                    {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1}]
    

def test_case_with_unknown_location():
    full_final_name = 'John J J Schmidtt'

    test_case = {"input": ['J J J S', 'John Schmidtt', 'J. Jingleheimer', 'John J. J. S.']}
    python_result, typescript_result = test_runner.run("extrapolate_best_full_name", "extrapolateBestFullName", test_case)

    test_runner.assert_strict_parity(python_result, typescript_result)
    assert python_result[0] == full_final_name
    assert typescript_result[0] == full_final_name
    assert python_result[1] == {
                                    1: 
                                        [
                                            {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 1}
                                        ], 
                                    2:  
                                        [
                                            {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 1}
                                        ]
                                }
    assert typescript_result[1] == {
                                        1: 
                                            [
                                                {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 1}
                                            ], 
                                        2:  
                                            [
                                                {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 1}
                                            ]
                                    }
    assert python_result[2] == [{'unedited_fragment': 'J', 'edited_fragment': 'J', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 6}, 
                                {'unedited_fragment': 'S', 'edited_fragment': 'S', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 2}, 
                                {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 2}, 
                                {'unedited_fragment': 'Schmidtt', 'edited_fragment': 'Schmidtt', 'length_of_unedited_fragment': 8, 'edited_fragment_length': 8, 'fragment_frequency': 1}, 
                                {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 1}]
    assert typescript_result[2] == [{'unedited_fragment': 'J', 'edited_fragment': 'J', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 6}, 
                                    {'unedited_fragment': 'S', 'edited_fragment': 'S', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 2}, 
                                    {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 2}, 
                                    {'unedited_fragment': 'Schmidtt', 'edited_fragment': 'Schmidtt', 'length_of_unedited_fragment': 8, 'edited_fragment_length': 8, 'fragment_frequency': 1}, 
                                    {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 1}]


def test_case_with_uneven_name_lengths():
    full_final_name = 'J J J Schmidtt'

    test_case = {"input": ['J J J S', 'John Jingleheimer Schmidtt', 'Jacob Jingleheimer Schmidtt']}
    python_result, typescript_result = test_runner.run("extrapolate_best_full_name", "extrapolateBestFullName", test_case)

    test_runner.assert_strict_parity(python_result, typescript_result)
    assert python_result[0] == full_final_name
    assert typescript_result[0] == full_final_name
    assert python_result[1] ==  {
                                    0:  
                                        [
                                            {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 1}, 
                                            {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1}
                                        ], 
                                    1:  
                                        [
                                            {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 1}, 
                                            {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 2}, 
                                            {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1} 
                                        ], 
                                    2: 
                                        [
                                            {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 1}, 
                                            {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 2}, 
                                            {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1}
                                        ]
                                }
    assert typescript_result[1] ==  {
                                        0:  
                                            [
                                                {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 1}, 
                                                {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1}
                                            ], 
                                        1:  
                                            [
                                                {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 1}, 
                                                {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 2}, 
                                                {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1} 
                                            ], 
                                        2: 
                                            [
                                                {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 1}, 
                                                {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 2}, 
                                                {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1}
                                            ]
                                    }
    assert python_result[2] ==  [{'unedited_fragment': 'J', 'edited_fragment': 'J', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 3}, 
                                 {'unedited_fragment': 'S', 'edited_fragment': 'S', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 1}, 
                                 {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 1}, 
                                 {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 2}, 
                                 {'unedited_fragment': 'Schmidtt', 'edited_fragment': 'Schmidtt', 'length_of_unedited_fragment': 8, 'edited_fragment_length': 8, 'fragment_frequency': 2}, 
                                 {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1}]
    assert typescript_result[2] == [{'unedited_fragment': 'J', 'edited_fragment': 'J', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 3}, 
                                    {'unedited_fragment': 'S', 'edited_fragment': 'S', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 1}, 
                                    {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 1}, 
                                    {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 2}, 
                                    {'unedited_fragment': 'Schmidtt', 'edited_fragment': 'Schmidtt', 'length_of_unedited_fragment': 8, 'edited_fragment_length': 8, 'fragment_frequency': 2}, 
                                    {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1}]


def test_case_with_conflicting_name_fragments():
    full_final_name = 'John J Jingleheimer Schmidtt'

    test_case = {"input": ['J J J S', 'John Jacob Jingleheimer Schmidtt', 'John Jangle Jingleheimer Schmidtt']}
    python_result, typescript_result = test_runner.run("extrapolate_best_full_name", "extrapolateBestFullName", test_case)

    test_runner.assert_strict_parity(python_result, typescript_result)
    assert python_result[0] == full_final_name
    assert typescript_result[0] == full_final_name
    assert python_result[1] == {
                                    1: 
                                        [
                                            {'unedited_fragment': 'Jangle', 'edited_fragment': 'Jangle', 'length_of_unedited_fragment': 6, 'edited_fragment_length': 6, 'fragment_frequency': 1}, 
                                            {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1}
                                        ]
                                }
    assert typescript_result[1] ==  {
                                        1: 
                                            [
                                                {'unedited_fragment': 'Jangle', 'edited_fragment': 'Jangle', 'length_of_unedited_fragment': 6, 'edited_fragment_length': 6, 'fragment_frequency': 1}, 
                                                {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1}
                                            ]
                                    }
    assert python_result[2] == [{'unedited_fragment': 'J', 'edited_fragment': 'J', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 3}, 
                                {'unedited_fragment': 'S', 'edited_fragment': 'S', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 1}, 
                                {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 2}, 
                                {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1}, 
                                {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 2}, 
                                {'unedited_fragment': 'Schmidtt', 'edited_fragment': 'Schmidtt', 'length_of_unedited_fragment': 8, 'edited_fragment_length': 8, 'fragment_frequency': 2}, 
                                {'unedited_fragment': 'Jangle', 'edited_fragment': 'Jangle', 'length_of_unedited_fragment': 6, 'edited_fragment_length': 6, 'fragment_frequency': 1}]
    assert typescript_result[2] == [{'unedited_fragment': 'J', 'edited_fragment': 'J', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 3}, 
                                    {'unedited_fragment': 'S', 'edited_fragment': 'S', 'length_of_unedited_fragment': 1, 'edited_fragment_length': 1, 'fragment_frequency': 1}, 
                                    {'unedited_fragment': 'John', 'edited_fragment': 'John', 'length_of_unedited_fragment': 4, 'edited_fragment_length': 4, 'fragment_frequency': 2}, 
                                    {'unedited_fragment': 'Jacob', 'edited_fragment': 'Jacob', 'length_of_unedited_fragment': 5, 'edited_fragment_length': 5, 'fragment_frequency': 1}, 
                                    {'unedited_fragment': 'Jingleheimer', 'edited_fragment': 'Jingleheimer', 'length_of_unedited_fragment': 12, 'edited_fragment_length': 12, 'fragment_frequency': 2}, 
                                    {'unedited_fragment': 'Schmidtt', 'edited_fragment': 'Schmidtt', 'length_of_unedited_fragment': 8, 'edited_fragment_length': 8, 'fragment_frequency': 2}, 
                                    {'unedited_fragment': 'Jangle', 'edited_fragment': 'Jangle', 'length_of_unedited_fragment': 6, 'edited_fragment_length': 6, 'fragment_frequency': 1}]



@pytest.mark.parametrize('names_to_test', ai_generated_name_lists_for_extrapolation, ids=lambda x: f"extrapolate to {x['expected_full_name']}")
def test_extrapolate_from_ai_generated_name_lists(name_to_test):

    test_case = {"input": name_to_test['list_of_variations']}
    python_result, typescript_result = test_runner.run("extrapolate_best_full_name", "extrapolateBestFullName", test_case)
    test_runner.assert_strict_parity(python_result, typescript_result)
    assert python_result[0].match == name_to_test["expected_full_name"]
    assert typescript_result[0].match == name_to_test["expected_full_name"]