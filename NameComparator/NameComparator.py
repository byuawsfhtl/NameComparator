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
        name_one (str): the version of name_one for this attempt 
        name_two (str): the version of name_two for this attempt
        word_combo (list[tuple[str, str, int]]): the matchup of words in the names and how well.
    """
    name_one: str
    name_two: str
    word_combo: list[tuple[str, str, int]] # TODO make this a model too

@dataclass
class ResultsOfNameComparison:
    """Represents the results of a name comparison.

    Attributes:
        name_one (str): the original name_one
        name_two (str): the original name_two
        match (bool): whether the names are a match. Defaults to False
        uniqueness (float): how unique the names were compared to chosen population. Defaults to 0.0.
        tooShort (bool): whether either of the names are one word or less. Defaults to True
        attempt1 (Attempt | None): Debugging data about the first attempt to compare the names. Defaults to None.
        attempt2 (Attempt | None): Debugging data about the second attempt to compare the names. Defaults to None.
        attempt3 (Attempt | None): Debugging data about the third attempt to compare the names. Defaults to None.
        attempt4 (Attempt | None): Debugging data about the fourth attempt to compare the names. Defaults to None.
    """
    name_one: str
    name_two: str
    match: bool = False
    uniqueness: float = 0.0
    tooShort: bool = True
    attempt1: Attempt | None = None
    attempt2: Attempt | None = None
    attempt3: Attempt | None = None
    attempt4: Attempt | None = None

def compareTwoNames(name_one:str, name_two:str, frequencyData:FrequencyData|None = None) -> ResultsOfNameComparison:
    """Compares two names to identify whether they are a fuzzy match.

    Args:
        name_one (str): a name
        name_two (str): a name
        frequencyData (FrequencyData | None, optional): the first name and surname frequencies in a chosen population- Defaults to None

    Returns:
        ResultsOfNameComparison: the data gleaned from the comparison(whether they are a match, whether one or both names is too generic,
        whether one or both names is too short, along with the debugging attempt data)
    """        
    # Deal with optional arg
    if frequencyData is None:
        frequencyData = FrequencyData(usaTo1950FirstNames, usaTo1950Surnames)

    # Data validation
    if not isinstance(name_one, str) or not isinstance(name_two, str):
        raise TypeError(f'name_one was {type(name_one)}. Must be str. name_two was {type(name_two)}. Must be str.')
    if not isinstance(frequencyData, FrequencyData):
        raise TypeError(f'frequencyData was {type(frequencyData)}. Must be FrequencyData.')

    # Create the return object to edit later
    results = ResultsOfNameComparison(name_one=name_one, name_two=name_two)

    # Clean the name
    name_one = cleanMod.clean_name(name_one)
    name_two = cleanMod.clean_name(name_two)
    name_one, name_two = cleanMod.clean_names_by_comparison(name_one, name_two)

    # Deal with too short names
    results.tooShort = insightMod.either_name_too_short(name_one, name_two)
    if not name_one:
        name_one = '_'
    if not name_two:
        name_two = '_'
    if (name_one == '_') or (name_two == '_'):
        return results
    
    # Find the uniqueness of this name matchup (ie. hopefully not 'John Smith' and 'J Smith')
    results.uniqueness = uniquenessMod.scoreUniqueness(name_one, name_two, frequencyData)

    # Remove nicknames before the actual comparison
    name_one, name_two = nicknameMod.removeNicknames(name_one, name_two)

    # 1st attempt: Checks if names are a match according to string comparison alone
    match, word_combo = comparisonMod.compare_spelling(name_one, name_two)
    results.attempt1 = Attempt(name_one, name_two, word_combo)
    if match:
        results.match = True
        return results

    # Failed first attempt. Check if names are even worth continuing
    if insightMod.is_worth_continuing(name_one, name_two) is False:
        return results

    # 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
    modifiedname_one, modifiedname_two = modifyMod.modifyNamesTogether(name_one, name_two)
    match, word_combo = comparisonMod.compare_spelling(modifiedname_one, modifiedname_two)
    results.attempt2 = Attempt(modifiedname_one, modifiedname_two, word_combo)
    if match:
        results.match = True
        return results
        
    # 3rd attempt: Checks if modified names are a match according to pronunciation
    ipaOfModname_one = cleanMod.clean_ipa(ipaMod.getIpa(modifiedname_one))
    ipaOfModname_two = cleanMod.clean_ipa(ipaMod.getIpa(modifiedname_two))
    ipaOfModname_one, ipaOfModname_two = modifyMod.modifyIpasTogether(ipaOfModname_one, ipaOfModname_two)
    match, word_combo = comparisonMod.pronunciation_comparison(ipaOfModname_one, ipaOfModname_two, modifiedname_one, modifiedname_two)
    results.attempt3 = Attempt(ipaOfModname_one, ipaOfModname_two, word_combo)
    if match:
        results.match = True
        return results

    # 4th attempt: Check if original names are a match according to pronunciation'
    ipa_of_name_one = cleanMod.clean_ipa(ipaMod.getIpa(name_one))
    ipa_of_name_two = cleanMod.clean_ipa(ipaMod.getIpa(name_two))
    ipa_of_name_one, ipa_of_name_two = modifyMod.modifyIpasTogether(ipa_of_name_one, ipa_of_name_two)
    match, word_combo = comparisonMod.pronunciation_comparison(ipa_of_name_one, ipa_of_name_two, name_one, name_two)
    results.attempt4 = Attempt(ipa_of_name_one, ipa_of_name_two, word_combo)
    if match:
        results.match = True
    return results