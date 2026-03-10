import { findWordMatchesAndQuality } from "./usefulTools";

/**
 * Identifies if a name comparison will always prove false.
 * 
 * @param nameOne - a name
 * @param nameTwo - a name
 * @returns whether the names are worth working on further
 */
export function isWorthContinuing(nameOne: string, nameTwo: string): boolean {
    const wordCombo = findWordMatchesAndQuality(nameOne, nameTwo);
    let oneLetterMatchFailCount = 0;
    for (const match of wordCombo) {
        const wordOne = nameOne[parseInt(match[0])];
        const wordTwo = nameTwo[parseInt(match[1])];
        const score = match[2];
        if (score === 0 && ((wordOne.length === 1) || (wordTwo.length === 1))) {
            oneLetterMatchFailCount += 1;
        }
    }
    if (oneLetterMatchFailCount >= 1 && wordCombo.length <= 3) {
        return false;
    }
    return true;    
}

/**
 * Identifies if either of the names is too short.
 * 
 * @param nameOne - a name
 * @param nameTwo - a name
 * @returns whether either was too short
 */
export function eitherNameTooShort(nameOne: string, nameTwo: string): boolean {
    const combo = findWordMatchesAndQuality(nameOne, nameTwo);
    const shortestWordCount = combo.length;
    return shortestWordCount < 2;
}