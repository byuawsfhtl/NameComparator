import * as fuzzball from 'fuzzball';
import { hungarianAlgorithm } from './hungarian';

/**
 * Identifies which words in either name are a match, and how well they match.
 * 
 * @param nameOne (string) - a name 
 * @param nameTwo (string)- a name
 * @returns [string, string, number][]: a list of tuples idenifying the index of the word in the first name,
            the index of the word in the second name, and the score of how well they match
 */
export function findWhichWordsMatchAndHowWell(nameOne:string, nameTwo:string) : [string, string, number][] {

        let wordsInA : string[] = nameOne.split(/\s+/);
        let wordsInB : string[] = nameTwo.split(/\s+/);
        if (wordsInA.length !== wordsInB.length) {
            if (wordsInA.length < wordsInB.length) {
              wordsInA = wordsInA.concat(new Array(wordsInB.length - wordsInA.length).fill(""));
            } else {
              wordsInB = wordsInB.concat(new Array(wordsInA.length - wordsInB.length).fill(""));
            }
        }

        let scores: number[][] = Array.from({ length: wordsInA.length }, () =>
            new Array(wordsInB.length).fill(0)
        );

        for (let i = 0; i < wordsInA.length; i++) {
            const wordOne = wordsInA[i];
            for (let j = 0; j < wordsInB.length; j++) {
                const wordTwo = wordsInB[j];
                
                scores[i][j] = -1e9
                if (wordOne == null || wordTwo == null) {
                    continue;
                }
            
                let score: number;
                if (wordOne.length === 1 || wordTwo.length === 1) {
                    score = wordOne[0] === wordTwo[0] ? 100 : 0;
                } else {
                    const ratio = fuzzball.ratio(wordOne, wordTwo);
                    if (wordOne[0] === wordTwo[0]) {
                        const prScore = fuzzball.partial_ratio(wordOne, wordTwo);
                        score = Math.max(ratio, prScore);
                    } else {
                        score = ratio;
                    }
                }
            
                scores[i][j] = score;
            }
        }  
        const indexedA = wordsInA.map((word, i) => (word !== '' ? String(i) : ''));
        const indexedB = wordsInB.map((word, i) => (word !== '' ? String(i) : ''));        
        return identifyBestMatchups(scores, indexedA, indexedB);
}

/**
 * Uses Hungarian algorithm to find the optimal assignments.
 * 
 * @param scores (number[][]) - the scores of acertain matchup
 * @param listA ((string | null)[]) - a list of indices as strings or null
 * @param listB ((string | null)[]) - a list of indices as strings or null
 * 
 * @returns [string, string, number][]: the word combo
 */
export function identifyBestMatchups(scores: number[][], listA: string[], listB: string[]) : [string, string, number][] {

    const negatedScores = scores.map(row => row.map(score => -score));
    let [rowInd, colInd] = hungarianAlgorithm(negatedScores);
    let bestCombination: [string, string, number][] = [];
    for (let idx = 0; idx < rowInd.length; idx++) {
        const i = rowInd[idx];
        const j = colInd[idx];
    
        const wordOne = listA[i];
        const wordTwo = listB[j];
        // Check if both listA[i] and listB[j] are not null
        if (wordOne !== "" && wordTwo !== "") {
          const matchupScore = scores[i][j];
          bestCombination.push([wordOne, wordTwo, matchupScore]);
        }
    }

    return bestCombination;
}

/**
 * Calculated how much editing a name or both names improved the score in comparision to the original names.
 * 
 * @param nameOne (string) - the original first name
 * @param nameTwo (string) - the original second name
 * @param nameOneEdited (string) - the edited first name
 * @param nameTwoEdited (string) - the edited second name
 * 
 * @returns [float, tuple, tuple]: the score of how much the edits improved the comparison (can be negative),
 *          the word combo of the original, the word combo of the edited version
 */
export function calculateEditImprovement(nameOne : string, nameTwo : string, nameOneEdited :string, nameTwoEdited : string): [number, [string, string, number][], [string, string, number][]] {
    let ogWordCombo = findWhichWordsMatchAndHowWell(nameOne, nameTwo);
    let editedWordCombo = findWhichWordsMatchAndHowWell(nameOneEdited, nameTwoEdited);
    if(!ogWordCombo.length || !editedWordCombo.length) {
        return [0, ogWordCombo, editedWordCombo]
    }
    const ogAverageScore = ogWordCombo.reduce((sum, [, , score]) => sum + score, 0) / ogWordCombo.length;
    const editedAverageScore = editedWordCombo.reduce((sum, [, , score]) => sum + score, 0) / editedWordCombo.length;
    const diff = editedAverageScore - ogAverageScore;

    return [diff, ogWordCombo, editedWordCombo]
}

/**
 * Identifies which words in the names match.
 * 
 * @param nameOne (string) - a name
 * @param nameTwo (string) - a name
 * 
 * @returns [int, int, string, string][] - the list of which words match. Tuples of: the index of word in nameOne, the index of word in nameTwo, in word in nameOne, the word in nameTwo
 */
export function getMatchingWordsAndIndices(nameOne : string, nameTwo : string): [number, number, string, string][] {
    let combo = findWhichWordsMatchAndHowWell(nameOne, nameTwo);
    let wordsInA = nameOne.split(/\s+/);
    let wordsInB = nameTwo.split(/\s+/);
    let matchIndices : [number, number][] = combo.map(
        ([a, b]) => [parseInt(a), parseInt(b)]
    );
    const matchIndicesWithWords = matchIndices.map(([i, j]) => [
        i,
        j,
        wordsInA[i],
        wordsInB[j]
    ] as [number, number, string, string]);
    
    return matchIndicesWithWords
}

/**
 * A class a-used for ease of editing specific words in names.
 */
export class NameEditor {
    private wordsInA : string[];
    private wordsInB : string[];

    /**
     * Splits the words for later editing
     * 
     * @param nameOne (string) - a name
     * @param nameTwo (string) - a name
     */
    constructor(nameOne : string, nameTwo : string){
        this.wordsInA = nameOne.split(' ');
        this.wordsInB = nameTwo.split(' ');
    }

    /**
     * Replaces the stored word for nameOne at the specified index.
     * 
     * @param index (number) - the specified index
     * @param updatedWord (string) - the rplacement string
     */
    public updateNameOne(index : number, updatedWord : string) {
        this.wordsInA[index] = updatedWord;
    }

    /**
     * Replaces the stored word for nameOne at the specified index.
     * 
     * @param index (number) - the specified index
     * @param updatedWord (string) - the rplacement string
     */
    public updateNameTwo(index : number, updatedWord : string) {
        this.wordsInB[index] = updatedWord;
    }

    /**
     * Retrieves the modified names
     * 
     * @returns [string, string] - the modified names
     */
    public getModifiedNames() : [string, string]{
        let nameOne = this.wordsInA.join(' ');
        let nameTwo = this.wordsInB.join(' ');
        if (!nameOne) {
            nameOne = '_';
        }
        if (!nameTwo) {
            nameTwo = '_';
        }
    
        return [nameOne, nameTwo];
    }
}

