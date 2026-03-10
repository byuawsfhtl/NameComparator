// test-clean.ts
import * as fuzzball from 'fuzzball';

function testFuzz(nameA: string, nameB:string) {
    let score = fuzzball.ratio(nameA, nameB);
    console.log("NameA: " + nameA + ", NameB: " + nameB +" Score: " + score);
}

// Example usage
testFuzz("*lb*rt", "g*l*rt");
testFuzz("d*l*m*n", "*l*m*n");
testFuzz("*", "*");
