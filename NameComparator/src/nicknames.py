import re

import NameComparator.data.nicknames.idToNicknameSet as idToNicknameSet
import NameComparator.data.nicknames.nicknameToId as nicknameToId

def removeNicknames(nameA:str, nameB:str) -> tuple[str, str]:
    """Replaces the nickname in one name for the official name found in the other.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        tuple[str, str]: the names (possibly with a nickname replaced)
    """        
    wordsInA = nameA.split()
    wordsInB = nameB.split()
    for wordA in wordsInA:
        if wordA in wordsInB:
            continue
        setOfIds = nicknameToId.data.get(wordA)
        if setOfIds is None:
            continue
        breaking = False
        for id in setOfIds:
            nicknames = idToNicknameSet.data[id].copy()
            nicknames.remove(wordA)
            for nickname in nicknames:
                if (nickname in wordsInA) and (nickname in wordsInB):
                    continue
                if nickname in wordsInB:
                    nameA = re.sub(rf"\b{wordA}\b", nickname, nameA, flags=re.IGNORECASE)
                    breaking = True
                    break
            if breaking:
                break
    return nameA, nameB