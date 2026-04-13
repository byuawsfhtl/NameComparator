import { cleanName, cleanNamesByComparison, cleanIpa } from './src/clean';
import { removeNicknames } from './src/nicknames';
import { isWorthContinuing, eitherNameTooShort } from './src/insights';
import { compareSpelling, pronunciationComparison } from './src/comparisons';
import { modifyNamesTogether, modifyIpasByComparison } from './src/modify';
import { getIpa } from './src/ipa';
import { scoreUniqueness } from './src/uniqueness';
import { FrequencyData } from './src/uniqueness';
import usaTo1950Surnames from '../data/frequency/surnamesUsaTo1950.json';
import usaTo1950FirstNames from '../data/frequency/firstNamesUsaTo1950.json';

/**
 * Represents an attempt at name comparison (often used for debugging).
 * 
 * @property {string} nameOne - The version of the first name to be used in this attempt
 * @property {string} nameTwo - The version of the second name to be used in this attempt
 * @property {[string, string, number][]} wordCombos - A list of lists describing the word matchups and quality
 * @property {number} scoreOfAttempt - The score associated with the percent confidence returned from this attempt
 */
export class Attempt {
  constructor(
    public nameOne: string,
    public nameTwo: string,
    public wordCombos: [string, string, number][],
    public scoreOfAttempt: number
  ) {}
}

/**
 * Represents the results of a name comparison.
 * 
 * @property {string} nameOne - The original nameOne
 * @property {string} nameTwo - The original nameTwo
 * @property {boolean} match - Whether or not the names are a match. Defaults to false
 * @property {number} uniqueness - How unique the names were in comparison to the chosen population. Defaults to 0.0
 * @property {boolean} tooShort - Whether or not either of the names are one word or less. Defaults to true
 * @property {Attempt | null} attemptOne - Debugging data about the first attempt to compare the names. Defaults to null
 * @property {Attempt | null} attemptTwo - Debugging data about the second attempt to compare the names. Defaults to null
 * @property {Attempt | null} attemptThree - Debugging data about the third attempt to compare the names. Defaults to null
 * @property {Attempt | null} attemptFour - Debugging data about the fourth attempt to compare the names. Defaults to null
 * @property {number} mostRecentAttemptScore - The percent confidence score associated with the most recent attempt that 
 *                                             was made while comparing the names
 * @property {number} averageScoreOfCombinedAttempts - The average percent confidence score from all of the attempts that 
 *                                                     were made while comparing the names
 */
export class ResultsOfNameComparison {
  constructor(
    public nameOne: string,
    public nameTwo: string,
    public match: boolean = false,
    public uniqueness: number = 0.0,
    public tooShort: boolean = true,
    public attemptOne: Attempt | null = null,
    public attemptTwo: Attempt | null = null,
    public attemptThree: Attempt | null = null,
    public attemptFour: Attempt | null = null,
    public mostRecentAttemptScore: number = 0,
    public averageScoreOfCombinedAttempts: number = 0
  ) {}
}

/**
 * Compares two names to identify whether or not they are a match.
 * 
 * @param nameOne - The first name to compare
 * @param nameTwo - The second name to compare
 * @param frequencyData - The first name and surname frequencies in 
 *                        a chosen population - Defaults to None
 * 
 * @returns The data gleaned from the comparison: whether or not they are a match, 
 *          whether or not one or both names is too generic, whether or not one or 
 *          both names is too short, and the attempt data for each different 
 *          comparison method used
 */
export function compareTwoNames(nameOne: string, nameTwo: string, frequencyData: FrequencyData | null = null): ResultsOfNameComparison {
  // Deal with the optional frequencyData argument
  if (!frequencyData) {
    frequencyData = new FrequencyData(usaTo1950FirstNames, usaTo1950Surnames);
  }

  // Data validation
  if (typeof nameOne !== 'string' || typeof nameTwo !== 'string') {
    throw new TypeError(`nameOne was ${typeof nameOne}. Must be string. nameTwo was ${typeof nameTwo}. Must be a string.`);
  }
  if (!(frequencyData instanceof FrequencyData)) {
    throw new TypeError(`frequencyData was the type ${typeof frequencyData}. Must be a FrequencyData boject.`);
  }

  // Create the return object to edit later
  let results = new ResultsOfNameComparison(nameOne, nameTwo);

  // Clean the names
  nameOne = cleanName(nameOne);
  nameTwo = cleanName(nameTwo);
  [nameOne, nameTwo] = cleanNamesByComparison(nameOne, nameTwo);

  // Deal with names that are too short
  results.tooShort = eitherNameTooShort(nameOne, nameTwo);
  if (!nameOne) {
    nameOne = '_'
  };
  if (!nameTwo) {
    nameTwo = '_'
  };
  if (nameOne === '_' || nameTwo === '_'){
    return results;
  } 

  // Find the uniqueness of this name matchup (ie. hopefully not 'John Smith' and 'J Smith')
  results.uniqueness = scoreUniqueness(nameOne, nameTwo, frequencyData);

  // Remove nicknames before the actual comparison
  [nameOne, nameTwo] = removeNicknames(nameOne, nameTwo);

  // 1st attempt: Checks if names are a match according to string comparison alone
  const [attemptOneMatch, attemptOneWordCombos, attemptOneScore] = compareSpelling(nameOne, nameTwo);
  results.attemptOne = new Attempt(nameOne, nameTwo, attemptOneWordCombos, attemptOneScore);
  if (attemptOneMatch) {
    results.match = true;
    results.mostRecentAttemptScore = attemptOneScore;
    results.averageScoreOfCombinedAttempts = attemptOneScore;
    return results;
  };

  // Failed first attempt. Check if names are even worth continuing
  if (isWorthContinuing(nameOne, nameTwo) === false){
    return results;
  } ;

  // 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
  const [modifiedNameOne, modifiedNameTwo] = modifyNamesTogether(nameOne, nameTwo);
  const[attemptTwoMatch, attemptTwoWordCombos, attemptTwoScore] = compareSpelling(modifiedNameOne, modifiedNameTwo);
  results.attemptTwo = new Attempt(modifiedNameOne, modifiedNameTwo, attemptTwoWordCombos, attemptTwoScore);
  if (attemptTwoMatch) {
    results.match = true;
    results.mostRecentAttemptScore = attemptTwoScore;
    results.averageScoreOfCombinedAttempts = ((attemptTwoScore + attemptOneScore) / 2);
    return results;
  };
  
  // 3rd attempt: Checks if modified names are a match according to pronunciation
  let ipaOfModifiedNameOne = cleanIpa(getIpa(modifiedNameOne));
  let ipaOfModifiedNameTwo = cleanIpa(getIpa(modifiedNameTwo));
  [ipaOfModifiedNameOne, ipaOfModifiedNameTwo] = modifyIpasByComparison(ipaOfModifiedNameOne, ipaOfModifiedNameTwo);
  const [attemptThreeMatch, attemptThreeWordCombos, attemptThreeScore] = pronunciationComparison(ipaOfModifiedNameOne, ipaOfModifiedNameTwo, modifiedNameOne, modifiedNameTwo);
  results.attemptThree = new Attempt(ipaOfModifiedNameOne, ipaOfModifiedNameTwo, attemptThreeWordCombos, attemptThreeScore);
  if (attemptThreeMatch) {
    results.match = true;
    results.mostRecentAttemptScore = attemptThreeScore;
    results.averageScoreOfCombinedAttempts = ((attemptThreeScore + attemptTwoScore + attemptOneScore) / 3);
    return results;
  };

  // 4th attempt: Check if original names are a match according to pronunciation
  let ipaOfNameOne = cleanIpa(getIpa(nameOne));
  let ipaOfNameTwo = cleanIpa(getIpa(nameTwo));
  [ipaOfNameOne, ipaOfNameTwo] = modifyIpasByComparison(ipaOfNameOne, ipaOfNameTwo);
  const [attemptFourMatch, attemptFourWordCombos, attemptFourScore] = pronunciationComparison(ipaOfNameOne, ipaOfNameTwo, nameOne, nameTwo);
  results.attemptFour = new Attempt(ipaOfNameOne, ipaOfNameTwo, attemptFourWordCombos, attemptFourScore);
  if (attemptFourMatch) {
    results.match = true;
    results.mostRecentAttemptScore = attemptFourScore;
    results.averageScoreOfCombinedAttempts = ((attemptFourScore + attemptThreeScore + attemptTwoScore + attemptOneScore) / 4);
  };
  return results;
};
