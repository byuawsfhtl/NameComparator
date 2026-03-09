import NameComparator.src.usefulTools as usefulToolsMod

def is_worth_continuing(name_one:str, name_two:str) -> bool:
    """Identifies if a name comparison will always prove false.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        bool: whether the names are worth working on further
    """        
    word_combo = usefulToolsMod.find_word_matches_and_quality(name_one, name_two)
    one_letter_match_fail_count = 0
    for match in word_combo:
        word_one = name_one[int(match[0])]
        word_two = name_two[int(match[1])]
        score = match[2]
        if (score == 0) and ((len(word_one) == 1) or ((len(word_two) == 1))):
            one_letter_match_fail_count += 1
    if (one_letter_match_fail_count >= 1) and (len(word_combo) <= 3):
        return False
    return True

def either_name_too_short(name_one:str, name_two:str) -> bool:
    """Identifies if either of the names is too short.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        bool: whether either was too short
    """        
    combo = usefulToolsMod.find_word_matches_and_quality(name_one, name_two)
    shortest_word_count = len(combo)
    if shortest_word_count < 2:
        return True
    return False
