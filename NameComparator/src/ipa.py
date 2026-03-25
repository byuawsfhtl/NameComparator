from functools import lru_cache
from unidecode import unidecode

import NameComparator.data.pronunciation.ipaAllNames as ipaAllNames
import NameComparator.data.pronunciation.ipaCommonWordParts as ipaCommonWordParts

def getIpa(name:str) -> str:
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

@lru_cache(maxsize=1_000)
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