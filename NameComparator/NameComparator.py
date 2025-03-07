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
        nameA (str): the version of nameA for this attempt 
        nameB (str): the version of nameB for this attempt
        wordCombo (list[tuple[str, str, int]]): the matchup of words in the names and how well.
    """
    nameA: str
    nameB: str
    wordCombo: list[tuple[str, str, int]] # TODO make this a model too

@dataclass
class ResultsOfNameComparison:
    """Represents the results of a name comparison.

    Attributes:
        nameA (str): the original nameA
        nameB (str): the original nameB
        match (bool): whether the names are a match. Defaults to False
        uniqueness (float): how unique the names were compared to chosen population. Defaults to 0.0.
        tooShort (bool): whether either of the names are one word or less. Defaults to True
        attempt1 (Attempt | None): Debugging data about the first attempt to compare the names. Defaults to None.
        attempt2 (Attempt | None): Debugging data about the second attempt to compare the names. Defaults to None.
        attempt3 (Attempt | None): Debugging data about the third attempt to compare the names. Defaults to None.
        attempt4 (Attempt | None): Debugging data about the fourth attempt to compare the names. Defaults to None.
    """
    nameA: str
    nameB: str
    match: bool = False
    uniqueness: float = 0.0
    tooShort: bool = True
    attempt1: Attempt | None = None
    attempt2: Attempt | None = None
    attempt3: Attempt | None = None
    attempt4: Attempt | None = None

def compareTwoNames(nameA:str, nameB:str, frequencyData:FrequencyData|None = None) -> ResultsOfNameComparison:
    """Compares two names to identify whether they are a fuzzy match.

    Args:
        nameA (str): a name
        nameB (str): a name
        frequencyData (FrequencyData | None, optional): the first name and surname frequencies in a chosen population- Defaults to None

    Returns:
        ResultsOfNameComparison: the data gleaned from the comparison(whether they are a match, whether one or both names is too generic,
        whether one or both names is too short, along with the debugging attempt data)
    """        
    # Deal with optional arg
    if frequencyData is None:
        frequencyData = FrequencyData(usaTo1950FirstNames, usaTo1950Surnames)

    # Data validation
    if not isinstance(nameA, str) or not isinstance(nameB, str):
        raise TypeError(f'nameA was {type(nameA)}. Must be str. nameB was {type(nameB)}. Must be str.')
    if not isinstance(frequencyData, FrequencyData):
        raise TypeError(f'frequencyData was {type(frequencyData)}. Must be FrequencyData.')

    # Create the return object to edit later
    results = ResultsOfNameComparison(nameA=nameA, nameB=nameB)

    # Clean the name
    nameA = cleanMod.cleanName(nameA)
    nameB = cleanMod.cleanName(nameB)
    nameA, nameB = cleanMod.cleanNamesTogether(nameA, nameB)

    # Deal with too short names
    results.tooShort = insightMod.eitherNameTooShort(nameA, nameB)
    if not nameA:
        nameA = '_'
    if not nameB:
        nameB = '_'
    if (nameA == '_') or (nameB == '_'):
        return results
    
    # Find the uniqueness of this name matchup (ie. hopefully not 'John Smith' and 'J Smith')
    results.uniqueness = uniquenessMod.scoreUniqueness(nameA, nameB, frequencyData)

    # Remove nicknames before the actual comparison
    nameA, nameB = nicknameMod.removeNicknames(nameA, nameB)

    # 1st attempt: Checks if names are a match according to string comparison alone
    match, wordCombo = comparisonMod.spellingComparison(nameA, nameB)
    results.attempt1 = Attempt(nameA, nameB, wordCombo)
    if match:
        results.match = True
        return results

    # Failed first attempt. Check if names are even worth continuing
    if insightMod.isWorthContinuing(nameA, nameB) is False:
        return results

    # 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
    modifiedNameA, modifiedNameB = modifyMod.modifyNamesTogether(nameA, nameB)
    match, wordCombo = comparisonMod.spellingComparison(modifiedNameA, modifiedNameB)
    results.attempt2 = Attempt(modifiedNameA, modifiedNameB, wordCombo)
    if match:
        results.match = True
        return results
        
    # 3rd attempt: Checks if modified names are a match according to pronunciation
    ipaOfModNameA = cleanMod.cleanIpa(ipaMod.getIpa(modifiedNameA))
    ipaOfModNameB = cleanMod.cleanIpa(ipaMod.getIpa(modifiedNameB))
    ipaOfModNameA, ipaOfModNameB = modifyMod.modifyIpasTogether(ipaOfModNameA, ipaOfModNameB)
    match, wordCombo = comparisonMod.pronunciationComparison(ipaOfModNameA, ipaOfModNameB, modifiedNameA, modifiedNameB)
    results.attempt3 = Attempt(ipaOfModNameA, ipaOfModNameB, wordCombo)
    if match:
        results.match = True
        return results

    # 4th attempt: Check if original names are a match according to pronunciation'
    ipaOfNameA = cleanMod.cleanIpa(ipaMod.getIpa(nameA))
    ipaOfNameB = cleanMod.cleanIpa(ipaMod.getIpa(nameB))
    ipaOfNameA, ipaOfNameB = modifyMod.modifyIpasTogether(ipaOfNameA, ipaOfNameB)
    match, wordCombo = comparisonMod.pronunciationComparison(ipaOfNameA, ipaOfNameB, nameA, nameB)
    results.attempt4 = Attempt(ipaOfNameA, ipaOfNameB, wordCombo)
    if match:
        results.match = True
    return results