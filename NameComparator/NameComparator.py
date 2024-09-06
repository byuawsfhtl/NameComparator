from typing import NamedTuple

import NameComparator.src.clean as cleanMod
import NameComparator.src.nicknames as nicknameMod
import NameComparator.src.insights as insightMod
import NameComparator.src.comparisons as comparisonMod
import NameComparator.src.modify as modifyMod
import NameComparator.src.ipa as ipaMod

class ResultsOfNameComparison(NamedTuple):
    pass


class NameComparator():
    """The class used for fuzzy comparing two names.
    """    
    @staticmethod
    def compareTwoNames(nameA:str, nameB:str) -> dict:
        """Compares two names to identify whether they are a fuzzy match.

        Args:
            nameA (str): a name
            nameB (str): a name

        Returns:
            dict: the data gleaned from the comparison (whether they are a match, whether one or both names is too generic, whether one or both names is too short, along with the debugging attempt data)
        """        
        data = {
            'match': False,
            'tooGeneric': False,
            'tooShort': False,
            'attempt1': None,
            'attempt2': None,
            'attempt3': None,
            'attempt4': None
        }
        if not isinstance(nameA, str):
            raise TypeError(f'nameA was {type(nameA)}. Must be str.')
        if not isinstance(nameB, str):
            raise TypeError(f'nameB was {type(nameB)}. Must be str.')

        nameA = cleanMod.cleanName(nameA)
        nameB = cleanMod.cleanName(nameB)
        nameA, nameB = cleanMod.cleanNamesTogether(nameA, nameB)
        data['tooShort'] = insightMod.eitherNameTooShort(nameA, nameB)
        if not nameA:
            nameA = '_'
        if not nameB:
            nameB = '_'
        if (nameA == '_') or (nameB == '_'):
            return data
        data['tooGeneric'] = insightMod.eitherNameTooGeneric(nameA, nameB)
        nameA, nameB = nicknameMod.removeNicknames(nameA, nameB)

        # 1st attempt: Checks if names are a match according to string comparison alone
        match, wordCombo = comparisonMod.spellingComparison(nameA, nameB)
        data['attempt1'] = (nameA, nameB, wordCombo)
        if match:
            data['match'] = True
            return data

        # Failed first attempt. Check if names are even worth continuing
        if insightMod.isWorthContinuing(nameA, nameB) is False:
            return data

        # 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
        modifiedNameA, modifiedNameB = modifyMod.modifyNamesTogether(nameA, nameB)
        match, wordCombo = comparisonMod.spellingComparison(modifiedNameA, modifiedNameB)
        data['attempt2'] = (modifiedNameA, modifiedNameB, wordCombo)
        if match:
            data['match'] = True
            return data
            
        # 3rd attempt: Checks if modified names are a match according to pronunciation
        ipaOfModNameA = ipaMod.getIpa(modifiedNameA)
        ipaOfModNameB = ipaMod.getIpa(modifiedNameB)
        ipaOfModNameA, ipaOfModNameB = modifyMod.modifyIpasTogether(ipaOfModNameA, ipaOfModNameB)
        match, wordCombo = comparisonMod.pronunciationComparison(ipaOfModNameA, ipaOfModNameB, modifiedNameA, modifiedNameB)
        data['attempt3'] = (ipaOfModNameA, ipaOfModNameB, wordCombo)
        if match:
            data['match'] = True
            return data

        # 4th attempt: Check if original names are a match according to pronunciation'
        ipaOfNameA = ipaMod.getIpa(nameA)
        ipaOfNameB = ipaMod.getIpa(nameB)
        ipaOfNameA, ipaOfNameB = modifyMod.modifyIpasTogether(ipaOfNameA, ipaOfNameB)
        match, wordCombo = comparisonMod.pronunciationComparison(ipaOfNameA, ipaOfNameB, nameA, nameB)
        data['attempt4'] = (ipaOfNameA, ipaOfNameB, wordCombo)
        if match:
            data['match'] = True
        return data