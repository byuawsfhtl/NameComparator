import pytest
from test_data._particleNames import particleNames as list_of_names_with_particles
from test_bulk_names_with_articles import test_runner

@pytest.mark.parametrize('names_to_test', list_of_names_with_particles, ids=lambda x: x['description'])
def test_on_names_with_particles(names_to_test):

    test_case = {"input": [names_to_test["name_one"], names_to_test["name_two"]]}
    python_result, typescript_result = test_runner.run("compare_two_names", "compareTwoNames", test_case)
    test_runner.assert_strict_parity(python_result, typescript_result)
    assert python_result.match == names_to_test["expected"]
    assert typescript_result.match == names_to_test["expected"]
