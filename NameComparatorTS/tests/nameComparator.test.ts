import { compareTwoNames } from '../nameComparator'; // Adjust path
import { FrequencyData } from '../src/uniqueness';
import rawTestCases from './name-comparison-results.json'; // Place this JSON in the same folder or update the path
// import rawTestCases from './small-test-set.json';
import usaTo1950Surnames from '../../data/frequency/surnamesUsaTo1950.json';
import usaTo1950FirstNames from '../../data/frequency/firstNamesUsaTo1950.json';


type TestCase = {
  nameOne: string;
  nameTwo: string;
  match: boolean;
  attemptOne: [string, string, number[]];
  attemptTwo: [string, string, number[]];
  attemptThree: [string, string, number[]];
  attemptFour: [string, string, number[]];
};

type FailedTestCase = {
  nameOne: string;
  nameTwo: string;
  match: boolean;
  attemptOne: Attempt | null;
  attemptTwo: Attempt | null;
  attemptThree: Attempt | null;
  attemptFour: Attempt | null;
};

type WordComboEntry = [string, string, number];
class Attempt {
  constructor(
    public nameOne: string,
    public nameTwo: string,
    public wordCombo: WordComboEntry[]
  ) {}
}

const frequencyData = new FrequencyData(usaTo1950FirstNames, usaTo1950Surnames);
const testCases = rawTestCases as TestCase[];
const failedTests: FailedTestCase[] = [];

describe('compareTwoNames with testCases.json', () => {
  testCases.forEach(({ nameOne, nameTwo, match }) => {
    test(`"${nameOne}" vs "${nameTwo}" should ${match ? 'match' : 'not match'}`, () => {
      const result = compareTwoNames(nameOne, nameTwo, frequencyData);

      if (result.match !== match) {
        failedTests.push({
          nameOne,
          nameTwo,
          match: result.match,
          attemptOne: result.attemptOne,
          attemptTwo: result.attemptTwo,
          attemptThree: result.attemptThree,
          attemptFour: result.attemptFour
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