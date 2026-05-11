import { ratio as fuzzball_ratio, partial_ratio as fuzzball_partial_ratio} from 'fuzzball';
import munkres from 'munkres-js';
import memoize from 'memoizee';
import { string } from 'mathjs';
import { getIpa } from './ipa.js';

// Note here that memoizee (and the memoize function) is the typescript equivalent of lru cache in python
export const findWordMatchesAndQuality = memoize(findWordMatchesAndQualityUnmemoized, {max: 1000});
/**
 * Identifies which words in either name are a match, and how well they match.
 * 
 * @param nameOne - The first name to check for matches
 * @param nameTwo - The second name to check for matches
 * @returns A list of tuples idenifying the index of the word in the first name,
            the index of the word in the second name, and the score of how well they match
 */
function findWordMatchesAndQualityUnmemoized(nameOne:string, nameTwo:string) : [string, string, number][] {

    console.error(`Entering TypeScript findWordMatchesAndQuality function with the names ${nameOne} and ${nameTwo}`);

    // Initialize empty list to store scores
    let wordsInNameOne : string[] = nameOne.trim().split(/\s+/);
    let wordsInNameTwo : string[] = nameTwo.trim().split(/\s+/);
    if (wordsInNameOne.length !== wordsInNameTwo.length) {
        if (wordsInNameOne.length < wordsInNameTwo.length) {
            wordsInNameOne = wordsInNameOne.concat(new Array(wordsInNameTwo.length - wordsInNameOne.length).fill(""));
        } else {
            wordsInNameTwo = wordsInNameTwo.concat(new Array(wordsInNameOne.length - wordsInNameTwo.length).fill(""));
        };
    };

    // Initialize an array of the proper size, filled with zeros
    let scores: number[][] = Array.from({ length: wordsInNameOne.length }, () =>
        new Array(wordsInNameTwo.length).fill(0)
    );

    console.error(`Found the list of words in the names in TypeScript. \nwordsInNameOne: ${wordsInNameOne} \nwordsInNameTwo: ${wordsInNameTwo}`);

    // Score each matchup
    for (let i = 0; i < wordsInNameOne.length; i++) {
        const wordOne = wordsInNameOne[i];
        for (let j = 0; j < wordsInNameTwo.length; j++) {
            const wordTwo = wordsInNameTwo[j];
            // Assign a very low finite score to dummy pairings
            scores[i][j] = -1e9
            if (wordOne === null || wordTwo === null || wordOne === "" || wordTwo === "") {
                continue;
            };
            // Determine the score of the word pairing
            const score = _determineScoreOfWordMatchup(wordOne, wordTwo);
            console.error(`TypeScript determined score of matchup for ${wordOne} and ${wordTwo} for this run is ${score}`)
            // Add the score
            scores[i][j] = score;
        };
    };
    
    const finalWordsInNameOne = wordsInNameOne.map((word, i) => ((word !== null && word !== '') ? String(i) : ''));
    const finalWordsInNameTwo = wordsInNameTwo.map((word, i) => ((word !== null && word !== '') ? String(i) : ''));        
    return identifyBestMatches(scores, finalWordsInNameOne, finalWordsInNameTwo);
};

/**
 * This is a helper function for findWordMatchesAndQuality to fix its
 * nesting depth. What it does is it takes in a word and an integer
 * representation of a list position for two different words. Then it
 * determines how closely the words match each other and assigns them a
 * score according to that. 
 * 
 * @param wordOne - The first word used in the comparison and scoring
 * @param wordTwo - The second word used in the comparison and scoring
 * 
 * @returns An integer representing the score to be added to the word pairing
 */
function _determineScoreOfWordMatchup(wordOne: string, wordTwo: string): number {

    let score: number;
    // If either of the scores is empty, it should be fine to say it's a match
    // with the empty space
    if (wordOne.length === 0 || wordTwo.length === 0) {
        score = 100;

    } else if (wordOne.length === 1 || wordTwo.length === 1) { // Assign the score this way if either is initial
        score = wordOne[0] === wordTwo[0] ? 100 : 0;

    } else { // For words longer than 2, either use ratio or partial ratio for score as shown below.
        const ratio = fuzzball_ratio(wordOne, wordTwo, {useCollator: false, full_process: false});
        if (wordOne[0] === wordTwo[0]) {
            const partialRatioScore = partialRatioWithParity(wordOne, wordTwo);
            console.error(`Found the partial ratio ${partialRatioScore} for ${wordOne} and ${wordTwo} in TypeScript`)
            score = Math.max(ratio, partialRatioScore);
        } else {
            score = ratio;
        };
    };

    return score;
}

/**
 * Uses the Hungarian algorithm to find the pair of two words that are the
 * closest match to each other from two lists.
 * 
 * @param scores - the scores of acertain matchup
 * @param listOne - a list of indices as strings or null
 * @param listTwo - a list of indices as strings or null
 * 
 * @returns A list of lists containing the two words that are the best match 
 *          and a score representing how closely they match
 */
export function identifyBestMatches(scores: number[][], listOne: string[], listTwo: string[]) : [string, string, number][] {
// Note that as a part of updating this function, I opted for a more well-tested external
// package for our hungarian algorithm (also known as the munkres algorithm). If it is
// ever necessary to revert for some reason, see the hungarian.ts file before any of the
// changes made on 3/16/2026
    console.error(`Input lists for identify matches in TypeScript: \nlistOne: ${listOne} \nlistTwo: ${listTwo}`);
    const modifiedScores = tiebreakMatchesConsistently(scores);
    console.error(`Making sure that matches tiebreak as expected. TypeScript tiebroken scores: ${modifiedScores}`);
    const negatedScores = modifiedScores.map(row => row.map(score => -score));
    console.error(`Checking that negated scores look the same in TypeScript: ${negatedScores}`);
    const hungarian_pairs_list = munkres(negatedScores);
    console.error(`Hungarian pairs list in TypeScript: \n${hungarian_pairs_list}`);
    let bestCombination: [string, string, number][] = [];
    for (let index = 0; index < hungarian_pairs_list.length; index++) {
        const i = hungarian_pairs_list[index][0];
        const j = hungarian_pairs_list[index][1];
    
        const wordOne = listOne[i];
        const wordTwo = listTwo[j];
        // This first if statement quickly removes any possible out of scope results from the matrix padding
        if (i >= listOne.length || j >= listTwo.length){
            continue;
        } else if (wordOne !== null && wordTwo !== null && wordOne !== "" && wordTwo !== "") {
          const matchupScore = scores[i][j];
          bestCombination.push([wordOne, wordTwo, matchupScore]);
        };
    };

    return bestCombination;
};

/**
 * Calculates how much editing a name or both names improved the score in comparision to the original names.
 * 
 * @param nameOne - the original first name
 * @param nameTwo - the original second name
 * @param nameOneEdited - the edited first name
 * @param nameTwoEdited - the edited second name
 * 
 * @returns The score of how much the edits improved the comparison (can be negative),
 *          the word combos of the original, and the word combos of the edited version
 */
export function calculateEditImprovement(nameOne : string, nameTwo : string, nameOneEdited :string, nameTwoEdited : string): [number, [string, string, number][], [string, string, number][]] {
    let nameOneIpa = getIpa(nameOne);
    let nameTwoIpa = getIpa(nameTwo);
    let originalWordCombos = findWordMatchesAndQuality(nameOneIpa, nameTwoIpa);
    let nameOneEditedIpa = getIpa(nameOneEdited);
    let nameTwoEditedIpa = getIpa(nameTwoEdited)
    let editedWordCombos = findWordMatchesAndQuality(nameOneEditedIpa, nameTwoEditedIpa);
    if(!originalWordCombos.length || !editedWordCombos.length) {
        return [0, originalWordCombos, editedWordCombos]
    };
    const originalAverageScore = originalWordCombos.reduce((sum, [, , score]) => sum + score, 0) / originalWordCombos.length;
    const editedAverageScore = editedWordCombos.reduce((sum, [, , score]) => sum + score, 0) / editedWordCombos.length;
    const diff = editedAverageScore - originalAverageScore;

    console.error(`End result of calculating edit improvements in TypeScript: nameOne - ${nameOne} nameOneIpa - ${nameOneIpa} nameTwo - ${nameTwo} nameTwoIpa - ${nameTwoIpa} originalAverageScore - ${originalAverageScore} nameOneEdited - ${nameOneEdited} nameOneEditedIpa - ${nameOneEditedIpa} nameTwoEdited - ${nameTwoEdited} nameTwoEditedIpa - ${nameOneEditedIpa} editedAverageScore - ${editedAverageScore} diff - ${diff}`);
    return [diff, originalWordCombos, editedWordCombos];
};

/**
 * Identifies which words in the names match and finds their indices.
 * 
 * @param nameOne - The first name to check for matches in
 * @param nameTwo - The second name to check for matches in
 * 
 * @returns A list of lists containing which words match. Each contained list has the index of a matching word 
 *          in name_one, the index of a matching word in name_two, the matching word in name_one, and the matching 
 *          word in name_two
 */
export function getMatchingWordsAndIndices(nameOne : string, nameTwo : string): [number, number, string, string][] {
    let combo = findWordMatchesAndQuality(nameOne, nameTwo);
    let wordsInNameOne = nameOne.trim().split(/\s+/);
    let wordsInNameTwo = nameTwo.trim().split(/\s+/);
    let matchIndices : [number, number][] = combo.map(
        ([a, b]) => [parseInt(a), parseInt(b)]
    );

    let matchIndicesWithWords:[number, number, string, string][] = [];

    for (let i = 0; i < matchIndices.length; i++){
        if ((matchIndices[i][0] < wordsInNameOne.length) && (matchIndices[i][1] < wordsInNameTwo.length)) {
            matchIndicesWithWords.push([matchIndices[i][0], matchIndices[i][1], wordsInNameOne[matchIndices[i][0]], wordsInNameTwo[matchIndices[i][1]]]);
        };
    };
    
    return matchIndicesWithWords;
};

/**
 * A class used for ease of editing specific words in names.
 */
export class NameEditor {
    private wordsInNameOne : string[];
    private wordsInNameTwo : string[];

    /**
     * Splits the words for later editing
     * 
     * @param nameOne - The first name to edit
     * @param nameTwo - The second name to edit
     */
    constructor(nameOne : string, nameTwo : string){
        this.wordsInNameOne = nameOne.trim().split(/\s+/);
        this.wordsInNameTwo = nameTwo.trim().split(/\s+/);
    };

    /**
     * Replaces the stored word for nameOne at the specified index.
     * 
     * @param index - The specified index
     * @param updatedWord - The replacement string
     */
    public updateNameOne(index : number, updatedWord : string) {
        this.wordsInNameOne[index] = updatedWord;
    };

    /**
     * Replaces the stored word for nameTwo at the specified index.
     * 
     * @param index - The specified index
     * @param updatedWord - The replacement string
     */
    public updateNameTwo(index : number, updatedWord : string) {
        this.wordsInNameTwo[index] = updatedWord;
    };

    /**
     * Retrieves the modified names
     * 
     * @returns The fist modified name and the second modified name
     */
    public getModifiedNames() : [string, string]{
        let nameOne = this.wordsInNameOne.join(' ');
        let nameTwo = this.wordsInNameTwo.join(' ');
        if (!nameOne) {
            nameOne = '_';
        };
        if (!nameTwo) {
            nameTwo = '_';
        };
    
        return [nameOne, nameTwo];
    };
};

export function partialRatioWithParity(stringOne: string, stringTwo:string): number{

    if (stringOne.length > stringTwo.length){
        [stringOne, stringTwo] = [stringTwo, stringOne];
    };
    var bestScore = 0;
    for(var i = 0; i < ((stringTwo.length - stringOne.length) + 1); i++){
        var window = stringTwo.slice(i,i + stringOne.length);
        var newScore = indelNormalizedSimilarity(stringOne, window) * 100;
        console.error(`New score in TypeScript: ${newScore}`);
        bestScore = Math.max(bestScore, newScore);
    };

    return Math.round(bestScore);
};

function tiebreakMatchesConsistently(inputMatrix: number[][], epsilonValue: number = 1e-3){
    const rows = inputMatrix.length;
    const columns = inputMatrix[0].length;
    return inputMatrix.map((row, i) =>
        // There is a match bonus in the Python version. It is functionally the same as
        // this line of code but looks different due to language differences
        row.map((val, j) => val + epsilonValue * ((columns - j) * rows + i) + (i === j ? 0.005 : 0))
    );
};

// This is needed to ensure parity with a Python function's behavior
function indelNormalizedSimilarity(a: string, b: string): number {
  const dp: number[][] = Array.from({ length: a.length + 1 }, (_, i) =>
    Array.from({ length: b.length + 1 }, (_, j) => (i === 0 ? j : j === 0 ? i : 0))
  );

  for (let i = 1; i <= a.length; i++) {
    for (let j = 1; j <= b.length; j++) {
      if (a[i - 1] === b[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1];
      } else {
        dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1]); // insert or delete only, no substitution
      };
    };
  };

  const editDistance = dp[a.length][b.length];
  return 1 - editDistance / (a.length + b.length);
};
