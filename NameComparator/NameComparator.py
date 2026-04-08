from dataclasses import dataclass
from typing import NamedTuple
from json import loads as json_loads
from importlib.resources import files

from NameComparator.src.clean import clean_name, clean_names_by_comparison, clean_ipa
from NameComparator.src.nicknames import remove_nicknames
from NameComparator.src.insights import is_worth_continuing, either_name_too_short
from NameComparator.src.comparisons import compare_spelling, pronunciation_comparison
from NameComparator.src.modify import modify_names_together, modify_ipas_by_comparison
from NameComparator.src.ipa import get_ipa
from NameComparator.src.uniqueness import score_uniqueness
from NameComparator.src.uniqueness import FrequencyData

unparsed_usa_to_1950_surnames = files('data').joinpath('frequency/surnamesUsaTo1950.json').read_text()
unparsed_usa_to_1950_first_names = files('data').joinpath('frequency/firstNamesUsaTo1950.json').read_text()

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