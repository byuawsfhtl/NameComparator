import * as fuzzball from "fuzzball";
import { identifyBestMatches, findWordMatchesAndQuality } from "./usefulTools";
import * as math from 'mathjs';

/**
 * Identifies if two names are a match according to a comparison based soley on spelling.
 * 
 * @param nameOne - a name
 * @param nameTwo - a name
 * 
 * @returns whether the names are a match, and the resulting word combo
 */
export function compareSpelling(nameOne: string, nameTwo: string): [boolean, any[]] {
    const wordCombo = findWordMatchesAndQuality(nameOne, nameTwo);
    const count = wordCombo.filter(tup => tup[2] > 80).length;
    const minimumLength = Math.min(nameOne.split(' ').length, nameTwo.split(' ').length);
    if (count >= 3 || count === minimumLength) {
        return [true, wordCombo];
    }
    // const [match, combo] = _consonantComparison(nameOne, nameTwo);
    if (_consonantComparison(nameOne, nameTwo)) {
        return [true, wordCombo];
    }
    return [false, wordCombo];
}

/**
 * Identifies if two names are a match according to consonant comparison.
 * 
 * @param nameOne - a name
 * @param nameTwo - a name
 * 
 * @returns whether the two names are a match according to consonant comparison
 */
function _consonantComparison(nameOne: string, nameTwo: string): boolean {
    const wordCombo = findWordMatchesAndQuality(nameOne, nameTwo);
    const minimumRequiredMatches = wordCombo.length;
    let numberOfConsonantMatches = 0;

    //const updatedWordCombos: [string, string, number][] = [];
    for (const tup of wordCombo) {
        const wordOne = nameOne.split(' ')[parseInt(tup[0])];
        const wordTwo = nameTwo.split(' ')[parseInt(tup[1])];
        const originalScoreForWords = Number(tup[2]);

        const consonantsInNameOne = _reduceToSimpleConsonants(wordOne);
        const consonantsInNameTwo = _reduceToSimpleConsonants(wordTwo);
        const consonantRatio = fuzzball.ratio(consonantsInNameOne, consonantsInNameTwo);
        //updatedWordCombos.push([consonantsInNameOne, consonantsInNameTwo, consonantRatio]);
        
        if (originalScoreForWords <= 30) continue;
        if (wordOne.length !== 1 && wordTwo.length !== 1) {
            const lowestSyllableCount = Math.min(
                consonantsInNameOne.split('я').length - 1,
                consonantsInNameTwo.split('я').length - 1
            );
            if (lowestSyllableCount < 2) continue;
        }
        if (consonantRatio <= 80 || (originalScoreForWords <= 60 && consonantRatio !== 100)) continue;

        numberOfConsonantMatches++;
    }

    const match = numberOfConsonantMatches > minimumRequiredMatches || numberOfConsonantMatches >= 3;
    //return [ match, updatedWordCombos ];
    return match
}

/**
 * Reduces a string to the simple consonant components.
 * 
 * @param string - a string
 * 
 * @returns the consonant components
 */
function _reduceToSimpleConsonants(string: string): string {
    return string
        .replace(/[aeiouy]/g, 'я')
        .replace(/\я{2,}/g, 'я')
        .replace(/(.)\1+/g, '$1');
}

/**
 * Identifies if two names are a match according to a pronunciation comparison.
 * 
 * @param ipaOfNameOne - the ipa of a name
 * @param ipaOfNameTwo - the ipa of a name
 * @param nameOne - a name
 * @param nameTwo - a name
 * 
 * @returns whether the names are a match, and the resulting word combo
 */
export function pronunciationComparison(ipaOfNameOne: string, ipaOfNameTwo: string, nameOne: string, nameTwo: string): [boolean, [string, string, number][]] {

    // Initialize empty list to store scores
    var wordsFromIpaOne = ipaOfNameOne.split(/\s+/);
    var wordsFromIpaTwo = ipaOfNameTwo.split(/\s+/);
    if (wordsFromIpaOne.length < wordsFromIpaTwo.length) {
        wordsFromIpaOne.push(...Array(wordsFromIpaTwo.length - wordsFromIpaOne.length).fill(null));
    }
    else if (wordsFromIpaOne.length > wordsFromIpaTwo.length) {
        wordsFromIpaTwo.push(...Array(wordsFromIpaOne.length - wordsFromIpaTwo.length).fill(null));
    }
    
    // Create a matrix of zeros using mathjs
    const scores = math.matrix(math.zeros([wordsFromIpaOne.length, wordsFromIpaTwo.length])) as math.Matrix;
    
    // Score each matchup
    var wordCombo = findWordMatchesAndQuality(nameOne, nameTwo);
    for (let indexOne = 0; indexOne < wordsFromIpaOne.length; indexOne++) {
        for (let indexTwo = 0; indexTwo < wordsFromIpaTwo.length; indexTwo++) {
            // Assign a default very low score for dummy pairings
            scores.set([indexOne, indexTwo], -1e9);
            
            const wordOne = wordsFromIpaOne[indexOne];
            const wordTwo = wordsFromIpaTwo[indexTwo];
            
            if (wordOne === null || wordTwo === null) {
                continue;
            }
            
            // Reassign the default score to all real pairings
            let score = fuzzball.ratio(wordOne, wordTwo);
            
            for (const [wordComboIndexOne, wordComboIndexTwo, initialScore] of wordCombo) {
                // Use initial score for initials (bad pun)
                if (indexOne === parseInt(wordComboIndexOne) && indexTwo === parseInt(wordComboIndexTwo) && (initialScore === 100 || initialScore === 0)) {
                    score = initialScore;
                }
            }
            
            scores.set([indexOne, indexTwo], score);
        }
    }
    
    // Identify the best matchups
    wordsFromIpaOne = wordsFromIpaOne.map((word, i) => word !== null ? String(i) : "");
    wordsFromIpaTwo = wordsFromIpaTwo.map((word, i) => word !== null ? String(i) : "");
    
    let scoreMatrix : number[][] = scores.toArray() as number[][];
    wordCombo = identifyBestMatches(scoreMatrix, wordsFromIpaOne, wordsFromIpaTwo);
    const lowestScore = Math.min(...wordCombo.map((tuple: [string, string, number]) => tuple[2]));
    
    // Return whether pronunciation match or not
    const minimumLength = Math.min(ipaOfNameOne.split(/\s+/).length, ipaOfNameTwo.split(/\s+/).length);
    if (minimumLength <= 2) {
        if (lowestScore >= 80) {
            return [true, wordCombo];
        }
        return [false, wordCombo];
    }
    if (minimumLength > 2) {
        if (lowestScore > 75) {
            return [true, wordCombo];
        }
        return [false, wordCombo];
    }
    
    // Default return to satisfy TypeScript
    return [false, wordCombo];
}