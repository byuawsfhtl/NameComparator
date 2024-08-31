from typing import NamedTuple

import NameComparator.dataProcessors.clean as cleanMod
import NameComparator.dataProcessors.nicknames as nicknameMod
import NameComparator.dataProcessors.insights as insightMod
import NameComparator.dataProcessors.comparisons as comparisonMod
import NameComparator.dataProcessors.modify as modifyMod
import NameComparator.dataProcessors.ipa as ipaMod

class ResultsOfNameComparison(NamedTuple):
    pass


class NameComparator():
    """The class used for fuzzy comparing two names.
    """    
    @staticmethod
    def compareTwoNames(name0:str, name1:str) -> dict:
        """Compares two names to identify whether they are a fuzzy match.

        Args:
            name0 (str): a name
            name1 (str): a name

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
        if not isinstance(name1, str):
            raise TypeError(f'name1 was {type(name1)}. Must be str.')

        name0 = cleanMod.cleanName(name0)
        name1 = cleanMod.cleanName(name1)
        name0, name1 = cleanMod.cleanNamesTogether(name0, name1)
        data['tooShort'] = insightMod.eitherNameTooShort(name0, name1)
        if not name0:
            name0 = '_'
        if not name1:
            name1 = '_'
        if (name0 == '_') or (name1 == '_'):
            return data
        data['tooGeneric'] = insightMod.eitherNameTooGeneric(name0, name1)
        name0, name1 = nicknameMod.removeNicknames(name0, name1)

        # 1st attempt: Checks if names are a match according to string comparison alone
        match, wordCombo = comparisonMod.spellingComparison(name0, name1)
        data['attempt1'] = (name0, name1, wordCombo)
        if match:
            data['match'] = True
            return data

        # Failed first attempt. Check if names are even worth continuing
        if insightMod.isWorthContinuing(name0, name1) is False:
            return data

        # 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
        modifiedName0, modifiedName1 = modifyMod.modifyNamesTogether(name0, name1)
        match, wordCombo = comparisonMod.spellingComparison(modifiedName0, modifiedName1)
        data['attempt2'] = (modifiedName0, modifiedName1, wordCombo)
        if match:
            data['match'] = True
            return data
            
        # 3rd attempt: Checks if modified names are a match according to pronunciation
        ipaOfModName0 = ipaMod.getIpa(modifiedName0)
        ipaOfModName1 = ipaMod.getIpa(modifiedName1)
        ipaOfModName0, ipaOfModName1 = modifyMod.modifyIpasTogether(ipaOfModName0, ipaOfModName1)
        match, wordCombo = comparisonMod.pronunciationComparison(ipaOfModName0, ipaOfModName1, modifiedName0, modifiedName1)
        data['attempt3'] = (ipaOfModName0, ipaOfModName1, wordCombo)
        if match:
            data['match'] = True
            return data

        # 4th attempt: Check if original names are a match according to pronunciation'
        ipaOfName0 = ipaMod.getIpa(name0)
        ipaOfName1 = ipaMod.getIpa(name1)
        ipaOfName0, ipaOfName1 = modifyMod.modifyIpasTogether(ipaOfName0, ipaOfName1)
        match, wordCombo = comparisonMod.pronunciationComparison(ipaOfName0, ipaOfName1, name0, name1)
        data['attempt4'] = (ipaOfName0, ipaOfName1, wordCombo)
        if match:
            data['match'] = True
        return data