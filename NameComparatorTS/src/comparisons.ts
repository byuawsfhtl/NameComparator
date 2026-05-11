import { ratio as fuzzball_ratio} from "fuzzball";
import { identifyBestMatches, findWordMatchesAndQuality } from "./usefulTools.js";
import { min as mathjs_min, matrix as mathjs_matrix_function, Matrix as mathjs_matrix_class, zeros as mathjs_zeros } from 'mathjs';

// Read the various variables from a file
import values from '../../data/variablesForComparisons.json' with { type: "json"};
const { maxScore, 
        guaranteedPassingScore,
        conditionallyPassingScore,
        furtherChecksNeededScore,
        guaranteedFailScore,
        fuzzyComparisonWeight,
        consonantComparisonWeight,
        numberOfValidCombosToSkipFurtherChecks,
        lengthNeededForConditionallyPassingPronunciationComparison,
        penaltyForMismatchedPrefixes
    } = values;

/**
 * Identifies if two names are a match according to a comparison based soley on spelling.
 * 
 * @param nameOne - The first name used in the spelling comparison
 * @param nameTwo - The second name used in the spelling comparison
 * 
 * @returns Whether the names are a match and the resulting word combo
 */
export function compareSpelling(nameOne: string, nameTwo: string): [boolean, any[], number] {

    console.error(`Comparing spelling for ${nameOne} and ${nameTwo} in TypeScript`);

    const wordCombos = findWordMatchesAndQuality(nameOne, nameTwo);

    let count = 0;
    let combinedScores = 0;
    let averagedScores = 0;

    for (const tuple of wordCombos){
        if (tuple[2] >= guaranteedPassingScore){
            count = count + 1;
        };
        combinedScores = combinedScores + tuple[2];
    };

    const minimumLength = mathjs_min(nameOne.split(' ').length, nameTwo.split(' ').length);

    if (count > 0){
        averagedScores = combinedScores / count;
    };

    if (count >= numberOfValidCombosToSkipFurtherChecks && count === minimumLength) {
        console.error(`Determined to return true in TypeScript. Current variables: count - ${count} numberOfValidCombosToSkipFurtherChecks - ${numberOfValidCombosToSkipFurtherChecks}, minimumLength - ${minimumLength}`);
        return [true, wordCombos, averagedScores];
    };

    // Determine if it matches on consonants or not if the whole fuzzy string comparison is unclear
    const [isConsonantMatch, consonantMatchScore] = _consonantComparison(nameOne, nameTwo, wordCombos);

    // Return the values, averaging the score and slightly favoring the initial fuzzy string match ones
    return [isConsonantMatch, wordCombos, ((averagedScores * fuzzyComparisonWeight) + (consonantMatchScore * consonantComparisonWeight))];
}

/**
 * Identifies if two names are a match according to consonant comparison.
 * 
 * @param nameOne - The first name used in the consonant comparison
 * @param nameTwo - The second name used in the consonant comparison
 * @param wordCombos - The word combos of the names, as found in compare_spelling
 * @returns Whether the two names are a match, according to consonant comparison
 */
function _consonantComparison(nameOne: string, nameTwo: string, wordCombos: [string, string, number][]): [boolean, number] {
    // Setup

    console.error(`Comparing consonants for ${nameOne} and ${nameTwo} in TypeScript`);

    const minimumRequiredMatches = wordCombos.length;
    let numberOfConsonantMatches = 0;
    let combinedScoresBasedOnConsonantFuzzyMatches = 0;
    let averageScore = 0;

    // Loop through every word match in the combo
    for (const tup of wordCombos) {
        // Get the matching word data
        const wordOne = nameOne.trim().split(/\s+/)[parseInt(tup[0])];
        const wordTwo = nameTwo.trim().split(/\s+/)[parseInt(tup[1])];
        const originalScoreForWords = Number(tup[2]);

        // Get the words as consonants
        const consonantsInNameOne = _reduceToSimpleConsonants(wordOne);
        const consonantsInNameTwo = _reduceToSimpleConsonants(wordTwo);
        const consonantRatio = fuzzball_ratio(consonantsInNameOne, consonantsInNameTwo, { full_process: false });

        console.error(`Consonants in each name in TypeScript - nameOne: ${consonantsInNameOne}  nameTwo: ${consonantsInNameTwo}`);
        console.error(`Consonant ratio in TypeScript: ${consonantRatio}`);
        
        // Continue if bad match
        if (originalScoreForWords <= guaranteedFailScore) {
            console.error("Below guaranteed fail score");
            continue;
        };
        if (wordOne.length !== 1 && wordTwo.length !== 1) { // # If neither word is an initial
            const lowestSyllableCount = mathjs_min(
                consonantsInNameOne.split('*').length - 1,
                consonantsInNameTwo.split('*').length - 1
            );
            console.error(`Lowest syllable count for words is ${lowestSyllableCount}`);
            if (lowestSyllableCount < 2) {
                console.error("Syllable count was too low");
                continue
            };
        };
        if (((consonantRatio < guaranteedPassingScore) || (originalScoreForWords < furtherChecksNeededScore)) && (consonantRatio !== maxScore)) {
            console.error(`Failed big check where consonantRatio = ${consonantRatio}, guaranteedPassingScore = ${guaranteedPassingScore}, originalScoreForWords = ${originalScoreForWords}, furtherChecksNeededScore = ${furtherChecksNeededScore}, and maxScore = ${maxScore}`);
            continue;
        };

        // If not rejected, increment the number of matches and increase the total score
        numberOfConsonantMatches = numberOfConsonantMatches + 1;
        combinedScoresBasedOnConsonantFuzzyMatches = combinedScoresBasedOnConsonantFuzzyMatches + consonantRatio;
    };

    // Find the average score of all of the matches, if relevant
    if (numberOfConsonantMatches > 0){
        averageScore = combinedScoresBasedOnConsonantFuzzyMatches / numberOfConsonantMatches;
    }

    // If there are enough matches, return true and a score. Otherwise return false and a score
    console.error(`Number of consonant matches in TypeScript: ${numberOfConsonantMatches}`);
    console.error(`Result of consonant comparison in TypeScript: ${[((numberOfConsonantMatches > minimumRequiredMatches) || (numberOfConsonantMatches >= numberOfValidCombosToSkipFurtherChecks)), averageScore]}`);
    return [((numberOfConsonantMatches > minimumRequiredMatches) || (numberOfConsonantMatches >= numberOfValidCombosToSkipFurtherChecks)), averageScore];
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
        .replace(/(.)\1+/g, `$1`);
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
export function pronunciationComparison(ipaOfNameOne: string, ipaOfNameTwo: string, nameOne: string, nameTwo: string): [boolean, [string, string, number][], number] {

    // Initialize empty list to store scores
    var wordsFromIpaOne = ipaOfNameOne.trim().split(/\s+/);
    var wordsFromIpaTwo = ipaOfNameTwo.trim().split(/\s+/);
    if (wordsFromIpaOne.length < wordsFromIpaTwo.length) {
        wordsFromIpaOne.push(...Array(wordsFromIpaTwo.length - wordsFromIpaOne.length).fill(null));
    } else if (wordsFromIpaOne.length > wordsFromIpaTwo.length) {
        wordsFromIpaTwo.push(...Array(wordsFromIpaOne.length - wordsFromIpaTwo.length).fill(null));
    };
    
    // Create a matrix of zeros using mathjs
    let scores = mathjs_matrix_function(mathjs_zeros([wordsFromIpaOne.length, wordsFromIpaTwo.length])) as mathjs_matrix_class;
    
    // Score each matchup
    var wordCombosForScores = findWordMatchesAndQuality(nameOne, nameTwo);
    _matchupScores(wordCombosForScores, scores, wordsFromIpaOne, wordsFromIpaTwo);
    
    // Identify the best matchups
    wordsFromIpaOne = wordsFromIpaOne.map((word, i) => word !== null ? String(i) : "");
    wordsFromIpaTwo = wordsFromIpaTwo.map((word, i) => word !== null ? String(i) : "");
    // This next line differs from the python version, but it's only due to TypeScript typing
    // shennanigans. It's functionally the same
    let scoreMatrix : number[][] = scores.toArray() as number[][];
    let wordCombos = identifyBestMatches(scoreMatrix, wordsFromIpaOne, wordsFromIpaTwo);
    // This defaults the minimum score to 0 if there is no real minimum score, or sets it to the smalles one otherwise
    const lowestScore = wordCombos.length > 0 ? mathjs_min(...wordCombos.map((tuple: [string, string, number]) => tuple[2])) : 0;
    
    // Return whether pronunciation match or not
    const minimumLength = mathjs_min(ipaOfNameOne.trim().split(/\s+/).length, ipaOfNameTwo.trim().split(/\s+/).length);
    if (minimumLength < lengthNeededForConditionallyPassingPronunciationComparison) {
        if (lowestScore >= guaranteedPassingScore) {
            return [true, wordCombos, lowestScore];
        };
        return [false, wordCombos, lowestScore];
    };
    if (minimumLength >= lengthNeededForConditionallyPassingPronunciationComparison) {
        if (lowestScore >= conditionallyPassingScore) {
            return [true, wordCombos, lowestScore];
        };
        return [false, wordCombos, lowestScore];
    };
    
    // Default return just in case something gets here
    return [false, wordCombos, lowestScore];
};

/**
 * Finds the score for the quality of each matchup of words that are potential matches, in terms of ipa
 * pronunciations. It then updates a list of scores to reflect this for later processing in the
 * pronunciation_comparison function.
 * 
 * @param wordCombosForScores - A list of word combinations that need to be scored
 * @param scores - A list of scores for all of the different word combinations
 * @param wordsFromIpaOne - A list of words that could match the ipa pronuncation of the first checked word
 * @param wordsFromIpaTwo - A list of words that could match the ipa pronuncation of the second checked word
 */
function _matchupScores(wordCombosForScores: [string, string, number][], scores: mathjs_matrix_class, wordsFromIpaOne: string[], wordsFromIpaTwo: string[]): void{

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
            let score = _scoreWordCombosHelper(wordOne, wordTwo, indexOne, indexTwo, wordCombosForScores);
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
 * @param wordCombosForScores - A list of words that could match the ipa pronuncation of the second checked word
 * 
 * @returns The score that should be set for a particular word combo
 */
function _scoreWordCombosHelper(wordOne: string, wordTwo: string, indexOne: number, indexTwo: number, wordCombosForScores: [string, string, number][]): number {

    let score = fuzzball_ratio(wordOne, wordTwo, { full_process: false });
    for (let i = 0; i < wordCombosForScores.length; i++){
        const [wordCombosForScoresIndexOne, wordCombosForScoresIndexTwo, initialScore] = wordCombosForScores[i];
        // Use initial score for initials (bad pun)
        if (indexOne === parseInt(wordCombosForScoresIndexOne) && indexTwo === parseInt(wordCombosForScoresIndexTwo) && (initialScore === 100 || initialScore === 0)) {
            score = initialScore;
        };
    };

    return score;
};