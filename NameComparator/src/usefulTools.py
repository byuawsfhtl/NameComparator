import numpy as np
from scipy.optimize import linear_sum_assignment
from fuzzywuzzy import fuzz

def findWhichWordsMatchAndHowWell(name0:str, name1:str) -> list[tuple[str, str, int]]:
    """Identifies which words in either name are a match, and how well they match.

    Args:
        name0 (str): a name
        name1 (str): a name

    Returns:
        list[tuple[str, str, int]]: a list of tuples idenifying the index of the word in the first name,
            the index of the word in the second name, and the score of how well they match
    """
    # Initialize empty list to store scores
    words0 = name0.split()
    words1 = name1.split()
    if len(words0) != len(words1):
        if len(words0) < len(words1):
            words0 += [None] * (len(words1) - len(words0))
        else:
            words1 += [None] * (len(words0) - len(words1))
    scores = np.zeros((len(words0), len(words1)))

    # Score each matchup
    for i, word0 in enumerate(words0):
        for j, word1 in enumerate(words1):
            # Assign a very low finite score to dummy pairings
            scores[i, j] = -1e9 
            if (word0 is None) or (word1 is None):
                continue
            # Assign the score this way if either is initial
            if (len(word0) == 1) or (len(word1) == 1):
                if (word0[0] == word1[0]):
                    score = 100
                else:
                    score = 0
            # For words longer than 2, either use ratio or partial ratio
            # for score as shown below.
            else:
                ratio = fuzz.ratio(word0, word1)
                if (word0[0] == word1[0]):
                    prScore = fuzz.partial_ratio(word0, word1)
                    score = max(ratio, prScore)
                else:
                    score = ratio
            # Add the score
            scores[i, j] = score
    
    # Identify the best matchups
    words0 = [str(i) if word is not None else None for i, word in enumerate(words0)]
    words1 = [str(i) if word is not None else None for i, word in enumerate(words1)]
    return identifyBestMatchups(scores=scores, listA=words0, listB=words1)

def identifyBestMatchups(scores:np.ndarray, listA:list[str|None], listB:list[str|None]) -> list[tuple[str, str, int]]:
        """Uses the Hungarian algorithm to find the optimal assignments.

        Args:
            scores (np.ndarray): the scores of a certain matchup
            listA (list[str | None]): a list of indices as strings or None
            listB (list[str | None]): a list of indices as strings or None

        Returns:
            list[tuple[str, str, int]]: the word combo
        """        
        rowInd, colInd = linear_sum_assignment(-scores)
        bestCombination = []
        for i, j in zip(rowInd, colInd):
            if (listA[i] is not None) and (listB[j] is not None):
                matchupScore = scores[i, j]
                bestCombination.append((listA[i], listB[j], matchupScore))
        return bestCombination

def calculateEditImprovement(name0:str, name1:str, name0Edited:str, name1Edited:str) -> tuple[float, tuple, tuple]:
    """Calculates how much editing a name or both names improved the score in comparison to the original names.

    Args:
        name0 (str): the original first name
        name1 (str): the original second name
        name0Edited (str): the edited first name
        name1Edited (str): the edited second name

    Returns:
        tuple[float, tuple, tuple]: the score of how much the edits improved the comparison (can be negative), 
        the word combo of the original, the word combo of the edited verison
    """        
    ogWordCombo = findWhichWordsMatchAndHowWell(name0, name1)
    editedWordCombo = findWhichWordsMatchAndHowWell(name0Edited, name1Edited)
    if (not ogWordCombo) or (not editedWordCombo):
        return 0, ogWordCombo, editedWordCombo
    ogAverageScore = sum(tup[2] for tup in ogWordCombo) / len(ogWordCombo)
    editedAverageScore = sum(tup[2] for tup in editedWordCombo) / len(editedWordCombo)
    diff = editedAverageScore - ogAverageScore
    return diff, ogWordCombo, editedWordCombo

def getPairIndicesAndWords(name0:str, name1:str) -> list[tuple[int, int, str, str]]:
        """Identifies which words in the names match.

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            list[tuple[int, int, str, str]]: the list of which words match. Tuples of: the index of word in name0, the index of word in name1, in word in name0, the word in name1
        """        
        combo = findWhichWordsMatchAndHowWell(name0, name1)
        words0 = name0.split()
        words1 = name1.split()
        matchIndices = [(int(tup[0]), int(tup[1])) for tup in combo]
        matchIndicesWithWords = [(tup[0], tup[1], words0[tup[0]], words1[tup[1]]) for tup in matchIndices]
        return matchIndicesWithWords

class NameEditor():
    """ A class used for ease of editing specific words in names.
    """        
    def __init__(self, name0:str, name1:str) -> None:
        """Splits the words for later editing.

        Args:
            name0 (str): a name
            name1 (str): a name
        """            
        self.words0 = name0.split()
        self.words1 = name1.split()
    
    def updateName0(self, index:int, updatedWord:str) -> None:
        """Replaces the stored word for name0 at the specified index.

        Args:
            index (int): the specified index
            updatedWord (str): the replacement string
        """
        self.words0[index] = updatedWord

    def updateName1(self, index:int, updatedWord:str) -> None:
        """Replaces the stored word for name1 at the specified index.

        Args:
            index (int): the specified index
            updatedWord (str): the replacement string
        """
        self.words1[index] = updatedWord

    def getModifiedNames(self) -> tuple[str, str]:
        """Retrieves the modified names.

        Returns:
            tuple[str, str]: the modified names
        """            
        name0 = ' '.join(self.words0)
        name1 = ' '.join(self.words1)
        if not name0:
            name0 = '_'
        if not name1:
            name1 = '_'
        return name0, name1