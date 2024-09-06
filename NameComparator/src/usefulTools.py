import numpy as np
from scipy.optimize import linear_sum_assignment
from fuzzywuzzy import fuzz

def findWhichWordsMatchAndHowWell(nameA:str, nameB:str) -> list[tuple[str, str, int]]:
    """Identifies which words in either name are a match, and how well they match.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        list[tuple[str, str, int]]: a list of tuples idenifying the index of the word in the first name,
            the index of the word in the second name, and the score of how well they match
    """
    # Initialize empty list to store scores
    wordsA = nameA.split()
    wordsListB = nameB.split()
    if len(wordsA) != len(wordsListB):
        if len(wordsA) < len(wordsListB):
            wordsA += [None] * (len(wordsListB) - len(wordsA))
        else:
            wordsListB += [None] * (len(wordsA) - len(wordsListB))
    scores = np.zeros((len(wordsA), len(wordsListB)))

    # Score each matchup
    for i, wordA in enumerate(wordsA):
        for j, wordB in enumerate(wordsListB):
            # Assign a very low finite score to dummy pairings
            scores[i, j] = -1e9 
            if (wordA is None) or (wordB is None):
                continue
            # Assign the score this way if either is initial
            if (len(wordA) == 1) or (len(wordB) == 1):
                if (wordA[0] == wordB[0]):
                    score = 100
                else:
                    score = 0
            # For words longer than 2, either use ratio or partial ratio
            # for score as shown below.
            else:
                ratio = fuzz.ratio(wordA, wordB)
                if (wordA[0] == wordB[0]):
                    prScore = fuzz.partial_ratio(wordA, wordB)
                    score = max(ratio, prScore)
                else:
                    score = ratio
            # Add the score
            scores[i, j] = score
    
    # Identify the best matchups
    wordsA = [str(i) if word is not None else None for i, word in enumerate(wordsA)]
    wordsListB = [str(i) if word is not None else None for i, word in enumerate(wordsListB)]
    return identifyBestMatchups(scores=scores, listA=wordsA, listB=wordsListB)

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

def calculateEditImprovement(nameA:str, nameB:str, nameAEdited:str, nameBEdited:str) -> tuple[float, tuple, tuple]:
    """Calculates how much editing a name or both names improved the score in comparison to the original names.

    Args:
        nameA (str): the original first name
        nameB (str): the original second name
        nameAEdited (str): the edited first name
        nameBEdited (str): the edited second name

    Returns:
        tuple[float, tuple, tuple]: the score of how much the edits improved the comparison (can be negative), 
        the word combo of the original, the word combo of the edited verison
    """        
    ogWordCombo = findWhichWordsMatchAndHowWell(nameA, nameB)
    editedWordCombo = findWhichWordsMatchAndHowWell(nameAEdited, nameBEdited)
    if (not ogWordCombo) or (not editedWordCombo):
        return 0, ogWordCombo, editedWordCombo
    ogAverageScore = sum(tup[2] for tup in ogWordCombo) / len(ogWordCombo)
    editedAverageScore = sum(tup[2] for tup in editedWordCombo) / len(editedWordCombo)
    diff = editedAverageScore - ogAverageScore
    return diff, ogWordCombo, editedWordCombo

def getPairIndicesAndWords(nameA:str, nameB:str) -> list[tuple[int, int, str, str]]:
        """Identifies which words in the names match.

        Args:
            nameA (str): a name
            nameB (str): a name

        Returns:
            list[tuple[int, int, str, str]]: the list of which words match. Tuples of: the index of word in nameA, the index of word in nameB, in word in nameA, the word in nameB
        """        
        combo = findWhichWordsMatchAndHowWell(nameA, nameB)
        wordsA = nameA.split()
        wordsB = nameB.split()
        matchIndices = [(int(tup[0]), int(tup[1])) for tup in combo]
        matchIndicesWithWords = [(tup[0], tup[1], wordsA[tup[0]], wordsB[tup[1]]) for tup in matchIndices]
        return matchIndicesWithWords

class NameEditor():
    """ A class used for ease of editing specific words in names.
    """        
    def __init__(self, nameA:str, nameB:str) -> None:
        """Splits the words for later editing.

        Args:
            nameA (str): a name
            nameB (str): a name
        """            
        self.wordsA = nameA.split()
        self.wordsB = nameB.split()
    
    def updateNameA(self, index:int, updatedWord:str) -> None:
        """Replaces the stored word for nameA at the specified index.

        Args:
            index (int): the specified index
            updatedWord (str): the replacement string
        """
        self.wordsA[index] = updatedWord

    def updateNameB(self, index:int, updatedWord:str) -> None:
        """Replaces the stored word for nameB at the specified index.

        Args:
            index (int): the specified index
            updatedWord (str): the replacement string
        """
        self.wordsB[index] = updatedWord

    def getModifiedNames(self) -> tuple[str, str]:
        """Retrieves the modified names.

        Returns:
            tuple[str, str]: the modified names
        """            
        nameA = ' '.join(self.wordsA)
        nameB = ' '.join(self.wordsB)
        if not nameA:
            nameA = '_'
        if not nameB:
            nameB = '_'
        return nameA, nameB