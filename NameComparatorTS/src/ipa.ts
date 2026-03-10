import memoize from 'memoizee';
import unidecode from 'unidecode';
import ipaAllNames from '../data/pronunciation/ipaAllNames.json';
import ipaCommonWordParts from '../data/pronunciation/ipaCommonWordParts.json';
// cosnt memoized = memoize(function, {max: 1000});

/**
 * Gets the pronunciation of a name
 * @param name - The name to get the pronunciation of
 * @returns The ipa pronunciation of the name
 */
export function getIpa(name: string): string {

    const pList = [];
    for (const word of name.split(/\s+/)) {
        pList.push(_getIpaOfOneWordMemoized(word));
    }
    return pList.join(' ');
}

/**
 * Gets the pronunciation of a word
 * @param word - The word to get the pronunciation of
 * @returns The ipa pronunciation of the word
 */
function _getIpaOfOneWord(word: string): string {

    var wordNormalized = unidecode(word.trim()).toLowerCase();
    const pronunciationList = Array(wordNormalized.length).fill("");

    /** Helps to identify poor substring choices for words for ipa.

        * @param substring - the ipa dissection
        * @param word - the full word
        * @param i - the start index of the substring
        * @param j - the end index of the substring

        * @returns whether it was a good substring
    */ 
    function substringSplitsTh(substring:string, word:string, i:number, j:number): boolean {
    
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

    // Tries to get the ipa from the word
    const [firstAttempt, success] = _wordPronunciationHailMary(wordNormalized);
    if (success) {
        return firstAttempt;
    }

    // While there are still letters to the word:
    var substringAdded = true;
    var largestSubstring = "";
    var pronunciationOfLargestSubstring = "";
    var largestSubstringLength = 0;
    var beginningIndexOfSubstring = 0;
    var endIndexOfSubstring = 0;
    while (substringAdded) {
        // Initialize variables to store the largest matching substring and its length
        substringAdded = false;
        largestSubstring = "";
        pronunciationOfLargestSubstring = "";
        largestSubstringLength = 0;
        beginningIndexOfSubstring = 0;
        endIndexOfSubstring = 0;

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
                    const [substringIpa, success1] = _stringPronunciationHailMary(substring);
                    if (!success1 || (substringIpa.length >= substring.length * 2) || (substringSplitsTh(substring, word, i, j))) {
                        continue;
                    }
                    else {
                        pronunciationOfLargestSubstring = substringIpa;
                    }
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
    

        if (substringAdded) {
            pronunciationList[beginningIndexOfSubstring] = pronunciationOfLargestSubstring;
        }
        const spaces = " ".repeat(largestSubstringLength);
        wordNormalized = wordNormalized.substring(0, beginningIndexOfSubstring) +
                    spaces +
                    wordNormalized.substring(endIndexOfSubstring);
    }
    const pronunciationOfWord = pronunciationList.join("");
    return pronunciationOfWord;
}

const _getIpaOfOneWordMemoized = memoize(_getIpaOfOneWord, {max: 1000});

/**
 * Tries to get the pronunciation from the predefined ipa dictionary.
 * @param word - The word to get the pronunciation of
 * @returns the ipa of the word (or the original word if not found), and whether it was found.
 */
function _wordPronunciationHailMary(word: string): [string, boolean] {

    const wordPronunciation = ipaAllNames[word as keyof typeof ipaAllNames];
    if (wordPronunciation) {
        return [wordPronunciation, true];
    }
    return [word, false];
}

/**
 * Helper function of _getIpaOfOneWord.
 * Tries to get the ipa of a string (with more than one letter).
 * @param word - The word to get the pronunciation of
 * @returns the ipa of the word (or the original word if not found), and whether it was found.
 */
function _stringPronunciationHailMary(word: string): [string, boolean] {

    const ipaPronunciation = ipaCommonWordParts[word as keyof typeof ipaCommonWordParts];
    if (ipaPronunciation) {
        return [ipaPronunciation, true];
    }
    return [word, false];
}