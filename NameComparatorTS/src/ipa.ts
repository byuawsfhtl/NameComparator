import fs from 'fs';
import path from 'path';
import memoize from 'memoizee';
import unidecode from 'unidecode';

// This is required to make sure that it reads in the characters correctly
import ipaAllNamesUnparsed from '../../data/pronunciation/ipaAllNames.json' with { type: 'json' };
const ipaAllNames = ipaAllNamesUnparsed as Record<string, string>;

import ipaCommonWordPartsUnparsed from '../../data/pronunciation/ipaCommonWordParts.json' with { type: 'json'}
const ipaCommonWordParts = ipaCommonWordPartsUnparsed as Record<string, string>;

// Note here that memoizee (and the memoize function) is the typescript equivalent of lru cache in python
export const getIpa = memoize(getIpaUnmemoized, {max: 1000});
/**
 * Gets the pronunciation of a name.
 * 
 * @param name - The name to get the pronunciation of
 * @returns The ipa pronunciation of the name
 */
function getIpaUnmemoized(name: string): string {

    const pronunciationList = [];
    for (const word of name.trim().split(/\s+/)) {
        pronunciationList.push(_getIpaOfOneWord(word));
        // console.error(`Current pronunciation list in TypeScript: ${pronunciationList}`);
    }

    // console.error(`Final pronunciation list in TypeScript: ${pronunciationList}`);
    return pronunciationList.join(' ');
}

// Note here that memoizee (and the memoize function) is the typescript equivalent of lru cache in python
const _getIpaOfOneWord = memoize(_getIpaOfOneWordUnmemoized, {max: 1000});
/**
 * Gets the pronunciation of a word.
 * 
 * @param word - The word to get the pronunciation of
 * @returns The ipa pronunciation of the word
 */
function _getIpaOfOneWordUnmemoized(word: string): string {

    // console.error(`Getting the IPA of the word ${word} in TypeScript`);

    // Setup
    var wordNormalized = word.trim();
    wordNormalized = unidecode(wordNormalized);
    wordNormalized = wordNormalized.toLowerCase();
    const pronunciationList = Array(wordNormalized.length).fill("");

    // Tries to get the ipa from the word
    const [firstAttempt, success] = _wordPronunciationIpaGuess(wordNormalized);
    if (success) {
        // console.error("Successfully guessed the word pronunciation in TypeScript");
        return firstAttempt;
    };

    // Initialize variables that will be needed later
    let beginningIndexOfSubstring;
    let endIndexOfSubstring;
    let pronunciationOfLargestSubstring;
    let largestSubstringLength;

    // While there are still letters to the word:
    var substringAdded = true;
    while (substringAdded) {
        
        [substringAdded, beginningIndexOfSubstring, endIndexOfSubstring, pronunciationOfLargestSubstring, largestSubstringLength] = _iterateAllPossibleSubstrings(wordNormalized);
    
        // Adds the substring to the list
        if (substringAdded) {
            pronunciationList[beginningIndexOfSubstring] = pronunciationOfLargestSubstring;
        }
        const spaces = " ".repeat(largestSubstringLength);
        wordNormalized = wordNormalized.substring(0, beginningIndexOfSubstring) +
                    spaces +
                    wordNormalized.substring(endIndexOfSubstring);
    }

    // Concatenates the list together at the end to get the pronunciation
    const pronunciationOfWord = pronunciationList.join("");
    return pronunciationOfWord;
}

/**
 * Iterates through all of the possible substrings of a word to find information
 * about which substrings are going to be the best ipa pronunciation representation
 * of the word.
 * 
 * @param word - The word that all the possible substrings of are being iterated through
 * @returns The following information: A boolean representing if the substring was added, 
 *          the beginning index of the substring, the end index of the substring, the 
 *          pronunciation of the largest substring, and the length of the largest substring
 */
function _iterateAllPossibleSubstrings(word:string): [boolean, number, number, string, number]{

    // console.error(`Iterating through all the possible substrings of ${word} in TypeScript`);

    // Initialize variables to store the largest matching substring and its length
    let substringAdded = false;
    let largestSubstring = "";
    let pronunciationOfLargestSubstring = "";
    let largestSubstringLength = 0;
    let beginningIndexOfSubstring = 0;
    let endIndexOfSubstring = 0;

    // Iterate over every possible substring
    for (let i = 0; i < word.length; i++) {
        for (let j = i + 1; j <= word.length + 1; j++) {
            var substring = word.substring(i, j);

            // console.error(`Checking possible pronunciation improvements for the substring ${substring} in TypeScript`)

            if (substring.length <= largestSubstringLength) {
                // console.error(`Skipped the substring ${substring} due to it being shorter than the largest substring in TypeScript`);
                continue;
            }
            if (substring.includes(" ")) {
                // console.error(`Skipped the substring ${substring} due to it containing a space in TypeScript`);
                continue;
            }
            if (substring.length > 1){
                const [ipaSubstring, success] = _stringPronunciationIpaGuess(substring);
                // console.error(`Variable check for skipping due to conditions in TypeScript: success - ${success} ipaSubstring.length - ${ipaSubstring.length} substring.length * 2 - ${substring.length * 2}, substringSplitsThSound(substring, word, i, j) - ${substringSplitsThSound(substring, word, i, j)}`);
                if (!success || (ipaSubstring.length >= substring.length * 2) || (substringSplitsThSound(substring, word, i, j))) {
                    // console.error(`Skipped the substring ${substring} due to many conditions in TypeScript`);
                    continue;
                }
                else {
                    pronunciationOfLargestSubstring = ipaSubstring;
                    // console.error(`Updated largest substring to be ${ipaSubstring} based on a guess in TypeScript`);
                }
            } else if (substring.length === 1) {
                const letterToPronunciation = {
                    "a": "æ", "b": "b", "c": "k", "d": "d", "e": "ɛ", "f": "f", "g": "g", "h": "h", "i": "ɪ",
                    "j": "ʤ", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "k", "r": "r",
                    "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "ks", "y": "j", "z": "z"
                };
                pronunciationOfLargestSubstring = letterToPronunciation[substring as keyof typeof letterToPronunciation] || largestSubstring;
                // console.error(`Updated largest substring to be ${pronunciationOfLargestSubstring} based on the letter to pronunciation table in TypeScript`);
            }

            largestSubstring = substring;
            substringAdded = true;
            largestSubstringLength = substring.length;
            beginningIndexOfSubstring = i;
            endIndexOfSubstring = j;
        }
    }

    // console.error(`After the for loop, the values of the variables are as follows in TypeScript: substringAdded - ${substringAdded} beginningIndexOfSubstring - ${beginningIndexOfSubstring} endIndexOfSubstring - ${endIndexOfSubstring} pronunciationOfLargestSubstring - ${pronunciationOfLargestSubstring} largestSubstringLength - ${largestSubstringLength}`);

    return [substringAdded, beginningIndexOfSubstring, endIndexOfSubstring, pronunciationOfLargestSubstring, largestSubstringLength]
}

/**
 * Tries to get the pronunciation from the predefined ipa dictionary.
 * 
 * @param word - The word to get the pronunciation of
 * @returns The ipa of the word (or the original word if not found), and whether it was found.
 */
function _wordPronunciationIpaGuess(word: string): [string, boolean] {

    const wordPronunciation = ipaAllNames[word] ?? "";
    // console.error(`Found the pronunciation '${wordPronunciation}' for ${word} in our data`)
    if (wordPronunciation) {
        return [wordPronunciation, true];
    }
    return [word, false];
}

/**
 * Helper function of _getIpaOfOneWord. Tries to get the ipa of a string 
 * with more than one letter.
 * 
 * @param string - A string that is longer than one letter to get the pronunciation of
 * @returns The ipa of the string (or the original string if not found), and whether it was found.
 */
function _stringPronunciationIpaGuess(string: string): [string, boolean] {

    // console.error(`Finding the pronunciation guess for the string ${string} in TypeScript`);

    const ipaPronunciation = ipaCommonWordParts[string];
    if (ipaPronunciation) {
        // console.error(`Found the pronunciation guess ${ipaPronunciation} for the string ${string} in TypeScript`);
        return [ipaPronunciation, true];
    }
    // console.error(`Failed to find a pronunciation guess for the string ${string} in TypeScript`);
    return [string, false];
}

/** Helps to identify poor substring choices for words for ipa.
 * 
 * @param substring - the ipa dissection
 * @param word - the full word
 * @param i - the start index of the substring
 * @param j - the end index of the substring
 * @returns A boolean representing whether or not it was a good substring
*/ 
function substringSplitsThSound(substring:string, word:string, i:number, j:number): boolean {

    // console.error(`The substring splitting on th sounds has the following variables on startup: substring - ${substring} word - ${word} i - ${i} j - ${j}`);

    if (i === j) {
        // console.error("i equalled j in TypeScript");
        return false;
    }
    if (i >= 0 && substring[0] === 'h' && word.at(i-1) === 't') {
        // console.error("The first true return case in TypeScript");
        return true;
    }
    if (j <= word.length - 1 && substring.at(-1) === 't' && word[j] === 'h') {
        // console.error("The second true return case in TypeScript");
        return true;
    }
    // console.error("Hit the default return case in TypeScript");
    return false;
}