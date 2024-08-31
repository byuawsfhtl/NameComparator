import re
from fuzzywuzzy import fuzz

import NameComparator.src.usefulTools as usefulToolsMod
import NameComparator.data.rulesSpelling as rulesSpelling
import NameComparator.data.rulesIpa as rulesIpa

def modifyNamesTogether(name0:str, nameB:str) -> tuple[str,str]:
    """Modifies the name together (changing them in a way that is much more intense than simply cleaning together).

    Args:
        name0 (str): a name
        nameB (str): a name

    Returns:
        tuple[str,str]: the modified names
    """        
    name0 = re.sub(r'ie\b', 'y', name0)
    nameB = re.sub(r'ie\b', 'y', nameB)
    name0, nameB = _removeOrInNames(name0, nameB)
    name0, nameB = _fixVowelMistakes(name0, nameB)
    name0, nameB = _fixSwappedChars(name0, nameB)
    name0, nameB = _dealWithWrongFirstChar(name0, nameB)
    for meatOption1, meatOption2, bottomBreads, topBreads, minLetters in rulesSpelling.data:
        name0, nameB = _replaceSubstringSandwichMeatIfMatchingBread(name0, nameB, meatOption1, meatOption2, bottomBreads, topBreads, minLetters)
    name0 = re.sub(r'\s+', ' ', name0)
    nameB = re.sub(r'\s+', ' ', nameB)
    name0 = name0.strip()
    nameB = nameB.strip()
    return name0, nameB

def _removeOrInNames(name0:str, nameB:str) -> tuple[str, str]:
    """Removes the word 'or' from a name (assuming that the name could have been 
    poorly indexed so that the indexer's guesses for a specific word of the name is still within the string).

    Args:
        name0 (str): a name
        nameB (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    if (not name0) or (not nameB):
        return name0, nameB
    name0 = name0.strip()
    nameB = nameB.strip()
    name0, nameB = name0.lower(), nameB.lower()

    # if or in neither
    if (not " or " in name0) and (not " or " in nameB):
        return name0, nameB
    
    # if or in both
    elif (" or " in name0) and (" or " in nameB):
        return name0, 

    # if or in nameA and not nameB
    elif " or " in name0:
        # Gets the score for if the word before 'or' is removed
        rightNameA = re.sub("[a-z]+ or ", " ", name0)
        if not rightNameA:
            rightNameA = '_'
        rightWordCombo = usefulToolsMod.findWhichWordsMatchAndHowWell(rightNameA, nameB)
        rightAverageScore = sum(tup[2] for tup in rightWordCombo) / len(rightWordCombo)
        # Gets the score for if the word after 'or' is removed
        leftNameA = re.sub(" or [a-z]+", " ", name0)
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
        rightWordCombo = usefulToolsMod.findWhichWordsMatchAndHowWell(rightNameB, name0)
        rightAverageScore = sum(tup[2] for tup in rightWordCombo) / len(rightWordCombo)
        # Gets the score for if the word after 'or' is removed
        leftNameB = re.sub(" or [a-z]+", " ", nameB)
        if not leftNameB:
            leftNameB = '_'
        leftWordCombo =  usefulToolsMod.findWhichWordsMatchAndHowWell(leftNameB, name0)
        leftAverageScore = sum(tup[2] for tup in leftWordCombo) / len(leftWordCombo)
        # Return the higher one
        if rightAverageScore >= leftAverageScore:
            return name0, rightNameB
        return name0, leftNameB

def _fixVowelMistakes(name0:str, nameB:str) -> tuple[str, str]:
    """Modifies two matching words in a name so that they are the same if 
    they are only different by one vowel and 5 letters or more.

    Args:
        name0 (str): a name
        nameB (str): a name

    Returns:
        tuple[str, str]: the two modified names
    """        
    ne = usefulToolsMod.NameEditor(name0, nameB)
    for index0, _, word0, word1 in usefulToolsMod.getPairIndicesAndWords(name0, nameB):
        # Continue if either word is less than 5 chars or not same length
        len0 = len(word0)
        len1 = len(word1)
        if len0 < 5:
            continue
        if len1 < 5:
            continue
        if len0 != len1:
            continue

        # Check if there is only one difference
        mismatchedIndex = None
        tooManyDiffs = False
        for i in range(len0):
            if word0[i] == word1[i]:
                continue
            if mismatchedIndex:
                tooManyDiffs = True
                break
            mismatchedIndex = i
        
        # Continue if there was not exactly one difference
        if (tooManyDiffs) or (mismatchedIndex is None):
            continue

        # Replace one of the letters to be the other if they are cooresponding
        charWord0 = word0[mismatchedIndex]
        charWord1 = word1[mismatchedIndex]
        cooresponding = ['ao', 'ea', 'iy']
        if (f'{charWord0}{charWord1}' in cooresponding) or (f'{charWord1}{charWord0}' in cooresponding):
            ne.updateName0(index0, word1)
    
    # Return the modified (or not) names
    return ne.getModifiedNames()

def _fixSwappedChars(name0:str, nameB:str) -> tuple[str, str]:
    """If two matching words (of 5 letters of more) for the two names are the same barring swapped letters (typo), makes the words the same.

    Args:
        name0 (str): a name
        nameB (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    ne = usefulToolsMod.NameEditor(name0, nameB)
    for index0, _, word0, word1 in usefulToolsMod.getPairIndicesAndWords(name0, nameB):
        # Skip if the words are not 5 long, are different length, or not fuzzy 80
        if len(word0) != 5:
            continue
        if len(word0) != len(word1):
            continue
        if fuzz.ratio(word1, word0) != 80:
            continue

        # Find how many differences and where
        diffCount = 0
        diffPositions = []
        for i in range(len(word0)):
            if word0[i] != word1[i]:
                diffCount += 1
                diffPositions.append(i)
        
        # Skip if there are not two differences, differences are not sequential, or not swappable
        if diffCount != 2:
            continue
        posI, posJ = diffPositions
        if abs(posI - posJ) != 1:
            continue
        if (word0[posI] != word1[posJ]) or (word0[posI] != word1[posJ]):
            continue

        # This is the scenerio we are looking for. Make the words identical
        ne.updateName0(index0, word1)
    
    # Return the modified (or not) names
    return ne.getModifiedNames()

def _dealWithWrongFirstChar(name0:str, nameB:str) -> tuple[str, str]:
    """If two matching words (of 5 letters or more) are the same barring the first letter, makes the same.

    Args:
        name0 (str): a name
        nameB (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    ne = usefulToolsMod.NameEditor(name0, nameB)
    for index1, _, word1, word2 in usefulToolsMod.getPairIndicesAndWords(name0, nameB):
        if word1 == word2:
            continue
        if (word1[1:] == word2[1:]) and (len(word1) > 4) and (len(word2) > 4):
            ne.updateName0(index1, word2)
    name0, nameB = ne.getModifiedNames()
    return name0, nameB

def _replaceSubstringSandwichMeatIfMatchingBread(name0:str, nameB:str, meatOption1:str, meatOption2:str, bottomBreadOptions:list[str], topBreadOptions:list[str], minRequiredLetters:int) -> tuple[str,str]:
    """For any given matching word pair, replaces a specific substring in one of the words, with a similar substring found in the other word.

    Args:
        name0 (str): a name
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
    if (meatOption1 not in name0 and meatOption2 not in name0) or (meatOption1 not in nameB and meatOption2 not in nameB):
        return name0, nameB

    ne = usefulToolsMod.NameEditor(name0, nameB)
    for index0, index1, word0, word1 in usefulToolsMod.getPairIndicesAndWords(name0, nameB):
        # Skip words that are not long enough for the given rule
        if len(word0) < minRequiredLetters or len(word1) < minRequiredLetters:
            continue

        # Add clear word breaks
        word0 = f"-{word0}-"
        word1 = f"-{word1}-"

        for bottomBread in bottomBreadOptions:
            if bottomBread not in word0 or bottomBread not in word1:
                continue

            for topBread in topBreadOptions:
                if topBread not in word0 or topBread not in word1:
                    continue

                # Skip the bread if the pattern is not found in both, if the middles (meats) are the same, or if the patterns are too far appart
                pattern = f"{bottomBread}({meatOption1}|{meatOption2}){topBread}"
                results1 = re.search(pattern, word0)
                results2 = re.search(pattern, word1)
                if not results1 or not results2:
                    continue
                if results1.group(0) == results2.group(0):
                    continue
                spanA1, spanB1 = results1.span()
                spanA2, spanB2 = results2.span()
                if not (abs(spanA1 - spanA2) <= 2 and abs(spanB1 - spanB2) <= 2):
                    continue

                # Update the words by replacing matching (different) middles with the meat option 2
                startIndexString1, endIndexString1 = results1.span()
                startIndexString2, endIndexString2 = results2.span()
                middleCoordsString1 = startIndexString1 + len(bottomBread), endIndexString1 - len(topBread)
                middleCoordsString2 = startIndexString2 + len(bottomBread), endIndexString2 - len(topBread)
                word0 = _overwriteWithSubstring(word0, meatOption2, middleCoordsString1[0], middleCoordsString1[1])
                word1 = _overwriteWithSubstring(word1, meatOption2, middleCoordsString2[0], middleCoordsString2[1])

        # Update the words for that match (though a change may not have occured)
        word0 = word0.replace("-", "")
        word1 = word1.replace("-", "")
        ne.updateName0(index0, word0)
        ne.updateNameB(index1, word1)

    # concatonates the two lists together back into strings
    name0, nameB = ne.getModifiedNames()
    return name0, nameB

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

def modifyIpasTogether(ipa0:str, ipa1:str) -> tuple[str,str]:
    """Modifies two ipas by comparing each to one another.

    Args:
        ipa1 (str): the first ipa name
        ipa2 (str): the second ipa name

    Returns:
        tuple[str,str]: the two modified names
    """
    for rule in rulesIpa.data:
        ipa0, ipa1 = _replaceSubstringSandwichMeatIfMatchingBread(ipa0, ipa1, rule[0], rule[1], rule[2], rule[3], rule[4])
    return ipa0, ipa1