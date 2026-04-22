from numpy import zeros as np_zeros
from numpy import ndarray
from functools import lru_cache
from munkres import Munkres
from rapidfuzz.fuzz import ratio as fuzz_ratio
from rapidfuzz.fuzz import partial_ratio as fuzz_partial_ratio

# Note here that lru cache is the python equivalent of memoizee in TypeScript
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

    print(f"Entering Python find_word_matches_and_quality function with the names {name_one} and {name_two}")

    # Initialize empty list to store scores
    words_in_name_one = name_one.split()
    words_in_name_two = name_two.split()
    if len(words_in_name_one) != len(words_in_name_two):
        if len(words_in_name_one) < len(words_in_name_two):
            words_in_name_one += [''] * (len(words_in_name_two) - len(words_in_name_one))
        else:
            words_in_name_two += [''] * (len(words_in_name_one) - len(words_in_name_two))

    scores = np_zeros((len(words_in_name_one), len(words_in_name_two)))

    # Score each matchup
    for i, word_one in enumerate(words_in_name_one):
        for j, word_two in enumerate(words_in_name_two):
            # Assign a very low finite score to dummy pairings
            scores[i, j] = -1e9 
            if (word_one is None) or (word_two is None) or (word_one == '') or (word_two == ''):
                continue
            # Determine the score of the word pairing
            score = _determine_score_of_word_matchup(word_one, word_two)
            print(f"Python determined score of matchup for {word_one} and {word_two} for this run is {score}")
            # Add the score
            scores[i, j] = score
    
    # Identify the best matchups
    final_words_in_name_one: list[str | None] = [str(i) if (word is not None and word != '') else '' for i, word in enumerate(words_in_name_one)]
    final_words_in_name_two: list[str | None] = [str(i) if (word is not None and word != '') else '' for i, word in enumerate(words_in_name_two)]
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

    # If either of the scores is empty, it should be fine to say it's a match
    # with the empty space
    if (len(word_one) == 0) or (len(word_two) == 0):
        score = 100

    # Assign the score this way if either is initial
    elif (len(word_one) == 1) or (len(word_two) == 1):
        if (word_one[0] == word_two[0]):
            score = 100
        else:
            score = 0

    # For words longer than 2, either use ratio or partial ratio for score as shown below.
    else:
        ratio = round(fuzz_ratio(word_one, word_two, processor=None))
        if (word_one[0] == word_two[0]):
            partial_ratio_score = round(fuzz_partial_ratio(word_one, word_two, processor=None))
            print(f"Found the partial ratio {partial_ratio_score} for {word_one} and {word_two} in Python")
            score = max(ratio, partial_ratio_score)
        else:
            score = ratio

    return score

# This function is only used in a single location, for small lists. Specifically, it is only reached if
# the compare_two_names function is called in NameComparator. If this changes it might be worth changing 
# this function to use the scipy.optimize linear_sum_assignment again. I changed it to use the munkres 
# linear sum for now since it will be much faster to import and have comparable run times with its
# current use cases
def identify_best_matches(scores:ndarray, list_one:list[str|None], list_two:list[str|None]) -> list[tuple[str, str, int]]:
        """Uses the Hungarian algorithm to find the pair of two words that are the
        closest match to each other from two lists.

        Args:
            scores: the scores of a certain matchup
            list_one: a list of indices as strings or None
            list_two: a list of indices as strings or None

        Returns:
            A list of tuples containing the two words that are the best match and a score
            representing how closely they match
        """   
        linear_sum_class = Munkres()     
        hungarian_pairs_list = linear_sum_class.compute(-scores)
        best_combinations = []
        for i, j in hungarian_pairs_list:
            # This first if statement quickly removes any possible out of scope results from the matrix padding
            if (int(i) >= len(list_one)) or (int(j) >= len(list_two)):
                continue
            elif (list_one[i] is not None) and (list_two[j] is not None) and (list_one[i] != '') and (list_two[j] != ''):
                matchup_score = round(scores[i, j])
                best_combinations.append((list_one[i], list_two[j], matchup_score))
        return best_combinations

def calculate_edit_improvement(name_one:str, name_two:str, name_one_edited:str, name_two_edited:str) -> tuple[float, list[tuple[str, str, int]], list[tuple[str, str, int]]]:
    """Calculates how much editing a name or both names improved the score in comparison to the original names.

    Args:
        name_one: the original first name
        name_two: the original second name
        name_one_edited: the edited first name
        name_two_edited: the edited second name

    Returns:
        A tuple containing the score of how much the edits improved the comparison (can be negative), 
        the word combos of the original, and the word combos of the edited verison
    """        
    original_word_combos = find_word_matches_and_quality(name_one, name_two)
    edited_word_combos = find_word_matches_and_quality(name_one_edited, name_two_edited)
    if (not original_word_combos) or (not edited_word_combos):
        return 0, original_word_combos, edited_word_combos
    original_average_score = sum(tup[2] for tup in original_word_combos) / len(original_word_combos)
    edited_average_score = sum(tup[2] for tup in edited_word_combos) / len(edited_word_combos)
    diff = edited_average_score - original_average_score
    return diff, original_word_combos, edited_word_combos

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

    match_indices_with_words = []

    for tuple in match_indices:
        if (tuple[0] < len(words_in_name_one)) and (tuple[1] < len(words_in_name_two)):
            match_indices_with_words.append((tuple[0], tuple[1], words_in_name_one[tuple[0]], words_in_name_two[tuple[1]]))

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