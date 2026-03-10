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
    public nameA: string,
    public nameB: string,
    public wordCombo: WordComboEntry[]
  ) {}
}

export class ResultsOfNameComparison {
  constructor(
    public nameA: string,
    public nameB: string,
    public match: boolean = false,
    public uniqueness: number = 0.0,
    public tooShort: boolean = true,
    public attempt1: Attempt | null = null,
    public attempt2: Attempt | null = null,
    public attempt3: Attempt | null = null,
    public attempt4: Attempt | null = null
  ) {}
}

export function compareTwoNames(
  nameA: string,
  nameB: string,
  frequencyData: FrequencyData | null = null
): ResultsOfNameComparison {
  if (!frequencyData) {
    frequencyData = new FrequencyData(usaTo1950FirstNames, usaTo1950Surnames);
  }

  if (typeof nameA !== 'string' || typeof nameB !== 'string') {
    throw new TypeError(`nameA was ${typeof nameA}. Must be string. nameB was ${typeof nameB}. Must be string.`);
  }
  if (!(frequencyData instanceof FrequencyData)) {
    throw new TypeError(`frequencyData was ${typeof frequencyData}. Must be FrequencyData.`);
  }

  const results = new ResultsOfNameComparison(nameA, nameB);

  nameA = cleanMod.cleanName(nameA);
  nameB = cleanMod.cleanName(nameB);

  [nameA, nameB] = cleanMod.cleanNamesTogether(nameA, nameB);

  results.tooShort = insightMod.eitherNameTooShort(nameA, nameB);
  if (!nameA) nameA = '_';
  if (!nameB) nameB = '_';
  if (nameA === '_' || nameB === '_'){
    return results;
  } 

  results.uniqueness = uniquenessMod.scoreUniqueness(nameA, nameB, frequencyData);

  [nameA, nameB] = nicknameMod.removeNicknames(nameA, nameB);

  let [match, wordCombo] = comparisonMod.spellingComparison(nameA, nameB);
  results.attempt1 = new Attempt(nameA, nameB, wordCombo);
  if (match) {
    results.match = true;
    return results;
  }

  if (!insightMod.isWorthContinuing(nameA, nameB)){
    return results;
  } 

  let [modifiedNameA, modifiedNameB] = modifyMod.modifyNamesTogether(nameA, nameB);

  [match, wordCombo] = comparisonMod.spellingComparison(modifiedNameA, modifiedNameB);
  results.attempt2 = new Attempt(modifiedNameA, modifiedNameB, wordCombo);
  if (match) {
    results.match = true;
    return results;
  }
  
  let ipaOfModNameA = cleanMod.cleanIpa(ipaMod.getIpa(modifiedNameA));
  let ipaOfModNameB = cleanMod.cleanIpa(ipaMod.getIpa(modifiedNameB));
  [ipaOfModNameA, ipaOfModNameB] = modifyMod.modifyIpasTogether(ipaOfModNameA, ipaOfModNameB);

  [match, wordCombo] = comparisonMod.pronunciationComparison(
    ipaOfModNameA,
    ipaOfModNameB,
    modifiedNameA,
    modifiedNameB
  );
  results.attempt3 = new Attempt(ipaOfModNameA, ipaOfModNameB, wordCombo);
  if (match) {
    results.match = true;
    return results;
  }

  let ipaOfNameA = cleanMod.cleanIpa(ipaMod.getIpa(nameA));
  let ipaOfNameB = cleanMod.cleanIpa(ipaMod.getIpa(nameB));
  [ipaOfNameA, ipaOfNameB] = modifyMod.modifyIpasTogether(ipaOfNameA, ipaOfNameB);
  
  [match, wordCombo] = comparisonMod.pronunciationComparison(
    ipaOfNameA,
    ipaOfNameB,
    nameA,
    nameB
  );
  results.attempt4 = new Attempt(ipaOfNameA, ipaOfNameB, wordCombo);
  if (match) {
    results.match = true;
  }
  return results;
}
