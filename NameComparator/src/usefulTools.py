from numpy import ndarray, array as numpy_array, zeros as np_zeros
from functools import lru_cache
from munkres import Munkres
from rapidfuzz.fuzz import ratio as fuzz_ratio
from rapidfuzz.distance.Indel import normalized_similarity
from math import floor as math_floor

from NameComparator.src.ipa import get_ipa

from json import loads as json_loads
from importlib.resources import files
prefix_list = json_loads(files('data').joinpath('possiblePrefixList.json').read_text(encoding='utf-8'))

# Note here that lru cache is the python equivalent of memoizee in TypeScript
@lru_cache(maxsize=1000)
def find_word_matches_and_quality(name_one:str, name_two:str) -> tuple[list[tuple[str, str, float]], int]:
    """Identifies which words in either name are a match, and how well they match.

    Args:
        name_one: The first name to check for matches
        name_two: The second name to check for matches

    Returns:
        A list of tuples idenifying the index of the word in the first name,
        the index of the word in the second name, and the score of how well they match.
        After that it returns a value representing the number of possible prefixes and
        other odd exceptions in the name
    """

    print(f"Entering Python find_word_matches_and_quality function with the names {name_one} and {name_two}")

    # Initialize a variable for exceptions regarding possible prefixes and warning flags we can ignore
    exception_count = 0

    # Initialize empty list to store scores
    words_in_name_one = name_one.split()
    words_in_name_two = name_two.split()
    if len(words_in_name_one) != len(words_in_name_two):
        if len(words_in_name_one) < len(words_in_name_two):
            words_in_name_one += [''] * (len(words_in_name_two) - len(words_in_name_one))
        else:
            words_in_name_two += [''] * (len(words_in_name_one) - len(words_in_name_two))

    scores = np_zeros((len(words_in_name_one), len(words_in_name_two)))

    print(f"Found the list of words in the names in Python. \nwords_in_name_one: {words_in_name_one} \nwords_in_name_two: {words_in_name_two}")

    # We need to keep track of the matchups that return an initial in case there is another, more complete match
    score_warnings = []
    not_initial_nearly_perfect_scores = []

    # Score each matchup
    for i, word_one in enumerate(words_in_name_one):
        for j, word_two in enumerate(words_in_name_two):
            # Assign a very low finite score to dummy pairings
            scores[i, j] = -1e9 
            if (word_one is None) or (word_two is None) or (word_one == '') or (word_two == ''):
                continue
            # Determine the score of the word pairing
            score, warning = _determine_score_of_word_matchup(word_one, word_two)
            print(f"Python determined score of matchup for {word_one} and {word_two} for this run is {score} and that the warning value is {warning}")
            # Add the score
            if warning:
                score_warnings.append((i, j))
            elif score >= 95:
                not_initial_nearly_perfect_scores.append((i, j))
            scores[i, j] = score

    # Figure out which warnings will and won't be problematic and re-score them accordingly
    _handle_warning_checks(score_warnings, not_initial_nearly_perfect_scores, scores, words_in_name_one, words_in_name_two)

    # Identify the indices of the final words in each name
    final_words_in_name_one = _get_final_words_for_name(words_in_name_one)
    final_words_in_name_two = _get_final_words_for_name(words_in_name_two)

    # Identify the best matchups
    best_combinations = identify_best_matches(scores=scores, list_one=final_words_in_name_one, list_two=final_words_in_name_two)

    # For each of the best combinations, we now need to note how many are a combo containing a possible prefix
    for found_combination in best_combinations:
        print(f"Checking the combination {found_combination} for prefixes in Python")
        if ((words_in_name_one[int(found_combination[0])] in prefix_list) or (words_in_name_two[int(found_combination[1])] in prefix_list)) and (words_in_name_one[int(found_combination[0])] != words_in_name_two[int(found_combination[1])]):
            print(f"Determined that there was a possible prefix in the combination {found_combination} in Python")
            exception_count = exception_count + 1

    return best_combinations, exception_count

def _get_final_words_for_name(words_in_name: list) -> list[str | None]:
    """This is a helper function designed to determine the indices of the
    positions of words in a name so that the best matches of those words
    can be determined later on. Part of it's purpose is to filter out
    spaces with removed names, nicknames, prefixes, etc.
    
    Args:
        words_in_name: A list of the words in the name, including any removed
            items
            
    Returns:
        A list of indices (as a string data type) that show the location in the
        original name of the kept words
    """
    
    final_list_of_word_indices = []

    for index, word in enumerate(words_in_name):
        if word is not None and word != '':
            final_list_of_word_indices.append(str(index))
        else:
            final_list_of_word_indices.append('')

    return final_list_of_word_indices




def _handle_warning_checks(score_warnings: list, not_initial_nearly_perfect_scores: list, scores: ndarray, words_in_name_one: list, words_in_name_two: list) -> None:
    """This is a helper function designed to handle updating scores to be accurate
    even when a single letter is in the name, based on whether or not it thinks
    the single letter should be a strong match. It changes the score to reflect
    how likely that single letter is to match something perfectly.

    Args:
        score_warnings: A list of all of the scores that have a value matching
            with a single letter. We need to iterate through and update the
            scores to be more accurate on these
        not_initial_nearly_perfect_scores: All of the scores of 100 or higher
            that don't have an initial in the pairing 
        scores: An array of the scores for all of the possible word matchups
            between name one and name two
        words_in_name_one: A list of all the words in name one
        words_in_name_two: A list of all of the words in name two
    """
    # This ensures that in a name pair like ben l love and ben del love the two loves will
    # be a better match than l and love, which is also technically a 100 but less accurate
    # than 'love' and 'love'
    for warning_to_check in score_warnings:
        print(f"Performing warning check with the following variables in Python: warning_to_check - {warning_to_check} not_initial_nearly_perfect_scores - {not_initial_nearly_perfect_scores}")
        # If there's a perfect full name match, we want to penalize the score of the initial
        # since we want the other nearly perfect matches to take priority
        if (len(not_initial_nearly_perfect_scores) >= 1) and any(warning_to_check[0] == specific_score[0] for specific_score in not_initial_nearly_perfect_scores):
            print("Failed the first warning check segment in Python")
            scores[warning_to_check[0], warning_to_check[1]] = 0
        elif (len(not_initial_nearly_perfect_scores) >= 2) and any(warning_to_check[1] == specific_score[1] for specific_score in not_initial_nearly_perfect_scores):
            print("Failed the second warning check segment in Python")
            scores[warning_to_check[0], warning_to_check[1]] = 0
        # If both of those are fine, we can likely add this warning as a possible odd exception
        elif words_in_name_one[warning_to_check[0]][0] == words_in_name_two[warning_to_check[1]][0] and len(words_in_name_one[warning_to_check[0]]) == len(words_in_name_two[warning_to_check[1]]):
            scores[warning_to_check[0], warning_to_check[1]] = 100
        elif words_in_name_one[warning_to_check[0]][0] == words_in_name_two[warning_to_check[1]][0]:
            scores[warning_to_check[0], warning_to_check[1]] = 85

def _determine_score_of_word_matchup(word_one: str, word_two: str) -> tuple[int, bool]:
    """This is a helper function for find_word_matches_and_quality to fix its
    nesting depth. What it does is it takes in a word and an integer
    representation of a list position for two different words. Then it
    determines how closely the words match each other and assigns them a
    score according to that.
    
    Args:
        word_one: The first word used in the comparison and scoring
        word_two: The second word used in the comparison and scoring
    
    Returns:
        A tuple with an integer representing the score to be added to the 
        word pairing and a warning if the name was an initial
    """

    warning_flag = False
    word_one_lenth = len(word_one)
    word_two_length = len(word_two)

    # If either of the scores is empty, it should be fine to say it's a match
    # with the empty space
    if (word_one_lenth == 0) or (word_two_length == 0):
        score = 100

    # Assign the score this way if both are an initial
    elif (word_one_lenth == 1 and word_two_length == 1):
        if (word_one[0] == word_two[0]):
            score = 100
            warning_flag = True
        else:
            score = 0
            
    # Assign the score this way if only one is an initial
    elif (word_one_lenth == 1) or (word_two_length == 1):
        if (word_one[0] == word_two[0]):
            score_division_helper = max(word_one_lenth, word_two_length)
            score = round_in_a_normal_way(100 / score_division_helper)
            warning_flag = True
        else:
            score = 0

    # For words longer than 2, either use ratio or partial ratio for score as shown below
    else:
        ratio = round_in_a_normal_way(fuzz_ratio(word_one, word_two, processor=None))
        print(f"Found the ratio {ratio} for {word_one} and {word_two} in Python")
        if (word_one[0] == word_two[0]):
            partial_ratio_score = round_in_a_normal_way(partial_ratio_with_parity(word_one, word_two))
            print(f"Found the partial ratio {partial_ratio_score} for {word_one} and {word_two} in Python")
            score = round_in_a_normal_way((ratio + partial_ratio_score ) / 2)
        else:
            score = ratio

    print (f"Final score for the ratios of {word_one} and {word_two} in Python is {score}")

    return score, warning_flag

# This function is only used in a single location, for small lists. Specifically, it is only reached if
# the compare_two_names function is called in NameComparator. If this changes it might be worth changing 
# this function to use the scipy.optimize linear_sum_assignment again. I changed it to use the munkres 
# linear sum for now since it will be much faster to import and have comparable run times with its
# current use cases
def identify_best_matches(scores:ndarray, list_one:list[str|None], list_two:list[str|None]) -> list[tuple[str, str, float]]:
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
    print(f"Input lists for identify matches in Python: \nlist_one: {list_one} \nlist_two: {list_two}")
    modified_scores = tiebreak_matches_consistently(scores)
    print(f'Making sure that matches tiebreak as expected. Python tiebroken scores: \n{modified_scores}')
    linear_sum_class = MakeMunkresConsistentWithTypeScript()     
    print(f"Checking that negated scores look the same in Python: \n{-modified_scores}")
    hungarian_pairs_list = linear_sum_class.compute((-modified_scores).tolist())
    print(f"Hungarian pairs list in Python: \n{hungarian_pairs_list}")
    best_combinations = []
    for i, j in hungarian_pairs_list:
        # This first if statement quickly removes any possible out of scope results from the matrix padding
        if (int(i) >= len(list_one)) or (int(j) >= len(list_two)):
            continue
        elif (list_one[i] is not None) and (list_two[j] is not None) and (list_one[i] != '') and (list_two[j] != ''):
            # This rounding and typecasting to a float is needed to make it match the TypeScript output in tests
            matchup_score = float(round_in_a_normal_way(float(scores[i, j])))
            best_combinations.append((list_one[i], list_two[j], matchup_score))
        
    return best_combinations

def calculate_edit_improvement(name_one:str, name_two:str, name_one_edited:str, name_two_edited:str) -> tuple[float, list[tuple[str, str, float]], list[tuple[str, str, float]]]:
    """Calculates how much editing a name or both names improved the score in comparison to the original names,
    using their pronunciations as the guide.

    Args:
        name_one: the original first name
        name_two: the original second name
        name_one_edited: the edited first name
        name_two_edited: the edited second name

    Returns:
        A tuple containing the score of how much the edits improved the comparison (can be negative), 
        the word combos of the original, and the word combos of the edited verison
    """
    # First run a quick check on it to see how the spelling changes line up
    original_word_combos, possible_prefix_count = find_word_matches_and_quality(name_one, name_two)
    edited_word_combos, possible_edited_prefix_count = find_word_matches_and_quality(name_one_edited, name_two_edited)
    print(f"Word combos for calculating edit improvments in Python: original_word_combos - {original_word_combos} edited_word_combos - {edited_word_combos}")
    if (not original_word_combos) or (not edited_word_combos):
        return 0, original_word_combos, edited_word_combos
    original_average_score = sum(tup[2] for tup in original_word_combos) / len(original_word_combos)
    edited_average_score = sum(tup[2] for tup in edited_word_combos) / len(edited_word_combos)
    diff = edited_average_score - original_average_score

    print(f"Checkpoint for calculating edit improvements in Python: name_one - {name_one} name_two - {name_two} original_average_score - {original_average_score} name_one_edited - {name_one_edited} name_two_edited - {name_two_edited} edited_average_score - {edited_average_score} diff - {diff}")

    # This is used to help determine if a name is an improvement in terms of used sections
    original_name_one_segments = name_one.split()
    original_name_two_segments = name_two.split()
    original_name_unused_segments = max(len(original_name_one_segments), len(original_name_two_segments)) - len(original_word_combos)

    edited_name_one_segments = name_one_edited.split()
    edited_name_two_segments = name_two_edited.split()
    edited_name_unused_segments = max(len(edited_name_one_segments), len(edited_name_two_segments)) - len(edited_word_combos)

    how_many_less_segments_in_edit = original_name_unused_segments - edited_name_unused_segments

    # If the edit uses less name segments and the diff isn't *too* massive, we want to keep going instead of stopping here
    if diff < -33 and how_many_less_segments_in_edit < 1:
        return diff, original_word_combos, edited_word_combos

    # If it passes the first set, we want to make sure that it also works with the pronunciations
    name_one_ipa = get_ipa(name_one)
    name_two_ipa = get_ipa(name_two)
    original_word_combos, possible_prefix_count = find_word_matches_and_quality(name_one_ipa, name_two_ipa)
    name_one_edited_ipa = get_ipa(name_one_edited)
    name_two_edited_ipa = get_ipa(name_two_edited)
    edited_word_combos, possible_edited_prefix_count = find_word_matches_and_quality(name_one_edited_ipa, name_two_edited_ipa)
    if (not original_word_combos) or (not edited_word_combos):
        return 0, original_word_combos, edited_word_combos
    original_average_score = sum(tup[2] for tup in original_word_combos) / len(original_word_combos)
    edited_average_score = sum(tup[2] for tup in edited_word_combos) / len(edited_word_combos)
    diff = edited_average_score - original_average_score

    print(f"End result of calculating edit improvements in Python: name_one - {name_one} name_one_ipa - {name_one_ipa} name_two - {name_two} name_two_ipa - {name_two_ipa} original_average_score - {original_average_score} name_one_edited - {name_one_edited} name_one_edited_ipa - {name_one_edited_ipa} name_two_edited - {name_two_edited} name_two_edited_ipa - {name_two_edited_ipa} edited_average_score - {edited_average_score} diff - {diff}")
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
    combo, possible_prefix_count = find_word_matches_and_quality(name_one, name_two)
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
    
def partial_ratio_with_parity(string_one: str, string_two: str) -> int:
    """This is an implementation of the same partial ratio function that TypeScript
    uses since Python's rapidfuzz uses a custom one that is inconsistent with every 
    other package and we needed a custom one to fix that.
    
    Args:
        string_one: The first string to run a levenshtein partial ratio on
        string_two: The second string to run a levenshtein partial ratio on
    
    Returns:
        The best score from the results of comparing the two strings by segments
    """
    # We need to make sure that whatever is labelled as the first string is shorter
    if len(string_one) > len(string_two):
        string_one, string_two = string_two, string_one
    best_score = 0
    for i in range((len(string_two) - len(string_one)) + 1):
        window = string_two[i:i + len(string_one)]
        new_score = normalized_similarity(string_one, window) * 100
        print(f"New score in Python: {new_score}, when rounded it's: {round_in_a_normal_way(new_score)}")
        best_score = max(best_score, new_score)
    return round_in_a_normal_way(best_score)

def tiebreak_matches_consistently(input_matrix: ndarray, epsilon_value: float = 1e-4) -> ndarray:
    """ This adds small tiebreaker values to the end of matrices before calling
    a hungarian algorithm on them to ensure that we get the results we want
    and that Python and TypeScript versions behave the same.

    Args:
        input_matrix: The matrix that will have it's scores modified
        epsilon_value: The value by which to change the data in the
            matrix. Defaults to 1e-4.

    Returns:
        An updated matrix, changed to tiebreak matches the same way between
        NameComparator versions and languages
    """
    rows, columns = input_matrix.shape
    new_matrix = []
    for i in range(rows):
        new_row = []
        for j in range(columns):
            # This match bonus is also in the TypeScript but looks different due to language differences
            match_bonus = 0.005 if i == j else 0
            new_row.append(input_matrix[i][j] + (epsilon_value * ((columns - j) * rows + i)) + match_bonus)
        new_matrix.append(new_row)
        
    return numpy_array(new_matrix)

def round_in_a_normal_way(number_to_round: float) -> int:
    """ Python by defaults rounds numbers using an irregular algorithm that's
    better for datasets but bad for our application. We want to round in the way
    that most people are taught, so this function does that.

    Args:
        number_to_round: The number that we want to round in a normal fashion

    Returns:
        A number, rounded to the nearest integer
    """

    return math_floor(number_to_round + 0.5)

class MakeMunkresConsistentWithTypeScript(Munkres):
    """This is a class designed to override Munkres to have a behavior that's
    consistent with other packages that do similar things in TypeScript.
    
    Attributes:
        C - An n by n matrix that we want to find the cost of
        row_covered - Rows that have been used in the formula
        col_covered - Columns that have been used in the formula
        n - The length of the sides of the matrix (what is n in the n by n matrix)
        Z0_r - See the Munkres documentation for information on this
        Z0_c - See the Munkres documentation for information on this
        marked - See the Munkres documentation for information on this
        path - See the Munkres documentation for information on this
    """
    def __init__(self) -> None:
        """Create a new instance of Munkres with overrides that help it to be 
        consistent with the TypeScript version.
        """
        self.C = []
        self.row_covered = []
        self.col_covered = []
        self.n = 0
        self.Z0_r = 0
        self.Z0_c = 0
        self.marked = None
        self.path = None

    def _Munkres__find_a_zero(self, row_val: int, col_val: int) -> tuple[int, int]:
        """This is an override for the algorithm that the Python Munkres package
        uses to be slightly less optimal, but in a way that is standard to other
        packages and creates parity with the TypeScript version. It's only used 
        in the Munkres algorithms and should be ignored unless something is 
        *really* wrong. Note that this won't be called in our code since it's
        just an override.

        Args:
            row_val: The value of a column in which to search for a zero (unused)
            col_val: The value of the column in which to search for a zero (unused)

        Returns:
            This returns a tuple that contains the location of a zero in the
            munkres Matrix
        """
        for i in range(self.n):
            for j in range(self.n):
                if (self.C[i][j] == 0 and
                    not self.row_covered[i] and
                    not self.col_covered[j]):
                    return (i, j)
        return (-1, -1)
