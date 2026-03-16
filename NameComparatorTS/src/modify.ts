import * as fuzzball from "fuzzball";

import { findWordMatchesAndQuality, getMatchingWordsAndIndices, NameEditor } from "./usefulTools"
import { data as spellingRules } from "../../data/rules/rulesSpelling"
import { data as ipaRules } from "../../data/rules/rulesIpa"

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
    [nameOne, nameTwo] = _removeWordOrFromNames(nameOne, nameTwo);
    [nameOne, nameTwo] = _fixVowelMistakes(nameOne, nameTwo);
    [nameOne, nameTwo] = _fixSwappedCharacters(nameOne, nameTwo);
    [nameOne, nameTwo] = _dealWithWrongFirstChar(nameOne, nameTwo);
    for ( const [middleSubstringOptionOne, middleSubstringOptionTwo, substringBeginnings, substringEndings, minimumLetters] of spellingRules) {
        [nameOne, nameTwo] = _replaceSubstringCentersIfNamesAreSimilar(nameOne, nameTwo, middleSubstringOptionOne, middleSubstringOptionTwo, substringBeginnings, substringEndings, minimumLetters);
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
function _removeWordOrFromNames(nameOne: string, nameTwo: string): [string, string] {
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
        let rightNameOne = nameOne.replace(/[a-z]+ or /g, " ");

        if (!rightNameOne) {
            rightNameOne = "_";
        }
        const rightWordCombo = findWordMatchesAndQuality(rightNameOne, nameTwo);
        const rightAverageScore = rightWordCombo.reduce((sum: number, [nothing, nothing2, score]: [string, string, number]) => sum + score, 0) / rightWordCombo.length;
        
        // Gets the score for if the word after 'or' is removed
        let leftnameOne = nameOne.replace(/ or [a-z]+/g, "");

        if (!leftnameOne) {
            leftnameOne = "_";
        }
        const leftWordCombo = findWordMatchesAndQuality(leftnameOne, nameTwo);
        const leftAverageScore = leftWordCombo.reduce((sum: number, [nothing, nothing2, score]: [string, string, number]) => sum + score, 0) / leftWordCombo.length;

        // Return the higher one
        if (rightAverageScore >= leftAverageScore) {
            return [rightNameOne, nameTwo];
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
        const rightWordCombo = findWordMatchesAndQuality(rightnameTwo, nameOne);
        const rightAverageScore = rightWordCombo.reduce((sum: number, [nothing, nothing2, score]: [string, string, number]) => sum + score, 0) / rightWordCombo.length;
        
        // Gets the score for if the word after 'or' is removed
        let leftNameTwo = nameTwo.replace(/ or [a-z]+/g, "");
        if (!leftNameTwo) {
            leftNameTwo = "_";
        }
        const leftWordCombo = findWordMatchesAndQuality(leftNameTwo, nameOne);
        const leftAverageScore = leftWordCombo.reduce((sum: number, [nothing, nothing2, score]: [string, string, number]) => sum + score, 0) / leftWordCombo.length;
        
        // Return the higher one
        if (rightAverageScore >= leftAverageScore) {
            return [nameOne, rightnameTwo];
        }
        return [nameOne, leftNameTwo];
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
    for (const [indexOne, _, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        // Continue if either word is less than 5 chars or not same length
        const lengthOne = wordOne.length;
        const lengthTwo = wordTwo.length;
        if (lengthOne < 5 || lengthTwo < 5 || lengthOne !== lengthTwo) {
            continue;
        }

        // Check if there is only one difference
        let mismatchedIndex = null;
        let tooManyDifferences = false;
        for (let i = 0; i < lengthOne; i++) {
            if (wordOne[i] === wordTwo[i]) {
                continue;
            }
            if (mismatchedIndex) {
                tooManyDifferences = true;
                break;
            }
            mismatchedIndex = i;
        }

        // Continue if there was not exactly one difference
        if (tooManyDifferences || mismatchedIndex === null) {
            continue;
        }

        // Replace one of the letters to be the other if they are cooresponding
        const charWordOne = wordOne[mismatchedIndex];
        const charWordTwo = wordTwo[mismatchedIndex];
        const cooresponding = ['ao', 'ea', 'iy'];
        if (cooresponding.includes(`${charWordOne}${charWordTwo}`) || cooresponding.includes(`${charWordTwo}${charWordOne}`)) {
            ne.updateNameOne(indexOne, wordTwo);
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
function _fixSwappedCharacters(nameOne: string, nameTwo: string): [string, string] {
    const ne = new NameEditor(nameOne, nameTwo);
    for (const [indexOne, _, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        // Skip if the words are not 5 long, are different length, or not fuzzy 80
        if (wordOne.length !== 5 || wordOne.length !== wordTwo.length || fuzzball.ratio(wordOne, wordTwo) !== 80) {
            continue;
        }

        // Find how many differences and where
        let differenceCount = 0;
        let differencePositions = [];
        for (let i = 0; i < wordOne.length; i++) {
            if (wordOne[i] !== wordTwo[i]) {
                differenceCount += 1;
                differencePositions.push(i);
            }
        }

        // Skip if there are not two differences, differences are not sequential, or not swappable
        if (differenceCount !== 2) {
            continue;
        }
        const positionOne = differencePositions[0];
        const positionTwo = differencePositions[1];
        if (Math.abs(positionOne - positionTwo) !== 1) {
            continue;
        }
        if (wordOne[positionOne] !== wordTwo[positionTwo] || wordOne[positionTwo] !== wordTwo[positionOne]) {
            continue;
        }

        // This is the scenerio we are looking for. Make the words identical
        ne.updateNameOne(indexOne, wordTwo);
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
    for (const [indexOne, _, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        if (wordOne === wordTwo) {
            continue;
        }
        if (wordOne.slice(1) === wordTwo.slice(1) && wordOne.length > 4 && wordTwo.length > 4) {
            ne.updateNameOne(indexOne, wordTwo);
        }
    }
    return ne.getModifiedNames();
}

/**
 * For any given matching word pair, replaces a specific substring in one of the words, with a similar substring found in the other word.
 * 
 * @param nameOne - a name
 * @param nameTwo - a name
 * @param middleSubstringOptionOne - the first possible middle of the substring
 * @param middleSubstringOptionTwo - the second possible middle of the substring
 * @param substringBeginnings - a list of possible beginnings to the substring. Whichever beginning is found in the one must be found in the other in order for the replacement to work
 * @param substringEndings - a list of possible endings to the substring. Whichever ending is found in the one must be found in the other in order for the replacement to work
 * @param minimumRequiredLetters - the minimum required letters to be found in both words in order for the replacement to work
 * @returns the modified names
 */
function _replaceSubstringCentersIfNamesAreSimilar(nameOne: string, nameTwo: string, middleSubstringOptionOne: string, middleSubstringOptionTwo: string, substringBeginnings: string[], substringEndings: string[], minimumRequiredLetters: number): [string, string] {
    // Return if both middles not in different words
    if ((!nameOne.includes(middleSubstringOptionOne) && !nameOne.includes(middleSubstringOptionTwo)) || (!nameTwo.includes(middleSubstringOptionOne) && !nameTwo.includes(middleSubstringOptionTwo))) {
        return [nameOne, nameTwo];
    }

    const ne = new NameEditor(nameOne, nameTwo);
    for (let [indexOne, indexTwo, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        // Skip words that are not long enough for the given rule
        if (wordOne.length < minimumRequiredLetters || wordTwo.length < minimumRequiredLetters) {
            continue;
        }
        
        // Add clear word breaks
        wordOne = `-${wordOne}-`;
        wordTwo = `-${wordTwo}-`;

        for (const substringBeginning of substringBeginnings) {
            if (!wordOne.includes(substringBeginning) || !wordTwo.includes(substringBeginning)) {
                continue;
            }

            for (const substringEnding of substringEndings) {
                if (!wordOne.includes(substringEnding) || !wordTwo.includes(substringEnding)) {
                    continue;
                }

                const pattern = new RegExp(`${substringBeginning}(${middleSubstringOptionOne}|${middleSubstringOptionTwo})${substringEnding}`);
                const resultListOne = pattern.exec(wordOne);
                const resultListTwo = pattern.exec(wordTwo);

                if (!resultListOne || !resultListTwo) continue;

                if (resultListOne[0] === resultListTwo[0]) continue;

                const startIndexStringA = resultListOne.index;
                const endIndexStringA = startIndexStringA + resultListOne[0].length;
                const startIndexStringB = resultListTwo.index;
                const endIndexStringB = startIndexStringB + resultListTwo[0].length;
                if (Math.abs(startIndexStringA- startIndexStringB) > 2 || Math.abs(endIndexStringA - endIndexStringB) > 2) {
                    continue;
                }
                
                // Update the words by replacing matching (different) middles with the meat option 2
                const [startIndexStringOne, endIndexStringOne] = [startIndexStringA, endIndexStringA];
                const [startIndexStringTwo, endIndexStringTwo] = [startIndexStringB, endIndexStringB];
                const middleCoordinateStringOne = [startIndexStringOne + substringBeginning.length, endIndexStringOne - substringEnding.length];
                const middleCoordinateStringTwo = [startIndexStringTwo + substringBeginning.length, endIndexStringTwo - substringEnding.length];
                wordOne = _overwriteWithSubstring(wordOne, middleSubstringOptionTwo, middleCoordinateStringOne[0], middleCoordinateStringOne[1]);
                wordTwo = _overwriteWithSubstring(wordTwo, middleSubstringOptionTwo, middleCoordinateStringTwo[0], middleCoordinateStringTwo[1]);
            }
        }

        // Update the words for that match (though a change may not have occured)
        wordOne = wordOne.replace(/-/g, "");
        wordTwo = wordTwo.replace(/-/g, "");

        ne.updateNameOne(indexOne, wordOne);
        ne.updateNameTwo(indexTwo, wordTwo);
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
 * @param ipaOne - a name
 * @param ipaTwo - a name
 * @returns the modified names
 */
export function modifyIpasByComparison(ipaOne: string, ipaTwo: string): [string, string] {
    for (const [middleSubstringOptionOne, middleSubstringOptionTwo, substringBeginnings, substringEndings, minimumLetters] of ipaRules) {
        [ipaOne, ipaTwo] = _replaceSubstringCentersIfNamesAreSimilar(ipaOne, ipaTwo, middleSubstringOptionOne, middleSubstringOptionTwo, substringBeginnings, substringEndings, minimumLetters);
    }
    return [ipaOne, ipaTwo];
}