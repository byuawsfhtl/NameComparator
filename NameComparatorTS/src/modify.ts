import { ratio as fuzzball_ratio } from "fuzzball";

import { findWordMatchesAndQuality, getMatchingWordsAndIndices, NameEditor } from "./usefulTools";
import spellingRules from "../../data/rules/rulesSpelling.json";
import ipaRules from "../../data/rules/rulesIpa.json";

/** 
 * Modifies the name together, changing them in a way that is much more intense than simply cleaning together.
 * 
 * @param nameOne - The first name to modify
 * @param nameTwo - The second name to modify
 * @returns The modified names
 */
export function modifyNamesTogether(nameOne: string, nameTwo: string): [string, string] {
    nameOne = nameOne.replace(/ie\b/g, "y");
    nameTwo = nameTwo.replace(/ie\b/g, "y");
    [nameOne, nameTwo] = _removeWordOrFromNames(nameOne, nameTwo);
    [nameOne, nameTwo] = _fixVowelMistakes(nameOne, nameTwo);
    [nameOne, nameTwo] = _fixSwappedCharacters(nameOne, nameTwo);
    [nameOne, nameTwo] = _dealWithWrongFirstChar(nameOne, nameTwo);
    for (const[middleSubstringOptionOne, middleSubstringOptionTwo, substringBeginnings, substringEndings, minimumLetters] of spellingRules as [string, string, string[], string[], number][]) {
        [nameOne, nameTwo] = _replaceSubstringCentersIfNamesAreSimilar(nameOne, nameTwo, middleSubstringOptionOne, middleSubstringOptionTwo, substringBeginnings, substringEndings, minimumLetters);
    }
    nameOne = nameOne.replace(/\s+/g, " ");
    nameTwo = nameTwo.replace(/\s+/g, " ");
    nameOne = nameOne.trim();
    nameTwo = nameTwo.trim();
    return [nameOne, nameTwo];
}

/**
 * Removes the word 'or' from a name. This might happen when a name has been poorly indexed,
 * which makes the indexer's guesses for a specific word of the name sta in the string, causing
 * the 'or'.
 * 
 * @param nameOne - The first name to remove the word 'or' from
 * @param nameTwo - The second name to remove the word 'or' from
 * @returns The modified names with a consistent use of 'or' (or lack thereof)
 */
function _removeWordOrFromNames(nameOne: string, nameTwo: string): [string, string] {
    if (!nameOne || !nameTwo) {
        return [nameOne, nameTwo];
    }
    nameOne = nameOne.trim();
    nameTwo = nameTwo.trim();
    nameOne = nameOne.toLowerCase();
    nameTwo = nameTwo.toLowerCase();

    // if 'or' in neither
    if (!nameOne.includes(" or ") && !nameTwo.includes(" or ")) {
        return [nameOne, nameTwo];
    }

    // if 'or' in both
    else if (nameOne.includes(" or ") && nameTwo.includes(" or ")) {
        return [nameOne, nameTwo];
    }

    // if 'or' in nameOne and not nameTwo
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

    // if 'or' in nameTwo and not nameOne
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
 * they are only different by one vowel and are 5 letters or longer.
 * 
 * @param nameOne - The first name to check for vowel differences in
 * @param nameTwo - The second name to check for vowel differences in
 * @returns A tuple containing the two modified names
 */
function _fixVowelMistakes(nameOne: string, nameTwo: string): [string, string] {
    const nameEditorInstance = new NameEditor(nameOne, nameTwo);
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
            nameEditorInstance.updateNameOne(indexOne, wordTwo);
        }
    }
    // Return the modified (or not) names
    return nameEditorInstance.getModifiedNames();
}

/**
 * If two matching words (of 5 letters of more) for the two names are the same 
 * barring swapped letters (such as a typo), this function makes the words the same.
 * 
 * @param nameOne - The first name to check for swapped letters
 * @param nameTwo - The second name to check for swapped letters
 * @returns A tuple containing the names, modified to remove any swapped letters
 */
function _fixSwappedCharacters(nameOne: string, nameTwo: string): [string, string] {
    const nameEditorInstance = new NameEditor(nameOne, nameTwo);
    for (const [indexOne, _, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        // Skip if the words are not 5 long, are different length, or not fuzzy 80
        if (wordOne.length !== 5 || wordOne.length !== wordTwo.length || fuzzball_ratio(wordOne, wordTwo) !== 80) {
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
        nameEditorInstance.updateNameOne(indexOne, wordTwo);
    }
    // Return the modified (or not) names
    return nameEditorInstance.getModifiedNames();
}

/**
 * If two matching words (of 5 letters or more) are the same barring the first letter, 
 * this function makes them the same.
 * 
 * @param nameOne - The first name to check for an incorrect first character
 * @param nameTwo - The second name to check for an incorrect first character
 * @returns The names, modified to have a matching first character
 */
function _dealWithWrongFirstChar(nameOne: string, nameTwo: string): [string, string] {
    const nameEditorInstance = new NameEditor(nameOne, nameTwo);
    for (const [indexOne, _, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        if (wordOne === wordTwo) {
            continue;
        }
        if (wordOne.slice(1) === wordTwo.slice(1) && wordOne.length > 4 && wordTwo.length > 4) {
            nameEditorInstance.updateNameOne(indexOne, wordTwo);
        }
    }
    return nameEditorInstance.getModifiedNames();
}

/**
 * For any given matching word pair, replaces a specific substring in one of the words with a similar substring found in the other word.
 * It checks this by comparing the beginnings and ends of words, then determining similarities of everything in between those and replacing
 * them if they seem like they indicate similar words. This could be compared to a 'word sandwich' of sorts where the beginnings and endings
 * are sort of like bread on the ends and the center substrings are like the fillings.
 * 
 * @param nameOne - The first name to check for similar substrings
 * @param nameTwo - The second name to check for similar substrings
 * @param middleSubstringOptionOne - The first possible middle of the substring
 * @param middleSubstringOptionTwo - The second possible middle of the substring
 * @param substringBeginnings - A list of possible beginnings to the substring. Whichever beginning is found in the one must be found in the 
 *                              other in order for the replacement to be considered valid
 * @param substringEndings - A list of possible endings to the substring. Whichever ending is found in the one must be found in the other in 
 *                           order for the replacement to be considered valid
 * @param minimumRequiredLetters - The minimum required letters to be found in both words in order for the replacement to be considered valid
 * @returns The names, modified to have the same substrings in the center (if applicable)
 */
function _replaceSubstringCentersIfNamesAreSimilar(nameOne: string, nameTwo: string, middleSubstringOptionOne: string, middleSubstringOptionTwo: string, possibleSubstringBeginnings: string[], possibleSubstringEndings: string[], minimumRequiredLetters: number): [string, string] {
    // Return if both middles not in different words
    if ((!nameOne.includes(middleSubstringOptionOne) && !nameOne.includes(middleSubstringOptionTwo)) || (!nameTwo.includes(middleSubstringOptionOne) && !nameTwo.includes(middleSubstringOptionTwo))) {
        return [nameOne, nameTwo];
    }

    const nameEditorInstance = new NameEditor(nameOne, nameTwo);
    for (let [indexOne, indexTwo, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        // Skip words that are not long enough for the given rule
        if (wordOne.length < minimumRequiredLetters || wordTwo.length < minimumRequiredLetters) {
            continue;
        }
        
        // Add clear word breaks
        wordOne = `-${wordOne}-`;
        wordTwo = `-${wordTwo}-`;

        // Check words for substring matches and make appropriate replacements and edits
        [wordOne, wordTwo] = _handleSubstringReplacementsAndChecks(wordOne, wordTwo, possibleSubstringBeginnings, middleSubstringOptionOne, middleSubstringOptionTwo, possibleSubstringEndings)

        // Update the words for that match (though a change may not have occured)
        wordOne = wordOne.replace(/-/g, "");
        wordTwo = wordTwo.replace(/-/g, "");
        nameEditorInstance.updateNameOne(indexOne, wordOne);
        nameEditorInstance.updateNameTwo(indexTwo, wordTwo);
    }
    
    // concatonates the two lists together back into strings
    [nameOne, nameTwo] = nameEditorInstance.getModifiedNames();
    return [nameOne, nameTwo];
}

/**
 * This is a helper function for _replace_substring_centers_if_names_are_similar
 * that helps with its cyclomatic complexity. It's actual function is to see if
 * substring patterns exist within word_one or word_two and then replace them to
 * be the same if they are close enough to what's in *both* word_one and word_two.
 * 
 * @param nameOne - The first word or name to look for substring matches in
 * @param nameTwo - The second word or name to look for substring matches in
 * @param possibleSubstringBeginnings - A list of all possible beginnings to a substring
 * @param middleSubstringOptionOne - The first possible middle of the substring
 * @param middleSubstringOptionTwo - The second possible middle of the substring
 * @param possibleSubstringEndings - A list of all possible endings to a substring
 * @returns The modified versions of word_one and word_two if any changes were made, or 
 * just word_one and word_two if none were made
 */
function _handleSubstringReplacementsAndChecks(wordOne: string, wordTwo: string, possibleSubstringBeginnings: string[], middleSubstringOptionOne: string, middleSubstringOptionTwo: string, possibleSubstringEndings: string[]): [string, string]{

    for (const substringBeginning of possibleSubstringBeginnings) {
        if (!wordOne.includes(substringBeginning) || !wordTwo.includes(substringBeginning)) {
            continue;
        }

        for (const substringEnding of possibleSubstringEndings) {
            if (!wordOne.includes(substringEnding) || !wordTwo.includes(substringEnding)) {
                continue;
            }

            // Skip the beginnings and ends if the pattern is not found in both,
            // if the middles are the same, or if the patterns are too far appart
            const pattern = new RegExp(`${substringBeginning}(${middleSubstringOptionOne}|${middleSubstringOptionTwo})${substringEnding}`);
            const resultListOne = pattern.exec(wordOne);
            const resultListTwo = pattern.exec(wordTwo);

            if (!resultListOne || !resultListTwo) continue;

            if (resultListOne[0] === resultListTwo[0]) continue;

            const startIndexOfListOneSpan = resultListOne.index;
            const endIndexOfListOneSpan = startIndexOfListOneSpan + resultListOne[0].length;
            const startIndexOfListTwoSpan = resultListTwo.index;
            const endIndexOfListTwoSpan = startIndexOfListTwoSpan + resultListTwo[0].length;

            if (Math.abs(startIndexOfListOneSpan - startIndexOfListTwoSpan) > 2 || Math.abs(endIndexOfListOneSpan - endIndexOfListTwoSpan) > 2) {
                continue;
            }
            
            // Update the words by replacing matching (different) middles with the meat option 2
            const [startIndexStringOne, endIndexStringOne] = [startIndexOfListOneSpan, endIndexOfListOneSpan];
            const [startIndexStringTwo, endIndexStringTwo] = [startIndexOfListTwoSpan, endIndexOfListTwoSpan];
            const middleCoordinateStringOne = [startIndexStringOne + substringBeginning.length, endIndexStringOne - substringEnding.length];
            const middleCoordinateStringTwo = [startIndexStringTwo + substringBeginning.length, endIndexStringTwo - substringEnding.length];
            wordOne = _overwriteWithSubstring(wordOne, middleSubstringOptionTwo, middleCoordinateStringOne[0], middleCoordinateStringOne[1]);
            wordTwo = _overwriteWithSubstring(wordTwo, middleSubstringOptionTwo, middleCoordinateStringTwo[0], middleCoordinateStringTwo[1]);
        }
    }

    return [wordOne, wordTwo]
}

/**
 * Overwrites a specific index range of a string with the replacement string.
 * 
 * @param string - The string to replace
 * @param replacement - The replacement string
 * @param startIndex - The start index for the replacement
 * @param endIndex - The end index for the replacement
 * @returns A new string, with the specified indices replaced by the replacement string
 */
function _overwriteWithSubstring(string: string, replacement: string, startIndex: number, endIndex: number): string {
    return string.slice(0, startIndex) + replacement + string.slice(endIndex);
}

/**
 * Modifies two ipas by comparing them to each other.
 * 
 * @param ipaOne - The first ipa of a name
 * @param ipaTwo - The second ipa of a name
 * @returns The modified ipas of two words or names
 */
export function modifyIpasByComparison(ipaOne: string, ipaTwo: string): [string, string] {
    for (const [middleSubstringOptionOne, middleSubstringOptionTwo, substringBeginnings, substringEndings, minimumLetters] of ipaRules as [string, string, string[], string[], number][]) {
        [ipaOne, ipaTwo] = _replaceSubstringCentersIfNamesAreSimilar(ipaOne, ipaTwo, middleSubstringOptionOne, middleSubstringOptionTwo, substringBeginnings, substringEndings, minimumLetters);
    }
    return [ipaOne, ipaTwo];
}