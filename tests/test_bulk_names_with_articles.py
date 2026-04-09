import pytest
from test_data._articleNames import articleNames as list_of_names_with_articles
from pyscripttestutils import PyScriptTestRunner
from NameComparator.NameComparator import compare_two_names, ResultsOfNameComparison
from pathlib import Path
# Set up the test runner stuff in the imports

# Note that the format of the test cases is as follows:
# a dictionary with an input, expected, and description (of the test)

path_for_typescript_version = Path(__file__).resolve().parent.parent / "NameComparatorTS" / "dist" / "NameComparatorTS" / "bridge_for_tests.js"

def typescript_deserializer(dictionary_input):
    deserialized_item = ResultsOfNameComparison(dictionary_input.get['nameOne'], dictionary_input.get['nameTwo'], dictionary_input.get['match'],
                                                dictionary_input.get['uniqueness'], dictionary_input.get['tooShort'], dictionary_input.get['attemptOne'],
                                                dictionary_input.get['attemptTwo', ''], dictionary_input.get['attemptThree', ''], dictionary_input.get['attemptFour', ''],
                                                dictionary_input.get['mostRecentAttemptScore'], dictionary_input.get['averageScoreOfCombinedAttempts'])
    
    return deserialized_item

test_runner = PyScriptTestRunner(path_for_typescript_version, deserializer=typescript_deserializer)

test_runner.add_method(compare_two_names, "compareTwoNames", executor = lambda args: compare_two_names(args[0], args[1]))

@pytest.mark.parametrize('names_to_test', list_of_names_with_articles, ids=lambda x: x['description'])
def test_on_names_with_articles(names_to_test):

    test_case = {"input": [names_to_test["name_one"], names_to_test["name_two"]]}
    python_result, typescript_result = test_runner.run("compare_two_names", "compareTwoNames", test_case)
    assert python_result.match == names_to_test["expected"]
    assert typescript_result.get("match", '') == names_to_test["expected"]
    test_runner.assert_strict_parity(python_result, typescript_result)