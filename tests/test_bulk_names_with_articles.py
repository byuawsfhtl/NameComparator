import pytest
from test_data._articleNames import articleNames as list_of_names_with_articles
from pyscripttestutils import PyScriptTestRunner
from NameComparator.NameComparator import compare_two_names
# Set up the test runner stuff in the imports

# Note that the format of the test cases is as follows:
# a dictionary with an input, expected, and description (of the test)

test_runner = PyScriptTestRunner()

@pytest.mark.parameterize('name_with_article_to_test', list_of_names_with_articles, ids=lambda x: x[''])
def test_on_names_with_articles(name_with_article_to_test):
    test_case = {"input": name_with_article_to_test["input"], "expected": name_with_article_to_test["expected"], "mocks": {}}

    # Use the test runner to return a python and typescript result

    # assert that the test cases are what is expected