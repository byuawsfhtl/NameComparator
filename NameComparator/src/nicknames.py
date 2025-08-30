import re

import NameComparator.data.nicknames.idToNicknameSet as id_to_nickname_set
import NameComparator.data.nicknames.nicknameToId as nickname_to_id

def remove_nicknames(name_a : str, name_b : str) -> tuple[str, str]:
    """Replaces the nickname in one name for the official name found in the other.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        the names (possibly with a nickname replaced)
    """        
    words_in_a = name_a.split()
    words_in_b = name_b.split()
    for word_a in words_in_a:
        if word_a in words_in_b:
            continue
        sets_of_ids = nickname_to_id.data.get(word_a)
        if sets_of_ids is None:
            continue
        breaking = False
        for id in sets_of_ids:
            nickname_pool = id_to_nickname_set.data[id].copy()
            nickname_pool.remove(word_a)
            for nickname in nickname_pool:
                if (nickname in words_in_a) and (nickname in words_in_b):
                    continue
                if nickname in words_in_b:
                    name_a = re.sub(rf"\b{word_a}\b", nickname, name_a, flags=re.IGNORECASE)
                    breaking = True
                    break
            if breaking:
                break
    return name_a, name_b