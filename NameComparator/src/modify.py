import re
from fuzzywuzzy import fuzz

import NameComparator.src.usefulTools as usefulToolsMod
import NameComparator.data.rules.rulesSpelling as rulesSpelling
import NameComparator.data.rules.rulesIpa as rulesIpa

def modifyNamesTogether(name_one:str, name_two:str) -> tuple[str,str]:
    """Modifies the name together (changing them in a way that is much more intense than simply cleaning together).

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str,str]: the modified names
    """        
    name_one = re.sub(r'ie\b', 'y', name_one)
    name_two = re.sub(r'ie\b', 'y', name_two)
    name_one, name_two = _removeOrInNames(name_one, name_two)
    name_one, name_two = _fixVowelMistakes(name_one, name_two)
    name_one, name_two = _fixSwappedChars(name_one, name_two)
    name_one, name_two = _dealWithWrongFirstChar(name_one, name_two)
    for meatOption1, meatOption2, bottomBreads, topBreads, minLetters in rulesSpelling.data:
        name_one, name_two = _replaceSubstringSandwichMeatIfMatchingBread(name_one, name_two, meatOption1, meatOption2, bottomBreads, topBreads, minLetters)
    name_one = re.sub(r'\s+', ' ', name_one)
    name_two = re.sub(r'\s+', ' ', name_two)
    name_one = name_one.strip()
    name_two = name_two.strip()
    return name_one, name_two

def _removeOrInNames(name_one:str, name_two:str) -> tuple[str, str]:
    """Removes the word 'or' from a name (assuming that the name could have been 
    poorly indexed so that the indexer's guesses for a specific word of the name is still within the string).

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    if (not name_one) or (not name_two):
        return name_one, name_two
    name_one = name_one.strip()
    name_two = name_two.strip()
    name_one, name_two = name_one.lower(), name_two.lower()

    # if or in neither
    if (not " or " in name_one) and (not " or " in name_two):
        return name_one, name_two
    
    # if or in both
    elif (" or " in name_one) and (" or " in name_two):
        return name_one, name_two

    # if or in name_one and not name_two
    elif " or " in name_one:
        # Gets the score for if the word before 'or' is removed
        rightname_one = re.sub("[a-z]+ or ", " ", name_one)
        if not rightname_one:
            rightname_one = '_'
        rightword_combo = usefulToolsMod.find_word_matches_and_quality(rightname_one, name_two)
        rightAverageScore = sum(tup[2] for tup in rightword_combo) / len(rightword_combo)
        # Gets the score for if the word after 'or' is removed
        leftname_one = re.sub(" or [a-z]+", " ", name_one)
        if not leftname_one:
            leftname_one = '_'
        leftword_combo =  usefulToolsMod.find_word_matches_and_quality(leftname_one, name_two)
        leftAverageScore = sum(tup[2] for tup in leftword_combo) / len(leftword_combo)
        # Return the higher one
        if rightAverageScore >= leftAverageScore:
            return rightname_one, name_two
        return leftname_one, name_two
    
    # if or in name_two and not name_one
    elif " or " in name_two:
        rightname_two = re.sub("[a-z]+ or ", " ", name_two)
        if not rightname_two:
            rightname_two = '_'
        rightword_combo = usefulToolsMod.find_word_matches_and_quality(rightname_two, name_one)
        rightAverageScore = sum(tup[2] for tup in rightword_combo) / len(rightword_combo)
        # Gets the score for if the word after 'or' is removed
        leftname_two = re.sub(" or [a-z]+", " ", name_two)
        if not leftname_two:
            leftname_two = '_'
        leftword_combo =  usefulToolsMod.find_word_matches_and_quality(leftname_two, name_one)
        leftAverageScore = sum(tup[2] for tup in leftword_combo) / len(leftword_combo)
        # Return the higher one
        if rightAverageScore >= leftAverageScore:
            return name_one, rightname_two
        return name_one, leftname_two

def _fixVowelMistakes(name_one:str, name_two:str) -> tuple[str, str]:
    """Modifies two matching words in a name so that they are the same if 
    they are only different by one vowel and 5 letters or more.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the two modified names
    """        
    ne = usefulToolsMod.NameEditor(name_one, name_two)
    for index_one, _, word_one, word_two in usefulToolsMod.get_matching_words_and_indices(name_one, name_two):
        # Continue if either word is less than 5 chars or not same length
        lenA = len(word_one)
        lenB = len(word_two)
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
            if word_one[i] == word_two[i]:
                continue
            if mismatchedIndex:
                tooManyDiffs = True
                break
            mismatchedIndex = i
        
        # Continue if there was not exactly one difference
        if (tooManyDiffs) or (mismatchedIndex is None):
            continue

        # Replace one of the letters to be the other if they are cooresponding
        charword_one = word_one[mismatchedIndex]
        charword_two = word_two[mismatchedIndex]
        cooresponding = ['ao', 'ea', 'iy']
        if (f'{charword_one}{charword_two}' in cooresponding) or (f'{charword_two}{charword_one}' in cooresponding):
            ne.update_name_one(index_one, word_two)
    
    # Return the modified (or not) names
    return ne.get_modified_names()

def _fixSwappedChars(name_one:str, name_two:str) -> tuple[str, str]:
    """If two matching words (of 5 letters of more) for the two names are the same barring swapped letters (typo), makes the words the same.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    ne = usefulToolsMod.NameEditor(name_one, name_two)
    for index_one, _, word_one, word_two in usefulToolsMod.get_matching_words_and_indices(name_one, name_two):
        # Skip if the words are not 5 long, are different length, or not fuzzy 80
        if len(word_one) != 5:
            continue
        if len(word_one) != len(word_two):
            continue
        if fuzz.ratio(word_two, word_one) != 80:
            continue

        # Find how many differences and where
        diffCount = 0
        diffPositions = []
        for i in range(len(word_one)):
            if word_one[i] != word_two[i]:
                diffCount += 1
                diffPositions.append(i)
        
        # Skip if there are not two differences, differences are not sequential, or not swappable
        if diffCount != 2:
            continue
        posI, posJ = diffPositions
        if abs(posI - posJ) != 1:
            continue
        if (word_one[posI] != word_two[posJ]) or (word_one[posI] != word_two[posJ]):
            continue

        # This is the scenerio we are looking for. Make the words identical
        ne.update_name_one(index_one, word_two)
    
    # Return the modified (or not) names
    return ne.get_modified_names()

def _dealWithWrongFirstChar(name_one:str, name_two:str) -> tuple[str, str]:
    """If two matching words (of 5 letters or more) are the same barring the first letter, makes the same.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    ne = usefulToolsMod.NameEditor(name_one, name_two)
    for index_one, _, word_one, word_two in usefulToolsMod.get_matching_words_and_indices(name_one, name_two):
        if word_one == word_two:
            continue
        if (word_one[1:] == word_two[1:]) and (len(word_one) > 4) and (len(word_two) > 4):
            ne.update_name_one(index_one, word_two)
    name_one, name_two = ne.get_modified_names()
    return name_one, name_two

def _replaceSubstringSandwichMeatIfMatchingBread(name_one:str, name_two:str, meatOption1:str, meatOption2:str, bottomBreadOptions:list[str], topBreadOptions:list[str], minRequiredLetters:int) -> tuple[str,str]:
    """For any given matching word pair, replaces a specific substring in one of the words, with a similar substring found in the other word.

    Args:
        name_one (str): a name
        name_two (str): a name
        meatOption1 (str): the first possible middle of the substring
        meatOption2 (str): the second possible middle of the substring
        bottomBreadOptions (list[str]): a list of possible beginnings to the substring. Whichever beginning is found in the one must be found in the other in order for the replacement to work
        topBreadOptions (list[str]): a list of possible endings to the substring. Whichever ending is found in the one must be found in the other in order for the replacement to work
        minRequiredLetters (int): the minimum required letters to be found in both words in order for the replacement to work

    Returns:
        tuple[str,str]: the modified names
    """        
    # Return if both middles not in different words
    if (meatOption1 not in name_one and meatOption2 not in name_one) or (meatOption1 not in name_two and meatOption2 not in name_two):
        return name_one, name_two

    ne = usefulToolsMod.NameEditor(name_one, name_two)
    for index_one, index_two, word_one, word_two in usefulToolsMod.get_matching_words_and_indices(name_one, name_two):
        # Skip words that are not long enough for the given rule
        if len(word_one) < minRequiredLetters or len(word_two) < minRequiredLetters:
            continue

        # Add clear word breaks
        word_one = f"-{word_one}-"
        word_two = f"-{word_two}-"

        for bottomBread in bottomBreadOptions:
            if bottomBread not in word_one or bottomBread not in word_two:
                continue

            for topBread in topBreadOptions:
                if topBread not in word_one or topBread not in word_two:
                    continue

                # Skip the bread if the pattern is not found in both, if the middles (meats) are the same, or if the patterns are too far appart
                pattern = f"{bottomBread}({meatOption1}|{meatOption2}){topBread}"
                resultsA = re.search(pattern, word_one)
                resultsB = re.search(pattern, word_two)
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
                word_one = _overwriteWithSubstring(word_one, meatOption2, middleCoordsStringA[0], middleCoordsStringA[1])
                word_two = _overwriteWithSubstring(word_two, meatOption2, middleCoordsStringB[0], middleCoordsStringB[1])

        # Update the words for that match (though a change may not have occured)
        word_one = word_one.replace("-", "")
        word_two = word_two.replace("-", "")
        ne.update_name_one(index_one, word_one)
        ne.update_name_two(index_two, word_two)

    # concatonates the two lists together back into strings
    name_one, name_two = ne.get_modified_names()
    return name_one, name_two

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