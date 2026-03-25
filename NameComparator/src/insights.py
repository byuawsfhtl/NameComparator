from NameComparator.src.usefulTools import find_word_matches_and_quality

def is_worth_continuing(name_one:str, name_two:str) -> bool:
    """Identifies if a name comparison will always prove false.

    Args:
        name_one: The first name used in a comparison
        name_two: The second name used in a comparison

    Returns:
        A boolean representing whether the names are worth working on further
    """        
    word_combos = find_word_matches_and_quality(name_one, name_two)
    one_letter_match_fail_count = 0
    for match in word_combos:
        word_one = name_one[int(match[0])]
        word_two = name_two[int(match[1])]
        score = match[2]
        if (score == 0) and ((len(word_one) == 1) or ((len(word_two) == 1))):
            one_letter_match_fail_count += 1
    if (one_letter_match_fail_count >= 1) and (len(word_combos) <= 3):
        return False
    return True

def either_name_too_short(name_one:str, name_two:str) -> bool:
    """Identifies if either of the names is too short.

    Args:
        name_one: The first name to check the length of
        name_two: The second name to check the length of

    Returns:
        A boolean representing if either name was too short
    """        
    combo = find_word_matches_and_quality(name_one, name_two)
    shortest_word_count = len(combo)
    return shortest_word_count < 2
