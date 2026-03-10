import rawNicknameToIdData from "../data/nicknames/nicknameTold.json";
import rawIdToNicknameSetData from "../data/nicknames/name_variants.json";

/**
 * Replaces the nickname in one name for the official name found in the other.
 * 
 * @param nameA - a name
 * @param nameB - a name
 * @returns the modified names (possibly with a nickname replaced)
 */
export function removeNicknames(nameA: string, nameB: string): [string, string] {
    const nicknameToIdData: Record<string, number[]> = rawNicknameToIdData;
    const idToNicknameSetData: Record<number, string[]> = rawIdToNicknameSetData;
    const wordsInA = nameA.split(/\s+/);
    const wordsInB = nameB.split(/\s+/);
    
    for (const wordA of wordsInA) {
        if (wordsInB.includes(wordA)) {
            continue;
        }
        const setOfIds = nicknameToIdData[wordA.toLowerCase()];
        if (!setOfIds) {
            continue;
        }
        let breaking = false;
        for (const id of setOfIds) {
            const nicknames = [...idToNicknameSetData[id]];
            const filteredNicknames = nicknames.filter(n => n !== wordA);
            for (const nickname of filteredNicknames) {
                if (wordsInA.includes(nickname) && wordsInB.includes(nickname)) {
                    continue;
                }
                if (wordsInB.includes(nickname)) {
                    nameA = nameA.replace(new RegExp(`\\b${wordA}\\b`, 'i'), nickname);
                    breaking = true;
                    break;
                }
            }
            if (breaking) {
                break;
            }
        }
    }
    return [nameA, nameB];
}
