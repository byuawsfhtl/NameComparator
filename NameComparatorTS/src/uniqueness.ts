import { getMatchingWordsAndIndices } from "./usefulTools.js";

/**
 * A class that stores the name frequencies for first names and surnames 
 * within a given population in two Records.
 * 
 * WARNING: When this is being made, the characters in the data *MUST* be 
 * in the utf-8 format before declaring this class or the comparison will 
 * be bad. This is especially true of international langauges.
 */
export class FrequencyData {
    public firstNameFrequencies: Record<string, number>;
    public surnameFrequencies: Record<string, number>;

    constructor(firstNameFrequencies: Record<string, number>, surnameFrequencies: Record<string, number>){
        this.firstNameFrequencies = firstNameFrequencies;
        this.surnameFrequencies = surnameFrequencies;
    }
}

/**
 * An enum representing the frequency upper bound of each uniqueness classification.
 */
export enum FrequencyUpperBound {
    GENERIC = 1/1,
    COMMON = 1/100,
    AVERAGE = 1/500,
    RARE = 1/1000,
    UNSEEN = 1/2000,
}

/**
 * An enum representing the classification of the uniqueness of a given word pair.
 */
export enum Uniqueness {
    GENERIC = 10,
    COMMON = 23,
    AVERAGE = 32,
    RARE = 42,
    UNSEEN = 65,
}

/**
 * Takes two names and gives them an algorithmically calculated uniqueness score
 * between 0 and 100.
 * 
 * @param nameOne - The first name to compare for a uniqueness score
 * @param nameTwo - The second name to compare for a uniqueness score
 * @param frequencyData - The first name and surname frequencies within a population
 * @returns A float numerically representing the uniqueness of the two names
 */
export function scoreUniqueness(nameOne: string, nameTwo: string, frequencyData: FrequencyData): number {

    // Get the max frequency of either word in each pair
    const wordPairs = getMatchingWordsAndIndices(nameOne, nameTwo);
    const scoresOfWordPairs = wordPairs.map(([_, __, wordOne, wordTwo]: [number, number, string, string]) => 
        _findWordPairUniqueness(wordOne, wordTwo, frequencyData)
    );

    // Return the sum, maxing out at 100
    return Math.min(100, scoresOfWordPairs.reduce((sum: number, score: number) => sum + score, 0));
}

/**
 * Given two words paired together, it will identify the least possible uniqueness
 * classification to assign the pair, based on which of the two occurs most frequently.
 * This can be based on either a surname or as a first name -- whichever is more frequent.
 * 
 * @param wordOne - The first word to score from a name
 * @param wordTwo - The second word to score from a name
 * @param frequencyData - The first name and surname frequencies within a population
 * @returns The uniqueness classification enum of the word pair
 * 
 * This will throw an error if the value is below 0 or greater than 1
 * 
 */
function _findWordPairUniqueness(wordOne: string, wordTwo: string, frequencyData: FrequencyData): Uniqueness {

    const wordOneFrequency = _getMaxFrequency(wordOne, frequencyData);
    const wordTwoFrequency = _getMaxFrequency(wordTwo, frequencyData);
    const pairFrequency = Math.max(wordOneFrequency, wordTwoFrequency);
    if (pairFrequency < 0) {
        throw new Error("Score is out of range");
    }
    else if (pairFrequency <= FrequencyUpperBound.UNSEEN) {
        return Uniqueness.UNSEEN;
    }
    else if (pairFrequency <= FrequencyUpperBound.RARE) {
        return Uniqueness.RARE;
    }
    else if (pairFrequency <= FrequencyUpperBound.AVERAGE) {
        return Uniqueness.AVERAGE;
    }
    else if (pairFrequency <= FrequencyUpperBound.COMMON) {
        return Uniqueness.COMMON;
    }
    else if (pairFrequency <= FrequencyUpperBound.GENERIC) {
        return Uniqueness.GENERIC;
    }
    else {
        throw new Error("Score is out of range");
    }
}

/**
 * Gets the maximum possible frequency for a given word, whether it is found more as a
 * first name or surname, given those frequencies for a given population. If the word is not
 * found in either dicts, defaults to the default frequency, which is very low.
 * 
 * @param word - The word from a name to score
 * @param frequencyData - The first name and surname frequencies in a population
 * @returns A float representing the maximum possible frequency for the word
 */
function _getMaxFrequency(word: string, frequencyData: FrequencyData): number {

    const defaultFrequency = FrequencyUpperBound.UNSEEN;
    const wordFirstNameFrequency = frequencyData.firstNameFrequencies[word] ?? defaultFrequency;
    const wordSurnameFrequency = frequencyData.surnameFrequencies[word] ?? defaultFrequency;
    const wordInitialFrequency = word.length === 1 ? 1/26 : defaultFrequency;
    return Math.max(wordFirstNameFrequency, wordSurnameFrequency, wordInitialFrequency);
}
