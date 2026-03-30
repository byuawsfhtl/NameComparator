import pytest
# Set up the test runner stuff in the imports

# Note that the format of the test cases is as follows:
# a dictionary with an input, expected, and description (of the test)

# Actually, I'm not entirely certain how to make this a real test case since it was poorly
# designed in the first place. TODO: Come back to this one and make it actually work and
# test something meaningful

@pytest.mark.parameterize('', 'imported_name_pairs', ids=lambda x: x[''])
def test_on_name_pairs(test_data):
