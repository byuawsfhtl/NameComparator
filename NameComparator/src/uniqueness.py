from typing import NamedTuple
from enum import Enum

from NameComparator.src.usefulTools import getPairIndicesAndWords

class FrequencyData(NamedTuple):
    """Stores the name frequencies for first names and surnames within a given population."""
    firstNameFrequencies: dict[str, str]
    surnameFrequencies: dict[str, str]

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

def scoreUniqueness(nameA:str, nameB:str, frequencyData:FrequencyData) -> float:
    """Takes two names and gives them an algorithmically calculated uniqueness score
    (between 0 and 100).

    Args:
        nameA (str): a name
        nameB (str): a name
        frequencyData (FrequencyData): the first name and surname frequencies in a pop

    Returns:
        float: the uniqueness score
    """    
    # Get the max frequency of either word in each pair
    wordPairs = getPairIndicesAndWords(nameA, nameB)
    scoresOfWordPairs = [_findWordPairUniqueness(wordA, wordB, frequencyData).value for _, _, wordA, wordB in wordPairs]
    
    # Return the sum, maxing out at 100
    return min(100, sum(scoresOfWordPairs))

def _findWordPairUniqueness(wordA:str, wordB:str, frequencyData:FrequencyData) -> Uniqueness:
    """Given two words paired together, it will identify the least possible uniqueness
    classification to assign the pair, based on which of the two occurs most frequently
    (as either a surname or as a first name- whichever is more frequent).

    Args:
        wordA (str): a word in a name
        wordB (str): a word in a name
        frequencyData (FrequencyData): the first name and surname frequencies in a population

    Raises:
        ValueError: if the frequency is below 0
        ValueError: if the frequency is greater than 1

    Returns:
        Uniqueness: the uniqueness classification of the word pair
    """    
    wordAFreq = _getMaxFrequency(wordA, frequencyData)
    wordBFreq = _getMaxFrequency(wordB, frequencyData)
    pairFreq = max(wordAFreq, wordBFreq)
    if pairFreq < 0:
        raise ValueError("Score is out of range")
    elif pairFreq <= FrequencyUpperBound.UNSEEN.value:
        return Uniqueness.UNSEEN
    elif pairFreq <= FrequencyUpperBound.RARE.value:
        return Uniqueness.RARE
    elif pairFreq <= FrequencyUpperBound.AVERAGE.value:
        return Uniqueness.AVERAGE
    elif pairFreq <= FrequencyUpperBound.COMMON.value:
        return Uniqueness.COMMON
    elif pairFreq <= FrequencyUpperBound.GENERIC.value:
        return Uniqueness.GENERIC
    else:
        raise ValueError("Score is out of range")

def _getMaxFrequency(word:str, frequencyData:FrequencyData) -> float:
    """Gets the maximum possible frequency for a given word, whether it is found more as a
    first name or surname, given those frequencies for a given population. If the word is not
    found in either dicts, defaults to the default frequency, which is very low.

    Args:
        word (str): a word in a name
        frequencyData (FrequencyData): the first name and surname frequencies in a population

    Returns:
        float: the frequency
    """    
    defaultFreq = FrequencyUpperBound.UNSEEN.value
    wordFirstNameFreq = frequencyData.firstNameFrequencies.get(word, defaultFreq)
    wordSurnameFreq = frequencyData.surnameFrequencies.get(word, defaultFreq)
    wordInitialFreq = 1/26 if len(word) == 1 else defaultFreq
    return max(wordFirstNameFreq, wordSurnameFreq, wordInitialFreq)