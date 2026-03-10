import * as fuzzball from "fuzzball";

import { findWhichWordsMatchAndHowWell, getPairIndicesAndWords, NameEditor } from "./usefulTools"
import { data as spellingRules } from "../data/rules/rulesSpelling"
import { data as ipaRules } from "../data/rules/rulesIpa"

/** 
 * Modifies the name together (changing them in a way that is much more intense than simply cleaning together).
 * 
 * @param nameA - a name
 * @param nameB - a name
 * @returns the modified names
 */
export function modifyNamesTogether(nameA: string, nameB: string): [string, string] {
    nameA = nameA.replace(/ie\b/g, "y");
    nameB = nameB.replace(/ie\b/g, "y");
    [nameA, nameB] = _removeOrInNames(nameA, nameB);
    [nameA, nameB] = _fixVowelMistakes(nameA, nameB);
    [nameA, nameB] = _fixSwappedChars(nameA, nameB);
    [nameA, nameB] = _dealWithWrongFirstChar(nameA, nameB);
    for ( const [meatOption1, meatOption2, bottomBreads, topBreads, minLetters] of spellingRules) {
        [nameA, nameB] = _replaceSubstringSandwichMeatIfMatchingBread(nameA, nameB, meatOption1, meatOption2, bottomBreads, topBreads, minLetters);
    }
    nameA = nameA.replace(/\s+/g, " ");
    nameB = nameB.replace(/\s+/g, " ");
    nameA = nameA.trim();
    nameB = nameB.trim();
    return [nameA, nameB];
}

/**
 * Removes the word 'or' from a name (assuming that the name could have been 
 * poorly indexed so that the indexer's guesses for a specific word of the name is still within the string).
 * 
 * @param nameA - a name
 * @param nameB - a name
 * @returns the modified names
 */
function _removeOrInNames(nameA: string, nameB: string): [string, string] {
    if (!nameA || !nameB) {
        return [nameA, nameB];
    }
    nameA = nameA.trim();
    nameB = nameB.trim();
    nameA = nameA.toLowerCase();
    nameB = nameB.toLowerCase();

    // if or in neither
    if (!nameA.includes(" or ") && !nameB.includes(" or ")) {
        return [nameA, nameB];
    }

    // if or in both
    else if (nameA.includes(" or ") && nameB.includes(" or ")) {
        return [nameA, nameB];
    }

    // if or in nameA and not nameB
    else if (nameA.includes(" or ")) {
        // Gets the score for if the word before 'or' is removed
        let rightNameA = nameA.replace(/[a-z]+ or /g, " ");

        if (!rightNameA) {
            rightNameA = "_";
        }
        const rightWordCombo = findWhichWordsMatchAndHowWell(rightNameA, nameB);
        const rightAverageScore = rightWordCombo.reduce((sum: number, [nothing, nothing2, score]: [string, string, number]) => sum + score, 0) / rightWordCombo.length;
        
        // Gets the score for if the word after 'or' is removed
        let leftNameA = nameA.replace(/ or [a-z]+/g, "");

        if (!leftNameA) {
            leftNameA = "_";
        }
        const leftWordCombo = findWhichWordsMatchAndHowWell(leftNameA, nameB);
        const leftAverageScore = leftWordCombo.reduce((sum: number, [nothing, nothing2, score]: [string, string, number]) => sum + score, 0) / leftWordCombo.length;

        // Return the higher one
        if (rightAverageScore >= leftAverageScore) {
            return [rightNameA, nameB];
        }
        return [leftNameA, nameB];
    }

    // if or in nameB and not nameA
    else if (nameB.includes(" or ")) {
        // Gets the score for if the word before 'or' is removed
        let rightNameB =  nameB.replace(/[a-z]+ or /g, " ");

        if (!rightNameB) {
            rightNameB = "_";
        }
        const rightWordCombo = findWhichWordsMatchAndHowWell(rightNameB, nameA);
        const rightAverageScore = rightWordCombo.reduce((sum: number, [nothing, nothing2, score]: [string, string, number]) => sum + score, 0) / rightWordCombo.length;
        
        // Gets the score for if the word after 'or' is removed
        let leftNameB = nameB.replace(/ or [a-z]+/g, "");
        if (!leftNameB) {
            leftNameB = "_";
        }
        const leftWordCombo = findWhichWordsMatchAndHowWell(leftNameB, nameA);
        const leftAverageScore = leftWordCombo.reduce((sum: number, [nothing, nothing2, score]: [string, string, number]) => sum + score, 0) / leftWordCombo.length;
        
        // Return the higher one
        if (rightAverageScore >= leftAverageScore) {
            return [nameA, rightNameB];
        }
        return [nameA, leftNameB];
    }
    return [nameA, nameB];
}

/**
 * Modifies two matching words in a name so that they are the same if 
 * they are only different by one vowel and 5 letters or more.
 * 
 * @param nameA - a name
 * @param nameB - a name
 * @returns the modified names
 */
function _fixVowelMistakes(nameA: string, nameB: string): [string, string] {
    const ne = new NameEditor(nameA, nameB);
    for (const [indexA, _, wordA, wordB] of getPairIndicesAndWords(nameA, nameB)) {
        // Continue if either word is less than 5 chars or not same length
        const lenA = wordA.length;
        const lenB = wordB.length;
        if (lenA < 5 || lenB < 5 || lenA !== lenB) {
            continue;
        }

        // Check if there is only one difference
        let mismatchedIndex = null;
        let tooManyDiffs = false;
        for (let i = 0; i < lenA; i++) {
            if (wordA[i] === wordB[i]) {
                continue;
            }
            if (mismatchedIndex) {
                tooManyDiffs = true;
                break;
            }
            mismatchedIndex = i;
        }

        // Continue if there was not exactly one difference
        if (tooManyDiffs || mismatchedIndex === null) {
            continue;
        }

        // Replace one of the letters to be the other if they are cooresponding
        const charWordA = wordA[mismatchedIndex];
        const charWordB = wordB[mismatchedIndex];
        const cooresponding = ['ao', 'ea', 'iy'];
        if (cooresponding.includes(`${charWordA}${charWordB}`) || cooresponding.includes(`${charWordB}${charWordA}`)) {
            ne.updateNameA(indexA, wordB);
        }
    }
    // Return the modified (or not) names
    return ne.getModifiedNames();
}

/**
 * If two matching words (of 5 letters of more) for the two names are the same barring swapped letters (typo), makes the words the same.
 * 
 * @param nameA - a name
 * @param nameB - a name
 * @returns the modified names
 */
function _fixSwappedChars(nameA: string, nameB: string): [string, string] {
    const ne = new NameEditor(nameA, nameB);
    for (const [indexA, _, wordA, wordB] of getPairIndicesAndWords(nameA, nameB)) {
        // Skip if the words are not 5 long, are different length, or not fuzzy 80
        if (wordA.length !== 5 || wordA.length !== wordB.length || fuzzball.ratio(wordA, wordB) !== 80) {
            continue;
        }

        // Find how many differences and where
        let diffCount = 0;
        let diffPositions = [];
        for (let i = 0; i < wordA.length; i++) {
            if (wordA[i] !== wordB[i]) {
                diffCount += 1;
                diffPositions.push(i);
            }
        }

        // Skip if there are not two differences, differences are not sequential, or not swappable
        if (diffCount !== 2) {
            continue;
        }
        const posI = diffPositions[0];
        const posJ = diffPositions[1];
        if (Math.abs(posI - posJ) !== 1) {
            continue;
        }
        if (wordA[posI] !== wordB[posJ] || wordA[posJ] !== wordB[posI]) {
            continue;
        }

        // This is the scenerio we are looking for. Make the words identical
        ne.updateNameA(indexA, wordB);
    }
    // Return the modified (or not) names
    return ne.getModifiedNames();
}

/**
 * If two matching words (of 5 letters or more) are the same barring the first letter, makes the same.
 * 
 * @param nameA - a name
 * @param nameB - a name
 * @returns the modified names
 */
function _dealWithWrongFirstChar(nameA: string, nameB: string): [string, string] {
    const ne = new NameEditor(nameA, nameB);
    for (const [indexA, _, wordA, wordB] of getPairIndicesAndWords(nameA, nameB)) {
        if (wordA === wordB) {
            continue;
        }
        if (wordA.slice(1) === wordB.slice(1) && wordA.length > 4 && wordB.length > 4) {
            ne.updateNameA(indexA, wordB);
        }
    }
    return ne.getModifiedNames();
}

/**
 * For any given matching word pair, replaces a specific substring in one of the words, with a similar substring found in the other word.
 * 
 * @param nameA - a name
 * @param nameB - a name
 * @param meatOption1 - the first possible middle of the substring
 * @param meatOption2 - the second possible middle of the substring
 * @param bottomBreads - a list of possible beginnings to the substring. Whichever beginning is found in the one must be found in the other in order for the replacement to work
 * @param topBreads - a list of possible endings to the substring. Whichever ending is found in the one must be found in the other in order for the replacement to work
 * @param minRequiredLetters - the minimum required letters to be found in both words in order for the replacement to work
 * @returns the modified names
 */
function _replaceSubstringSandwichMeatIfMatchingBread(nameA: string, nameB: string, meatOption1: string, meatOption2: string, bottomBreads: string[], topBreads: string[], minRequiredLetters: number): [string, string] {
    // Return if both middles not in different words
    if ((!nameA.includes(meatOption1) && !nameA.includes(meatOption2)) || (!nameB.includes(meatOption1) && !nameB.includes(meatOption2))) {
        return [nameA, nameB];
    }

    const ne = new NameEditor(nameA, nameB);
    for (let [indexA, indexB, wordA, wordB] of getPairIndicesAndWords(nameA, nameB)) {
        // Skip words that are not long enough for the given rule
        if (wordA.length < minRequiredLetters || wordB.length < minRequiredLetters) {
            continue;
        }
        
        // Add clear word breaks
        wordA = `-${wordA}-`;
        wordB = `-${wordB}-`;

        for (const bottomBread of bottomBreads) {
            if (!wordA.includes(bottomBread) || !wordB.includes(bottomBread)) {
                continue;
            }

            for (const topBread of topBreads) {
                if (!wordA.includes(topBread) || !wordB.includes(topBread)) {
                    continue;
                }

                const pattern = new RegExp(`${bottomBread}(${meatOption1}|${meatOption2})${topBread}`);
                const resultsA = pattern.exec(wordA);
                const resultsB = pattern.exec(wordB);

                if (!resultsA || !resultsB) continue;

                if (resultsA[0] === resultsB[0]) continue;

                const spanA1 = resultsA.index;
                const spanB1 = spanA1 + resultsA[0].length;
                const spanA2 = resultsB.index;
                const spanB2 = spanA2 + resultsB[0].length;
                if (Math.abs(spanA1 - spanA2) > 2 || Math.abs(spanB1 - spanB2) > 2) {
                    continue;
                }
                
                // Update the words by replacing matching (different) middles with the meat option 2
                const [startIndexStringA, endIndexStringA] = [spanA1, spanB1];
                const [startIndexStringB, endIndexStringB] = [spanA2, spanB2];
                const middleCoordsStringA = [startIndexStringA + bottomBread.length, endIndexStringA - topBread.length];
                const middleCoordsStringB = [startIndexStringB + bottomBread.length, endIndexStringB - topBread.length];
                wordA = _overwriteWithSubstring(wordA, meatOption2, middleCoordsStringA[0], middleCoordsStringA[1])
                wordB = _overwriteWithSubstring(wordB, meatOption2, middleCoordsStringB[0], middleCoordsStringB[1])
            }
        }

        // Update the words for that match (though a change may not have occured)
        wordA = wordA.replace(/-/g, "");
        wordB = wordB.replace(/-/g, "");

        ne.updateNameA(indexA, wordA);
        ne.updateNameB(indexB, wordB);
    }
    
    // concatonates the two lists together back into strings
    [nameA, nameB] = ne.getModifiedNames();
    return [nameA, nameB];
}

/**
 * Overwrites a specific index range of a string with the replacement string.
 * 
 * @param string - the string to replace
 * @param replacement - the replacement string
 * @param startIndex - the start index for the replacement
 * @param endIndex - the end index for the replacement
 * @returns the modified string
 */
function _overwriteWithSubstring(string: string, replacement: string, startIndex: number, endIndex: number): string {
    return string.slice(0, startIndex) + replacement + string.slice(endIndex);
}

/**
 * Modifies two ipas by comparing each to one another.
 * 
 * @param ipaA - a name
 * @param ipaB - a name
 * @returns the modified names
 */
export function modifyIpasTogether(ipaA: string, ipaB: string): [string, string] {
    for (const [meatOption1, meatOption2, bottomBreads, topBreads, minLetters] of ipaRules) {
        [ipaA, ipaB] = _replaceSubstringSandwichMeatIfMatchingBread(ipaA, ipaB, meatOption1, meatOption2, bottomBreads, topBreads, minLetters);
    }
    return [ipaA, ipaB];
}