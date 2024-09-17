from dataclasses import dataclass

import NameComparator.src.clean as cleanMod
import NameComparator.src.nicknames as nicknameMod
import NameComparator.src.insights as insightMod
import NameComparator.src.comparisons as comparisonMod
import NameComparator.src.modify as modifyMod
import NameComparator.src.ipa as ipaMod

@dataclass
class ResultsOfNameComparison:
    """Represents the results of a name comparison.

    Attributes:
        nameA (str): the original nameA
        nameB (str): the original nameB
        tooShort (bool): whether either of the names are one word or less. Defaults to True
        tooGeneric (bool): whether either of the names is too generic. Defaults to True
        match (bool): whether the names are a match. Defaults to False
        attempt1WordCombo (list[tuple[str, str, int]]|None): the first matchup of words. Defaults to None
        attempt1NameA (str|None): the edited nameA after the first attempt. Defaults to None
        attempt1NameB (str|None): the edited nameB after the first attempt. Defaults to None
        attempt2WordCombo (list[tuple[str, str, int]]|None): the second matchup of words. Defaults to None
        attempt2NameA (str|None): the edited nameA after the second attempt. Defaults to None
        attempt2NameB (str|None): the edited nameB after the second attempt. Defaults to None
        attempt3WordCombo (list[tuple[str, str, int]]|None): the third matchup of words. Defaults to None
        attempt3NameA (str|None): the nameA pronunciation after the third attempt. Defaults to None
        attempt3NameB (str|None): the nameB pronunciation after the third attempt. Defaults to None
        attempt4WordCombo (list[tuple[str, str, int]]|None): the fourth matchup of words. Defaults to None
        attempt4NameA (str|None): the nameA pronunciation after the fourth attempt. Defaults to None
        attempt4NameB (str|None): the nameB pronunciation after the fourth attempt. Defaults to None
    """    
    nameA: str
    nameB: str
    tooShort: bool = True
    tooGeneric: bool = True
    match: bool = False
    attempt1WordCombo: list[tuple[str, str, int]]|None = None
    attempt1NameA: str|None = None
    attempt1NameB: str|None = None
    attempt2WordCombo: list[tuple[str, str, int]]|None = None
    attempt2NameA: str|None = None
    attempt2NameB: str|None = None
    attempt3WordCombo: list[tuple[str, str, int]]|None = None
    attempt3NameA: str|None = None
    attempt3NameB: str|None = None
    attempt4WordCombo: list[tuple[str, str, int]]|None = None
    attempt4NameA: str|None = None
    attempt4NameB: str|None = None

def compareTwoNames(nameA:str, nameB:str) -> ResultsOfNameComparison:
    """Compares two names to identify whether they are a fuzzy match.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        dict: the data gleaned from the comparison (whether they are a match, whether one or both names is too generic, whether one or both names is too short, along with the debugging attempt data)
    """        
    # Throw an error if an arg isn't right
    if not isinstance(nameA, str):
        raise TypeError(f'nameA was {type(nameA)}. Must be str.')
    if not isinstance(nameB, str):
        raise TypeError(f'nameB was {type(nameB)}. Must be str.')

    # Get info unrelated to name match
    results = ResultsOfNameComparison(nameA=nameA, nameB=nameB)
    nameA = cleanMod.cleanName(nameA)
    nameB = cleanMod.cleanName(nameB)
    nameA, nameB = cleanMod.cleanNamesTogether(nameA, nameB)
    results.tooShort = insightMod.eitherNameTooShort(nameA, nameB)
    if not nameA:
        nameA = '_'
    if not nameB:
        nameB = '_'
    if (nameA == '_') or (nameB == '_'):
        return results
    results.tooGeneric = insightMod.eitherNameTooGeneric(nameA, nameB)
    nameA, nameB = nicknameMod.removeNicknames(nameA, nameB)

    # 1st attempt: Checks if names are a match according to string comparison alone
    match, wordCombo = comparisonMod.spellingComparison(nameA, nameB)
    results.attempt1WordCombo = wordCombo
    results.attempt1NameA = nameA
    results.attempt1NameB = nameB
    if match:
        results.match = True
        return results

    # Failed first attempt. Check if names are even worth continuing
    if insightMod.isWorthContinuing(nameA, nameB) is False:
        return results

    # 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
    modifiedNameA, modifiedNameB = modifyMod.modifyNamesTogether(nameA, nameB)
    match, wordCombo = comparisonMod.spellingComparison(modifiedNameA, modifiedNameB)
    results.attempt2WordCombo = wordCombo
    results.attempt2NameA = modifiedNameA
    results.attempt2NameB = modifiedNameB
    if match:
        results.match = True
        return results
        
    # 3rd attempt: Checks if modified names are a match according to pronunciation
    ipaOfModNameA = cleanMod.cleanIpa(ipaMod.getIpa(modifiedNameA))
    ipaOfModNameB = cleanMod.cleanIpa(ipaMod.getIpa(modifiedNameB))
    ipaOfModNameA, ipaOfModNameB = modifyMod.modifyIpasTogether(ipaOfModNameA, ipaOfModNameB)
    match, wordCombo = comparisonMod.pronunciationComparison(ipaOfModNameA, ipaOfModNameB, modifiedNameA, modifiedNameB)
    results.attempt3WordCombo = wordCombo
    results.attempt3NameA = ipaOfModNameA
    results.attempt3NameB = ipaOfModNameB
    if match:
        results.match = True
        return results

    # 4th attempt: Check if original names are a match according to pronunciation'
    ipaOfNameA = cleanMod.cleanIpa(ipaMod.getIpa(nameA))
    ipaOfNameB = cleanMod.cleanIpa(ipaMod.getIpa(nameB))
    ipaOfNameA, ipaOfNameB = modifyMod.modifyIpasTogether(ipaOfNameA, ipaOfNameB)
    match, wordCombo = comparisonMod.pronunciationComparison(ipaOfNameA, ipaOfNameB, nameA, nameB)
    results.attempt4WordCombo = wordCombo
    results.attempt4NameA = ipaOfNameA
    results.attempt4NameB = ipaOfNameB, 
    if match:
        results.match = True
    return results