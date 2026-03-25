import re
from fuzzywuzzy import fuzz

import NameComparator.src.usefulTools as usefulToolsMod
import NameComparator.data.rules.rulesSpelling as rulesSpelling
import NameComparator.data.rules.rulesIpa as rulesIpa

def modifyNamesTogether(nameA:str, nameB:str) -> tuple[str,str]:
    """Modifies the name together (changing them in a way that is much more intense than simply cleaning together).

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        tuple[str,str]: the modified names
    """        
    nameA = re.sub(r'ie\b', 'y', nameA)
    nameB = re.sub(r'ie\b', 'y', nameB)
    nameA, nameB = _removeOrInNames(nameA, nameB)
    nameA, nameB = _fixVowelMistakes(nameA, nameB)
    nameA, nameB = _fixSwappedChars(nameA, nameB)
    nameA, nameB = _dealWithWrongFirstChar(nameA, nameB)
    for meatOption1, meatOption2, bottomBreads, topBreads, minLetters in rulesSpelling.data:
        nameA, nameB = _replaceSubstringSandwichMeatIfMatchingBread(nameA, nameB, meatOption1, meatOption2, bottomBreads, topBreads, minLetters)
    nameA = re.sub(r'\s+', ' ', nameA)
    nameB = re.sub(r'\s+', ' ', nameB)
    nameA = nameA.strip()
    nameB = nameB.strip()
    return nameA, nameB

def _removeOrInNames(nameA:str, nameB:str) -> tuple[str, str]:
    """Removes the word 'or' from a name (assuming that the name could have been 
    poorly indexed so that the indexer's guesses for a specific word of the name is still within the string).

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    if (not nameA) or (not nameB):
        return nameA, nameB
    nameA = nameA.strip()
    nameB = nameB.strip()
    nameA, nameB = nameA.lower(), nameB.lower()

    # if or in neither
    if (not " or " in nameA) and (not " or " in nameB):
        return nameA, nameB
    
    # if or in both
    elif (" or " in nameA) and (" or " in nameB):
        return nameA, nameB

    # if or in nameA and not nameB
    elif " or " in nameA:
        # Gets the score for if the word before 'or' is removed
        rightNameA = re.sub("[a-z]+ or ", " ", nameA)
        if not rightNameA:
            rightNameA = '_'
        rightWordCombo = usefulToolsMod.findWhichWordsMatchAndHowWell(rightNameA, nameB)
        rightAverageScore = sum(tup[2] for tup in rightWordCombo) / len(rightWordCombo)
        # Gets the score for if the word after 'or' is removed
        leftNameA = re.sub(" or [a-z]+", " ", nameA)
        if not leftNameA:
            leftNameA = '_'
        leftWordCombo =  usefulToolsMod.findWhichWordsMatchAndHowWell(leftNameA, nameB)
        leftAverageScore = sum(tup[2] for tup in leftWordCombo) / len(leftWordCombo)
        # Return the higher one
        if rightAverageScore >= leftAverageScore:
            return rightNameA, nameB
        return leftNameA, nameB
    
    # if or in nameB and not nameA
    elif " or " in nameB:
        rightNameB = re.sub("[a-z]+ or ", " ", nameB)
        if not rightNameB:
            rightNameB = '_'
        rightWordCombo = usefulToolsMod.findWhichWordsMatchAndHowWell(rightNameB, nameA)
        rightAverageScore = sum(tup[2] for tup in rightWordCombo) / len(rightWordCombo)
        # Gets the score for if the word after 'or' is removed
        leftNameB = re.sub(" or [a-z]+", " ", nameB)
        if not leftNameB:
            leftNameB = '_'
        leftWordCombo =  usefulToolsMod.findWhichWordsMatchAndHowWell(leftNameB, nameA)
        leftAverageScore = sum(tup[2] for tup in leftWordCombo) / len(leftWordCombo)
        # Return the higher one
        if rightAverageScore >= leftAverageScore:
            return nameA, rightNameB
        return nameA, leftNameB

def _fixVowelMistakes(nameA:str, nameB:str) -> tuple[str, str]:
    """Modifies two matching words in a name so that they are the same if 
    they are only different by one vowel and 5 letters or more.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        tuple[str, str]: the two modified names
    """        
    ne = usefulToolsMod.NameEditor(nameA, nameB)
    for indexA, _, wordA, wordB in usefulToolsMod.getPairIndicesAndWords(nameA, nameB):
        # Continue if either word is less than 5 chars or not same length
        lenA = len(wordA)
        lenB = len(wordB)
        if lenA < 5:
            continue
        if lenB < 5:
            continue
        if lenA != lenB:
            continue

        # Check if there is only one difference
        mismatchedIndex = None
        tooManyDiffs = False
        for i in range(lenA):
            if wordA[i] == wordB[i]:
                continue
            if mismatchedIndex:
                tooManyDiffs = True
                break
            mismatchedIndex = i
        
        # Continue if there was not exactly one difference
        if (tooManyDiffs) or (mismatchedIndex is None):
            continue

        # Replace one of the letters to be the other if they are cooresponding
        charWordA = wordA[mismatchedIndex]
        charWordB = wordB[mismatchedIndex]
        cooresponding = ['ao', 'ea', 'iy']
        if (f'{charWordA}{charWordB}' in cooresponding) or (f'{charWordB}{charWordA}' in cooresponding):
            ne.updateNameA(indexA, wordB)
    
    # Return the modified (or not) names
    return ne.getModifiedNames()

def _fixSwappedChars(nameA:str, nameB:str) -> tuple[str, str]:
    """If two matching words (of 5 letters of more) for the two names are the same barring swapped letters (typo), makes the words the same.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    ne = usefulToolsMod.NameEditor(nameA, nameB)
    for indexA, _, wordA, wordB in usefulToolsMod.getPairIndicesAndWords(nameA, nameB):
        # Skip if the words are not 5 long, are different length, or not fuzzy 80
        if len(wordA) != 5:
            continue
        if len(wordA) != len(wordB):
            continue
        if fuzz.ratio(wordB, wordA) != 80:
            continue

        # Find how many differences and where
        diffCount = 0
        diffPositions = []
        for i in range(len(wordA)):
            if wordA[i] != wordB[i]:
                diffCount += 1
                diffPositions.append(i)
        
        # Skip if there are not two differences, differences are not sequential, or not swappable
        if diffCount != 2:
            continue
        posI, posJ = diffPositions
        if abs(posI - posJ) != 1:
            continue
        if (wordA[posI] != wordB[posJ]) or (wordA[posI] != wordB[posJ]):
            continue

        # This is the scenerio we are looking for. Make the words identical
        ne.updateNameA(indexA, wordB)
    
    # Return the modified (or not) names
    return ne.getModifiedNames()

def _dealWithWrongFirstChar(nameA:str, nameB:str) -> tuple[str, str]:
    """If two matching words (of 5 letters or more) are the same barring the first letter, makes the same.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    ne = usefulToolsMod.NameEditor(nameA, nameB)
    for indexA, _, wordA, wordB in usefulToolsMod.getPairIndicesAndWords(nameA, nameB):
        if wordA == wordB:
            continue
        if (wordA[1:] == wordB[1:]) and (len(wordA) > 4) and (len(wordB) > 4):
            ne.updateNameA(indexA, wordB)
    nameA, nameB = ne.getModifiedNames()
    return nameA, nameB

def _replaceSubstringSandwichMeatIfMatchingBread(nameA:str, nameB:str, meatOption1:str, meatOption2:str, bottomBreadOptions:list[str], topBreadOptions:list[str], minRequiredLetters:int) -> tuple[str,str]:
    """For any given matching word pair, replaces a specific substring in one of the words, with a similar substring found in the other word.

    Args:
        nameA (str): a name
        nameB (str): a name
        meatOption1 (str): the first possible middle of the substring
        meatOption2 (str): the second possible middle of the substring
        bottomBreadOptions (list[str]): a list of possible beginnings to the substring. Whichever beginning is found in the one must be found in the other in order for the replacement to work
        topBreadOptions (list[str]): a list of possible endings to the substring. Whichever ending is found in the one must be found in the other in order for the replacement to work
        minRequiredLetters (int): the minimum required letters to be found in both words in order for the replacement to work

    Returns:
        tuple[str,str]: the modified names
    """        
    # Return if both middles not in different words
    if (meatOption1 not in nameA and meatOption2 not in nameA) or (meatOption1 not in nameB and meatOption2 not in nameB):
        return nameA, nameB

    ne = usefulToolsMod.NameEditor(nameA, nameB)
    for indexA, indexB, wordA, wordB in usefulToolsMod.getPairIndicesAndWords(nameA, nameB):
        # Skip words that are not long enough for the given rule
        if len(wordA) < minRequiredLetters or len(wordB) < minRequiredLetters:
            continue

        # Add clear word breaks
        wordA = f"-{wordA}-"
        wordB = f"-{wordB}-"

        for bottomBread in bottomBreadOptions:
            if bottomBread not in wordA or bottomBread not in wordB:
                continue

            for topBread in topBreadOptions:
                if topBread not in wordA or topBread not in wordB:
                    continue

                # Skip the bread if the pattern is not found in both, if the middles (meats) are the same, or if the patterns are too far appart
                pattern = f"{bottomBread}({meatOption1}|{meatOption2}){topBread}"
                resultsA = re.search(pattern, wordA)
                resultsB = re.search(pattern, wordB)
                if not resultsA or not resultsB:
                    continue
                if resultsA.group(0) == resultsB.group(0):
                    continue
                spanA1, spanB1 = resultsA.span()
                spanA2, spanB2 = resultsB.span()
                if not (abs(spanA1 - spanA2) <= 2 and abs(spanB1 - spanB2) <= 2):
                    continue

                # Update the words by replacing matching (different) middles with the meat option 2
                startIndexStringA, endIndexStringA = resultsA.span()
                startIndexStringB, endIndexStringB = resultsB.span()
                middleCoordsStringA = startIndexStringA + len(bottomBread), endIndexStringA - len(topBread)
                middleCoordsStringB = startIndexStringB + len(bottomBread), endIndexStringB - len(topBread)
                wordA = _overwriteWithSubstring(wordA, meatOption2, middleCoordsStringA[0], middleCoordsStringA[1])
                wordB = _overwriteWithSubstring(wordB, meatOption2, middleCoordsStringB[0], middleCoordsStringB[1])

        # Update the words for that match (though a change may not have occured)
        wordA = wordA.replace("-", "")
        wordB = wordB.replace("-", "")
        ne.updateNameA(indexA, wordA)
        ne.updateNameB(indexB, wordB)

    # concatonates the two lists together back into strings
    nameA, nameB = ne.getModifiedNames()
    return nameA, nameB

def _overwriteWithSubstring(string:str, replacement:str, startIndex:int, endIndex:int) -> str:
    """Overwrites a specific index range of a string with the replacement string.

    Args:
        string (str): the string to replace
        replacement (str): the replacement string
        startIndex (int): the start index for the replacement
        endIndex (int): the end index for the replacement

    Returns:
        _type_: _description_
    """
    stringList = list(string)
    stringList[startIndex:endIndex] = replacement
    newString = ''.join(stringList)
    return newString

def modifyIpasTogether(ipaA:str, ipaB:str) -> tuple[str,str]:
    """Modifies two ipas by comparing each to one another.

    Args:
        ipaA (str): the ipa of a name
        ipaB (str): the ipa of a name

    Returns:
        tuple[str,str]: the two modified names
    """
    for meatOption1, meatOption2, bottomBreads, topBreads, minLetters in rulesIpa.data:
        ipaA, ipaB = _replaceSubstringSandwichMeatIfMatchingBread(ipaA, ipaB, meatOption1, meatOption2, bottomBreads, topBreads, minLetters)
    return ipaA, ipaB