import re

import NameComparator.data.nicknames.idToNicknameSet as idToNicknameSet
import NameComparator.data.nicknames.nicknameToId as nicknameToId

def remove_nicknames(name_one:str, name_two:str) -> tuple[str, str]:
    """Replaces the nickname in one name for the official name found in the other.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the names (possibly with a nickname replaced)
    """        
    words_in_name_one = name_one.split()
    words_in_name_two = name_two.split()
    for word_one in words_in_name_one:
        if word_one in words_in_name_two:
            continue
        set_of_ids = nicknameToId.data.get(word_one)
        if set_of_ids is None:
            continue
        name_one = _remove_based_on_id_information(set_of_ids, word_one, name_one, words_in_name_one, words_in_name_two)

    return name_one, name_two

def _remove_based_on_id_information(set_of_ids, word_one, name_one, words_in_name_one, words_in_name_two):
    """This is a helper function for remove_nicknames that fixes it's nesting depth
    for the python standard checks. Tbh, I'm not entirely sure what this is doing but
    if you were to cut the code from this and paste it over the call to it inside of
    remove_nicknames, it will all work exactly as intended.
    
    Args:
        set_of_ids: A set of different ids corresponding to nicknames for word_one
        word_one: The word to check for nicknames
        name_one: The name that word_one came from, which will need to be modified
            at the end of the function
        words_in_name_one: A list of all of the words inside of name_one
        words_in_name_two: A list of all of the words inside of name_two, which is
            what word_one and name_one are being compared against in remove_nicknames
        
    Returns:
        A modified version of name_one with nicknames that are removed    
    """
    
    breaking = False
    for id in set_of_ids:
        nicknames = idToNicknameSet.data[id].copy()
        nicknames.remove(word_one)
        for nickname in nicknames:
            if (nickname in words_in_name_one) and (nickname in words_in_name_two):
                continue
            if nickname in words_in_name_two:
                name_one = re.sub(rf"\b{word_one}\b", nickname, name_one, flags=re.IGNORECASE)
                breaking = True
                break
        if breaking:
            break

    return name_one