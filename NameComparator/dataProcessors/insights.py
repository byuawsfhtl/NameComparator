import NameComparator.dataProcessors.usefulTools as usefulToolsMod
import NameComparator.data.topSurnames as topSurnames

def isWorthContinuing(name0:str, name1:str) -> bool:
    """Identifies if a name comparison will always prove false.

    Args:
        name0 (str): _description_
        name1 (str): _description_

    Returns:
        bool: whether the names are worth working on further
    """        
    wordCombo = usefulToolsMod.findWhichWordsMatchAndHowWell(name0, name1)
    oneLetterMatchFailCount = 0
    for match in wordCombo:
        word0 = name0[int(match[0])]
        word1 = name1[int(match[1])]
        score = match[2]
        if (score == 0) and ((len(word0) == 1) or ((len(word1) == 1))):
            oneLetterMatchFailCount += 1
    if (oneLetterMatchFailCount >= 1) and (len(wordCombo) <= 3):
        return False
    return True

def eitherNameTooShort(name0:str, name1:str) -> bool:
    """Identifies if either of the names is too short.

    Args:
        name0 (str): a name
        name1 (str): a name

    Returns:
        bool: whether either was too short
    """        
    combo = usefulToolsMod.findWhichWordsMatchAndHowWell(name0, name1)
    shortestWordCount = len(combo)
    if shortestWordCount < 2:
        return True
    return False

def eitherNameTooGeneric(name0:str, name1:str) -> bool:
    """Identifies if either name is too generic using lastname.

    Args:
        name0 (str): a name
        name1 (str): a name

    Returns:
        bool: whether the name is too generic
    """        
    # Return False if either name is missing a lastname
    shortestWordCount = min(len(name0.split()), len(name1.split()))
    if shortestWordCount <= 1:
        return False
    # If both last names are very rare, returns False
    if _hasRareSurname(name0) and _hasRareSurname(name1):
        return False
    # Check if the numbers of initials in all pairs makes a word match too uncertain
    nonInitialMatchCount = 0
    for _, _, word0, word1 in usefulToolsMod.getPairIndicesAndWords(name0, name1):
        initialInWord0 = (len(word0) == 1)
        initialInWord1 = (len(word1) == 1)
        if initialInWord0 or initialInWord1:
            continue
        nonInitialMatchCount += 1
    if shortestWordCount <= nonInitialMatchCount + 1:
        return True
    return False

def _hasRareSurname(name:str) -> bool:
    """Identifies if a name has a rare surname.

    Args:
        name (str): a name

    Returns:
        bool: whether the name's surname is rare
    """        
    surname = name.split()[-1]
    if surname not in topSurnames.data:
        return True
    return False