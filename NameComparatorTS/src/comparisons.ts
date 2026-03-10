import * as fuzzball from "fuzzball";
import { identifyBestMatchups, findWhichWordsMatchAndHowWell } from "./usefulTools";
import * as math from 'mathjs';

/**
 * Identifies if two names are a match according to a comparison based soley on spelling.
 * 
 * @param nameA - a name
 * @param nameB - a name
 * 
 * @returns whether the names are a match, and the resulting word combo
 */
export function spellingComparison(nameA: string, nameB: string): [boolean, any[]] {
    const wordCombo = findWhichWordsMatchAndHowWell(nameA, nameB);
    const count = wordCombo.filter(tup => tup[2] > 80).length;
    const minLength = Math.min(nameA.split(' ').length, nameB.split(' ').length);
    if (count >= 3 || count === minLength) {
        return [true, wordCombo];
    }
    // const [match, combo] = _consonantComparison(nameA, nameB);
    if (_consonantComparison(nameA, nameB)) {
        return [true, wordCombo];
    }
    return [false, wordCombo];
}

/**
 * Identifies if two names are a match according to consonant comparison.
 * 
 * @param nameA - a name
 * @param nameB - a name
 * 
 * @returns whether the two names are a match according to consonant comparison
 */
function _consonantComparison(nameA: string, nameB: string): boolean {
    const wordCombo = findWhichWordsMatchAndHowWell(nameA, nameB);
    const minRequiredMatches = wordCombo.length;
    let numWordConsonantMatches = 0;

    //const updatedWordCombos: [string, string, number][] = [];
    for (const tup of wordCombo) {
        const wordA = nameA.split(' ')[parseInt(tup[0])];
        const wordB = nameB.split(' ')[parseInt(tup[1])];
        const originalScoreForWords = Number(tup[2]);

        const consonantsNameA = _reduceToSimpleConsonants(wordA);
        const consonantsNameB = _reduceToSimpleConsonants(wordB);
        const consonantsRatio = fuzzball.ratio(consonantsNameA, consonantsNameB);
        //updatedWordCombos.push([consonantsNameA, consonantsNameB, consonantsRatio]);
        
        if (originalScoreForWords <= 30) continue;
        if (wordA.length !== 1 && wordB.length !== 1) {
            const lowestSyllableCount = Math.min(
                consonantsNameA.split('я').length - 1,
                consonantsNameB.split('я').length - 1
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
 * @param ipaOfNameA - the ipa of a name
 * @param ipaOfNameB - the ipa of a name
 * @param nameA - a name
 * @param nameB - a name
 * 
 * @returns whether the names are a match, and the resulting word combo
 */
export function pronunciationComparison(ipaOfNameA: string, ipaOfNameB: string, nameA: string, nameB: string): [boolean, [string, string, number][]] {

    // Initialize empty list to store scores
    var ipaWordsA = ipaOfNameA.split(/\s+/);
    var ipaWordsB = ipaOfNameB.split(/\s+/);
    if (ipaWordsA.length < ipaWordsB.length) {
        ipaWordsA.push(...Array(ipaWordsB.length - ipaWordsA.length).fill(null));
    }
    else if (ipaWordsA.length > ipaWordsB.length) {
        ipaWordsB.push(...Array(ipaWordsA.length - ipaWordsB.length).fill(null));
    }
    
    // Create a matrix of zeros using mathjs
    const scores = math.matrix(math.zeros([ipaWordsA.length, ipaWordsB.length])) as math.Matrix;
    
    // Score each matchup
    var wordCombo = findWhichWordsMatchAndHowWell(nameA, nameB);
    for (let indexA = 0; indexA < ipaWordsA.length; indexA++) {
        for (let indexB = 0; indexB < ipaWordsB.length; indexB++) {
            // Assign a default very low score for dummy pairings
            scores.set([indexA, indexB], -1e9);
            
            const wordA = ipaWordsA[indexA];
            const wordB = ipaWordsB[indexB];
            
            if (wordA === null || wordB === null) {
                continue;
            }
            
            // Reassign the default score to all real pairings
            let score = fuzzball.ratio(wordA, wordB);
            
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
    const minLength = Math.min(ipaOfNameA.split(/\s+/).length, ipaOfNameB.split(/\s+/).length);
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