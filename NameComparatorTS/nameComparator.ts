import * as cleanMod from './src/clean';
import * as nicknameMod from './src/nicknames';
import * as insightMod from './src/insights';
import * as comparisonMod from './src/comparisons';
import * as modifyMod from './src/modify';
import * as ipaMod from './src/ipa';
import * as uniquenessMod from './src/uniqueness';
import { FrequencyData } from './src/uniqueness';
import usaTo1950Surnames from '../data/frequency/surnamesUsaTo1950.json';
import usaTo1950FirstNames from '../data/frequency/firstNamesUsaTo1950.json';

/**
 * Represents an attempt at name comparison (often used for debugging).
 * 
 * @property {string} nameOne - The version of the first name to be used in this attempt
 * @property {string} nameTwo - The version of the second name to be used in this attempt
 * @property {[string, string, number][]} wordCombo - A list of tuples describing the word matchups and quality
 */
export class Attempt {
  constructor(
    public nameOne: string,
    public nameTwo: string,
    public wordCombo: [string, string, number][]
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
    public attemptFour: Attempt | null = null
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
  nameOne = cleanMod.cleanName(nameOne);
  nameTwo = cleanMod.cleanName(nameTwo);
  [nameOne, nameTwo] = cleanMod.cleanNamesByComparison(nameOne, nameTwo);

  // Deal with names that are too short
  results.tooShort = insightMod.eitherNameTooShort(nameOne, nameTwo);
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
  results.uniqueness = uniquenessMod.scoreUniqueness(nameOne, nameTwo, frequencyData);

  // Remove nicknames before the actual comparison
  [nameOne, nameTwo] = nicknameMod.removeNicknames(nameOne, nameTwo);

  // 1st attempt: Checks if names are a match according to string comparison alone
  let [match, wordCombo] = comparisonMod.compareSpelling(nameOne, nameTwo);
  results.attemptOne = new Attempt(nameOne, nameTwo, wordCombo);
  if (match) {
    results.match = true;
    return results;
  }

  // Failed first attempt. Check if names are even worth continuing
  if (insightMod.isWorthContinuing(nameOne, nameTwo) === false){
    return results;
  } 

  // 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
  let [modifiedNameOne, modifiedNameTwo] = modifyMod.modifyNamesTogether(nameOne, nameTwo);
  [match, wordCombo] = comparisonMod.compareSpelling(modifiedNameOne, modifiedNameTwo);
  results.attemptTwo = new Attempt(modifiedNameOne, modifiedNameTwo, wordCombo);
  if (match) {
    results.match = true;
    return results;
  }
  
  // 3rd attempt: Checks if modified names are a match according to pronunciation
  let ipaOfModifiedNameOne = cleanMod.cleanIpa(ipaMod.getIpa(modifiedNameOne));
  let ipaOfModifiedNameTwo = cleanMod.cleanIpa(ipaMod.getIpa(modifiedNameTwo));
  [ipaOfModifiedNameOne, ipaOfModifiedNameTwo] = modifyMod.modifyIpasByComparison(ipaOfModifiedNameOne, ipaOfModifiedNameTwo);
  [match, wordCombo] = comparisonMod.pronunciationComparison(ipaOfModifiedNameOne, ipaOfModifiedNameTwo, modifiedNameOne, modifiedNameTwo);
  results.attemptThree = new Attempt(ipaOfModifiedNameOne, ipaOfModifiedNameTwo, wordCombo);
  if (match) {
    results.match = true;
    return results;
  }

  // 4th attempt: Check if original names are a match according to pronunciation
  let ipaOfNameOne = cleanMod.cleanIpa(ipaMod.getIpa(nameOne));
  let ipaOfNameTwo = cleanMod.cleanIpa(ipaMod.getIpa(nameTwo));
  [ipaOfNameOne, ipaOfNameTwo] = modifyMod.modifyIpasByComparison(ipaOfNameOne, ipaOfNameTwo);
  [match, wordCombo] = comparisonMod.pronunciationComparison(ipaOfNameOne, ipaOfNameTwo, nameOne, nameTwo);
  results.attemptFour = new Attempt(ipaOfNameOne, ipaOfNameTwo, wordCombo);
  if (match) {
    results.match = true;
  }
  return results;
}
