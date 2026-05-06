import pytest
from test_data._articleNames import articleNames as list_of_names_with_articles
from pyscripttestutils import PyScriptTestRunner
from NameComparator.NameComparator import compare_two_names, ResultsOfNameComparison, Attempt
from pathlib import Path
# Set up the test runner stuff in the imports

# Note that the format of the test cases is as follows:
# a dictionary with an input, expected, and description (of the test)

path_for_typescript_version = Path(__file__).resolve().parent.parent / "NameComparatorTS" / "dist" / "NameComparatorTS" / "bridge_for_tests.js"

def typescript_deserializer(dictionary_input: dict):
    deserialized_item = ResultsOfNameComparison(dictionary_input.get('nameOne', ''), 
                                                dictionary_input.get('nameTwo', ''), 
                                                dictionary_input.get('match', ''),
                                                dictionary_input.get('uniqueness', ''), 
                                                dictionary_input.get('tooShort', ''), 
                                                make_into_attempt_class(dictionary_input.get('attemptOne', '')),
                                                make_into_attempt_class(dictionary_input.get('attemptTwo', '')), 
                                                make_into_attempt_class(dictionary_input.get('attemptThree', '')), 
                                                make_into_attempt_class(dictionary_input.get('attemptFour', '')), 
                                                float(dictionary_input.get('mostRecentAttemptScore', '')), 
                                                float(dictionary_input.get('averageScoreOfCombinedAttempts', '')))
    
    return deserialized_item

def make_into_attempt_class(input_item: dict):
    if input_item:
        return Attempt(input_item['nameOne'], 
                       input_item['nameTwo'], 
                       reformat_word_combos(input_item['wordCombos']), 
                       float(input_item['scoreOfAttempt']))
    
    return None

def reformat_word_combos(word_combo_list: list):

    reformatted_word_combos: list = []

    for item in word_combo_list:
        new_item = (item[0], item[1], float(item[2]))
        reformatted_word_combos.append(new_item)

    return reformatted_word_combos


test_runner = PyScriptTestRunner(path_for_typescript_version, deserializer=typescript_deserializer)

test_runner.add_method(compare_two_names, "compareTwoNames", executor = lambda args: compare_two_names(args[0], args[1]))

def test_for_specific_person():
    test_case = {"input": ["benjamin averbook", "benjamin lewis averbach"]}
    python_result, typescript_result = test_runner.run("compare_two_names", "compareTwoNames", test_case)
    test_runner.assert_strict_parity(python_result, typescript_result)
    assert typescript_result.match == False
    assert python_result.match == False


@pytest.mark.parametrize('names_to_test', list_of_names_with_articles, ids=lambda x: x['description'])
def test_on_names_with_articles(names_to_test):

    test_case = {"input": [names_to_test["name_one"], names_to_test["name_two"]]}
    python_result, typescript_result = test_runner.run("compare_two_names", "compareTwoNames", test_case)
    assert python_result.match == names_to_test["expected"]
    assert typescript_result.match == names_to_test["expected"]
    test_runner.assert_strict_parity(python_result, typescript_result)