from functools import lru_cache
from unidecode import unidecode

import NameComparator.data.pronunciation.ipaOnellNames as ipaOnellNames
import NameComparator.data.pronunciation.ipaCommonWordParts as ipaCommonWordParts

def get_ipa(name:str) -> str:
    """Gets the pronunciation of the name.

    Args:
        name (str): a name

    Returns:
        str: the ipa of the name
    """        
    pronunciation_list = []
    for word in name.split():
        pronunciation_list.append(_get_ipa_of_one_word(word))
    pronunciation_of_name = " ".join(pronunciation_list)
    return pronunciation_of_name

@lru_cache(maxsize=1_000)
def _get_ipa_of_one_word(word:str) -> str:
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
    pronunciation_list = [""] * len(word)

    # Tries to get the ipa from the plain word
    first_attempt, success = _word_pronunciation_ipa_guess(word)
    if success:
        return first_attempt

    # While there are still letters in the word
    substring_added = True
    while substring_added:

        substring_added, beginning_index_of_substring, end_index_of_substring, pronunciation_of_largest_substring, largest_substring_length = _iterate_all_possible_substrings(word)

        # Adds the substring to the list
        if substring_added:
            pronunciation_list[beginning_index_of_substring] = pronunciation_of_largest_substring
        spaces = " " * largest_substring_length
        word = word.rstrip()
        word = word[:beginning_index_of_substring] + spaces + word[end_index_of_substring:]

    # Concatenates the list together at the end to get the pronunciation
    pronunciation = "".join(pronunciation_list)
    return pronunciation

def _iterate_all_possible_substrings(word: str) -> tuple[bool, int, int, str, int]:
    """ Iterates through all of the possible substrings of a word to find information
    about which substrings are going to be the best ipa pronunciation representation
    of the word.
    
    Args:
        word: the word that all the possible substrings of are being iterated through
    
    Returns:
        A tuple containing the following information: A boolean representing if the 
        substring was added, the beginning index of the substring, the end index of 
        the substring, the pronunciation of the largest substring, and the length of 
        the largest substring
    """


    # Initialize variables to store the largest matching substring and its length
    substring_added = False
    largest_substring = ""
    pronunciation_of_largest_substring = ""
    largest_substring_length = 0
    beginning_index_of_substring = 0
    end_index_of_substring = 0

    # Iterate over every possible substring
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            substring = word[i:j]

            if len(substring) <= largest_substring_length:
                continue
            if " " in substring:
                continue
            if len(substring) > 1:
                ipa_substring, success = _string_pronuncation_ipa_guess(substring)
                if (not success) or (len(ipa_substring) >= len(substring) * 2) or (substring_splits_th_sound(substring, word, i, j)): continue
                else: pronunciation_of_largest_substring = ipa_substring
            elif len(substring) == 1:
                letter_to_pronunciation = {
                "a": "æ", "b": "b", "c": "k", "d": "d", "e": "ɛ", "f": "f", "g": "g", "h": "h", "i": "ɪ",
                "j": "ʤ", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "k", "r": "r",
                "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "ks", "y": "j", "z": "z"
                }
                pronunciation_of_largest_substring = letter_to_pronunciation.get(substring, largest_substring)

            largest_substring = substring
            substring_added = True
            largest_substring_length = len(substring)
            beginning_index_of_substring = i
            end_index_of_substring = j

    return substring_added, beginning_index_of_substring, end_index_of_substring, pronunciation_of_largest_substring, largest_substring_length

def _word_pronunciation_ipa_guess(word:str) -> tuple[str, bool]:
    """Tries to get the pronunciation from the predefined ipa dictionary.

    Args:
        word (str): the regular word

    Returns:
        tuple[str, bool]: the ipa of the word (or the original word if not found), and whether it was found.
    """        
    word_pronunciation = ipaOnellNames.data.get(word)
    if word_pronunciation != None:
        return word_pronunciation, True
    return word, False

def _string_pronuncation_ipa_guess(string:str) -> tuple[str, bool]:
    """Helper function of _get_ipa_of_one_word.
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

def substring_splits_th_sound(substring:str, word:str, i:int, j:int) -> bool:
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