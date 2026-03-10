import { findWhichWordsMatchAndHowWell } from "./usefulTools";

/**
 * Identifies if a name comparison will always prove false.
 * 
 * @param nameA - a name
 * @param nameB - a name
 * @returns whether the names are worth working on further
 */
export function isWorthContinuing(nameA: string, nameB: string): boolean {
    const wordCombo = findWhichWordsMatchAndHowWell(nameA, nameB);
    let oneLetterMatchFailCount = 0;
    for (const match of wordCombo) {
        const wordA = nameA[parseInt(match[0])];
        const wordB = nameB[parseInt(match[1])];
        const score = match[2];
        if (score === 0 && ((wordA.length === 1) || (wordB.length === 1))) {
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
 * @param nameA - a name
 * @param nameB - a name
 * @returns whether either was too short
 */
export function eitherNameTooShort(nameA: string, nameB: string): boolean {
    const combo = findWhichWordsMatchAndHowWell(nameA, nameB);
    const shortestWordCount = combo.length;
    return shortestWordCount < 2;
}