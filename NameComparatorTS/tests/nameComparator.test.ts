import { compareTwoNames } from '../nameComparator'; // Adjust path
import { FrequencyData } from '../src/uniqueness';
import rawTestCases from './name-comparison-results.json'; // Place this JSON in the same folder or update the path
// import rawTestCases from './small-test-set.json';
import usaTo1950Surnames from '../data/frequency/surnamesUsaTo1950.json';
import usaTo1950FirstNames from '../data/frequency/firstNamesUsaTo1950.json';


type TestCase = {
  nameA: string;
  nameB: string;
  match: boolean;
  attempt1: [string, string, number[]];
  attempt2: [string, string, number[]];
  attempt3: [string, string, number[]];
  attempt4: [string, string, number[]];
};

type FailedTestCase = {
  nameA: string;
  nameB: string;
  match: boolean;
  attempt1: Attempt | null;
  attempt2: Attempt | null;
  attempt3: Attempt | null;
  attempt4: Attempt | null;
};

type WordComboEntry = [string, string, number];
class Attempt {
  constructor(
    public nameA: string,
    public nameB: string,
    public wordCombo: WordComboEntry[]
  ) {}
}

const frequencyData = new FrequencyData(usaTo1950FirstNames, usaTo1950Surnames);
const testCases = rawTestCases as TestCase[];
const failedTests: FailedTestCase[] = [];

describe('compareTwoNames with testCases.json', () => {
  testCases.forEach(({ nameA, nameB, match }) => {
    test(`"${nameA}" vs "${nameB}" should ${match ? 'match' : 'not match'}`, () => {
      const result = compareTwoNames(nameA, nameB, frequencyData);

      if (result.match !== match) {
        failedTests.push({
          nameA,
          nameB,
          match: result.match,
          attempt1: result.attempt1,
          attempt2: result.attempt2,
          attempt3: result.attempt3,
          attempt4: result.attempt4
        });
      }

      expect(result.match).toBe(match);
    });
  });
});

afterAll(() => {
  const fs = require('fs');
  const path = require('path');
  const outputPath = path.join(__dirname, 'failed-name-tests.json');

  if (failedTests.length > 0) {
    fs.writeFileSync(outputPath, JSON.stringify(failedTests, null, 2), 'utf-8');
    console.log(`Saved ${failedTests.length} failed tests to ${outputPath}`);
  } else {
    console.log('All name tests passed. No failures to write.');
  }
});