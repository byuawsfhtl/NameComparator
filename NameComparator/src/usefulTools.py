import numpy as np
from functools import lru_cache
from scipy.optimize import linear_sum_assignment
from fuzzywuzzy import fuzz

@lru_cache(maxsize=1_000)
def find_word_matches_and_quality(name_one:str, name_two:str) -> list[tuple[str, str, int]]:
    """Identifies which words in either name are a match, and how well they match.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        list[tuple[str, str, int]]: a list of tuples idenifying the index of the word in the first name,
            the index of the word in the second name, and the score of how well they match
    """
    # Initialize empty list to store scores
    wordsInA = name_one.split()
    wordsInB = name_two.split()
    if len(wordsInA) != len(wordsInB):
        if len(wordsInA) < len(wordsInB):
            wordsInA += [None] * (len(wordsInB) - len(wordsInA))
        else:
            wordsInB += [None] * (len(wordsInA) - len(wordsInB))
    scores = np.zeros((len(wordsInA), len(wordsInB)))

    # Score each matchup
    for i, word_one in enumerate(wordsInA):
        for j, word_two in enumerate(wordsInB):
            # Assign a very low finite score to dummy pairings
            scores[i, j] = -1e9 
            if (word_one is None) or (word_two is None):
                continue
            # Assign the score this way if either is initial
            if (len(word_one) == 1) or (len(word_two) == 1):
                if (word_one[0] == word_two[0]):
                    score = 100
                else:
                    score = 0
            # For words longer than 2, either use ratio or partial ratio for score as shown below.
            else:
                ratio = fuzz.ratio(word_one, word_two)
                if (word_one[0] == word_two[0]):
                    prScore = fuzz.partial_ratio(word_one, word_two)
                    score = max(ratio, prScore)
                else:
                    score = ratio
            # Add the score
            scores[i, j] = score
    
    # Identify the best matchups
    wordsInA = [str(i) if word is not None else None for i, word in enumerate(wordsInA)]
    wordsInB = [str(i) if word is not None else None for i, word in enumerate(wordsInB)]
    return identify_best_matches(scores=scores, list_one=wordsInA, list_two=wordsInB)

def identify_best_matches(scores:np.ndarray, list_one:list[str|None], list_two:list[str|None]) -> list[tuple[str, str, int]]:
        """Uses the Hungarian algorithm to find the optimal assignments.

        Args:
            scores (np.ndarray): the scores of a certain matchup
            list_one (list[str | None]): a list of indices as strings or None
            list_two (list[str | None]): a list of indices as strings or None

        Returns:
            list[tuple[str, str, int]]: the word combo
        """        
        rowInd, colInd = linear_sum_assignment(-scores)
        bestCombination = []
        for i, j in zip(rowInd, colInd):
            if (list_one[i] is not None) and (list_two[j] is not None):
                matchupScore = scores[i, j]
                bestCombination.append((list_one[i], list_two[j], matchupScore))
        return bestCombination

def calculate_edit_improvement(name_one:str, name_two:str, name_oneEdited:str, name_twoEdited:str) -> tuple[float, tuple, tuple]:
    """Calculates how much editing a name or both names improved the score in comparison to the original names.

    Args:
        name_one (str): the original first name
        name_two (str): the original second name
        name_oneEdited (str): the edited first name
        name_twoEdited (str): the edited second name

    Returns:
        tuple[float, tuple, tuple]: the score of how much the edits improved the comparison (can be negative), 
        the word combo of the original, the word combo of the edited verison
    """        
    ogword_combo = find_word_matches_and_quality(name_one, name_two)
    editedword_combo = find_word_matches_and_quality(name_oneEdited, name_twoEdited)
    if (not ogword_combo) or (not editedword_combo):
        return 0, ogword_combo, editedword_combo
    ogAverageScore = sum(tup[2] for tup in ogword_combo) / len(ogword_combo)
    editedAverageScore = sum(tup[2] for tup in editedword_combo) / len(editedword_combo)
    diff = editedAverageScore - ogAverageScore
    return diff, ogword_combo, editedword_combo

def get_matching_words_and_indices(name_one:str, name_two:str) -> list[tuple[int, int, str, str]]:
    """Identifies which words in the names match and finds their indices.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        list[tuple[int, int, str, str]]: the list of which words match. Tuples of: the index of word in name_one, the index of word in name_two, in word in name_one, the word in name_two
    """        
    combo = find_word_matches_and_quality(name_one, name_two)
    wordsInA = name_one.split()
    wordsInB = name_two.split()
    matchIndices = [(int(tup[0]), int(tup[1])) for tup in combo]
    matchIndicesWithWords = [(tup[0], tup[1], wordsInA[tup[0]], wordsInB[tup[1]]) for tup in matchIndices]
    return matchIndicesWithWords

class NameEditor():
    """ A class used for ease of editing specific words in names.
    """        
    def __init__(self, name_one:str, name_two:str) -> None:
        """Splits the words for later editing.

        Args:
            name_one (str): a name
            name_two (str): a name
        """            
        self.wordsInA = name_one.split()
        self.wordsInB = name_two.split()
    
    def update_name_one(self, index:int, updatedWord:str) -> None:
        """Replaces the stored word for name_one at the specified index.

        Args:
            index (int): the specified index
            updatedWord (str): the replacement string
        """
        self.wordsInA[index] = updatedWord

    def update_name_two(self, index:int, updatedWord:str) -> None:
        """Replaces the stored word for name_two at the specified index.

        Args:
            index (int): the specified index
            updatedWord (str): the replacement string
        """
        self.wordsInB[index] = updatedWord

    def get_modified_names(self) -> tuple[str, str]:
        """Retrieves the modified names.

        Returns:
            tuple[str, str]: the modified names
        """            
        name_one = ' '.join(self.wordsInA)
        name_two = ' '.join(self.wordsInB)
        if not name_one:
            name_one = '_'
        if not name_two:
            name_two = '_'
        return name_one, name_two