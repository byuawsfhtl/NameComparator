import memoize from 'memoizee';
import unidecode from 'unidecode';
import ipaAllNames from '../../data/pronunciation/ipaAllNames.json';
import ipaCommonWordParts from '../../data/pronunciation/ipaCommonWordParts.json';

// const memoized = memoize(function, {max: 1000});

/**
 * Gets the pronunciation of a name.
 * 
 * @param name - The name to get the pronunciation of
 * @returns The ipa pronunciation of the name
 */
export function getIpa(name: string): string {

    const pronunciationList = [];
    for (const word of name.trim().split(/\s+/)) {
        pronunciationList.push(_getIpaOfOneWordMemoized(word));
    }
    return pronunciationList.join(' ');
}

// Note here that memoizee is the typescript equivalent of lru cache in python
const _getIpaOfOneWordMemoized = memoize(_getIpaOfOneWord, {max: 1000});

/**
 * Gets the pronunciation of a word.
 * 
 * @param word - The word to get the pronunciation of
 * @returns The ipa pronunciation of the word
 */
function _getIpaOfOneWord(word: string): string {

    var wordNormalized = unidecode(word.trim()).toLowerCase();
    const pronunciationList = Array(wordNormalized.length).fill("");

    // Tries to get the ipa from the word
    const [firstAttempt, success] = _wordPronunciationIpaGuess(wordNormalized);
    if (success) {
        return firstAttempt;
    }

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
function _iterateAllPossibleSubstrings(wordNormalized:string): [boolean, number, number, string, number]{

    // Initialize variables to store the largest matching substring and its length
    let substringAdded = false;
    let largestSubstring = "";
    let pronunciationOfLargestSubstring = "";
    let largestSubstringLength = 0;
    let beginningIndexOfSubstring = 0;
    let endIndexOfSubstring = 0;

    // Iterate over every possible substring
    for (let i = 0; i < wordNormalized.length; i++) {
        for (let j = i + 1; j <= wordNormalized.length + 1; j++) {
            var substring = wordNormalized.substring(i, j);

            if (substring.length <= largestSubstringLength) {
                continue;
            }
            if (substring.includes(" ")) {
                continue;
            }
            if (substring.length > 1){
                const [ipaSubstring, success] = _stringPronunciationIpaGuess(substring);
                if (!success || (ipaSubstring.length >= substring.length * 2) || (substringSplitsThSound(substring, wordNormalized, i, j))) {continue;}
                else {pronunciationOfLargestSubstring = ipaSubstring;}
            } else if (substring.length === 1) {
                const letterToPronunciation = {
                "a": "æ", "b": "b", "c": "k", "d": "d", "e": "ɛ", "f": "f", "g": "g", "h": "h", "i": "ɪ",
                "j": "ʤ", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "k", "r": "r",
                "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "ks", "y": "j", "z": "z"
                };
                pronunciationOfLargestSubstring = letterToPronunciation[substring as keyof typeof letterToPronunciation] || largestSubstring;
            }

            largestSubstring = substring;
            substringAdded = true;
            largestSubstringLength = substring.length;
            beginningIndexOfSubstring = i;
            endIndexOfSubstring = j;
        }
    }

    return [substringAdded, beginningIndexOfSubstring, endIndexOfSubstring, pronunciationOfLargestSubstring, largestSubstringLength]
}

/**
 * Tries to get the pronunciation from the predefined ipa dictionary.
 * 
 * @param word - The word to get the pronunciation of
 * @returns The ipa of the word (or the original word if not found), and whether it was found.
 */
function _wordPronunciationIpaGuess(word: string): [string, boolean] {

    const wordPronunciation = ipaAllNames[word as keyof typeof ipaAllNames];
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

    const ipaPronunciation = ipaCommonWordParts[string as keyof typeof ipaCommonWordParts];
    if (ipaPronunciation) {
        return [ipaPronunciation, true];
    }
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

    if (i === j) {
        return false;
    }
    if (i >= 0 && substring[0] === 'h' && word[i-1] === 't') {
        return true;
    }
    if (j <= word.length - 1 && substring[substring.length - 1] == 't' && word[j] === 'h') {
        return true;
    }
    return false;
}