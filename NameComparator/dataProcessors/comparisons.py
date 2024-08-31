import re
import numpy as np
from functools import lru_cache
from fuzzywuzzy import fuzz
from unidecode import unidecode

from NameComparator.dataProcessors.modify import modifyIpasTogether
from NameComparator.dataProcessors.usefulTools import findWhichWordsMatchAndHowWell, identifyBestMatchups
import NameComparator.data.ipaAllNames as ipaAllNames
import NameComparator.data.ipaCommonWordParts as ipaCommonWordParts

def spellingComparison(name0:str, name1:str) -> tuple[bool, list]:
    """Identifies if two names are a match according to a comparison based soley on spelling.

    Args:
        name0 (str): a name
        name1 (str): a name

    Returns:
        tuple[bool, list]: whether the names are a match, and the resulting word combo
    """        
    wordCombo = findWhichWordsMatchAndHowWell(name0, name1)
    count = sum(1 for tup in wordCombo if tup[2] > 80)
    minLength = min(len(name0.split()), len(name1.split()))
    if (count >= 3) or (count == minLength):
        return True, wordCombo
    if _consonantComparison(name0, name1):
        return True, wordCombo
    return False, wordCombo

def _consonantComparison(name0:str, name1:str) -> bool:
    """Identifies if two names are a match according to consonant comparison.

    Args:
        name0 (str): a name
        name1 (str): a name

    Returns:
        bool: whether the two names are a match according to consonant comparison
    """        
    # Setup
    wordCombo = findWhichWordsMatchAndHowWell(name0, name1)
    minRequiredMatches = len(wordCombo)
    numWordConsonantMatches = 0

    # Loop through every word match in the combo
    for tup in wordCombo:
        # Get the matching word data
        word0:str = name0.split()[int(tup[0])]
        word1:str = name1.split()[int(tup[1])]
        originalScoreForWords:int = int(tup[2])

        # Get the words as consonants
        consonantsName0 = _reduceToSimpleConsonants(word0)
        consonantsName1 = _reduceToSimpleConsonants(word1)
        consonantsRatio = fuzz.ratio(consonantsName0, consonantsName1)

        # Continue if bad match
        if originalScoreForWords <= 30:
            continue
        if (len(word0) != 1) and (len(word1) != 1): #if neither word is initial
            lowestSyllableCount = min(consonantsName0.count("*"), consonantsName1.count("*"))
            if lowestSyllableCount < 2:
                continue
        if (consonantsRatio <= 80 or originalScoreForWords <= 60) and consonantsRatio != 100:
            continue

        # If not rejected, increment the number of matches
        numWordConsonantMatches += 1

    # If enough matches, return true. Otherwise return false.
    if (numWordConsonantMatches > minRequiredMatches) or (numWordConsonantMatches >= 3):
        return True
    else:
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

def pronunciationComparison(name0:str, name1:str) -> tuple[bool, list, str, str]:
    """Identifies whether two names are a match according to a pronunciation comparison.

    Args:
        name0 (str): a name
        name1 (str): a name

    Returns:
        tuple[bool, list, str, str]: whether the name was a match, the word combo, the ipa of name0, the ipa of name1
    """        
    # Gets Ipas
    ipaOfName0 = _getIpa(name0)
    ipaOfName1 = _getIpa(name1)

    # Cleans Ipas
    ipaOfName0 = _standardizeIpa(ipaOfName0)
    ipaOfName1 = _standardizeIpa(ipaOfName1)
    ipaOfName0, ipaOfName1 = modifyIpasTogether(ipaOfName0, ipaOfName1)

    # Initialize empty list to store scores
    words0 = ipaOfName0.split()
    words1 = ipaOfName1.split()
    if len(words0) != len(words1):
        if len(words0) < len(words1):
            words0 += [None] * (len(words1) - len(words0))
        else:
            words1 += [None] * (len(words0) - len(words1))
    scores = np.zeros((len(words0), len(words1)))

    # Score each matchup
    wordCombo = findWhichWordsMatchAndHowWell(name0, name1)
    for i, word0 in enumerate(words0):
        for j, word1 in enumerate(words1):
            # Assign a very low finite score to dummy pairings
            scores[i, j] = -1e9 
            if (word0 is None) or (word1 is None):
                continue
            # Use fuzz.ratio to compare the words and store the score
            score = fuzz.ratio(word0, word1)
            # Updates the score if one of the words was an initial
            for k in range(len(wordCombo)):
                index1, index2, initialScore = wordCombo[k]
                if i == int(index1) and j == int(index2) and (initialScore == 100 or initialScore == 0):
                    score = initialScore

            # Add the score to scores
            scores[i, j] = score

    # identify the best matchups
    words0 = [str(i) if word is not None else None for i, word in enumerate(words0)]
    words1 = [str(i) if word is not None else None for i, word in enumerate(words1)]
    wordCombo = identifyBestMatchups(scores=scores, listA=words0, listB=words1)
    lowestScore = min(wordCombo, key=lambda tuple: tuple[2])[2]

    # If the shortest name is two words in length
    minLength = min(len(ipaOfName0.split()), len(ipaOfName1.split()))
    if minLength <= 2:
        # If the lowest score match is greater than or equal to 80, it's a good pronunciation match
        if lowestScore >= 80:
            return True, wordCombo, ipaOfName0, ipaOfName1
        # Otherwise, it's probably not a match
        return False, wordCombo, ipaOfName0, ipaOfName1

    # If the shortest name is more than two words
    if minLength > 2:
        # If the lowest score match is greater than 75, it's a good pronunciation match
        if lowestScore > 75:
            return True, wordCombo, ipaOfName0, ipaOfName1
        # Otherwise, it's probably not a match
        return False, wordCombo, ipaOfName0, ipaOfName1
    
def _standardizeIpa(ipa:str) -> str:
    """cleans ipa to get rid of double ipa-consonants and other mistakes.

    Args:
        ipa (str): the ipa of a word

    Returns:
        str: the cleaned ipa
    """        
    allIpaConsonants = ['l', 'd', 'z', 'b', 't', 'k', 'n', 's', 'w', 'v', 'ð', 'ʒ', 'ʧ', 'θ', 'h', 'g', 'ʤ', 'ŋ', 'p', 'm', 'ʃ', 'f', 'j', 'r']
    for consonant in allIpaConsonants:
        doubleConsonant = consonant + consonant
        if doubleConsonant in ipa:
            ipa = ipa.replace(doubleConsonant, consonant)
    ipa = ipa.replace("ɛɛ", "i")
    ipa = ipa.replace("ɪɪ", "ɪ")
    ipa = ipa.replace("iɪ", "i")
    ipa = ipa.replace("ŋg", "ŋ")
    ipa = ipa.replace(",", "")
    if not ipa:
        ipa = '_'
    return ipa

def _getIpa(name:str) -> str:
    """Gets the pronunciation of the name.

    Args:
        name (str): a name

    Returns:
        str: the ipa of the name
    """        
    pList = []
    for word in name.split():
        pList.append(_getIpaOfOneWord(word))
    pronunciationOfName = " ".join(pList)
    return pronunciationOfName

@lru_cache(maxsize=1000)
def _getIpaOfOneWord(word:str) -> str:
    """Gets the pronunciation of one word.

    Args:
        word (str): a word

    Returns:
        str: the ipa of the word
    """
    # Setup
    word = word.strip()
    word = unidecode(word)
    word = word.lower()
    pronunciationList = [""] * len(word)
    def substringSplitsTh(substring:str, word:str, i:int, j:int) -> bool:
        """Helps to identify poor substring choices for words for ipa.

        Args:
            substring (str): the ipa dissection
            word (str): the full word
            i (int): the start index of the substring
            j (int): the end index of the substring

        Returns:
            bool: whether it was a good substring
        """            
        if i == j:
            return False
        if i >= 0 and substring[0] == 'h' and word[i - 1] == 't':
            return True
        if j <= len(word) - 1 and substring[-1] == 't' and word[j] == 'h':
            return True
        return False

    # Tries to get the ipa from the plain word
    firstAttempt, success = _wordPronunciationHailMary(word)
    if success:
        return firstAttempt

    # While there are still letters in the word
    substringAdded = True
    while substringAdded:
        # Initialize variables to store the largest matching substring and its length
        substringAdded = False
        largestSubstring = ""
        pronunciationOfLargestSubstring = ""
        largestSubstringLen = 0
        beginningIndexOfSubstring = 0
        endIndexOfSubstring = 0

        # Iterate over every possible substring
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                substring = word[i:j]

                if len(substring) <= largestSubstringLen:
                    continue
                if " " in substring:
                    continue
                if len(substring) > 1:
                    substringIpa, success = _stringPronuncationHailMary(substring)
                    if (not success) or (len(substringIpa) >= len(substring) * 2) or (substringSplitsTh(substring, word, i, j)):
                        continue
                    else:
                        pronunciationOfLargestSubstring = substringIpa
                elif len(substring) == 1:
                    letterToPronunciation = {
                        "a": "æ", "b": "b", "c": "k", "d": "d", "e": "ɛ", "f": "f", "g": "g", "h": "h", "i": "ɪ",
                        "j": "ʤ", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "k", "r": "r",
                        "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "ks", "y": "j", "z": "z"
                    }
                    pronunciationOfLargestSubstring = letterToPronunciation.get(substring, largestSubstring)

                largestSubstring = substring
                substringAdded = True
                largestSubstringLen = len(substring)
                beginningIndexOfSubstring = i
                endIndexOfSubstring = j

        # Adds the substring to the list
        if substringAdded:
            pronunciationList[beginningIndexOfSubstring] = pronunciationOfLargestSubstring
        spaces = " " * largestSubstringLen
        word = word.rstrip()
        word = word[:beginningIndexOfSubstring] + spaces + word[endIndexOfSubstring:]

    # Concatenates the list together at the end to get the pronunciation
    pronunciation = "".join(pronunciationList)
    return pronunciation

def _wordPronunciationHailMary(word:str) -> tuple[str, bool]:
    """Tries to get the pronunciation from the predefined ipa dictionary.

    Args:
        word (str): the regular word

    Returns:
        tuple[str, bool]: the ipa of the word (or the original word if not found), and whether it was found.
    """        
    wordPronuncation = ipaAllNames.data.get(word)
    if wordPronuncation != None:
        return wordPronuncation, True
    return word, False

def _stringPronuncationHailMary(string:str) -> tuple[str, bool]:
    """Helper function of _getIpaOfOneWord.
    Tries to get the ipa of a string (with more than one letter).

    Args:
        string (str): a string that is longer than one letter

    Returns:
        tuple[str, bool]: the ipa of the string (or the original string if not found), and whether it was found.
    """        
    ipaPronunciation = ipaCommonWordParts.data.get(string)
    if ipaPronunciation != None:
        return ipaPronunciation, True
    return string, False