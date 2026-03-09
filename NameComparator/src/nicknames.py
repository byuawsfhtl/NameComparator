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
    return name_one, name_two