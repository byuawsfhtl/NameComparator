import fs from 'fs';
import path from 'path';

// This is required to make sure that it reads in the characters correctly
const nicknameToIdData = JSON.parse(
    fs.readFileSync(path.resolve(__dirname, '../../data/nicknames/nicknameToId.json'), 'utf-8')
) as Record<string, number[]>;

const idToNicknameSetData = JSON.parse(
    fs.readFileSync(path.resolve(__dirname, '../../data/nicknames/nameVariants.json'), 'utf-8')
) as Record<number, string[]>;

/**
 * Replaces the nickname in one name for the official name found in the other
 * if any nicknames are found.
 * 
 * @param nameOne - The first name to look through for nicknames
 * @param nameTwo - The second name to look through for nicknames
 * @returns The names, possibly modified with a nickname replaced
 */
export function removeNicknames(nameOne: string, nameTwo: string): [string, string] {

    const nicknameToIdDataAsRecord: Record<string, number[]> = nicknameToIdData;
    const wordsInNameOne = nameOne.trim().split(/\s+/);
    const wordsInNameTwo = nameTwo.trim().split(/\s+/);
    
    for (const wordOne of wordsInNameOne) {
        if (wordsInNameTwo.includes(wordOne)) {
            continue;
        };
        const setOfIds = nicknameToIdDataAsRecord[wordOne.toLowerCase()];
        if (!setOfIds) {
            continue;
        };
        nameOne = _removeBasedOnIdInformation(setOfIds, wordOne, nameOne, wordsInNameOne, wordsInNameTwo);
    };
    return [nameOne, nameTwo];
};

function _removeBasedOnIdInformation(setOfIds: number[], wordOne: string, nameOne: string, wordsInNameOne: string[], wordsInNameTwo: string[]): string {

    const idToNicknameSetDataAsRecord: Record<number, string[]> = idToNicknameSetData;
    let breaking = false;

    for (const id of setOfIds) {
        const nicknames = [...idToNicknameSetDataAsRecord[id]];
        const filteredNicknames = nicknames.filter(n => n !== wordOne);
        for (const nickname of filteredNicknames) {
            if (wordsInNameOne.includes(nickname) && wordsInNameTwo.includes(nickname)) {
                continue;
            };
            if (wordsInNameTwo.includes(nickname)) {
                nameOne = nameOne.replace(new RegExp(`\\b${wordOne}\\b`, 'i'), nickname);
                breaking = true;
                break;
            };
        };
        if (breaking) {
            break;
        };
    };

    return nameOne;
};
