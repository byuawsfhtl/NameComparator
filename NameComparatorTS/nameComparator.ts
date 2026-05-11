import fs from 'fs';
import path from 'path';
import { cleanName, cleanNamesByComparison, cleanIpa } from './src/clean.js';
import { removeNicknames } from './src/nicknames.js';
import { isWorthContinuing, eitherNameTooShort } from './src/insights.js';
import { compareSpelling, pronunciationComparison } from './src/comparisons.js';
import { modifyNamesTogether, modifyIpasByComparison } from './src/modify.js';
import { getIpa } from './src/ipa.js';
import { scoreUniqueness, FrequencyData } from './src/uniqueness.js';

// This is required to make sure that it reads in the characters correctly
import usaTo1950SurnamesUnparsed from '../data/frequency/surnamesUsaTo1950.json' with {type: 'json'};
const usaTo1950Surnames = usaTo1950SurnamesUnparsed as Record<string, number>;

import usaTo1950FirstNamesUnparsed from '../data/frequency/firstNamesUsaTo1950.json' with  {type: 'json'};
const usaTo1950FirstNames = usaTo1950FirstNamesUnparsed as Record<string, number>;

// Read the penalty variable from a file
import values from '../data/variablesForComparisons.json' with { type: "json"};
const { maxScore, 
        guaranteedPassingScore,
        conditionallyPassingScore,
        furtherChecksNeededScore,
        guaranteedFailScore,
        fuzzyComparisonWeight,
        consonantComparisonWeight,
        numberOfValidCombosToSkipFurtherChecks,
        lengthNeededForConditionallyPassingPronunciationComparison,
        penaltyForMismatchedPrefixes
  } = values;

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
 * @property {boolean} notWorthContinuing - Whether or not NameComparator determined if the name was not worth
 *                                          running more checks on after the first check
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
    public mostRecentAttemptScore: number = 0.0,
    public averageScoreOfCombinedAttempts: number = 0.0,
    public notWorthContinuing: boolean = false
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

  var appliedPenalty: number = 0;
  var shouldApplyPenalty = false;

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
  console.error(`Cleaning nameOne in TypeScript. Name before cleaning: ${nameOne}`);
  nameOne = cleanName(nameOne);
  console.error(`Cleaning nameTwo in TypeScript. Name before cleaning: ${nameTwo}`);
  nameTwo = cleanName(nameTwo);
  console.error("Cleaning names by comparison in TypeScript");
  [nameOne, nameTwo, shouldApplyPenalty] = cleanNamesByComparison(nameOne, nameTwo);
  console.error(`Names after cleaning in TypeScript - nameOne: ${nameOne}  nameTwo: ${nameTwo}`);

  if (shouldApplyPenalty === true){
    appliedPenalty = penaltyForMismatchedPrefixes
  };

  // Deal with names that are too short
  console.error("Determining if either name is too short in TypeScript");
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
  console.error("Scoring name uniqueness in TypeScript");
  results.uniqueness = scoreUniqueness(nameOne, nameTwo, frequencyData);

  // Remove nicknames before the actual comparison
  console.error("Removing nicknames in TypeScript");
  [nameOne, nameTwo] = removeNicknames(nameOne, nameTwo);

  // 1st attempt: Checks if names are a match according to string comparison alone
  console.error("Starting TypeScript attempt one");
  var [attemptOneMatch, attemptOneWordCombos, attemptOneScore] = compareSpelling(nameOne, nameTwo);
  attemptOneScore = attemptOneScore + appliedPenalty;
  results.attemptOne = new Attempt(nameOne, nameTwo, attemptOneWordCombos, attemptOneScore);
  if (attemptOneMatch) {
    results.match = true;
    results.mostRecentAttemptScore = attemptOneScore;
    results.averageScoreOfCombinedAttempts = attemptOneScore;
    return results;
  };

  console.error(`Check to make sure the names weren't modified strangely after attempt one in TypeScript: nameOne - ${nameOne} nameTwo - ${nameTwo}`);

  // Failed first attempt. Check if names are even worth continuing
  if (isWorthContinuing(nameOne, nameTwo) === false){
    results.notWorthContinuing = true;
    results.mostRecentAttemptScore = attemptOneScore;
    results.averageScoreOfCombinedAttempts = attemptOneScore;
    return results;
  };

  console.error(`Check to make sure the names weren't modified strangely after continuation check in TypeScript: nameOne - ${nameOne} nameTwo - ${nameTwo}`);

  // 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
  console.error("Starting TypeScript attempt two");
  const [modifiedNameOne, modifiedNameTwo] = modifyNamesTogether(nameOne, nameTwo);
  var [attemptTwoMatch, attemptTwoWordCombos, attemptTwoScore] = compareSpelling(modifiedNameOne, modifiedNameTwo);
  attemptTwoScore = attemptTwoScore + appliedPenalty;
  results.attemptTwo = new Attempt(modifiedNameOne, modifiedNameTwo, attemptTwoWordCombos, attemptTwoScore);
  if (attemptTwoMatch) {
    results.match = true;
    results.mostRecentAttemptScore = attemptTwoScore;
    results.averageScoreOfCombinedAttempts = ((attemptTwoScore + attemptOneScore) / 2);
    return results;
  };

  // This is just to help with a test case
  let testModifyOne = getIpa(modifiedNameOne);
  let testModifyTwo = getIpa(modifiedNameTwo);
  console.error(`Retrieved ipas in TypeScript: nameOne - ${testModifyOne} nameTwo - ${testModifyTwo}`);
  
  // 3rd attempt: Checks if modified names are a match according to pronunciation
  console.error("Starting TypeScript attempt three");
  let ipaOfModifiedNameOne = cleanIpa(getIpa(modifiedNameOne));
  let ipaOfModifiedNameTwo = cleanIpa(getIpa(modifiedNameTwo));
  console.error(`TypeScript cleaned ipas in attempt three: nameOne - ${ipaOfModifiedNameOne}, nameTwo - ${ipaOfModifiedNameTwo}`);
  [ipaOfModifiedNameOne, ipaOfModifiedNameTwo] = modifyIpasByComparison(ipaOfModifiedNameOne, ipaOfModifiedNameTwo);
  console.error(`TypeScript ipas after modifying by comparison in attempt three: nameOne - ${ipaOfModifiedNameOne}, nameTwo - ${ipaOfModifiedNameTwo}`);
  var [attemptThreeMatch, attemptThreeWordCombos, attemptThreeScore] = pronunciationComparison(ipaOfModifiedNameOne, ipaOfModifiedNameTwo, modifiedNameOne, modifiedNameTwo);
  attemptThreeScore = attemptThreeScore + appliedPenalty;
  results.attemptThree = new Attempt(ipaOfModifiedNameOne, ipaOfModifiedNameTwo, attemptThreeWordCombos, attemptThreeScore);
  if (attemptThreeMatch) {
    results.match = true;
    results.mostRecentAttemptScore = attemptThreeScore;
    results.averageScoreOfCombinedAttempts = ((attemptThreeScore + attemptTwoScore + attemptOneScore) / 3);
    return results;
  };

  // 4th attempt: Check if original names are a match according to pronunciation
  console.error("Starting TypeScript attempt four");
  let ipaOfNameOne = cleanIpa(getIpa(nameOne));
  let ipaOfNameTwo = cleanIpa(getIpa(nameTwo));
  console.error(`TypeScript cleaned ipas in attempt four: nameOne - ${ipaOfNameOne}, nameTwo - ${ipaOfNameTwo}`);
  [ipaOfNameOne, ipaOfNameTwo] = modifyIpasByComparison(ipaOfNameOne, ipaOfNameTwo);
  console.error(`TypeScript ipas after modifying by comparison in attempt four: nameOne - ${ipaOfNameOne}, nameTwo - ${ipaOfNameTwo}`);
  var [attemptFourMatch, attemptFourWordCombos, attemptFourScore] = pronunciationComparison(ipaOfNameOne, ipaOfNameTwo, nameOne, nameTwo);
  attemptFourScore = attemptFourScore + appliedPenalty;
  results.attemptFour = new Attempt(ipaOfNameOne, ipaOfNameTwo, attemptFourWordCombos, attemptFourScore);

  if (attemptFourMatch) {
    results.match = true;
  };

  // Since we want the return values to be right, we need this to be a default case for them
  results.mostRecentAttemptScore = attemptFourScore;
  results.averageScoreOfCombinedAttempts = ((attemptFourScore + attemptThreeScore + attemptTwoScore + attemptOneScore) / 4);

  return results;
};
