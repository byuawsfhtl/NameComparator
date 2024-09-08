import re
import numpy as np
from fuzzywuzzy import fuzz

import NameComparator.src.usefulTools as usefulToolsMod

def spellingComparison(nameA:str, nameB:str) -> tuple[bool, list]:
    """Identifies if two names are a match according to a comparison based soley on spelling.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        tuple[bool, list]: whether the names are a match, and the resulting word combo
    """        
    wordCombo = usefulToolsMod.findWhichWordsMatchAndHowWell(nameA, nameB)
    count = sum(1 for tup in wordCombo if tup[2] > 80)
    minLength = min(len(nameA.split()), len(nameB.split()))
    if (count >= 3) or (count == minLength):
        return True, wordCombo
    if _consonantComparison(nameA, nameB):
        return True, wordCombo
    return False, wordCombo

def _consonantComparison(nameA:str, nameB:str) -> bool:
    """Identifies if two names are a match according to consonant comparison.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        bool: whether the two names are a match according to consonant comparison
    """        
    # Setup
    wordCombo = usefulToolsMod.findWhichWordsMatchAndHowWell(nameA, nameB)
    minRequiredMatches = len(wordCombo)
    numWordConsonantMatches = 0

    # Loop through every word match in the combo
    for tup in wordCombo:
        # Get the matching word data
        wordA = nameA.split()[int(tup[0])]
        wordB = nameB.split()[int(tup[1])]
        originalScoreForWords:int = int(tup[2])

        # Get the words as consonants
        consonantsNameA = _reduceToSimpleConsonants(wordA)
        consonantsNameB = _reduceToSimpleConsonants(wordB)
        consonantsRatio = fuzz.ratio(consonantsNameA, consonantsNameB)

        # Continue if bad match
        if originalScoreForWords <= 30:
            continue
        if (len(wordA) != 1) and (len(wordB) != 1): #if neither word is initial
            lowestSyllableCount = min(consonantsNameA.count("*"), consonantsNameB.count("*"))
            if lowestSyllableCount < 2:
                continue
        if (consonantsRatio <= 80 or originalScoreForWords <= 60) and consonantsRatio != 100:
            continue

        # If not rejected, increment the number of matches
        numWordConsonantMatches += 1

    # If enough matches, return true. Otherwise return false.
    if (numWordConsonantMatches > minRequiredMatches) or (numWordConsonantMatches >= 3):
        return True
    return False
    
def _reduceToSimpleConsonants(string:str) -> str:
    """Reduces a string to the simple consonant componants.

    Args:
        string (str): a string

    Returns:
        str: the consonant componants
    """            
    string = re.sub("a|e|i|o|u|y", "*", string)
    string = string.replace("**", "*")
    string = re.sub(r'(.)\1+', r'\1', string)
    return string

def pronunciationComparison(ipaOfNameA:str, ipaOfNameB:str, nameA:str, nameB:str) -> tuple[bool, list]:
    """Identifies whether two names are a match according to a pronunciation comparison.

    Args:
        ipaOfNameA (str): the ipa of a name
        ipaOfNameB (str): the ipa of a name
        nameA (str): a name
        nameB (str): a name
        
    Returns:
        tuple[bool, list]: whether the name was a match, and the word combo
    """        
    # Initialize empty list to store scores
    ipaWordsA = ipaOfNameA.split()
    ipaWordsB = ipaOfNameB.split()
    if len(ipaWordsA) < len(ipaWordsB):
        ipaWordsA += [None] * (len(ipaWordsB) - len(ipaWordsA))
    elif len(ipaWordsA) > len(ipaWordsB):
        ipaWordsB += [None] * (len(ipaWordsA) - len(ipaWordsB))
    scores = np.zeros((len(ipaWordsA), len(ipaWordsB)))

    # Score each matchup
    wordCombo = usefulToolsMod.findWhichWordsMatchAndHowWell(nameA, nameB)
    for indexA, wordA in enumerate(ipaWordsA):
        for indexB, wordB in enumerate(ipaWordsB):
            # Assign a default very low score for dummy pairings
            scores[indexA, indexB] = -1e9 
            if (wordA is None) or (wordB is None):
                continue
            # Reassign the default score to all real pairings
            score = fuzz.ratio(wordA, wordB)
            for item in range(len(wordCombo)):
                indexX, indexY, initialScore = wordCombo[item]
                # Use initial score for initials (bad pun)
                if indexA == int(indexX) and indexB == int(indexY) and (initialScore == 100 or initialScore == 0):
                    score = initialScore
            scores[indexA, indexB] = score

    # Identify the best matchups
    ipaWordsA = [str(i) if word is not None else None for i, word in enumerate(ipaWordsA)]
    ipaWordsB = [str(i) if word is not None else None for i, word in enumerate(ipaWordsB)]
    wordCombo = usefulToolsMod.identifyBestMatchups(scores=scores, listA=ipaWordsA, listB=ipaWordsB)
    lowestScore = min(wordCombo, key=lambda tuple: tuple[2])[2]
    
    # Return whether pronunciaion match or not
    minLength = min(len(ipaOfNameA.split()), len(ipaOfNameB.split()))
    if minLength <= 2:
        if lowestScore >= 80:
            return True, wordCombo
        return False, wordCombo
    if minLength > 2:
        if lowestScore > 75:
            return True, wordCombo
        return False, wordCombo