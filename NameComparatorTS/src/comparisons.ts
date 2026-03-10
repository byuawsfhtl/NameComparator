import * as fuzzball from "fuzzball";
import { identifyBestMatchups, findWhichWordsMatchAndHowWell } from "./usefulTools";
import * as math from 'mathjs';

/**
 * Identifies if two names are a match according to a comparison based soley on spelling.
 * 
 * @param nameOne - a name
 * @param nameTwo - a name
 * 
 * @returns whether the names are a match, and the resulting word combo
 */
export function spellingComparison(nameOne: string, nameTwo: string): [boolean, any[]] {
    const wordCombo = findWhichWordsMatchAndHowWell(nameOne, nameTwo);
    const count = wordCombo.filter(tup => tup[2] > 80).length;
    const minLength = Math.min(nameOne.split(' ').length, nameTwo.split(' ').length);
    if (count >= 3 || count === minLength) {
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
    const wordCombo = findWhichWordsMatchAndHowWell(nameOne, nameTwo);
    const minRequiredMatches = wordCombo.length;
    let numWordConsonantMatches = 0;

    //const updatedWordCombos: [string, string, number][] = [];
    for (const tup of wordCombo) {
        const wordOne = nameOne.split(' ')[parseInt(tup[0])];
        const wordTwo = nameTwo.split(' ')[parseInt(tup[1])];
        const originalScoreForWords = Number(tup[2]);

        const consonantsnameOne = _reduceToSimpleConsonants(wordOne);
        const consonantsnameTwo = _reduceToSimpleConsonants(wordTwo);
        const consonantsRatio = fuzzball.ratio(consonantsnameOne, consonantsnameTwo);
        //updatedWordCombos.push([consonantsnameOne, consonantsnameTwo, consonantsRatio]);
        
        if (originalScoreForWords <= 30) continue;
        if (wordOne.length !== 1 && wordTwo.length !== 1) {
            const lowestSyllableCount = Math.min(
                consonantsnameOne.split('я').length - 1,
                consonantsnameTwo.split('я').length - 1
            );
            if (lowestSyllableCount < 2) continue;
        }
        if (consonantsRatio <= 80 || (originalScoreForWords <= 60 && consonantsRatio !== 100)) continue;

        numWordConsonantMatches++;
    }

    const match = numWordConsonantMatches > minRequiredMatches || numWordConsonantMatches >= 3;
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
 * @param ipaOfnameOne - the ipa of a name
 * @param ipaOfnameTwo - the ipa of a name
 * @param nameOne - a name
 * @param nameTwo - a name
 * 
 * @returns whether the names are a match, and the resulting word combo
 */
export function pronunciationComparison(ipaOfnameOne: string, ipaOfnameTwo: string, nameOne: string, nameTwo: string): [boolean, [string, string, number][]] {

    // Initialize empty list to store scores
    var ipaWordsA = ipaOfnameOne.split(/\s+/);
    var ipaWordsB = ipaOfnameTwo.split(/\s+/);
    if (ipaWordsA.length < ipaWordsB.length) {
        ipaWordsA.push(...Array(ipaWordsB.length - ipaWordsA.length).fill(null));
    }
    else if (ipaWordsA.length > ipaWordsB.length) {
        ipaWordsB.push(...Array(ipaWordsA.length - ipaWordsB.length).fill(null));
    }
    
    // Create a matrix of zeros using mathjs
    const scores = math.matrix(math.zeros([ipaWordsA.length, ipaWordsB.length])) as math.Matrix;
    
    // Score each matchup
    var wordCombo = findWhichWordsMatchAndHowWell(nameOne, nameTwo);
    for (let indexA = 0; indexA < ipaWordsA.length; indexA++) {
        for (let indexB = 0; indexB < ipaWordsB.length; indexB++) {
            // Assign a default very low score for dummy pairings
            scores.set([indexA, indexB], -1e9);
            
            const wordOne = ipaWordsA[indexA];
            const wordTwo = ipaWordsB[indexB];
            
            if (wordOne === null || wordTwo === null) {
                continue;
            }
            
            // Reassign the default score to all real pairings
            let score = fuzzball.ratio(wordOne, wordTwo);
            
            for (const [indexX, indexY, initialScore] of wordCombo) {
                // Use initial score for initials (bad pun)
                if (indexA === parseInt(indexX) && indexB === parseInt(indexY) && (initialScore === 100 || initialScore === 0)) {
                    score = initialScore;
                }
            }
            
            scores.set([indexA, indexB], score);
        }
    }
    
    // Identify the best matchups
    ipaWordsA = ipaWordsA.map((word, i) => word !== null ? String(i) : "");
    ipaWordsB = ipaWordsB.map((word, i) => word !== null ? String(i) : "");
    
    let scoreMatrix : number[][] = scores.toArray() as number[][];
    wordCombo = identifyBestMatchups(scoreMatrix, ipaWordsA, ipaWordsB);
    const lowestScore = Math.min(...wordCombo.map((tuple: [string, string, number]) => tuple[2]));
    
    // Return whether pronunciation match or not
    const minLength = Math.min(ipaOfnameOne.split(/\s+/).length, ipaOfnameTwo.split(/\s+/).length);
    if (minLength <= 2) {
        if (lowestScore >= 80) {
            return [true, wordCombo];
        }
        return [false, wordCombo];
    }
    if (minLength > 2) {
        if (lowestScore > 75) {
            return [true, wordCombo];
        }
        return [false, wordCombo];
    }
    
    // Default return to satisfy TypeScript
    return [false, wordCombo];
}