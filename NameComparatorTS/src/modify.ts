import * as fuzzball from "fuzzball";

import { findWhichWordsMatchAndHowWell, getMatchingWordsAndIndices, NameEditor } from "./usefulTools"
import { data as spellingRules } from "../data/rules/rulesSpelling"
import { data as ipaRules } from "../data/rules/rulesIpa"

/** 
 * Modifies the name together (changing them in a way that is much more intense than simply cleaning together).
 * 
 * @param nameOne - a name
 * @param nameTwo - a name
 * @returns the modified names
 */
export function modifyNamesTogether(nameOne: string, nameTwo: string): [string, string] {
    nameOne = nameOne.replace(/ie\b/g, "y");
    nameTwo = nameTwo.replace(/ie\b/g, "y");
    [nameOne, nameTwo] = _removeOrInNames(nameOne, nameTwo);
    [nameOne, nameTwo] = _fixVowelMistakes(nameOne, nameTwo);
    [nameOne, nameTwo] = _fixSwappedChars(nameOne, nameTwo);
    [nameOne, nameTwo] = _dealWithWrongFirstChar(nameOne, nameTwo);
    for ( const [meatOption1, meatOption2, bottomBreads, topBreads, minLetters] of spellingRules) {
        [nameOne, nameTwo] = _replaceSubstringSandwichMeatIfMatchingBread(nameOne, nameTwo, meatOption1, meatOption2, bottomBreads, topBreads, minLetters);
    }
    nameOne = nameOne.replace(/\s+/g, " ");
    nameTwo = nameTwo.replace(/\s+/g, " ");
    nameOne = nameOne.trim();
    nameTwo = nameTwo.trim();
    return [nameOne, nameTwo];
}

/**
 * Removes the word 'or' from a name (assuming that the name could have been 
 * poorly indexed so that the indexer's guesses for a specific word of the name is still within the string).
 * 
 * @param nameOne - a name
 * @param nameTwo - a name
 * @returns the modified names
 */
function _removeOrInNames(nameOne: string, nameTwo: string): [string, string] {
    if (!nameOne || !nameTwo) {
        return [nameOne, nameTwo];
    }
    nameOne = nameOne.trim();
    nameTwo = nameTwo.trim();
    nameOne = nameOne.toLowerCase();
    nameTwo = nameTwo.toLowerCase();

    // if or in neither
    if (!nameOne.includes(" or ") && !nameTwo.includes(" or ")) {
        return [nameOne, nameTwo];
    }

    // if or in both
    else if (nameOne.includes(" or ") && nameTwo.includes(" or ")) {
        return [nameOne, nameTwo];
    }

    // if or in nameOne and not nameTwo
    else if (nameOne.includes(" or ")) {
        // Gets the score for if the word before 'or' is removed
        let rightnameOne = nameOne.replace(/[a-z]+ or /g, " ");

        if (!rightnameOne) {
            rightnameOne = "_";
        }
        const rightWordCombo = findWhichWordsMatchAndHowWell(rightnameOne, nameTwo);
        const rightAverageScore = rightWordCombo.reduce((sum: number, [nothing, nothing2, score]: [string, string, number]) => sum + score, 0) / rightWordCombo.length;
        
        // Gets the score for if the word after 'or' is removed
        let leftnameOne = nameOne.replace(/ or [a-z]+/g, "");

        if (!leftnameOne) {
            leftnameOne = "_";
        }
        const leftWordCombo = findWhichWordsMatchAndHowWell(leftnameOne, nameTwo);
        const leftAverageScore = leftWordCombo.reduce((sum: number, [nothing, nothing2, score]: [string, string, number]) => sum + score, 0) / leftWordCombo.length;

        // Return the higher one
        if (rightAverageScore >= leftAverageScore) {
            return [rightnameOne, nameTwo];
        }
        return [leftnameOne, nameTwo];
    }

    // if or in nameTwo and not nameOne
    else if (nameTwo.includes(" or ")) {
        // Gets the score for if the word before 'or' is removed
        let rightnameTwo =  nameTwo.replace(/[a-z]+ or /g, " ");

        if (!rightnameTwo) {
            rightnameTwo = "_";
        }
        const rightWordCombo = findWhichWordsMatchAndHowWell(rightnameTwo, nameOne);
        const rightAverageScore = rightWordCombo.reduce((sum: number, [nothing, nothing2, score]: [string, string, number]) => sum + score, 0) / rightWordCombo.length;
        
        // Gets the score for if the word after 'or' is removed
        let leftnameTwo = nameTwo.replace(/ or [a-z]+/g, "");
        if (!leftnameTwo) {
            leftnameTwo = "_";
        }
        const leftWordCombo = findWhichWordsMatchAndHowWell(leftnameTwo, nameOne);
        const leftAverageScore = leftWordCombo.reduce((sum: number, [nothing, nothing2, score]: [string, string, number]) => sum + score, 0) / leftWordCombo.length;
        
        // Return the higher one
        if (rightAverageScore >= leftAverageScore) {
            return [nameOne, rightnameTwo];
        }
        return [nameOne, leftnameTwo];
    }
    return [nameOne, nameTwo];
}

/**
 * Modifies two matching words in a name so that they are the same if 
 * they are only different by one vowel and 5 letters or more.
 * 
 * @param nameOne - a name
 * @param nameTwo - a name
 * @returns the modified names
 */
function _fixVowelMistakes(nameOne: string, nameTwo: string): [string, string] {
    const ne = new NameEditor(nameOne, nameTwo);
    for (const [indexA, _, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        // Continue if either word is less than 5 chars or not same length
        const lenA = wordOne.length;
        const lenB = wordTwo.length;
        if (lenA < 5 || lenB < 5 || lenA !== lenB) {
            continue;
        }

        // Check if there is only one difference
        let mismatchedIndex = null;
        let tooManyDiffs = false;
        for (let i = 0; i < lenA; i++) {
            if (wordOne[i] === wordTwo[i]) {
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
        const charwordOne = wordOne[mismatchedIndex];
        const charwordTwo = wordTwo[mismatchedIndex];
        const cooresponding = ['ao', 'ea', 'iy'];
        if (cooresponding.includes(`${charwordOne}${charwordTwo}`) || cooresponding.includes(`${charwordTwo}${charwordOne}`)) {
            ne.updateNameOne(indexA, wordTwo);
        }
    }
    // Return the modified (or not) names
    return ne.getModifiedNames();
}

/**
 * If two matching words (of 5 letters of more) for the two names are the same barring swapped letters (typo), makes the words the same.
 * 
 * @param nameOne - a name
 * @param nameTwo - a name
 * @returns the modified names
 */
function _fixSwappedChars(nameOne: string, nameTwo: string): [string, string] {
    const ne = new NameEditor(nameOne, nameTwo);
    for (const [indexA, _, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        // Skip if the words are not 5 long, are different length, or not fuzzy 80
        if (wordOne.length !== 5 || wordOne.length !== wordTwo.length || fuzzball.ratio(wordOne, wordTwo) !== 80) {
            continue;
        }

        // Find how many differences and where
        let diffCount = 0;
        let diffPositions = [];
        for (let i = 0; i < wordOne.length; i++) {
            if (wordOne[i] !== wordTwo[i]) {
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
        if (wordOne[posI] !== wordTwo[posJ] || wordOne[posJ] !== wordTwo[posI]) {
            continue;
        }

        // This is the scenerio we are looking for. Make the words identical
        ne.updateNameOne(indexA, wordTwo);
    }
    // Return the modified (or not) names
    return ne.getModifiedNames();
}

/**
 * If two matching words (of 5 letters or more) are the same barring the first letter, makes the same.
 * 
 * @param nameOne - a name
 * @param nameTwo - a name
 * @returns the modified names
 */
function _dealWithWrongFirstChar(nameOne: string, nameTwo: string): [string, string] {
    const ne = new NameEditor(nameOne, nameTwo);
    for (const [indexA, _, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        if (wordOne === wordTwo) {
            continue;
        }
        if (wordOne.slice(1) === wordTwo.slice(1) && wordOne.length > 4 && wordTwo.length > 4) {
            ne.updateNameOne(indexA, wordTwo);
        }
    }
    return ne.getModifiedNames();
}

/**
 * For any given matching word pair, replaces a specific substring in one of the words, with a similar substring found in the other word.
 * 
 * @param nameOne - a name
 * @param nameTwo - a name
 * @param meatOption1 - the first possible middle of the substring
 * @param meatOption2 - the second possible middle of the substring
 * @param bottomBreads - a list of possible beginnings to the substring. Whichever beginning is found in the one must be found in the other in order for the replacement to work
 * @param topBreads - a list of possible endings to the substring. Whichever ending is found in the one must be found in the other in order for the replacement to work
 * @param minRequiredLetters - the minimum required letters to be found in both words in order for the replacement to work
 * @returns the modified names
 */
function _replaceSubstringSandwichMeatIfMatchingBread(nameOne: string, nameTwo: string, meatOption1: string, meatOption2: string, bottomBreads: string[], topBreads: string[], minRequiredLetters: number): [string, string] {
    // Return if both middles not in different words
    if ((!nameOne.includes(meatOption1) && !nameOne.includes(meatOption2)) || (!nameTwo.includes(meatOption1) && !nameTwo.includes(meatOption2))) {
        return [nameOne, nameTwo];
    }

    const ne = new NameEditor(nameOne, nameTwo);
    for (let [indexA, indexB, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        // Skip words that are not long enough for the given rule
        if (wordOne.length < minRequiredLetters || wordTwo.length < minRequiredLetters) {
            continue;
        }
        
        // Add clear word breaks
        wordOne = `-${wordOne}-`;
        wordTwo = `-${wordTwo}-`;

        for (const bottomBread of bottomBreads) {
            if (!wordOne.includes(bottomBread) || !wordTwo.includes(bottomBread)) {
                continue;
            }

            for (const topBread of topBreads) {
                if (!wordOne.includes(topBread) || !wordTwo.includes(topBread)) {
                    continue;
                }

                const pattern = new RegExp(`${bottomBread}(${meatOption1}|${meatOption2})${topBread}`);
                const resultsA = pattern.exec(wordOne);
                const resultsB = pattern.exec(wordTwo);

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
                wordOne = _overwriteWithSubstring(wordOne, meatOption2, middleCoordsStringA[0], middleCoordsStringA[1])
                wordTwo = _overwriteWithSubstring(wordTwo, meatOption2, middleCoordsStringB[0], middleCoordsStringB[1])
            }
        }

        // Update the words for that match (though a change may not have occured)
        wordOne = wordOne.replace(/-/g, "");
        wordTwo = wordTwo.replace(/-/g, "");

        ne.updateNameOne(indexA, wordOne);
        ne.updateNameTwo(indexB, wordTwo);
    }
    
    // concatonates the two lists together back into strings
    [nameOne, nameTwo] = ne.getModifiedNames();
    return [nameOne, nameTwo];
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