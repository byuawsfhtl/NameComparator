import rawNicknameToIdData from "../data/nicknames/nicknameTold.json";
import rawIdToNicknameSetData from "../data/nicknames/name_variants.json";

/**
 * Replaces the nickname in one name for the official name found in the other.
 * 
 * @param nameOne - a name
 * @param nameTwo - a name
 * @returns the modified names (possibly with a nickname replaced)
 */
export function removeNicknames(nameOne: string, nameTwo: string): [string, string] {
    const nicknameToIdData: Record<string, number[]> = rawNicknameToIdData;
    const idToNicknameSetData: Record<number, string[]> = rawIdToNicknameSetData;
    const wordsInA = nameOne.split(/\s+/);
    const wordsInB = nameTwo.split(/\s+/);
    
    for (const wordOne of wordsInA) {
        if (wordsInB.includes(wordOne)) {
            continue;
        }
        const setOfIds = nicknameToIdData[wordOne.toLowerCase()];
        if (!setOfIds) {
            continue;
        }
        let breaking = false;
        for (const id of setOfIds) {
            const nicknames = [...idToNicknameSetData[id]];
            const filteredNicknames = nicknames.filter(n => n !== wordOne);
            for (const nickname of filteredNicknames) {
                if (wordsInA.includes(nickname) && wordsInB.includes(nickname)) {
                    continue;
                }
                if (wordsInB.includes(nickname)) {
                    nameOne = nameOne.replace(new RegExp(`\\b${wordOne}\\b`, 'i'), nickname);
                    breaking = true;
                    break;
                }
            }
            if (breaking) {
                break;
            }
        }
    }
    return [nameOne, nameTwo];
}
