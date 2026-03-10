import { getPairIndicesAndWords } from "./usefulTools";

/**
 * Stores the name frequencies for first names and surnames within a given population.
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
 * Represents the frequency upper bound of each uniqueness classification.
 */
export enum FrequencyUpperBound {
    GENERIC = 1/1,
    COMMON = 1/100,
    AVERAGE = 1/500,
    RARE = 1/1000,
    UNSEEN = 1/2000,
}

/**
 * Represents the classification of the uniqueness of a given word pair.
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
 * (between 0 and 100).
 * 
 * @param nameA - The first name to score.
 * @param nameB - The second name to score.
 * @param frequencyData - The first name and surname frequencies in a pop
 * @returns The uniqueness score.
 */
export function scoreUniqueness(nameA: string, nameB: string, frequencyData: FrequencyData): number {

    const wordPairs = getPairIndicesAndWords(nameA, nameB);
    
    const scoresOfWordPairs = wordPairs.map(([_, __, wordA, wordB]: [number, number, string, string]) => 
        _findWordPairUniqueness(wordA, wordB, frequencyData)
    );

    return Math.min(100, scoresOfWordPairs.reduce((sum: number, score: number) => sum + score, 0));
}

/**
 * Given two words paired together, it will identify the least possible uniqueness
 * classification to assign the pair, based on which of the two occurs most frequently
 * (as either a surname or as a first name- whichever is more frequent).
 * 
 * @param wordA - The first word to score.
 * @param wordB - The second word to score.
 * @param frequencyData - The first name and surname frequencies in a pop
 * @returns The uniqueness classification of the word pair.
 */
function _findWordPairUniqueness(wordA: string, wordB: string, frequencyData: FrequencyData): Uniqueness {

    const wordAFreq = _getMaxFrequency(wordA, frequencyData);
    const wordBFreq = _getMaxFrequency(wordB, frequencyData);
    const pairFreq = Math.max(wordAFreq, wordBFreq);
    if (pairFreq < 0) {
        throw new Error("Score is out of range");
    }
    else if (pairFreq <= FrequencyUpperBound.UNSEEN) {
        return Uniqueness.UNSEEN;
    }
    else if (pairFreq <= FrequencyUpperBound.RARE) {
        return Uniqueness.RARE;
    }
    else if (pairFreq <= FrequencyUpperBound.AVERAGE) {
        return Uniqueness.AVERAGE;
    }
    else if (pairFreq <= FrequencyUpperBound.COMMON) {
        return Uniqueness.COMMON;
    }
    else if (pairFreq <= FrequencyUpperBound.GENERIC) {
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
 * @param word - The word to score.
 * @param frequencyData - The first name and surname frequencies in a pop
 * @returns The maximum possible frequency for the word.
 */
function _getMaxFrequency(word: string, frequencyData: FrequencyData): number {

    const defaultFreq = FrequencyUpperBound.UNSEEN;
    const wordFirstNameFreq = frequencyData.firstNameFrequencies[word] ?? defaultFreq;
    const wordSurnameFreq = frequencyData.surnameFrequencies[word] ?? defaultFreq;
    const wordInitialFreq = word.length === 1 ? 1/26 : defaultFreq;
    return Math.max(wordFirstNameFreq, wordSurnameFreq, wordInitialFreq);
}
