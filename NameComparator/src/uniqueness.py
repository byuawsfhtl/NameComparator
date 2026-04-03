from typing import NamedTuple
from enum import Enum

from NameComparator.src.useful_tools import get_matching_words_and_indices

class FrequencyData(NamedTuple):
    """A named tuple that stores the name frequencies for first names and surnames 
    within a given population in two dictionaries."""
    first_name_frequencies: dict[str, str]
    surname_frequencies: dict[str, str]

class FrequencyUpperBound(Enum):
    """An enum representing the frequency upper bound of each uniqueness classification."""
    GENERIC = 1/1
    COMMON = 1/100
    AVERAGE = 1/500
    RARE = 1/1000
    UNSEEN = 1/2000

class Uniqueness(Enum):
    """An enum representing the classification of the uniqueness of a given word pair."""
    GENERIC = 10
    COMMON = 23
    AVERAGE = 32
    RARE = 42
    UNSEEN = 65

def score_uniqueness(name_one:str, name_two:str, frequency_data:FrequencyData) -> float:
    """Takes two names and gives them an algorithmically calculated uniqueness score
    between 0 and 100.

    Args:
        name_one: The first name to compare for a uniqueness score
        name_two: The second name to compare for a uniqueness score
        frequency_data: The first name and surname frequencies within a population

    Returns:
        A float numerically representing the uniqueness of the two names
    """    
    # Get the max frequency of either word in each pair
    word_pairs = get_matching_words_and_indices(name_one, name_two)
    scores_of_word_pairs = [_find_word_pair_uniqueness(word_one, word_two, frequency_data).value for _, _, word_one, word_two in word_pairs]
    
    # Return the sum, maxing out at 100
    return min(100, sum(scores_of_word_pairs))

def _find_word_pair_uniqueness(word_one:str, word_two:str, frequency_data:FrequencyData) -> Uniqueness:
    """Given two words paired together, it will identify the least possible uniqueness
    classification to assign the pair, based on which of the two occurs most frequently.
    This can be based on either a surname or as a first name -- whichever is more frequent.

    Args:
        word_one: The first word to score from a name
        word_two: The second word to score from a name
        frequency_data: The first name and surname frequencies within a population

    Raises:
        ValueError: If the frequency is below 0
        ValueError: If the frequency is greater than 1

    Returns:
        Uniqueness: The uniqueness classification enum of the word pair
    """    
    word_one_frequency = _get_max_frequency(word_one, frequency_data)
    word_two_frequency = _get_max_frequency(word_two, frequency_data)
    pair_frequency = max(word_one_frequency, word_two_frequency)
    if pair_frequency < 0:
        raise ValueError("Score is out of range")
    elif pair_frequency <= FrequencyUpperBound.UNSEEN.value:
        return Uniqueness.UNSEEN
    elif pair_frequency <= FrequencyUpperBound.RARE.value:
        return Uniqueness.RARE
    elif pair_frequency <= FrequencyUpperBound.AVERAGE.value:
        return Uniqueness.AVERAGE
    elif pair_frequency <= FrequencyUpperBound.COMMON.value:
        return Uniqueness.COMMON
    elif pair_frequency <= FrequencyUpperBound.GENERIC.value:
        return Uniqueness.GENERIC
    else:
        raise ValueError("Score is out of range")

def _get_max_frequency(word:str, frequency_data:FrequencyData) -> float:
    """Gets the maximum possible frequency for a given word, whether it is found more as a
    first name or surname, given those frequencies for a given population. If the word is not
    found in either dicts, defaults to the default frequency, which is very low.

    Args:
        word (str): The word from a name to score
        frequency_data (frequency_data): The first name and surname frequencies in a population

    Returns:
        A float representing the maximum possible frequency for the word
    """    
    default_frequency = FrequencyUpperBound.UNSEEN.value
    word_first_name_frequency = frequency_data.first_name_frequencies.get(word, default_frequency)
    word_surname_frequency = frequency_data.surname_frequencies.get(word, default_frequency)
    word_initial_frequency = 1/26 if len(word) == 1 else default_frequency
    return max(word_first_name_frequency, word_surname_frequency, word_initial_frequency)