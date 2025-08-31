from typing import NamedTuple
from enum import Enum

from NameComparator.src.usefulTools import get_pair_indices_and_words

class FrequencyData(NamedTuple):
    """Stores the name frequencies for first names and surnames within a given population."""
    first_name_frequencies: dict[str, str]
    surname_frequencies: dict[str, str]

class FrequencyUpperBound(Enum):
    """Represents the frequency upper bound of each uniqueness classification."""
    GENERIC = 1/1
    COMMON = 1/100
    AVERAGE = 1/500
    RARE = 1/1000
    UNSEEN = 1/2000

class Uniqueness(Enum):
    """Represents the classification of the uniqueness of a given word pair."""
    GENERIC = 10
    COMMON = 23
    AVERAGE = 32
    RARE = 42
    UNSEEN = 65

def score_uniqueness(name_a : str, name_b : str, frequency_data:FrequencyData) -> float:
    """Takes two names and gives them an algorithmically calculated uniqueness score
    (between 0 and 100).

    Args:
        name_a: the name of a person
        name_b: the name of a person
        frequency_data: the first name and surname frequencies in a pop

    Returns:
        float: the uniqueness score
    """    
    # Get the max frequency of either word in each pair
    word_pairs = get_pair_indices_and_words(name_a, name_b)
    scores_of_word_pairs = [_findWordPairUniqueness(word_a, word_b, frequency_data).value for _, _, word_a, word_b in word_pairs]
    
    # Return the sum, maxing out at 100
    return min(100, sum(scores_of_word_pairs))

def _findWordPairUniqueness(word_a : str, word_b : str, frequency_data:FrequencyData) -> Uniqueness:
    """Given two words paired together, it will identify the least possible uniqueness
    classification to assign the pair, based on which of the two occurs most frequently
    (as either a surname or as a first name- whichever is more frequent).

    Args:
        word_a: a word in a name
        word_b: a word in a name
        frequency_data: the first name and surname frequencies in a population

    Raises:
        ValueError: if the frequency is below 0
        ValueError: if the frequency is greater than 1

    Returns:
        Uniqueness: the uniqueness classification of the word pair
    """    
    word_a_freq = _get_max_frequency(word_a, frequency_data)
    word_b_freq = _get_max_frequency(word_b, frequency_data)
    pair_freq = max(word_a_freq, word_b_freq)
    if pair_freq < 0:
        raise ValueError("Score is out of range")
    elif pair_freq <= FrequencyUpperBound.UNSEEN.value:
        return Uniqueness.UNSEEN
    elif pair_freq <= FrequencyUpperBound.RARE.value:
        return Uniqueness.RARE
    elif pair_freq <= FrequencyUpperBound.AVERAGE.value:
        return Uniqueness.AVERAGE
    elif pair_freq <= FrequencyUpperBound.COMMON.value:
        return Uniqueness.COMMON
    elif pair_freq <= FrequencyUpperBound.GENERIC.value:
        return Uniqueness.GENERIC
    else:
        raise ValueError("Score is out of range")

def _get_max_frequency(word : str, frequency_data : FrequencyData) -> float:
    """Gets the maximum possible frequency for a given word, whether it is found more as a
    first name or surname, given those frequencies for a given population. If the word is not
    found in either dicts, defaults to the default frequency, which is very low.

    Args:
        word: a word in a name
        frequency_data: the first name and surname frequencies in a population

    Returns:
        float: the frequency
    """    
    default_freq = FrequencyUpperBound.UNSEEN.value
    word_first_name_freq = frequency_data.first_name_frequencies.get(word, default_freq)
    word_surname_freq = frequency_data.surname_frequencies.get(word, default_freq)
    word_initial_freq = 1/26 if len(word) == 1 else default_freq
    return max(word_first_name_freq, word_surname_freq, word_initial_freq)