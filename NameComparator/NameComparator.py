from dataclasses import dataclass
from typing import NamedTuple
from json import loads as json_loads
from importlib.resources import files

import NameComparator.src.clean as cleanMod
import NameComparator.src.nicknames as nicknameMod
import NameComparator.src.insights as insightMod
import NameComparator.src.comparisons as comparisonMod
import NameComparator.src.modify as modifyMod
import NameComparator.src.ipa as ipaMod
import NameComparator.src.uniqueness as uniquenessMod
from NameComparator.src.uniqueness import FrequencyData

unparsed_usa_to_1950_surnames = files('NameComparator').joinpath('data/frequency/surnamesUsaTo1950.json').read_text()
unparsed_usa_to_1950_first_names = files('NameComparator').joinpath('data/frequency/firstNamesUsaTo1950.json').read_text()

class Attempt(NamedTuple):
    """Represents an attempt at name comparison (often used for debugging).

    Attributes:
        name_one: The version of the first name to be used in this attempt
        name_two: The version of the second name to be used in this attempt
        word_combo: A list of tuples describing the word matchups and quality
    """
    name_one: str
    name_two: str
    word_combo: list[tuple[str, str, int]] # TODO make this a model too

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
    name_one = cleanMod.clean_name(name_one)
    name_two = cleanMod.clean_name(name_two)
    name_one, name_two = cleanMod.clean_names_by_comparison(name_one, name_two)

    # Deal with names that are too short
    results.too_short = insightMod.either_name_too_short(name_one, name_two)
    if not name_one:
        name_one = '_'
    if not name_two:
        name_two = '_'
    if (name_one == '_') or (name_two == '_'):
        return results
    
    # Find the uniqueness of this name matchup (ie. hopefully not 'John Smith' and 'J Smith')
    results.uniqueness = uniquenessMod.score_uniqueness(name_one, name_two, frequency_data)

    # Remove nicknames before the actual comparison
    name_one, name_two = nicknameMod.remove_nicknames(name_one, name_two)

    # 1st attempt: Checks if names are a match according to string comparison alone
    match, word_combo = comparisonMod.compare_spelling(name_one, name_two)
    results.attempt_one = Attempt(name_one, name_two, word_combo)
    if match:
        results.match = True
        return results

    # Failed first attempt. Check if names are even worth continuing
    if insightMod.is_worth_continuing(name_one, name_two) is False:
        return results

    # 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
    modified_name_one, modified_name_two = modifyMod.modify_names_together(name_one, name_two)
    match, word_combo = comparisonMod.compare_spelling(modified_name_one, modified_name_two)
    results.attempt_two = Attempt(modified_name_one, modified_name_two, word_combo)
    if match:
        results.match = True
        return results
        
    # 3rd attempt: Checks if modified names are a match according to pronunciation
    ipa_of_modified_name_one = cleanMod.clean_ipa(ipaMod.get_ipa(modified_name_one))
    ipa_of_modified_name_two = cleanMod.clean_ipa(ipaMod.get_ipa(modified_name_two))
    ipa_of_modified_name_one, ipa_of_modified_name_two = modifyMod.modify_ipas_by_comparison(ipa_of_modified_name_one, ipa_of_modified_name_two)
    match, word_combo = comparisonMod.pronunciation_comparison(ipa_of_modified_name_one, ipa_of_modified_name_two, modified_name_one, modified_name_two)
    results.attempt_three = Attempt(ipa_of_modified_name_one, ipa_of_modified_name_two, word_combo)
    if match:
        results.match = True
        return results

    # 4th attempt: Check if original names are a match according to pronunciation
    ipa_of_name_one = cleanMod.clean_ipa(ipaMod.get_ipa(name_one))
    ipa_of_name_two = cleanMod.clean_ipa(ipaMod.get_ipa(name_two))
    ipa_of_name_one, ipa_of_name_two = modifyMod.modify_ipas_by_comparison(ipa_of_name_one, ipa_of_name_two)
    match, word_combo = comparisonMod.pronunciation_comparison(ipa_of_name_one, ipa_of_name_two, name_one, name_two)
    results.attempt_four = Attempt(ipa_of_name_one, ipa_of_name_two, word_combo)
    if match:
        results.match = True
    return results