import * as cleanMod from './src/clean';
import * as nicknameMod from './src/nicknames';
import * as insightMod from './src/insights';
import * as comparisonMod from './src/comparisons';
import * as modifyMod from './src/modify';
import * as ipaMod from './src/ipa';
import * as uniquenessMod from './src/uniqueness';
import { FrequencyData } from './src/uniqueness';
import usaTo1950Surnames from './data/frequency/surnamesUsaTo1950.json';
import usaTo1950FirstNames from './data/frequency/firstNamesUsaTo1950.json';

export type WordComboEntry = [string, string, number];

export class Attempt {
  constructor(
    public nameOne: string,
    public nameTwo: string,
    public wordCombo: WordComboEntry[]
  ) {}
}

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

export function compareTwoNames(
  nameOne: string,
  nameTwo: string,
  frequencyData: FrequencyData | null = null
): ResultsOfNameComparison {
  if (!frequencyData) {
    frequencyData = new FrequencyData(usaTo1950FirstNames, usaTo1950Surnames);
  }

  if (typeof nameOne !== 'string' || typeof nameTwo !== 'string') {
    throw new TypeError(`nameOne was ${typeof nameOne}. Must be string. nameTwo was ${typeof nameTwo}. Must be string.`);
  }
  if (!(frequencyData instanceof FrequencyData)) {
    throw new TypeError(`frequencyData was ${typeof frequencyData}. Must be FrequencyData.`);
  }

  const results = new ResultsOfNameComparison(nameOne, nameTwo);

  nameOne = cleanMod.cleanName(nameOne);
  nameTwo = cleanMod.cleanName(nameTwo);

  [nameOne, nameTwo] = cleanMod.cleanNamesByComparison(nameOne, nameTwo);

  results.tooShort = insightMod.eitherNameTooShort(nameOne, nameTwo);
  if (!nameOne) nameOne = '_';
  if (!nameTwo) nameTwo = '_';
  if (nameOne === '_' || nameTwo === '_'){
    return results;
  } 

  results.uniqueness = uniquenessMod.scoreUniqueness(nameOne, nameTwo, frequencyData);

  [nameOne, nameTwo] = nicknameMod.removeNicknames(nameOne, nameTwo);

  let [match, wordCombo] = comparisonMod.compareSpelling(nameOne, nameTwo);
  results.attemptOne = new Attempt(nameOne, nameTwo, wordCombo);
  if (match) {
    results.match = true;
    return results;
  }

  if (!insightMod.isWorthContinuing(nameOne, nameTwo)){
    return results;
  } 

  let [modifiedNameOne, modifiedNameTwo] = modifyMod.modifyNamesTogether(nameOne, nameTwo);

  [match, wordCombo] = comparisonMod.compareSpelling(modifiedNameOne, modifiedNameTwo);
  results.attemptTwo = new Attempt(modifiedNameOne, modifiedNameTwo, wordCombo);
  if (match) {
    results.match = true;
    return results;
  }
  
  let ipaOfModnameOne = cleanMod.cleanIpa(ipaMod.getIpa(modifiedNameOne));
  let ipaOfModnameTwo = cleanMod.cleanIpa(ipaMod.getIpa(modifiedNameTwo));
  [ipaOfModnameOne, ipaOfModnameTwo] = modifyMod.modifyIpasByComparison(ipaOfModnameOne, ipaOfModnameTwo);

  [match, wordCombo] = comparisonMod.pronunciationComparison(
    ipaOfModnameOne,
    ipaOfModnameTwo,
    modifiedNameOne,
    modifiedNameTwo
  );
  results.attemptThree = new Attempt(ipaOfModnameOne, ipaOfModnameTwo, wordCombo);
  if (match) {
    results.match = true;
    return results;
  }

  let ipaOfNameOne = cleanMod.cleanIpa(ipaMod.getIpa(nameOne));
  let ipaOfNameTwo = cleanMod.cleanIpa(ipaMod.getIpa(nameTwo));
  [ipaOfNameOne, ipaOfNameTwo] = modifyMod.modifyIpasByComparison(ipaOfNameOne, ipaOfNameTwo);
  
  [match, wordCombo] = comparisonMod.pronunciationComparison(
    ipaOfNameOne,
    ipaOfNameTwo,
    nameOne,
    nameTwo
  );
  results.attemptFour = new Attempt(ipaOfNameOne, ipaOfNameTwo, wordCombo);
  if (match) {
    results.match = true;
  }
  return results;
}
