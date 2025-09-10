from functools import lru_cache
from unidecode import unidecode

import NameComparator.src.clean as cleanMod
import NameComparator.data.pronunciation.ipaAllNames as ipaAllNames
import NameComparator.data.pronunciation.ipaCommonWordParts as ipaCommonWordParts

@lru_cache(maxsize=10_000)
def get_ipa(name: str) -> str:
    """Gets the pronunciation of the name.

    Args:
        name: a name

    Returns:
        str: the ipa of the name
    """        
    ipa_words = []
    for word in name.split():
        ipa_words.append(get_ipa_of_one_word(word))
    pronunciation_of_name = " ".join(ipa_words)
    return pronunciation_of_name

@lru_cache(maxsize=10_000)
def get_ipa_of_one_word(word: str) -> str:
    """Gets the pronunciation of one word.

    Args:
        word: a word

    Returns:
        str: the ipa of the word
    """
    # Setup
    word = word.strip()
    word = unidecode(word)
    word = word.lower()
    ipa_words = [""] * len(word)
    def substring_splits_th(substring: str, word: str, i:int, j:int) -> bool:
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
    first_attempt, success = _word_pronunciation_hail_mary(word)
    if success:
        return cleanMod.clean_ipa(first_attempt)

    # While there are still letters in the word
    substring_added = True
    while substring_added:
        # Initialize variables to store the largest matching substring and its length
        substring_added = False
        largest_substring = ""
        pronunciation_of_largest_substring = ""
        largest_substring_len = 0
        beginning_index_of_substring = 0
        end_index_of_substring = 0

        # Iterate over every possible substring
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                substring = word[i:j]

                if len(substring) <= largest_substring_len:
                    continue
                if " " in substring:
                    continue
                if len(substring) > 1:
                    substring_ipa, success = _stringPronuncationHailMary(substring)
                    if (not success) or (len(substring_ipa) >= len(substring) * 2) or (substring_splits_th(substring, word, i, j)):
                        continue
                    else:
                        pronunciation_of_largest_substring = substring_ipa
                elif len(substring) == 1:
                    letter_to_pronunciation = {
                        "a": "æ", "b": "b", "c": "k", "d": "d", "e": "ɛ", "f": "f", "g": "g", "h": "h", "i": "ɪ",
                        "j": "ʤ", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "k", "r": "r",
                        "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "ks", "y": "j", "z": "z"
                    }
                    pronunciation_of_largest_substring = letter_to_pronunciation.get(substring, largest_substring)

                largest_substring = substring
                substring_added = True
                largest_substring_len = len(substring)
                beginning_index_of_substring = i
                end_index_of_substring = j

        # Adds the substring to the list
        if substring_added:
            ipa_words[beginning_index_of_substring] = pronunciation_of_largest_substring
        spaces = " " * largest_substring_len
        word = word.rstrip()
        word = word[:beginning_index_of_substring] + spaces + word[end_index_of_substring:]

    # Concatenates the list together at the end to get the pronunciation
    pronunciation = "".join(ipa_words)
    pronunciation = cleanMod.clean_ipa(pronunciation)
    return pronunciation

def _word_pronunciation_hail_mary(word: str) -> tuple[str, bool]:
    """Tries to get the pronunciation from the predefined ipa dictionary.

    Args:
        word (str): the regular word

    Returns:
        tuple[str, bool]: the ipa of the word (or the original word if not found), and whether it was found.
    """        
    word_pronuncation = ipaAllNames.data.get(word)
    if word_pronuncation != None:
        return word_pronuncation, True
    return word, False

def _stringPronuncationHailMary(string: str) -> tuple[str, bool]:
    """Helper function of _getIpaOfOneWord.
    Tries to get the ipa of a string (with more than one letter).

    Args:
        string (str): a string that is longer than one letter

    Returns:
        tuple[str, bool]: the ipa of the string (or the original string if not found), and whether it was found.
    """        
    ipa_pronunciation = ipaCommonWordParts.data.get(string)
    if ipa_pronunciation != None:
        return ipa_pronunciation, True
    return string, False