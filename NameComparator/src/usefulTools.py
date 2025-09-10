from functools import lru_cache
from fuzzywuzzy import fuzz
from typing import NamedTuple

from HungarianScorer.HungarianScorer import HungarianScorer

class WordInName(NamedTuple):
    string: str
    index: int

class Matchup(NamedTuple):
    word_in_name_a: WordInName
    word_in_name_b: WordInName
    score: float

@lru_cache()
def find_which_words_match_and_how_well(name_a: str, name_b: str) -> list[Matchup]:
    """Identifies which words in either name are a match, and how well they match.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        list[tuple[str, str, int]]: a list of tuples idenifying the index of the word in the first name,
            the index of the word in the second name, and the score of how well they match
    """
    all_words_a = [WordInName(string=word, index=i) for i, word in enumerate(name_a.split())]
    all_words_b = [WordInName(string=word, index=i) for i, word in enumerate(name_b.split())]
    optimal_matchups = HungarianScorer.getBestCombo(all_words_a, all_words_b, _get_matchup_score)
    return [Matchup(*triple) for triple in optimal_matchups]

def _get_matchup_score(a: WordInName, b: WordInName) -> float:
    word_a = a.string
    word_b = b.string
    if (len(word_a) == 1) or (len(word_b) == 1):
        return 100 if (word_a[0] == word_b[0]) else 0
    return _get_fuzzy_score(word_a, word_b)

@lru_cache(maxsize=1_000_000)
def _get_fuzzy_score(word_a: str, word_b: str) -> float:
    ratio = fuzz.ratio(word_a, word_b)
    if (word_a[0] == word_b[0]):
        partial_ratio = fuzz.partial_ratio(word_a, word_b)
        return max(ratio, partial_ratio)
    return ratio




def calculate_edit_improvement(name_a: str, name_b: str, name_a_edited: str, name_b_edited: str) -> tuple[float, tuple, tuple]:
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
    all_matchups_original = find_which_words_match_and_how_well(name_a, name_b)
    all_matchups_edited = find_which_words_match_and_how_well(name_a_edited, name_b_edited)
    if (not all_matchups_original) or (not all_matchups_edited):
        return 0, all_matchups_original, all_matchups_edited
    average_score_original = sum(matchup.score for matchup in all_matchups_original) / len(all_matchups_original)
    average_score_edited = sum(matchup.score for matchup in all_matchups_edited) / len(all_matchups_edited)
    diff = average_score_edited - average_score_original
    return diff, all_matchups_original, all_matchups_edited

class NameEditor():
    """ A class used for ease of editing specific words in names.
    """        
    def __init__(self, name_a: str, name_b: str) -> None:
        """Splits the words for later editing.

        Args:
            name_a: the name of a person
            name_b: the name of a person
        """            
        self.words_in_a = name_a.split()
        self.words_in_b = name_b.split()
    
    def update_name_a(self, index:int, updated_word: str) -> None:
        """Replaces the stored word for nameA at the specified index.

        Args:
            index: the specified index
            updated_word: the replacement string

        Returns:
            None
        """
        self.words_in_a[index] = updated_word

    def update_name_b(self, index:int, updated_word: str) -> None:
        """Replaces the stored word for nameB at the specified index.

        Args:
            index: the specified index
            updated_word: the replacement string

        Returns:
            None
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