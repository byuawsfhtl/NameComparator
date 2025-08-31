import numpy as np
from functools import lru_cache
from scipy.optimize import linear_sum_assignment
from fuzzywuzzy import fuzz

@lru_cache(maxsize=1_000)
def find_which_words_match_and_how_well(name_a : str, name_b : str) -> list[tuple[str, str, int]]:
    """Identifies which words in either name are a match, and how well they match.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        list[tuple[str, str, int]]: a list of tuples idenifying the index of the word in the first name,
            the index of the word in the second name, and the score of how well they match
    """
    # Initialize empty list to store scores
    words_in_a = name_a.split()
    words_in_b = name_b.split()
    if len(words_in_a) != len(words_in_b):
        if len(words_in_a) < len(words_in_b):
            words_in_a += [None] * (len(words_in_b) - len(words_in_a))
        else:
            words_in_b += [None] * (len(words_in_a) - len(words_in_b))
    scores = np.zeros((len(words_in_a), len(words_in_b)))

    # Score each matchup
    for i, word_a in enumerate(words_in_a):
        for j, word_b in enumerate(words_in_b):
            # Assign a very low finite score to dummy pairings
            scores[i, j] = -1e9 
            if (word_a is None) or (word_b is None):
                continue
            # Assign the score this way if either is initial
            if (len(word_a) == 1) or (len(word_b) == 1):
                if (word_a[0] == word_b[0]):
                    score = 100
                else:
                    score = 0
            # For words longer than 2, either use ratio or partial ratio for score as shown below.
            else:
                ratio = fuzz.ratio(word_a, word_b)
                if (word_a[0] == word_b[0]):
                    pr_score = fuzz.partial_ratio(word_a, word_b)
                    score = max(ratio, pr_score)
                else:
                    score = ratio
            # Add the score
            scores[i, j] = score
    
    # Identify the best matchups
    words_in_a = [str(i) if word is not None else None for i, word in enumerate(words_in_a)]
    words_in_b = [str(i) if word is not None else None for i, word in enumerate(words_in_b)]
    return identify_best_matchups(scores=scores, list_a=words_in_a, list_b=words_in_b)

def identify_best_matchups(scores:np.ndarray, list_a:list[str|None], list_b:list[str|None]) -> list[tuple[str, str, int]]:
        """Uses the Hungarian algorithm to find the optimal assignments.

        Args:
            scores: the scores of a certain matchup
            list_a: a list of indices as strings or None
            list_b: a list of indices as strings or None

        Returns:
            list[tuple[str, str, int]]: the word combo
        """        
        row_ind, col_ind = linear_sum_assignment(-scores)
        best_combination = []
        for i, j in zip(row_ind, col_ind):
            if (list_a[i] is not None) and (list_b[j] is not None):
                matchup_score = scores[i, j]
                best_combination.append((list_a[i], list_b[j], matchup_score))
        return best_combination

def calculate_edit_improvement(name_a : str, name_b : str, name_a_edited : str, name_b_edited : str) -> tuple[float, tuple, tuple]:
    """Calculates how much editing a name or both names improved the score in comparison to the original names.

    Args:
        name_a: the name of a person
        name_b: the name of a person
        name_a_edited: the edited first name
        name_b_edited: the edited second name

    Returns:
        tuple[float, tuple, tuple]: the score of how much the edits improved the comparison (can be negative), 
        the word combo of the original, the word combo of the edited verison
    """        
    og_word_combo = find_which_words_match_and_how_well(name_a, name_b)
    edited_word_combo = find_which_words_match_and_how_well(name_a_edited, name_b_edited)
    if (not og_word_combo) or (not edited_word_combo):
        return 0, og_word_combo, edited_word_combo
    og_average_score = sum(tup[2] for tup in og_word_combo) / len(og_word_combo)
    edited_average_score = sum(tup[2] for tup in edited_word_combo) / len(edited_word_combo)
    diff = edited_average_score - og_average_score
    return diff, og_word_combo, edited_word_combo

def get_pair_indices_and_words(name_a : str, name_b : str) -> list[tuple[int, int, str, str]]:
    """Identifies which words in the names match.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        list[tuple[int, int, str, str]]: the list of which words match. Tuples of: the index of word in nameA, the index of word in nameB, in word in nameA, the word in nameB
    """        
    combo = find_which_words_match_and_how_well(name_a, name_b)
    words_in_a = name_a.split()
    words_in_b = name_b.split()
    match_indices = [(int(tup[0]), int(tup[1])) for tup in combo]
    match_indices_with_words = [(tup[0], tup[1], words_in_a[tup[0]], words_in_b[tup[1]]) for tup in match_indices]
    return match_indices_with_words

class NameEditor():
    """ A class used for ease of editing specific words in names.
    """        
    def __init__(self, name_a : str, name_b : str) -> None:
        """Splits the words for later editing.

        Args:
            name_a: the name of a person
            name_b: the name of a person
        """            
        self.words_in_a = name_a.split()
        self.words_in_b = name_b.split()
    
    def update_name_a(self, index:int, updated_word : str) -> None:
        """Replaces the stored word for nameA at the specified index.

        Args:
            index: the specified index
            updated_word: the replacement string

        Returns:
            None
        """
        self.words_in_a[index] = updated_word

    def update_name_b(self, index:int, updated_word : str) -> None:
        """Replaces the stored word for nameB at the specified index.

        Args:
            index (int): the specified index
            updatedWord (str): the replacement string
        """
        self.words_in_b[index] = updated_word

    def get_modified_names(self) -> tuple[str, str]:
        """Retrieves the modified names.

        Returns:
            tuple[str, str]: the modified names
        """            
        name_a = ' '.join(self.words_in_a)
        name_b = ' '.join(self.words_in_b)
        if not name_a:
            name_a = '_'
        if not name_b:
            name_b = '_'
        return name_a, name_b