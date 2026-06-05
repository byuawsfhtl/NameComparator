import { ratio as fuzzball_ratio, partial_ratio as fuzzball_partial_ratio} from 'fuzzball';
import munkres from 'munkres-js';
import memoize from 'memoizee';
import { string } from 'mathjs';
import { getIpa } from './ipa.js';
import { warn } from 'console';

// Note here that memoizee (and the memoize function) is the typescript equivalent of lru cache in python
export const findWordMatchesAndQuality = memoize(findWordMatchesAndQualityUnmemoized, {max: 1000});
/**
 * Identifies which words in either name are a match, and how well they match.
 * 
 * @param nameOne - The first name to check for matches
 * @param nameTwo - The second name to check for matches
 * @returns A list of lists idenifying the index of the word in the first name,
 *          the index of the word in the second name, and the score of how well 
 *          they match. After that it returns a value representing the number 
 *          of possible prefixes and other odd exceptions in the name
 */
function findWordMatchesAndQualityUnmemoized(nameOne:string, nameTwo:string) : [[string, string, number][], number] {

    console.error(`Entering TypeScript findWordMatchesAndQuality function with the names ${nameOne} and ${nameTwo}`);

    // Initialize a variable for exceptions regarding possible prefixes and warning flags we can ignore
    let exceptionCount = 0;

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

    // We need to keep track of the matchups that return an initial in case there is another, more complete match
    let scoreWarnings = [];
    let notInitialNearlyPerfectScores = [];

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
            const [score, warning] = _determineScoreOfWordMatchup(wordOne, wordTwo);
            console.error(`TypeScript determined score of matchup for ${wordOne} and ${wordTwo} for this run is ${score} and that the warning value is ${warning}`);
            if (warning === true){
                scoreWarnings.push([i, j]);
            } else if (score >= 95){
                notInitialNearlyPerfectScores.push([i, j]);
            };
            // Add the score
            scores[i][j] = score;
        };
    };

    // This ensures that in a name pair like ben l love and ben del love the two loves will
    // be a better match than l and love, which is also technically a 100 but less accurate
    // than 'love' and 'love'
    for (const warningToCheck of scoreWarnings){
        console.error(`Performing warning check with the following variables in TypeScript: warningToCheck - ${warningToCheck} notInitialNearlyPerfectScores - ${notInitialNearlyPerfectScores}`);
        // If there's a perfect full name match, we want to penalize the score of the initial
        // since we want the other nearly perfect matches to take priority
        if ((notInitialNearlyPerfectScores.length >= 1) && (notInitialNearlyPerfectScores.some(specificScore => warningToCheck[0] === specificScore[0]))){
            console.error("Failed the first warning check segment in TypeScript");
            scores[warningToCheck[0]][warningToCheck[1]] = 0;
        } else if ((notInitialNearlyPerfectScores.length >= 2) && (notInitialNearlyPerfectScores.some(specificScore => warningToCheck[1] === specificScore[1]))){
            console.error("Failed the second warning check segment in TypeScript");
            scores[warningToCheck[0]][warningToCheck[1]] = 0;
        // If both of those are fine, we can likely add this warning as a possible odd exception
        } else if ((wordsInNameOne[warningToCheck[0]][0] === wordsInNameTwo[warningToCheck[1]][0]) && (wordsInNameOne[warningToCheck[0]].length === wordsInNameTwo[warningToCheck[1]].length)){
            scores[warningToCheck[0]][warningToCheck[1]] = 100;
        } else if (wordsInNameOne[warningToCheck[0]][0] === wordsInNameTwo[warningToCheck[1]][0]){
            scores[warningToCheck[0]][warningToCheck[1]] = 85;
        };
    };
    
    // Identify the best matchups
    const finalWordsInNameOne = wordsInNameOne.map((word, i) => ((word !== null && word !== '') ? String(i) : ''));
    const finalWordsInNameTwo = wordsInNameTwo.map((word, i) => ((word !== null && word !== '') ? String(i) : ''));

    const bestCombinations = identifyBestMatches(scores, finalWordsInNameOne, finalWordsInNameTwo);

    // For each of the best combinations, we now need to note how many are a combo containing a possible prefix
    const possiblePrefixes = [
        "d'", "de", "fi", "santa", "san", "de la", "de los", "del", "la", "le", "du", "dela", "los", 
        "der", "den", "vanden", "vander", "vande", "van", "von", 'di', 'dil', 'mc', 'mac'
    ];
    for (const foundCombination of bestCombinations){
        console.error(`Checking the combination ${foundCombination} for prefixes in TypeScript`);
        if ((((possiblePrefixes.includes(wordsInNameOne[Number(foundCombination[0])])) === true) || (possiblePrefixes.includes(wordsInNameTwo[Number(foundCombination[1])]) === true)) && (wordsInNameOne[Number(foundCombination[0])] != wordsInNameTwo[Number(foundCombination[1])])){
            console.error(`Determined that there was a possible prefix in the combination ${foundCombination} in TypeScript`);
            exceptionCount = exceptionCount + 1;
        };
    };

    return [bestCombinations, exceptionCount];
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
function _determineScoreOfWordMatchup(wordOne: string, wordTwo: string): [number, boolean] {

    let warningFlag = false;
    const wordOneLength = wordOne.length;
    const wordTwoLength = wordTwo.length;
    let score: number;

    // If either of the scores is empty, it should be fine to say it's a match
    // with the empty space
    if (wordOneLength === 0 || wordTwoLength === 0) {
        score = 100;

    // Assign the score this way if both are an initial
    } else if (wordOneLength === 1 && wordTwoLength === 1) {
        if (wordOne[0] === wordTwo[0]){
            score = 100;
            warningFlag = true;
        } else {
            score = 0;
        };

    // Assign the score this way if only one is an initial
    } else if (wordOneLength === 1 || wordTwoLength === 1) {
        if (wordOne[0] === wordTwo[0]){
            const scoreDivisionHelper = Math.max(wordOneLength, wordTwoLength)
            score = Math.round(100 / scoreDivisionHelper);
            warningFlag = true;
        } else {
            score = 0
        };

    // For words longer than 2, either use ratio or partial ratio for score as shown below
    } else {
        const ratio = fuzzball_ratio(wordOne, wordTwo, {useCollator: false, full_process: false});
        console.error(`Found the ratio ${ratio} for ${wordOne} and ${wordTwo} in TypeScript`)
        if (wordOne[0] === wordTwo[0]) {
            const partialRatioScore = Math.round(partialRatioWithParity(wordOne, wordTwo));
            console.error(`Found the partial ratio ${partialRatioScore} for ${wordOne} and ${wordTwo} in TypeScript`)
            score = Math.round((ratio + partialRatioScore) / 2);
        } else {
            score = ratio;
        };
    };

    console.error(`Final score for the ratios of ${wordOne} and ${wordTwo} in TypeScript is ${score}`);

    return [score, warningFlag];
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
export function identifyBestMatches(scores: number[][], listOne: string[], listTwo: string[]) : [string, string, number][]{
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
    let bestCombinations: [string, string, number][] = [];
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
          bestCombinations.push([wordOne, wordTwo, matchupScore]);
        };
    };

    return bestCombinations;
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

    let [originalWordCombos, possiblePrefixCount] = findWordMatchesAndQuality(nameOne, nameTwo);
    let [editedWordCombos, possibleEditedPrefixCount] = findWordMatchesAndQuality(nameOneEdited, nameTwoEdited);
    console.error(`Word combos for calculating edit improvments in TypeScript: originalWordCombos - ${originalWordCombos} editedWordCombos - ${editedWordCombos}`);
    if(!originalWordCombos.length || !editedWordCombos.length) {
        return [0, originalWordCombos, editedWordCombos]
    };
    let originalAverageScore = originalWordCombos.reduce((sum, [, , score]) => sum + score, 0) / originalWordCombos.length;
    let editedAverageScore = editedWordCombos.reduce((sum, [, , score]) => sum + score, 0) / editedWordCombos.length;
    let diff = editedAverageScore - originalAverageScore;

    console.error(`Checkpoint for calculating edit improvements in TypeScript: nameOne - ${nameOne} nameTwo - ${nameTwo} originalAverageScore - ${originalAverageScore} nameOneEdited - ${nameOneEdited} nameTwoEdited - ${nameTwoEdited} editedAverageScore - ${editedAverageScore} diff - ${diff}`);

    let originalNameOneSegments: string[] = nameOne.trim().split(/\s+/);
    let originalNameTwoSegments: string[] = nameTwo.trim().split(/\s+/);
    let originalNameUnusedSegments: number = Math.max(originalNameOneSegments.length, originalNameTwoSegments.length) - originalWordCombos.length;

    let editedNameOneSegments: string[] = nameOneEdited.trim().split(/\s+/);
    let editedNameTwoSegments: string[] = nameTwoEdited.trim().split(/\s+/);
    let editedNameUnusedSegments: number = Math.max(editedNameOneSegments.length, editedNameTwoSegments.length) - editedWordCombos.length;

    let howManyLessSegmentsInEdit: number = originalNameUnusedSegments - editedNameUnusedSegments;

    if (diff < -33 && howManyLessSegmentsInEdit < 1){
        return [diff, originalWordCombos, editedWordCombos];
    };

    // If it passes the first set, we want to make sure that it also works with the pronunciations
    const nameOneIpa = getIpa(nameOne);
    const nameTwoIpa = getIpa(nameTwo);
    [originalWordCombos, possiblePrefixCount] = findWordMatchesAndQuality(nameOneIpa, nameTwoIpa);
    const nameOneEditedIpa = getIpa(nameOneEdited);
    const nameTwoEditedIpa = getIpa(nameTwoEdited);
    [editedWordCombos, possibleEditedPrefixCount] = findWordMatchesAndQuality(nameOneEditedIpa, nameTwoEditedIpa);
    if(!originalWordCombos.length || !editedWordCombos.length) {
        return [0, originalWordCombos, editedWordCombos]
    };
    originalAverageScore = originalWordCombos.reduce((sum, [, , score]) => sum + score, 0) / originalWordCombos.length;
    editedAverageScore = editedWordCombos.reduce((sum, [, , score]) => sum + score, 0) / editedWordCombos.length;
    diff = editedAverageScore - originalAverageScore;

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
    let [combo, possiblePrefixCount] = findWordMatchesAndQuality(nameOne, nameTwo);
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

function tiebreakMatchesConsistently(inputMatrix: number[][], epsilonValue: number = 1e-4){
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
