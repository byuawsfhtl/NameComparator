// test-clean.ts
import * as fuzzball from 'fuzzball';

function testFuzz(nameOne: string, nameTwo:string) {
    let score = fuzzball.ratio(nameOne, nameTwo);
    console.log("nameOne: " + nameOne + ", nameTwo: " + nameTwo +" Score: " + score);
}

// Example usage
testFuzz("*lb*rt", "g*l*rt");
testFuzz("d*l*m*n", "*l*m*n");
testFuzz("*", "*");
