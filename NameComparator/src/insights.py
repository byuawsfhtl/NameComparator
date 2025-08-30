import NameComparator.src.usefulTools as usefulToolsMod

def is_worth_continuing(name_a : str, name_b : str) -> bool:
    """Identifies if a name comparison will always prove false.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        bool: whether the names are worth working on further
    """        
    word_combo = usefulToolsMod.find_which_words_match_and_how_well(name_a, name_b)
    one_letter_match_fail_count = 0
    for match in word_combo:
        word_a = name_a[int(match[0])]
        word_b = name_b[int(match[1])]
        score = match[2]
        if (score == 0) and ((len(word_a) == 1) or ((len(word_b) == 1))):
            one_letter_match_fail_count += 1
    if (one_letter_match_fail_count >= 1) and (len(word_combo) <= 3):
        return False
    return True

def either_name_too_short(name_a : str, name_b : str) -> bool:
    """Identifies if either of the names is too short.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        bool: whether either was too short
    """        
    combo = usefulToolsMod.find_which_words_match_and_how_well(name_a, name_b)
    shortest_word_count = len(combo)
    if shortest_word_count < 2:
        return True
    return False
