import * as fuzzball from 'fuzzball';
import { hungarianAlgorithm } from './hungarian';

/**
 * Identifies which words in either name are a match, and how well they match.
 * 
 * @param nameA (string) - a name 
 * @param nameB (string)- a name
 * @returns [string, string, number][]: a list of tuples idenifying the index of the word in the first name,
            the index of the word in the second name, and the score of how well they match
 */
export function findWhichWordsMatchAndHowWell(nameA:string, nameB:string) : [string, string, number][] {

        let wordsInA : string[] = nameA.split(/\s+/);
        let wordsInB : string[] = nameB.split(/\s+/);
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
            const wordA = wordsInA[i];
            for (let j = 0; j < wordsInB.length; j++) {
                const wordB = wordsInB[j];
                
                scores[i][j] = -1e9
                if (wordA == null || wordB == null) {
                    continue;
                }
            
                let score: number;
                if (wordA.length === 1 || wordB.length === 1) {
                    score = wordA[0] === wordB[0] ? 100 : 0;
                } else {
                    const ratio = fuzzball.ratio(wordA, wordB);
                    if (wordA[0] === wordB[0]) {
                        const prScore = fuzzball.partial_ratio(wordA, wordB);
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
    
        const wordA = listA[i];
        const wordB = listB[j];
        // Check if both listA[i] and listB[j] are not null
        if (wordA !== "" && wordB !== "") {
          const matchupScore = scores[i][j];
          bestCombination.push([wordA, wordB, matchupScore]);
        }
    }

    return bestCombination;
}

/**
 * Calculated how much editing a name or both names improved the score in comparision to the original names.
 * 
 * @param nameA (string) - the original first name
 * @param nameB (string) - the original second name
 * @param nameAEdited (string) - the edited first name
 * @param nameBEdited (string) - the edited second name
 * 
 * @returns [float, tuple, tuple]: the score of how much the edits improved the comparison (can be negative),
 *          the word combo of the original, the word combo of the edited version
 */
export function calculateEditImprovement(nameA : string, nameB : string, nameAEdited :string, nameBEdited : string): [number, [string, string, number][], [string, string, number][]] {
    let ogWordCombo = findWhichWordsMatchAndHowWell(nameA, nameB);
    let editedWordCombo = findWhichWordsMatchAndHowWell(nameAEdited, nameBEdited);
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
 * @param nameA (string) - a name
 * @param nameB (string) - a name
 * 
 * @returns [int, int, string, string][] - the list of which words match. Tuples of: the index of word in nameA, the index of word in nameB, in word in nameA, the word in nameB
 */
export function getPairIndicesAndWords(nameA : string, nameB : string): [number, number, string, string][] {
    let combo = findWhichWordsMatchAndHowWell(nameA, nameB);
    let wordsInA = nameA.split(/\s+/);
    let wordsInB = nameB.split(/\s+/);
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
     * @param nameA (string) - a name
     * @param nameB (string) - a name
     */
    constructor(nameA : string, nameB : string){
        this.wordsInA = nameA.split(' ');
        this.wordsInB = nameB.split(' ');
    }

    /**
     * Replaces the stored word for nameA at the specified index.
     * 
     * @param index (number) - the specified index
     * @param updatedWord (string) - the rplacement string
     */
    public updateNameA(index : number, updatedWord : string) {
        this.wordsInA[index] = updatedWord;
    }

    /**
     * Replaces the stored word for nameA at the specified index.
     * 
     * @param index (number) - the specified index
     * @param updatedWord (string) - the rplacement string
     */
    public updateNameB(index : number, updatedWord : string) {
        this.wordsInB[index] = updatedWord;
    }

    /**
     * Retrieves the modified names
     * 
     * @returns [string, string] - the modified names
     */
    public getModifiedNames() : [string, string]{
        let nameA = this.wordsInA.join(' ');
        let nameB = this.wordsInB.join(' ');
        if (!nameA) {
            nameA = '_';
        }
        if (!nameB) {
            nameB = '_';
        }
    
        return [nameA, nameB];
    }
}

