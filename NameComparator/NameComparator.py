from typing import NamedTuple

from NameComparator.dataProcessors.clean import cleanName, cleanNamesTogether
from NameComparator.dataProcessors.nicknames import removeNicknames
from NameComparator.dataProcessors.insights import eitherNameTooGeneric, eitherNameTooShort, isWorthContinuing
from NameComparator.dataProcessors.comparisons import spellingComparison, pronunciationComparison
from NameComparator.dataProcessors.modify import modifyNamesTogether

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

        name0 = cleanName(name0)
        name1 = cleanName(name1)
        name0, name1 = cleanNamesTogether(name0, name1)
        data['tooShort'] = eitherNameTooShort(name0, name1)
        if not name0:
            name0 = '_'
        if not name1:
            name1 = '_'
        if (name0 == '_') or (name1 == '_'):
            return data
        data['tooGeneric'] = eitherNameTooGeneric(name0, name1)
        name0, name1 = removeNicknames(name0, name1)

        # 1st attempt: Checks if names are a match according to string comparison alone
        match, wordCombo = spellingComparison(name0, name1)
        data['attempt1'] = (name0, name1, wordCombo)
        if match:
            data['match'] = True
            return data

        # Failed first attempt. Check if names are even worth continuing
        if isWorthContinuing(name0, name1) is False:
            return data

        # 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
        modifiedName0, modifiedName1 = modifyNamesTogether(name0, name1)
        match, wordCombo = spellingComparison(modifiedName0, modifiedName1)
        data['attempt2'] = (modifiedName0, modifiedName1, wordCombo)
        if match:
            data['match'] = True
            return data
            
        # 3rd attempt: Checks if modified names are a match according to pronunciation
        match, wordCombo, ipaModifiedName0, ipaModifiedName1 = pronunciationComparison(modifiedName0, modifiedName1)
        data['attempt3'] = (ipaModifiedName0, ipaModifiedName1, wordCombo)
        if match:
            data['match'] = True
            return data

        # 4th attempt: Check if original names are a match according to pronunciation
        match, wordCombo, ipaName0, ipaName1 = pronunciationComparison(name0, name1)
        data['attempt4'] = (ipaName0, ipaName1, wordCombo)
        if match:
            data['match'] = True
        return data