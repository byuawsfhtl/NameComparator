from functools import lru_cache
from unidecode import unidecode
from json import loads as json_loads
from importlib.resources import files

# This is required to make sure that it reads in the characters correctly
unparsed_all_ipa_names = files('data').joinpath('pronunciation/ipaAllNames.json').read_text(encoding='utf-8')
unparsed_common_ipa_word_parts = files('data').joinpath('pronunciation/ipaCommonWordParts.json').read_text(encoding='utf-8')

# Note here that lru cache is the python equivalent of memoizee in TypeScript
@lru_cache(maxsize=1000)
def get_ipa(name:str) -> str:
    """Gets the pronunciation of a name.

    Args:
        name: The name to get the pronunciation of

    Returns:
        The ipa pronunciation of the name
    """        
    pronunciation_list = []
    for word in name.split():
        pronunciation_list.append(_get_ipa_of_one_word(word))
        print(f"Current pronunciation list in Python: {pronunciation_list}")
    pronunciation_of_name = " ".join(pronunciation_list)

    print(f"Final pronunciation list in Python: {pronunciation_list}")
    return pronunciation_of_name

# Note here that lru cache is the python equivalent of memoizee in TypeScript
@lru_cache(maxsize=1000)
def _get_ipa_of_one_word(word:str) -> str:
    """Gets the pronunciation of a word.

    Args:
        word: The word to get the pronunciation of

    Returns:
        The ipa pronunciation of the word
    """

    print(f"Getting the IPA of the word {word} in Python")

    # Setup
    word = word.strip()
    word = unidecode(word)
    word = word.lower()
    pronunciation_list = [""] * len(word)

    # Tries to get the ipa from the plain word
    first_attempt, success = _word_pronunciation_ipa_guess(word)
    if success:
        print("Successfully guessed the word pronunciation in Python")
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
        word: The word that all the possible substrings of are being iterated through
    
    Returns:
        A tuple containing the following information: A boolean representing if the 
        substring was added, the beginning index of the substring, the end index of 
        the substring, the pronunciation of the largest substring, and the length of 
        the largest substring
    """

    print(f"Iterating through all the possible substrings of {word} in Python")

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

            print(f"Checking possible pronunciation improvements for the substring {substring} in Python")

            if len(substring) <= largest_substring_length:
                print(f"Skipped the substring {substring} due to it being shorter than the largest substring in Python")
                continue
            if " " in substring:
                print(f"Skipped the substring {substring} due to it containing a space in Python")
                continue
            if len(substring) > 1:
                ipa_substring, success = _string_pronuncation_ipa_guess(substring)
                print(f"Variable check for skipping due to conditions in Python: success - {success}, len(ipa_substring) - {len(ipa_substring)} (len(substring) * 2) - {(len(substring) * 2)}, substring_splits_th_sound(substring, word, i, j) - {substring_splits_th_sound(substring, word, i, j)}")
                if (not success) or (len(ipa_substring) >= (len(substring) * 2)) or (substring_splits_th_sound(substring, word, i, j)): 
                    print(f"Skipped the substring {substring} due to many conditions in Python")
                    continue
                else: 
                    pronunciation_of_largest_substring = ipa_substring
                    print(f"Updated largest substring to be {ipa_substring} based on a guess in Python")
            elif len(substring) == 1:
                letter_to_pronunciation = {
                    "a": "æ", "b": "b", "c": "k", "d": "d", "e": "ɛ", "f": "f", "g": "g", "h": "h", "i": "ɪ",
                    "j": "ʤ", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "k", "r": "r",
                    "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "ks", "y": "j", "z": "z"
                }
                pronunciation_of_largest_substring = letter_to_pronunciation.get(substring, largest_substring)
                print(f"Updated largest substring to be {pronunciation_of_largest_substring} based on the letter to pronunciation table in Python")

            largest_substring = substring
            substring_added = True
            largest_substring_length = len(substring)
            beginning_index_of_substring = i
            end_index_of_substring = j

    print(f"After the for loop, the values of the variables are as follows in TypeScript: substring_added - {substring_added} beginning_index_of_substring - {beginning_index_of_substring} end_index_of_substring - {end_index_of_substring} pronunciation_of_largest_substring - {pronunciation_of_largest_substring} largest_substring_length - {largest_substring_length}")

    return substring_added, beginning_index_of_substring, end_index_of_substring, pronunciation_of_largest_substring, largest_substring_length

def _word_pronunciation_ipa_guess(word:str) -> tuple[str, bool]:
    """Tries to get the pronunciation from the predefined ipa dictionary.

    Args:
        word: The word to get the pronunciation of

    Returns:
        A tuple comtaining the ipa of the word (or the original word if not found), and whether it was found.
    """        
    word_pronunciation = json_loads(unparsed_all_ipa_names).get(word, '')
    print(f"Found the pronunciation '{word_pronunciation}' for {word} in our data")
    if word_pronunciation:
        return word_pronunciation, True
    return word, False

def _string_pronuncation_ipa_guess(string:str) -> tuple[str, bool]:
    """Helper function of _get_ipa_of_one_word. Tries to get the ipa of a string 
    with more than one letter.

    Args:
        string: A string that is longer than one letter to get the pronunciation of

    Returns:
        A tuple containing the ipa of the string (or the original string if not found), and whether it was found.
    """        

    print(f"Finding the pronunciation guess for the string {string} in Python")

    ipa_pronunciation = json_loads(unparsed_common_ipa_word_parts).get(string, '')
    if ipa_pronunciation:
        print(f"Found the pronunciation guess {ipa_pronunciation} for the string {string} in Python")
        return ipa_pronunciation, True
    print(f"Failed to find a pronunciation guess for the string {string} in Python")
    return string, False

def substring_splits_th_sound(substring:str, word:str, i:int, j:int) -> bool:
    """Helps to identify poor substring choices for words for ipa.

    Args:
        substring: The ipa dissection
        word: The full word
        i: The start index of the substring
        j: The end index of the substring

    Returns:
        A boolean representing whether or not it was a good substring
    """      

    print(f"The substring splitting on th sounds has the following variables on startup: substring - {substring} word - {word} i - {i} j - {j}")

    if i == j:
        print("i equalled j in Python")
        return False
    if i >= 0 and substring[0] == 'h' and word[i - 1] == 't':
        print("The first true return case in Python")
        return True
    if j <= len(word) - 1 and substring[-1] == 't' and word[j] == 'h':
        print("The second true return case in Python")
        return True
    print("Hit the default return case in Python")
    return False