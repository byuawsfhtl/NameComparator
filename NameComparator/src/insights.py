import NameComparator.src.usefulTools as usefulToolsMod
import NameComparator.data.topSurnames as topSurnames

def isWorthContinuing(nameA:str, nameB:str) -> bool:
    """Identifies if a name comparison will always prove false.

    Args:
        nameA (str): _description_
        nameB (str): _description_

    Returns:
        bool: whether the names are worth working on further
    """        
    wordCombo = usefulToolsMod.findWhichWordsMatchAndHowWell(nameA, nameB)
    oneLetterMatchFailCount = 0
    for match in wordCombo:
        wordA = nameA[int(match[0])]
        wordB = nameB[int(match[1])]
        score = match[2]
        if (score == 0) and ((len(wordA) == 1) or ((len(wordB) == 1))):
            oneLetterMatchFailCount += 1
    if (oneLetterMatchFailCount >= 1) and (len(wordCombo) <= 3):
        return False
    return True

def eitherNameTooShort(nameA:str, nameB:str) -> bool:
    """Identifies if either of the names is too short.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        bool: whether either was too short
    """        
    combo = usefulToolsMod.findWhichWordsMatchAndHowWell(nameA, nameB)
    shortestWordCount = len(combo)
    if shortestWordCount < 2:
        return True
    return False

def eitherNameTooGeneric(nameA:str, nameB:str) -> bool:
    """Identifies if either name is too generic using lastname.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        bool: whether the name is too generic
    """        
    # Return False if either name is missing a lastname
    shortestWordCount = min(len(nameA.split()), len(nameB.split()))
    if shortestWordCount <= 1:
        return False
    # If both last names are very rare, returns False
    if _hasRareSurname(nameA) and _hasRareSurname(nameB):
        return False
    # Check if the numbers of initials in all pairs makes a word match too uncertain
    nonInitialMatchCount = 0
    for _, _, wordA, wordB in usefulToolsMod.getPairIndicesAndWords(nameA, nameB):
        initialInWordA = (len(wordA) == 1)
        initialInWordB = (len(wordB) == 1)
        if initialInWordA or initialInWordB:
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