import re

import NameComparator.data.nicknames.idToNicknameSet as idToNicknameSet
import NameComparator.data.nicknames.nicknameToId as nicknameToId

def removeNicknames(name_one:str, name_two:str) -> tuple[str, str]:
    """Replaces the nickname in one name for the official name found in the other.

    Args:
        name_one (str): a name
        name_two (str): a name

    Returns:
        tuple[str, str]: the names (possibly with a nickname replaced)
    """        
    wordsInA = name_one.split()
    wordsInB = name_two.split()
    for word_one in wordsInA:
        if word_one in wordsInB:
            continue
        setOfIds = nicknameToId.data.get(word_one)
        if setOfIds is None:
            continue
        breaking = False
        for id in setOfIds:
            nicknames = idToNicknameSet.data[id].copy()
            nicknames.remove(word_one)
            for nickname in nicknames:
                if (nickname in wordsInA) and (nickname in wordsInB):
                    continue
                if nickname in wordsInB:
                    name_one = re.sub(rf"\b{word_one}\b", nickname, name_one, flags=re.IGNORECASE)
                    breaking = True
                    break
            if breaking:
                break
    return name_one, name_two