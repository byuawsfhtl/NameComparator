import NameComparator.src.usefulTools as usefulToolsMod

def isWorthContinuing(nameA:str, nameB:str) -> bool:
    """Identifies if a name comparison will always prove false.

    Args:
        nameA (str): a name
        nameB (str): a name

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
