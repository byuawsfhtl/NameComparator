from dataclasses import dataclass
from typing import NamedTuple

import NameComparator.src.clean as cleanMod
import NameComparator.src.nicknames as nicknameMod
import NameComparator.src.insights as insightMod
import NameComparator.src.comparisons as comparisonMod
import NameComparator.src.modify as modifyMod
import NameComparator.src.ipa as ipaMod
import NameComparator.src.uniqueness as uniquenessMod
from NameComparator.src.uniqueness import FrequencyData
from NameComparator.data.frequency.surnamesUsaTo1950 import data as usaTo1950Surnames
from NameComparator.data.frequency.firstNamesUsaTo1950 import data as usaTo1950FirstNames

class Attempt(NamedTuple):
    """Represents an attempt at name comparison (often used for debugging).

    Attributes:
        name_a: the version of name_a for this attempt 
        name_b: the version of name_b for this attempt
        word_combo (list[tuple[str, str, int]]): the matchup of words in the names and how well.
    """
    name_a: str
    name_b: str
    word_combo: list[tuple[str, str, int]] # TODO make this a model too

@dataclass
class ResultsOfNameComparison:
    """Represents the results of a name comparison.

    Attributes:
        name_a: the original nameA
        name_b: the original nameB
        match: whether the names are a match. Defaults to False
        uniqueness: how unique the names were compared to chosen population. Defaults to 0.0.
        too_short: whether either of the names are one word or less. Defaults to True
        attempt_1: Debugging data about the first attempt to compare the names. Defaults to None.
        attempt_2: Debugging data about the second attempt to compare the names. Defaults to None.
        attempt_3: Debugging data about the third attempt to compare the names. Defaults to None.
        attempt_4: Debugging data about the fourth attempt to compare the names. Defaults to None.
    """
    name_a: str
    name_b: str
    match: bool = False
    uniqueness: float = 0.0
    too_short: bool = True
    attempt_1: Attempt | None = None
    attempt_2: Attempt | None = None
    attempt_3: Attempt | None = None
    attempt_4: Attempt | None = None

def compare_two_names(name_a: str, name_b: str, frequency_data:FrequencyData|None = None) -> ResultsOfNameComparison:
    """Compares two names to identify whether they are a fuzzy match.

    Args:
        name_a: the name of a person
        name_b: the name of a person
        frequency_data: the first name + surname frequencies in a chosen population- Defaults to None

    Returns:
        ResultsOfNameComparison: the data gleaned from the comparison(whether they are a match, whether one or both names is too generic,
        whether one or both names is too short, along with the debugging attempt data)
    """        
    # Deal with optional arg
    if frequency_data is None:
        frequency_data = FrequencyData(usaTo1950FirstNames, usaTo1950Surnames)

    # Data validation
    if not isinstance(name_a, str) or not isinstance(name_b, str):
        raise TypeError(f'nameA was {type(name_a)}. Must be str. nameB was {type(name_b)}. Must be str.')
    if not isinstance(frequency_data, FrequencyData):
        raise TypeError(f'frequencyData was {type(frequency_data)}. Must be FrequencyData.')

    # Create the return object to edit later
    results = ResultsOfNameComparison(name_a=name_a, name_b=name_b)

    # Clean the name
    name_a = cleanMod.clean_name(name_a)
    name_b = cleanMod.clean_name(name_b)
    name_a, name_b = cleanMod.clean_names_together(name_a, name_b)

    # Deal with too short names
    results.too_short = insightMod.either_name_too_short(name_a, name_b)
    if not name_a:
        name_a = '_'
    if not name_b:
        name_b = '_'
    if (name_a == '_') or (name_b == '_'):
        return results
    
    # Find the uniqueness of this name matchup (ie. hopefully not 'John Smith' and 'J Smith')
    results.uniqueness = uniquenessMod.score_uniqueness(name_a, name_b, frequency_data)

    # Remove nicknames before the actual comparison
    name_a, name_b = nicknameMod.remove_nicknames(name_a, name_b)

    # 1st attempt: Checks if names are a match according to string comparison alone
    match, word_combo = comparisonMod.spelling_comparison(name_a, name_b)
    results.attempt_1 = Attempt(name_a, name_b, word_combo)
    if match:
        results.match = True
        return results

    # Failed first attempt. Check if names are even worth continuing
    if insightMod.is_worth_continuing(name_a, name_b) is False:
        return results

    # 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
    modified_name_a, modified_name_b = modifyMod.modify_names_together(name_a, name_b)
    match, word_combo = comparisonMod.spelling_comparison(modified_name_a, modified_name_b)
    results.attempt_2 = Attempt(modified_name_a, modified_name_b, word_combo)
    if match:
        results.match = True
        return results
        
    # 3rd attempt: Checks if modified names are a match according to pronunciation
    ipa_of_modified_name_a = cleanMod.clean_ipa(ipaMod.get_ipa(modified_name_a))
    ipa_of_modified_name_b = cleanMod.clean_ipa(ipaMod.get_ipa(modified_name_b))
    match, word_combo = comparisonMod.pronunciation_comparison(modified_name_a, modified_name_b)
    results.attempt_3 = Attempt(ipa_of_modified_name_a, ipa_of_modified_name_b, word_combo)
    if match:
        results.match = True
        return results

    # 4th attempt: Check if original names are a match according to pronunciation'
    ipa_of_name_a = ipaMod.get_ipa(name_a)
    ipa_of_name_b = ipaMod.get_ipa(name_b)
    match, word_combo = comparisonMod.pronunciation_comparison(name_a, name_b)
    results.attempt_4 = Attempt(ipa_of_name_a, ipa_of_name_b, word_combo)
    if match:
        results.match = True
    return results
