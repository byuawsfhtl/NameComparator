import numpy as np
from functools import lru_cache
from munkres import Munkres
from fuzzywuzzy import fuzz

@lru_cache(maxsize=1_000)
def find_word_matches_and_quality(name_one:str, name_two:str) -> list[tuple[str, str, int]]:
    """Identifies which words in either name are a match, and how well they match.

    Args:
        name_one: The first name to check for matches
        name_two: The second name to check for matches

    Returns:
        A list of tuples idenifying the index of the word in the first name,
        the index of the word in the second name, and the score of how well they match
    """
    # Initialize empty list to store scores
    words_in_name_one = name_one.split()
    words_in_name_two = name_two.split()
    if len(words_in_name_one) != len(words_in_name_two):
        if len(words_in_name_one) < len(words_in_name_two):
            words_in_name_one += [''] * (len(words_in_name_two) - len(words_in_name_one))
        else:
            words_in_name_two += [''] * (len(words_in_name_one) - len(words_in_name_two))
    scores = np.zeros((len(words_in_name_one), len(words_in_name_two)))

    # Score each matchup
    for i, word_one in enumerate(words_in_name_one):
        for j, word_two in enumerate(words_in_name_two):
            # Assign a very low finite score to dummy pairings
            scores[i, j] = -1e9 
            if (word_one is None) or (word_two is None):
                continue
            # Determine the score of the word pairing
            score = _determine_score_of_word_matchup(word_one, word_two)
            # Add the score
            scores[i, j] = score
    
    # Identify the best matchups
    final_words_in_name_one: list[str | None] = [str(i) if word is not None else '' for i, word in enumerate(words_in_name_one)]
    final_words_in_name_two: list[str | None] = [str(i) if word is not None else '' for i, word in enumerate(words_in_name_two)]
    return identify_best_matches(scores=scores, list_one=final_words_in_name_one, list_two=final_words_in_name_two)

def _determine_score_of_word_matchup(word_one: str, word_two: str) -> int:
    """This is a helper function for find_word_matches_and_quality to fix its
    nesting depth. What it does is it takes in a word and an integer
    representation of a list position for two different words. Then it
    determines how closely the words match each other and assigns them a
    score according to that.
    
    Args:
        word_one: The first word used in the comparison and scoring
        word_two: The second word used in the comparison and scoring
    
    Returns:
        An integer representing the score to be added to the word pairing
    """

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
            partial_ratio_score = fuzz.partial_ratio(word_one, word_two)
            score = max(ratio, partial_ratio_score)
        else:
            score = ratio

    return score

# This function is only used in a single location, for small lists. Specifically, it is only reached if
# the compare_two_names function is called in NameComparator. If this changes it might be worth changing 
# this function to use the scipy.optimize linear_sum_assignment again. I changed it to use the munkres 
# linear sum for now since it will be much faster to import and have comparable run times with its
# current use cases
def identify_best_matches(scores:np.ndarray, list_one:list[str|None], list_two:list[str|None]) -> list[tuple[str, str, int]]:
        """Uses the Hungarian algorithm to find the pair of two words that are the
        closest match to each other from two lists.

        Args:
            scores: the scores of a certain matchup
            list_one: a list of indices as strings or None
            list_two: a list of indices as strings or None

        Returns:
            A tuple containing the two words that are the best match and a score
            representing how closely they match
        """   
        linear_sum_class = Munkres()     
        list_of_paired_indices = linear_sum_class.compute(-scores)
        best_combination = []
        for i, j in list_of_paired_indices:
            if (list_one[i] is not None) and (list_two[j] is not None):
                matchup_score = scores[i, j]
                best_combination.append((list_one[i], list_two[j], matchup_score))
        return best_combination

def calculate_edit_improvement(name_one:str, name_two:str, name_one_edited:str, name_two_edited:str) -> tuple[float, tuple, tuple]:
    """Calculates how much editing a name or both names improved the score in comparison to the original names.

    Args:
        name_one: the original first name
        name_two: the original second name
        name_one_edited: the edited first name
        name_two_edited: the edited second name

    Returns:
        A tuple containing the score of how much the edits improved the comparison (can be negative), 
        the word combo of the original, and the word combo of the edited verison
    """        
    original_word_combo = find_word_matches_and_quality(name_one, name_two)
    edited_word_combo = find_word_matches_and_quality(name_one_edited, name_two_edited)
    if (not original_word_combo) or (not edited_word_combo):
        return 0, original_word_combo, edited_word_combo
    original_average_score = sum(tup[2] for tup in original_word_combo) / len(original_word_combo)
    edited_average_score = sum(tup[2] for tup in edited_word_combo) / len(edited_word_combo)
    diff = edited_average_score - original_average_score
    return diff, original_word_combo, edited_word_combo

def get_matching_words_and_indices(name_one:str, name_two:str) -> list[tuple[int, int, str, str]]:
    """Identifies which words in the names match and finds their indices.

    Args:
        name_one: The first name to check for matches in
        name_two: The second name to check for matches in

    Returns:
        A list of tuples containing which words match. The tuples contain the index of a matching word in name_one, 
        the index of a matching word in name_two, the matching word in name_one, and the matching word in name_two
    """        
    combo = find_word_matches_and_quality(name_one, name_two)
    words_in_name_one = name_one.split()
    words_in_name_two = name_two.split()
    match_indices = [(int(tup[0]), int(tup[1])) for tup in combo]
    match_indices_with_words = [(tup[0], tup[1], words_in_name_one[tup[0]], words_in_name_two[tup[1]]) for tup in match_indices]
    return match_indices_with_words

class NameEditor():
    """ A class used for ease of editing specific words in names.
    """        
    def __init__(self, name_one:str, name_two:str) -> None:
        """Splits the words for later editing.

        Args:
            name_one: The first name to edit
            name_two: The second name to edit
        """            
        self.words_in_name_one = name_one.split()
        self.words_in_name_two = name_two.split()
    
    def update_name_one(self, index:int, updated_word:str) -> None:
        """Replaces the stored word for name_one at the specified index.

        Args:
            index: The specified index
            updated_word: The replacement string
        """
        self.words_in_name_one[index] = updated_word

    def update_name_two(self, index:int, updated_word:str) -> None:
        """Replaces the stored word for name_two at the specified index.

        Args:
            index: The specified index
            updated_word: The replacement string
        """
        self.words_in_name_two[index] = updated_word

    def get_modified_names(self) -> tuple[str, str]:
        """Retrieves the modified names.

        Returns:
            A tuple containing the fist modified name and the second modified name
        """            
        name_one = ' '.join(self.words_in_name_one)
        name_two = ' '.join(self.words_in_name_two)
        if not name_one:
            name_one = '_'
        if not name_two:
            name_two = '_'
        return name_one, name_two