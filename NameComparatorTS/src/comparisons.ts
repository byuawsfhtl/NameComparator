import * as fuzzball from "fuzzball";
import { identifyBestMatches, findWordMatchesAndQuality } from "./usefulTools";
import * as math from 'mathjs';

/**
 * Identifies if two names are a match according to a comparison based soley on spelling.
 * 
 * @param nameOne - The first name used in the spelling comparison
 * @param nameTwo - The second name used in the spelling comparison
 * 
 * @returns Whether the names are a match and the resulting word combo
 */
export function compareSpelling(nameOne: string, nameTwo: string): [boolean, any[]] {
    const wordCombo = findWordMatchesAndQuality(nameOne, nameTwo);
    const count = wordCombo.filter(tup => tup[2] > 80).length;
    const minimumLength = Math.min(nameOne.split(' ').length, nameTwo.split(' ').length);
    if (count >= 3 || count === minimumLength) {
        return [true, wordCombo];
    };
    if (_consonantComparison(nameOne, nameTwo)) {
        return [true, wordCombo];
    };
    return [false, wordCombo];
};

/**
 * Identifies if two names are a match according to consonant comparison.
 * 
 * @param nameOne - The first name used in the consonant comparison
 * @param nameTwo - The second name used in the consonant comparison
 * @returns Whether the two names are a match, according to consonant comparison
 */
function _consonantComparison(nameOne: string, nameTwo: string): boolean {
    // Setup
    const wordCombo = findWordMatchesAndQuality(nameOne, nameTwo);
    const minimumRequiredMatches = wordCombo.length;
    let numberOfConsonantMatches = 0;

    // Loop through every word match in the combo
    for (const tup of wordCombo) {
        // Get the matching word data
        const wordOne = nameOne.split(' ')[parseInt(tup[0])];
        const wordTwo = nameTwo.split(' ')[parseInt(tup[1])];
        const originalScoreForWords = Number(tup[2]);

        // Get the words as consonants
        const consonantsInNameOne = _reduceToSimpleConsonants(wordOne);
        const consonantsInNameTwo = _reduceToSimpleConsonants(wordTwo);
        const consonantRatio = fuzzball.ratio(consonantsInNameOne, consonantsInNameTwo);
        
        // Continue if bad match
        if (originalScoreForWords <= 30) {
            continue;
        };
        if (wordOne.length !== 1 && wordTwo.length !== 1) { // # If neither word is an initial
            const lowestSyllableCount = Math.min(
                consonantsInNameOne.split('я').length - 1,
                consonantsInNameTwo.split('я').length - 1
            );
            if (lowestSyllableCount < 2) continue;
        };
        if (consonantRatio <= 80 || (originalScoreForWords <= 60 && consonantRatio !== 100)) {
            continue;
        };

        // If not rejected, increment the number of matches
        numberOfConsonantMatches++;
    };

    // If enough matches, return true. Otherwise return false.
    return (numberOfConsonantMatches > minimumRequiredMatches) || (numberOfConsonantMatches >= 3);
};

/**
 * Reduces a string to its simple consonant components.
 * 
 * @param string - The string we want to reduce
 * 
 * @returns A string containing only the consonants of the original string, separated
            by asterisks
 */
function _reduceToSimpleConsonants(string: string): string {
    return string
        .replace(/[aeiouy]/g, '*')
        .replace(/\*{2,}/g, '*')
        .replace(/(.)\1+/g, '$1');
};

/**
 * Identifies if two names are a match according to a pronunciation comparison.
 * 
 * @param ipaOfNameOne - The ipa of the first name to compare the pronuncation of
 * @param ipaOfNameTwo - The ipa of the second name to compare the pronuncation of
 * @param nameOne - The first name to compare the pronuncation of
 * @param nameTwo - The second name to compare the pronuncation of
 * 
 * @returns Whether or not the name was a match and the word combo
 */
export function pronunciationComparison(ipaOfNameOne: string, ipaOfNameTwo: string, nameOne: string, nameTwo: string): [boolean, [string, string, number][]] {

    // Initialize empty list to store scores
    var wordsFromIpaOne = ipaOfNameOne.split(/\s+/);
    var wordsFromIpaTwo = ipaOfNameTwo.split(/\s+/);
    if (wordsFromIpaOne.length < wordsFromIpaTwo.length) {
        wordsFromIpaOne.push(...Array(wordsFromIpaTwo.length - wordsFromIpaOne.length).fill(null));
    } else if (wordsFromIpaOne.length > wordsFromIpaTwo.length) {
        wordsFromIpaTwo.push(...Array(wordsFromIpaOne.length - wordsFromIpaTwo.length).fill(null));
    };
    
    // Create a matrix of zeros using mathjs
    let scores = math.matrix(math.zeros([wordsFromIpaOne.length, wordsFromIpaTwo.length])) as math.Matrix;
    
    // Score each matchup
    var wordComboForScores = findWordMatchesAndQuality(nameOne, nameTwo);
    _matchupScores(wordComboForScores, scores, wordsFromIpaOne, wordsFromIpaTwo);
    
    // Identify the best matchups
    wordsFromIpaOne = wordsFromIpaOne.map((word, i) => word !== null ? String(i) : "");
    wordsFromIpaTwo = wordsFromIpaTwo.map((word, i) => word !== null ? String(i) : "");
    // This next line differs from the python version, but it's only due to TypeScript typing
    // shennanigans. It's functionally the same
    let scoreMatrix : number[][] = scores.toArray() as number[][];
    let wordCombo = identifyBestMatches(scoreMatrix, wordsFromIpaOne, wordsFromIpaTwo);
    const lowestScore = Math.min(...wordCombo.map((tuple: [string, string, number]) => tuple[2]));
    
    // Return whether pronunciation match or not
    const minimumLength = Math.min(ipaOfNameOne.split(/\s+/).length, ipaOfNameTwo.split(/\s+/).length);
    if (minimumLength <= 2) {
        if (lowestScore >= 80) {
            return [true, wordCombo];
        };
        return [false, wordCombo];
    };
    if (minimumLength > 2) {
        if (lowestScore > 75) {
            return [true, wordCombo];
        };
        return [false, wordCombo];
    };
    
    // Default return just in case something gets here
    return [false, wordCombo];
};

/**
 * Finds the score for the quality of each matchup of words that are potential matches, in terms of ipa
 * pronunciations. It then updates a list of scores to reflect this for later processing in the
 * pronunciation_comparison function.
 * 
 * @param wordComboForScores - A list of word combinations that need to be scored
 * @param scores - A list of scores for all of the different word combinations
 * @param wordsFromIpaOne - A list of words that could match the ipa pronuncation of the first checked word
 * @param wordsFromIpaTwo - A list of words that could match the ipa pronuncation of the second checked word
 */
function _matchupScores(wordComboForScores: [string, string, number][], scores: math.Matrix, wordsFromIpaOne: string[], wordsFromIpaTwo: string[]): void{

    for (let indexOne = 0; indexOne < wordsFromIpaOne.length; indexOne++) {
        for (let indexTwo = 0; indexTwo < wordsFromIpaTwo.length; indexTwo++) {
            // Assign a default very low score for dummy pairings
            scores.set([indexOne, indexTwo], -1e9);

            // Typescript needs these declarations, but python doesn't
            const wordOne = wordsFromIpaOne[indexOne];
            const wordTwo = wordsFromIpaTwo[indexTwo];

            if (wordOne === null || wordTwo === null) {
                continue;
            };
            
            // Reassign the default score to all real pairings
            let score = _scoreWordCombosHelper(wordOne, wordTwo, indexOne, indexTwo, wordComboForScores);
            scores.set([indexOne, indexTwo], score);
        };
    };
};

/**
 * This function is a helper function to reduce the nesting depth of _matchup_scores.
 * What it does is it compares all of the scores for a word combo and then finds a score
 * that is going to be more accurate for them, as opposed to a default score.
 * 
 * @param wordOne - A list of word combinations that need to be scored
 * @param wordTwo - A list of scores for all of the different word combinations
 * @param indexOne - A list of words that could match the ipa pronuncation of the first checked word
 * @param indexTwo - A list of words that could match the ipa pronuncation of the second checked word
 * @param wordComboForScores - A list of words that could match the ipa pronuncation of the second checked word
 * 
 * @returns The score that should be set for a particular word combo
 */
function _scoreWordCombosHelper(wordOne: string, wordTwo: string, indexOne: number, indexTwo: number, wordComboForScores: [string, string, number][]): number {

    let score = fuzzball.ratio(wordOne, wordTwo);
    for (let i = 0; i < wordComboForScores.length; i++){
        const [wordComboForScoresIndexOne, wordComboForScoresIndexTwo, initialScore] = wordComboForScores[i];
        // Use initial score for initials (bad pun)
        if (indexOne === parseInt(wordComboForScoresIndexOne) && indexTwo === parseInt(wordComboForScoresIndexTwo) && (initialScore === 100 || initialScore === 0)) {
            score = initialScore;
        };
    };

    return score;
};