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
    def compareTwoNames(name0:str, nameB:str) -> dict:
        """Compares two names to identify whether they are a fuzzy match.

        Args:
            name0 (str): a name
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
        if not isinstance(name0, str):
            raise TypeError(f'name0 was {type(name0)}. Must be str.')
        if not isinstance(nameB, str):
            raise TypeError(f'nameB was {type(nameB)}. Must be str.')

        name0 = cleanMod.cleanName(name0)
        nameB = cleanMod.cleanName(nameB)
        name0, nameB = cleanMod.cleanNamesTogether(name0, nameB)
        data['tooShort'] = insightMod.eitherNameTooShort(name0, nameB)
        if not name0:
            name0 = '_'
        if not nameB:
            nameB = '_'
        if (name0 == '_') or (nameB == '_'):
            return data
        data['tooGeneric'] = insightMod.eitherNameTooGeneric(name0, nameB)
        name0, nameB = nicknameMod.removeNicknames(name0, nameB)

        # 1st attempt: Checks if names are a match according to string comparison alone
        match, wordCombo = comparisonMod.spellingComparison(name0, nameB)
        data['attempt1'] = (name0, nameB, wordCombo)
        if match:
            data['match'] = True
            return data

        # Failed first attempt. Check if names are even worth continuing
        if insightMod.isWorthContinuing(name0, nameB) is False:
            return data

        # 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
        modifiedName0, modifiedNameB = modifyMod.modifyNamesTogether(name0, nameB)
        match, wordCombo = comparisonMod.spellingComparison(modifiedName0, modifiedNameB)
        data['attempt2'] = (modifiedName0, modifiedNameB, wordCombo)
        if match:
            data['match'] = True
            return data
            
        # 3rd attempt: Checks if modified names are a match according to pronunciation
        ipaOfModName0 = ipaMod.getIpa(modifiedName0)
        ipaOfModNameB = ipaMod.getIpa(modifiedNameB)
        ipaOfModName0, ipaOfModNameB = modifyMod.modifyIpasTogether(ipaOfModName0, ipaOfModNameB)
        match, wordCombo = comparisonMod.pronunciationComparison(ipaOfModName0, ipaOfModNameB, modifiedName0, modifiedNameB)
        data['attempt3'] = (ipaOfModName0, ipaOfModNameB, wordCombo)
        if match:
            data['match'] = True
            return data

        # 4th attempt: Check if original names are a match according to pronunciation'
        ipaOfName0 = ipaMod.getIpa(name0)
        ipaOfNameB = ipaMod.getIpa(nameB)
        ipaOfName0, ipaOfNameB = modifyMod.modifyIpasTogether(ipaOfName0, ipaOfNameB)
        match, wordCombo = comparisonMod.pronunciationComparison(ipaOfName0, ipaOfNameB, name0, nameB)
        data['attempt4'] = (ipaOfName0, ipaOfNameB, wordCombo)
        if match:
            data['match'] = True
        return data