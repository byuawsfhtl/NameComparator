import { findWordMatchesAndQuality } from "./usefulTools.js";

/**
 * Identifies if a name comparison will always prove false.
 * 
 * @param nameOne - The first name used in a comparison
 * @param nameTwo - The second name used in a comparison
 * @returns Whether the names are worth working on further
 */
export function isWorthContinuing(nameOne: string, nameTwo: string): boolean {
    const [wordCombos, possiblePrefixCount] = findWordMatchesAndQuality(nameOne, nameTwo);
    let oneLetterMatchFailCount = 0;
    const nameOneAsList = nameOne.trim().split(/\s+/);
    const nameTwoAsList = nameTwo.trim().split(/\s+/);
    for (const match of wordCombos) {
        const wordOne = nameOneAsList[parseInt(match[0])];
        const wordTwo = nameTwoAsList[parseInt(match[1])];
        const score = match[2];
        if (score === 0 && ((wordOne.length === 1) || (wordTwo.length === 1))) {
            oneLetterMatchFailCount += 1;
        }
    }
    if (oneLetterMatchFailCount >= 1 && wordCombos.length <= 3) {
        return false;
    }
    return true;    
}

/**
 * Identifies if either of the names is too short.
 * 
 * @param nameOne - The first name to check the length of
 * @param nameTwo - The second name to check the length of
 * @returns If either name was too short
 */
export function eitherNameTooShort(nameOne: string, nameTwo: string): boolean {
    const [combo, possiblePrefixCount] = findWordMatchesAndQuality(nameOne, nameTwo);
    const shortestWordCount = combo.length;
    return shortestWordCount < 2;
}