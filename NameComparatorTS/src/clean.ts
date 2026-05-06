import unidecode from 'unidecode';
import { ratio as fuzzball_ratio, partial_ratio as fuzzball_partial_ratio} from 'fuzzball';

import { calculateEditImprovement, getMatchingWordsAndIndices, NameEditor } from './usefulTools.js';
import { compareSpelling } from './comparisons.js';

/**
 * Cleans a singular name to get rid of extra or unhelpful data, and to standardize surnames.
 * 
 * @param name - The name to clean
 * @returns The cleaned name
 */
export function cleanName(name: string): string {

    // Deal with blank names
    if (name == "" ||typeof name !== 'string') {
        return "_";
    };

    // Deal with whitespace
    name = name.replace(/[^\S ]/g, ' ');
    name = name.replace(/\s+/g, ' ');
    name = name.trim();

    // Standardize name into ascii
    name = unidecode(name);
    name = name.toLowerCase();

    // Deal with blank names again
    if (name == "") {
        return "_";
    };

    // Remove Punctuation
    name = name.replace(/[.,?;\"*()]/g, '');

    // Remove spaces after apostrophe
    name = name.replace(/' +/g, "'");

    // Remove jr and sr
    name = name.replace(/\bjr\b/gi, "").replace(/\bjunior\b/gi, "");
    name = name.replace(/\bsr\b/gi, "").replace(/\bsenior\b/gi, "");

    // Remove titles
    name = name.replace(/\bprof\b/g, '').replace(/\bprofessor\b/g, '');
    name = name.replace(/\bmr\b/g, '').replace(/\bmister\b/g, '');
    name = name.replace(/\bmrs\b/g, '').replace(/\bmissus\b/g, '');
    name = name.replace(/\bmiss\b/g, '').replace(/\bms\b/g, '');
    name = name.replace(/\bdr\b/g, '').replace(/\bdoctor\b/g, '');
    name = name.replace(/\bstudent\b/g, '');
    name = name.replace(/\brev\b/g, '').replace(/reverend/g, '');

    // Remove family relations
    name = name.replace(/\bsister\b/g, '').replace(/\bbrother\b/g, '').replace(/\bmother\b/g, '').replace(/\bfather\b/g, '');
    name = name.replace(/ in law/g, '');

    // Remove "head of household"
    name = name.replace(/head of household/g, '');

    // Remove Common Abbreviations
    const commonAbreviations = {
        'wm': 'william',
        'geo': 'george',
        'chas': 'charles',
        'thos': 'thomas',
        'jas': 'james',
        'jno': 'john',
        'robt': 'robert',
        'jos': 'joseph',
        'benj': 'benjamin'
    };
    const nameAsList = [];
    for (const word of name.trim().split(/\s+/)) {
        nameAsList.push(commonAbreviations[word as keyof typeof commonAbreviations] || word);
    };
    name = nameAsList.join(' ');

    // Remove stuff like 'the 3rd'
    name = name.replace(/the [1-9][a-z]2,6/g, '').replace(" the ", "");

    // Remove Roman numerals
    name = name.trim().split(/\s+/)
        .map(word => word.replace(/\b(ii|iii|iv)\b/, ''))  // Remove Roman numerals ii, iii, iv
        .join(' ');

    // remove 'no suffix'
    name = name.replace("no suffix", "");

    // Deal with Dutch names
    // name = name.replace(/\bvan de\b/g, 'vande')
    //            .replace(/\bvan den\b/g, 'vanden')
    //            .replace(/\bvan der\b/g, 'vander');
    
    // Deal with whitespace one last time, then return
    name = name.replace(/\s+/g, ' ')
               .trim();
    if (name == "") {
        return "_";
    };

    console.error(`TypeScript cleaned the name to be ${name}`);

    return name;
};

/**
 * Cleans two names together, fixing common errors to standardize.
 * 
 * @param nameOne - The first name to clean
 * @param nameTwo - The second name to clean
 * @returns The two cleaned names and a boolean noting whether or 
            not to perform a confidence penalty based on if a prefix 
            was removed
 */
export function cleanNamesByComparison(nameOne: string = "_", nameTwo: string = "_"): [string, string, boolean] {

    var shouldPenaltyApply = false;
    var wasScottishPrefixRemoved = false;
    var wasMcOrMacRemoved = false;
    var wasPrefixModified = false;

    // Return if either name is blank
    if (nameOne == "_" || nameTwo == "_") {
        return [nameOne, nameTwo, false]
    };

    // Deal with dashes
    [nameOne, nameTwo] = _dealWithDashes(nameOne, nameTwo);

    // Deal with Scottish and Irish names
    [nameOne, nameTwo, wasScottishPrefixRemoved] = _fixRelatedPrefixes(nameOne, nameTwo, 'mac', 'mc');
    [nameOne, nameTwo, wasMcOrMacRemoved] = _fixMcAndMacNames(nameOne, nameTwo);

    // Deal with just Irish names
    const irishNamesStartingWithO = [
        'beirne', 'berry', 'boyle', 'bryant', 'brian', 'brien', 'bryan', 'ceallaigh', 'conner',
        'connor', 'conor', 'daniel', 'day', 'dean', 'dea', 'doherty', 'donnell', 'donnel', 'donoghue',
        'donohue', 'donovan', 'dowd', 'driscoll', 'fallon', 'farrell', 'flaherty', 'flanagan', 'flynn',
        'gara', 'gorman', 'grady', 'guinn', 'guin', 'hagan', 'haire', 'hair', 'halloran', 'hanlon',
        'hara', 'hare', 'harra', 'harrow', 'haver', 'hearn', 'hern', 'herron', 'higgins', 'hora',
        'kane', 'keefe', 'keeffe', 'kelley', 'kelly', 'laughlin', 'leary', 'loughlin', 'mahoney',
        'mahony', 'maley', 'malley', 'mara', 'mary', 'meara', 'melia', 'moore', 'more', 'muir',
        'murchu', 'mure', 'murphy', 'neall', 'neal', 'neill', 'neil', 'ney', 'niall', 'quinn', 'regan',
        'reilly', 'riley', 'riordan', 'roark', 'rorke', 'rourke', 'ryan', 'shaughnessy', 'shea',
        'shields', 'sullivan', 'toole', 'tool',
    ];

    if (nameOne.includes(" o ") || nameOne.includes(" o") || nameTwo.includes(" o ") || nameTwo.includes(" o")){
        for (const surname of irishNamesStartingWithO) {
            if (nameOne.includes(surname) || nameTwo.includes(surname)){
                [nameOne, nameTwo] = _removeIrishO(nameOne, nameTwo, surname);
            };
        };
    };

    // Deal with prefixes and optional intros that make the match worse
    [nameOne, nameTwo, wasPrefixModified] = _handlePrefixesInNames(nameOne, nameTwo);

    // Combine words that are one word in the other name
    while (true) {
        let combined: boolean;
        [combined, nameOne, nameTwo] = _combineSplitWords(nameOne, nameTwo);
        if (!combined) {
            break;
        };
    };
    while (true) {
        let combined: boolean;
        [combined, nameTwo, nameOne] = _combineSplitWords(nameTwo, nameOne);
        if (!combined) {
            break;
        };
    };

    // Remove extra spaces
    nameOne = nameOne.replace(/\s+/g, ' ')
                     .trim();
    nameTwo = nameTwo.replace(/\s+/g, ' ')
                     .trim();

    if ((wasMcOrMacRemoved === true) || (wasPrefixModified === true) || (wasScottishPrefixRemoved === true)){
        shouldPenaltyApply = true;
    };

    // Return if either name is blank
    if (nameOne == "") {
        nameOne = "_";
    };
    if (nameTwo == "") {
        nameTwo = "_";
    };

    return [nameOne, nameTwo, shouldPenaltyApply];
};

/**
 * This is a helper function for clean_names_by_comparison that helps manage its
 * cyclomatic complexity. It takes in two names that are going to be compared later
 * on and figures out what needs to be done with prefixes that might be on them to
 * ensure that later standardization goes smoothly.
 * 
 * @param nameOne - The first name to run prefix checks and handling on
 * @param nameTwo - The second name to run prefix checks and handling on
 * @returns A tuple containing the input names, with prefixes modified in a way that 
 *          lets them be standardized later on
 */
function _handlePrefixesInNames(nameOne: string, nameTwo: string): [string, string, boolean]{

    console.error(`Handling prefixes in names ${nameOne} and ${nameTwo} in TypeScript`);

    // Create a list of prefixes to check
    const possible_prefixes = [
        "d'", "de", "fi", "santa", "san", "de la", "de los", "del", "la", "le", "du", "dela", "los", 
        "der", "den", "vanden", "vander", "vande", "van", "von", 'di', 'dil'
    ];

    // Deal with any prefix and optional intros that make the match worse
    nameOne = nameOne.replace(/\s+/, ' ')
                     .trim();
    nameTwo = nameTwo.replace(/\s+/, ' ')
                     .trim();
    var wasAPrefixModified = false;

    for (const prefix of possible_prefixes){
        if (nameOne.includes(` ${prefix}`) || nameTwo.includes(` ${prefix}`)){

            var didWeFixPrefixes = false;
            var didWeRemovePrefixes = false;

            if ((prefix === "de") || (prefix ==="di")){
                console.error("Found a de or di prefix in a word in TypeScript");
                [nameOne, nameTwo, didWeFixPrefixes] = _fixRelatedPrefixes(nameOne, nameTwo, 'de', 'di');
                [nameOne, nameTwo, didWeRemovePrefixes] = _removeUnnecessaryPrefixes('de', nameOne, nameTwo);
                // [nameOne, nameTwo] = _combinePrefixWithSurnameifInBoth(nameOne, nameTwo, 'de');
            } else if ((prefix === "del") || (prefix === "dil")){
                console.error("Found a del or dil prefix in a word in TypeScript");
                [nameOne, nameTwo, didWeFixPrefixes] = _fixRelatedPrefixes(nameOne, nameTwo, 'del', 'dil');
                [nameOne, nameTwo, didWeRemovePrefixes] = _removeUnnecessaryPrefixes('del', nameOne, nameTwo);
            } else if (prefix === "van") {
                console.error("Found a van prefix in a word in TypeScript");
                [nameOne, nameTwo, didWeRemovePrefixes] = _removeUnnecessaryPrefixes('van', nameOne, nameTwo);
                // [nameOne, nameTwo] = _combinePrefixWithSurnameifInBoth(nameOne, nameTwo, 'van');
            } else {
                console.error("Found a generic prefix in a word in TypeScript");
                [nameOne, nameTwo, didWeRemovePrefixes] = _removeUnnecessaryPrefixes(prefix, nameOne, nameTwo);
            };

            if ((didWeFixPrefixes === true) || (didWeRemovePrefixes === true)){
                wasAPrefixModified = true;
            };
        };
    };

    console.error(`Finished handling names in prefixes in TypeScript. Final result - nameOne: ${nameOne}  nameTwo: ${nameTwo}`);

    return [nameOne, nameTwo, wasAPrefixModified];
};

/**
 * Cleans both names in order to deal with dashes in names.
 * 
 * @param nameOne - The first name to clean
 * @param nameTwo - The second name to clean
 * @returns A tuple containing the modified names with consistency in dashes
 */
function _dealWithDashes(nameOne: string, nameTwo: string): [string, string] {

    // Return old if no dash in either
    if (!nameOne.includes('-') && !nameTwo.includes('-')) {
        return [nameOne, nameTwo];
    };

    // Return old if dash in both
    if (nameOne.includes('-') && nameTwo.includes('-')) {
        return [nameOne, nameTwo];
    };

    // Try replacing the dash with a space, and combine words if necessary
    var nameOneEdited = nameOne.replace('-', ' ');
    var nameTwoEdited = nameTwo.replace('-', ' ');
    if (!nameOneEdited) {
        nameOneEdited = "_";
    };
    if (!nameTwoEdited) {
        nameTwoEdited = "_";
    };
    var [combined, nameOneEdited, nameTwoEdited] = _combineSplitWords(nameOneEdited, nameTwoEdited);
    
    // Return old if the score did not improve
    const [diff, useless, uselessTwo] = calculateEditImprovement(nameOne, nameTwo, nameOneEdited, nameTwoEdited);
    if (diff <= 0) {
        return [nameOne, nameTwo];
    };

    return [nameOneEdited, nameTwoEdited];
}

/**
 * Combines words within one of the names if that combination is one word in the other name.
 * 
 * @param nameOne - The first name to clean
 * @param nameTwo - The second name to clean
 * @returns Whether or not the names were modified and the modified names
 */
function _combineSplitWords(nameOne: string, nameTwo: string): [boolean, string, string] {

    console.error(`Combining split words ${nameOne} and ${nameTwo} in TypeScript`);

    const wordsInNameOne = nameOne.trim().split(/\s+/);

    // Do not combine words that are only two in length
    if (wordsInNameOne.length < 3) {
        console.error("Words aren't long enough to combine");
        return [false, nameOne, nameTwo];
    };

    // Do not combine words that are already a good spelling match
    if (compareSpelling(nameOne, nameTwo)[0]) {
        console.error("Words are not a good spelling match");
        return [false, nameOne, nameTwo];
    };
    
    for (const [indexOne, indexTwo, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        // Skip if wordOne and wordTwo are not a good match
        if (fuzzball_partial_ratio(wordOne, wordTwo, { full_process: false }) < 75) {
            continue;
        };

        // Skip if either word is only an initial
        if (wordOne.length == 1 || wordTwo.length == 1) {
            continue;
        };

        // Find the left and right neighbors
        var leftNeighbor = (indexOne - 1) >= 0 ? wordsInNameOne[indexOne - 1] : "";
        var rightNeighbor = (indexOne + 1) < wordsInNameOne.length ? wordsInNameOne[indexOne + 1] : "";

        // Skip neighbors if they are initials
        leftNeighbor = leftNeighbor.length > 1 ? leftNeighbor : '';
        rightNeighbor = rightNeighbor.length > 1 ? rightNeighbor : '';
        if (!leftNeighbor && !rightNeighbor) {
            return [false, nameOne, nameTwo];
        };

        var [chosenNeighbor, compound, neighborIndex] = _chooseBestNeighborWord(wordOne, indexOne, wordTwo, leftNeighbor, rightNeighbor);

        // Skip if the neighbor is a bad partial match to wordTwo's match
        if (fuzzball_partial_ratio(chosenNeighbor, wordTwo, { full_process: false }) < 65) {
            continue;
        };

        // Check if the compound is significantly better than the original
        const originalScore = fuzzball_ratio(wordOne, wordTwo, { full_process: false });
        const compoundScore = fuzzball_ratio(compound, wordTwo, { full_process: false });
        if (compoundScore < originalScore + 20) {
            continue;
        };
        const differenceOfOriginalLengths = Math.abs(wordTwo.length - wordOne.length);
        const differenceOfCompoundLengths = Math.abs(wordTwo.length - compound.length);
        if (differenceOfOriginalLengths < differenceOfCompoundLengths) {
            continue;
        };

        // If the compound was a better match, use a name editor to create an edited nameOne where the words are combined
        const nameEditorInstance = new NameEditor(nameOne, nameTwo);
        nameEditorInstance.updateNameOne(indexOne, compound);
        nameEditorInstance.updateNameOne(neighborIndex, '');
        const [nameOneEdited, notUsed] = nameEditorInstance.getModifiedNames();

        // If the edited nameOne is better (or only slightly worse), go with the edited version
        const [improvement, useless, uselessTwo] = calculateEditImprovement(nameOne, nameTwo, nameOneEdited, nameTwo);
        if (improvement > -1) {
            return [true, nameOneEdited, nameTwo];
        };
    };

    // If no edits were beneficial, just return the original words
    return [false, nameOne, nameTwo];
};

/**
 * Cleans names to deal with prefixes that are different by spelling, but functionally the same.
 * 
 * @param nameOne - The first name to clean
 * @param nameTwo - The second name to clean
 * @param prefixVariantOne - The first related prefix to check
 * @param prefixVariantTwo - The second related prefix to check
 * @returns The two cleaned names, cleaned to have consistent prefixes, and a boolean 
            representing if changes were made to either of the names
 */
function _fixRelatedPrefixes(nameOne: string, nameTwo: string, prefixVariantOne: string, prefixVariantTwo: string): [string, string, boolean] {

    console.error(`Fixing prefixes for the names ${nameOne} and ${nameTwo} in TypeScript`);

    // Return if prefixVariantOne in neither or prefixVariantTwo in neither
    if (!nameOne.includes(` ${prefixVariantOne}`) && !nameTwo.includes(` ${prefixVariantOne}`)) {
        console.error(`Final result of fixing prefixes in TypeScript - nameOne: ${nameOne}  nameTwo ${nameTwo}`);
        return [nameOne, nameTwo, false];
    };
    if (!nameOne.includes(` ${prefixVariantTwo}`) && !nameTwo.includes(` ${prefixVariantTwo}`)) {
        console.error(`Final result of fixing prefixes in TypeScript - nameOne: ${nameOne}  nameTwo ${nameTwo}`);
        return [nameOne, nameTwo, false];
    };

    // Return if prefixVariantOne in both or prefixVariantTwo in both
    if (nameOne.includes(` ${prefixVariantOne}`) && nameTwo.includes(` ${prefixVariantOne}`)) {
        console.error(`Final result of fixing prefixes in TypeScript - nameOne: ${nameOne}  nameTwo ${nameTwo}`);
        return [nameOne, nameTwo, false];
    };
    if (nameOne.includes(` ${prefixVariantTwo}`) && nameTwo.includes(` ${prefixVariantTwo}`)) {
        console.error(`Final result of fixing prefixes in TypeScript - nameOne: ${nameOne}  nameTwo ${nameTwo}`);
        return [nameOne, nameTwo, false];
    };

    // Replace prefixVariantTwo with prefixVariantOne
    if (nameOne.includes(` ${prefixVariantTwo}`)) {
        nameOne = nameOne.replace(` ${prefixVariantTwo}`, ` ${prefixVariantOne}`);
    } else {
        nameTwo = nameTwo.replace(` ${prefixVariantTwo}`, ` ${prefixVariantOne}`);
    };

    console.error(`Final result of fixing prefixes in TypeScript - nameOne: ${nameOne}  nameTwo ${nameTwo}`);

    return [nameOne, nameTwo, true];
};

/**
 * This function looks at the words that are directly to the right and left of a specific word and then
 * performs a partial ratio to figure out which word is a better match for the specific word. It then
 * returns the compund.
 * 
 * @param wordOne - The word that is being checked for matches
 * @param indexOne - The index of the word that is being checked for matches
 * @param wordTwo - A word used as a reference point in comparison to the selected word
 * @param leftNeighbor - The word to the left of a selected word
 * @param rightNeighbor - The word to the right of a selected word
 * @returns Three items, containing the better neighbor word choice, the compound of the selected
            word and the better neighbor, and the index of the word that is selected as a better 
            neighbor 
 */
function _chooseBestNeighborWord(wordOne: string, indexOne: number, wordTwo: string, leftNeighbor: string, rightNeighbor: string): [string, string, number] {
    
    // Choose the neighbor that best matches wordOne's match
    let wasLeftChosen: boolean;
    if (!leftNeighbor) {
        wasLeftChosen = false;
    } else if (!rightNeighbor) {
        wasLeftChosen = true;
    } else {
        const leftScore = fuzzball_partial_ratio(leftNeighbor, wordTwo, { full_process: false });
        const rightScore = fuzzball_partial_ratio(rightNeighbor, wordTwo, { full_process: false });
        if (leftScore > rightScore) {
            wasLeftChosen = true;
        } else {
            wasLeftChosen = false;
        };
    };

    // Initialize the chosen neighbor, compound, and neighbor index
    let chosenNeighbor: string;
    let compound: string;
    let neighborIndex: number;
    if (wasLeftChosen) {
        chosenNeighbor = leftNeighbor;
        compound = `${leftNeighbor}${wordOne}`;
        neighborIndex = indexOne - 1;
    } else {
        chosenNeighbor = rightNeighbor;
        compound = `${wordOne}${rightNeighbor}`;
        neighborIndex = indexOne + 1;
    };

    return [chosenNeighbor, compound, neighborIndex];
};

/**
 * Modifies names to fix problems where mc or mac are in either names and don't match when they should.
 * 
 * @param nameOne - The first name to clean
 * @param nameTwo - The second name to clean
 * @returns The two names, modified to have matching 'mc' or 'mac' uses, and 
            a boolean representing whether or not the names were modified
 */
function _fixMcAndMacNames(nameOne: string, nameTwo: string): [string, string, boolean] {

    // Return names if mc and mac aren't in either of them
    if (_determineIfSkipNamesInFixMcAndMacNames(nameOne, nameTwo)){
        return [nameOne, nameTwo, false];
    };

    // Combine split words (if any)
    let thingWeDontCareAbout: boolean;
    [thingWeDontCareAbout, nameOne, nameTwo] = _combineSplitWords(nameOne, nameTwo);

    // Edit the names, if necessary
    const nameEditorInstance = new NameEditor(nameOne, nameTwo);
    var wasMcOrMacRemoved = false;
    for (const prefix of ['mc', 'mac']) {
        for (const [indexOne, indexTwo, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {

            var tempFlagForChanges = false;

            // Skip pair if the prefix is in both words
            if (wordOne.startsWith(prefix) && wordTwo.startsWith(prefix)) {
                continue;
            };

            // Skip pair if the prefix is not in either of them
            if (wordOne.startsWith(prefix) && wordTwo.startsWith(prefix)) {
                continue;
            };

            // Skip pair if either word is a firstname
            if (indexOne < 1 || indexTwo < 1) {
                continue;
            };

            // Skip pair if the shortest word is only 4 long
            if (Math.min(wordOne.length, wordTwo.length) < 3) {
                continue;
            };

            // Skip pair if they are already a solid match
            if (fuzzball_ratio(wordOne, wordTwo, { full_process: false }) > 80) {
                continue;
            };

            // Skip pair if the prefix is removed and not a good fuzzy match
            if (wordOne.startsWith(prefix)) {
                var updatedWordOne = wordOne.replace(prefix, '');
                var updatedWordTwo = wordTwo;
                tempFlagForChanges = true;
            } else {
                updatedWordOne = wordOne;
                updatedWordTwo = wordTwo.replace(prefix, '');
                tempFlagForChanges = true;
            };
            if (fuzzball_ratio(updatedWordOne, updatedWordTwo, { full_process: false }) < 75) {
                continue;
            };

            // Update the words
            nameEditorInstance.updateNameOne(indexOne, updatedWordOne);
            nameEditorInstance.updateNameTwo(indexTwo, updatedWordTwo);
            wasMcOrMacRemoved = tempFlagForChanges;
        };
    };

    // Return the edited (or not) names
    const [editedNameOne, editedNameTwo] = nameEditorInstance.getModifiedNames();

    return [editedNameOne, editedNameTwo, wasMcOrMacRemoved];
};

/**
 * A simple function to determine if the prefixes 'mc' or 'mac' are in two selected names to
 * decide if names should be skipped in the _fix_mc_and_mac_names function.
 * 
 * @param nameOne - The first name to check
 * @param nameTwo - The second name to check
 * @returns True if 'mc' and 'mac' are absent from all of the names, indicating that the function can
            skip them. Otherwise, returns false indicating that they need further checks
 */
function _determineIfSkipNamesInFixMcAndMacNames(nameOne: string, nameTwo: string): boolean {
    return (!nameOne.includes('mc') && !nameOne.includes("mac") && !nameTwo.includes('mc') && !nameTwo.includes("mac"));
};

/**
 * Removes the irish O if needed for easier name comparison.
 * 
 * @param nameOne - The first name to remove a possible Irish o from
 * @param nameTwo - The second name to remove a possible Irish o from
 * @param surname - one of the irish surnames that often starts with O'
 * @returns The two modified names, with the Irish o removed
 */
function _removeIrishO(nameOne: string, nameTwo: string, surname: string): [string, string] {

    // Edit the names
    const surnameOne = nameOne.trim().split(/\s+/).pop() || '';
    if (fuzzball_ratio(surnameOne, surname, { full_process: false }) > 75) {
        if (surnameOne[0] == 'o') {
            nameOne = nameOne.replace(surnameOne, surname);
        } else {
            nameOne = nameOne.replace(`o ${surnameOne}`, surname);
        };
    };
    const surnameTwo = nameTwo.trim().split(/\s+/).pop() || '';
    if (fuzzball_ratio(surnameTwo, surname, { full_process: false }) > 75) {
        if (surnameTwo[0] == 'o') {
            nameTwo = nameTwo.replace(surnameTwo, surname);
        } else {
            nameTwo = nameTwo.replace(`o ${surnameTwo}`, surname);
        };
    };

    return [nameOne, nameTwo];
};

/**
 * Removes an unnecessary prefix from either or both of the names if 
 * it would make it harder to detect a name match.
 * 
 * @param prefix - The prefix to (probably) remove from the names
 * @param nameOne - The first name to remove a possible prefix from
 * @param nameTwo - The second name to remove a possible prefix from
 * @returns The two names, modified to have their prefixes removed
            if it's easier to find a name match without them. After 
            this it has a boolean representing whether or not a 
            prefix was removed
 */
function _removeUnnecessaryPrefixes(prefix: string, nameOne: string = "_", nameTwo: string = "_"): [string, string, boolean] {

    console.error(`Removing unnecessary prefix ${prefix} from ${nameOne} and ${nameTwo} in TypeScript`);

    // If the prefix is not in either names, return the names
    if (!nameOne.includes(` ${prefix}`) && !nameTwo.includes(` ${prefix}`)) {
        console.error(`Result of removing unnecessary prefixes in TypeScript - nameOne: ${nameOne}  nameTwo: ${nameTwo}`);
        console.error("TypeScript determined the prefix wasn't in either name")
        return [nameOne, nameTwo, false];
    };
    
    // If the names are already a good match, return the names
    console.error(`Result of compare spelling on the initial two words in TypeScript: ${compareSpelling(nameOne, nameTwo)}`);
    if (compareSpelling(nameOne, nameTwo)[0]) {
        console.error(`Result of removing unnecessary prefixes in TypeScript - nameOne: ${nameOne}  nameTwo: ${nameTwo}`);
        console.error("TypeScript determined the names were already a good enough spelling match");
        return [nameOne, nameTwo, false];
    };

    // Setup
    let nameOneEdited = nameOne;
    let nameTwoEdited = nameTwo;
    const spaceThenPrefixThenSpace = ` ${prefix} `;
    const spaceThenPrefix = ` ${prefix}`;

    var editsMade = false;

    // If the names have different prefix patterns, make them match the same one
    if (nameOne.includes(spaceThenPrefixThenSpace) && nameTwo.includes(spaceThenPrefix)) {
        console.error("Made an edit to the names in TypeScript, following the first possibility");
        nameOneEdited = nameOneEdited.replace(spaceThenPrefixThenSpace, spaceThenPrefix);
        editsMade = true;
    } else if (nameOne.includes(spaceThenPrefix) && nameTwo.includes(spaceThenPrefixThenSpace)) {
        console.error("Made an edit to the names in TypeScript, following the second possibility");
        nameTwoEdited = nameTwoEdited.replace(spaceThenPrefixThenSpace, spaceThenPrefix);
        editsMade = true;
    };

    // If nothing was changed above, this will simply remove the prefixes since they likely don't matter
    console.error(`Names before prefix removal in TypeScript: ${nameOne}, ${nameTwo}`);
    nameOneEdited = nameOneEdited.replace(spaceThenPrefixThenSpace, " ");
    nameTwoEdited = nameTwoEdited.replace(spaceThenPrefixThenSpace, " ");
    console.error(`Names after prefix removal in TypeScript: ${nameOneEdited}, ${nameTwoEdited}`);
    nameOneEdited = nameOneEdited.replace(/\s+/, " ");
    nameTwoEdited = nameTwoEdited.replace(/\s+/, " ");

    console.error(`In TypeScript, for the names ${nameOneEdited} and ${nameTwoEdited}, the first edit check has the value ${editsMade}`);
    
    // If no edits were made, try removing spaceThenPrefix if only in nameOne and it's a long word
    if (editsMade === false){
        [nameOneEdited, editsMade] = _removeSpaceThenPrefixFromUneditedNames(prefix, spaceThenPrefix, nameOneEdited, nameTwoEdited);
    };

    console.error(`In TypeScript, for the names ${nameOneEdited} and ${nameTwoEdited}, the second edit check has the value ${editsMade}`);

    // If no edits were made, try removing spaceThenPrefix if only in nameTwo and it's a long word
    if (editsMade === false){
        [nameTwoEdited, editsMade] = _removeSpaceThenPrefixFromUneditedNames(prefix, spaceThenPrefix, nameTwoEdited, nameOneEdited);
    };

    console.error(`In TypeScript, for the names ${nameOneEdited} and ${nameTwoEdited}, one final edit check is a good idea. It has a value of ${editsMade}`);

    // If the edits were significantly beneficial (or pass spell), return the edited versions
    const [improvement, useless, useless2] = calculateEditImprovement(nameOne, nameTwo, nameOneEdited, nameTwoEdited);
    console.error(`Edit improvement value in TypeScript at this point: ${improvement}`);
    if (improvement >= 10 || compareSpelling(nameOneEdited, nameTwoEdited)[0]) {
        console.error(`Result of removing unnecessary prefixes in TypeScript - nameOne: ${nameOneEdited}  nameTwo: ${nameTwoEdited}`);
        console.error("Calculated an edit improvement in TypeScript that was beneficial");
        return [nameOneEdited, nameTwoEdited, editsMade];
    };

    // Finally, if the words are identical other than the prefix, remove the prefix
    var prefixRemoved = false;
    [nameOneEdited, nameTwoEdited, prefixRemoved] = _removePrefixIfPrefixIsOnlyDifferenceInNames(prefix, nameOneEdited, nameTwoEdited);
    
    console.error(`Result of removing unnecessary prefixes in TypeScript - nameOne: ${nameOneEdited}  nameTwo: ${nameTwoEdited}`);
    console.error("TypeScript ran through all cases in _removeUnnecessaryPrefixes");

    if ((prefixRemoved === true) || (editsMade === true)){
        editsMade = true;
    } else {
        editsMade = false;
    };

    return [nameOneEdited, nameTwoEdited, editsMade];
}

/**
 * This is a helper function for _remove_unnecessary_prefixes that is intended to help
 * resolve its cyclomatic complexity. This function will remove a prefix from two names 
 * that are identical outside of the prefix.
 * 
 * @param prefix - The prefix to check to see if it is the only difference
 * @param nameOne - The first name to compare and possibly remove a prefix from
 * @param nameTwo - The second name to compare and possibly remove a prefix from
 * @returns A tuple containing two names, modified to remove the prefix if they are 
            identical, or the names as input if they aren't identical outside of the 
            prefix. It also has a boolean after this, representing whether or not a 
            prefix was removed
 */
function _removePrefixIfPrefixIsOnlyDifferenceInNames(prefix: string, nameOne: string, nameTwo: string): [string, string, boolean]{

    let nameEditorInstance = new NameEditor(nameOne, nameTwo);
    var nameEdited = false;

    for (const [indexOne, indexTwo, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        if (wordOne.startsWith(prefix) && wordOne.slice(prefix.length) == wordTwo && wordTwo.length > 2) {
            nameEditorInstance.updateNameOne(indexOne, wordOne.slice(prefix.length));
            nameEdited = true;
            console.error("Removed the prefix in TypeScript because it's the only difference between the names");
        } else if (wordTwo.startsWith(prefix) && wordTwo.slice(prefix.length) == wordOne && wordOne.length > 2) {
            nameEditorInstance.updateNameTwo(indexTwo, wordTwo.slice(prefix.length));
            nameEdited = true;
            console.error("Removed the prefix in TypeScript because it's the only difference between the names");
        };
    };

    [nameOne, nameTwo] = nameEditorInstance.getModifiedNames();

    return [nameOne, nameTwo, nameEdited];
};

/**
 * This is a helper function for _remove_unnecessary_prefixes that is intended to remove
 * the " prefix" pattern from words that may or may not have it, if the same pattern is not
 * present in a second word. The utility of this is to create parity between different name
 * parts so they can be accurately compared later.
 * 
 * @param prefix - The possible prefix that needs to be removed
 * @param spaceThenPrefix - A string containing a space before the prefix, used for boolean 
 *                          comparisons and regex matching
 * @param nameToPossiblyChange - The name to check for needed changes
 * @param otherName - The name to compare the target name to, to check for needed changes
 * @returns The end result of the name changes if there were any (or the unchanged name) 
 *          and a boolean variable indicating if any changes were made to
 *          name_to_possibly_change during this function call
 */
function _removeSpaceThenPrefixFromUneditedNames(prefix: string, spaceThenPrefix: string, nameToPossiblyChange: string, otherName: string): [string, boolean] {

    var editHappened: boolean = false;
    const pattern = new RegExp(`\\b${spaceThenPrefix}\\w*\\b`);
    const isSpaceThenPrefixOnlyInNameToChange: boolean = ((nameToPossiblyChange.includes(spaceThenPrefix) === true) && (otherName.includes(spaceThenPrefix) === false));
    const matchInNameToPossiblyChange = nameToPossiblyChange.match(pattern);
    console.error(`Value check for remove space then prefix from unedited names in TypeScript: pattern - ${pattern} isSpaceThenPrefixOnlyInNameToChange - ${isSpaceThenPrefixOnlyInNameToChange} matchInNameToPossiblyChange - ${matchInNameToPossiblyChange}`);
    if ((isSpaceThenPrefixOnlyInNameToChange === true) && (matchInNameToPossiblyChange !== null)){
        var matchedWord = matchInNameToPossiblyChange[0];
        console.error(`Checking matched word value in TypeScript: ${matchedWord}`);
        if (matchedWord.length > (prefix.length + 4)){
            console.error(`TypeScript name before change: ${nameToPossiblyChange}`);
            nameToPossiblyChange = nameToPossiblyChange.replace(spaceThenPrefix, " ");
            console.error(`TypeScript name after change: ${nameToPossiblyChange}`);
            editHappened = true;
        };
    };

    console.error(`TypeScript name after all space the prefix removals: ${nameToPossiblyChange}`);

    return [nameToPossiblyChange, editHappened]
};

/**
 * Combines the prefix with the surname in both of the names if the prefix exists in both.
 * 
 * @param nameOne - The first name to possibly modify
 * @param nameTwo - The second name to possibly modify
 * @param prefix - The prefix to combine with the surname
 * @returns A tuple containing the names with any changes that were made to them or the 
 *          unchanged names
 */
function _combinePrefixWithSurnameifInBoth(nameOne: string, nameTwo: string, prefix: string): [string, string] {

    // Return if ' prefix ' in neither
    if (!nameOne.includes(` ${prefix} `) || !nameTwo.includes(` ${prefix} `)) {
        return [nameOne, nameTwo];
    };

    // Get the letter after ' prefix '
    const letterOne = nameOne[nameOne.indexOf(` ${prefix} `) + 4];
    const letterTwo = nameTwo[nameTwo.indexOf(` ${prefix} `) + 4];

    // If the letter after matches, replace ' prefix ' with ' prefix'
    if (letterOne == letterTwo) {
        nameOne = nameOne.replace(` ${prefix} `, ` ${prefix}`);
        nameTwo = nameTwo.replace(` ${prefix} `, ` ${prefix}`);
    };

    return [nameOne, nameTwo];
};

/**
 * Cleans ipa to get rid of double ipa-consonants and other mistakes.
 * 
 * @param ipa - The ipa to clean
 * @returns The cleaned ipa
 */
export function cleanIpa(ipa: string): string {

    const allIpaConsonants = ['l', 'd', 'z', 'b', 't', 'k', 'n', 's', 'w', 'v', 'ð', 'ʒ', 'ʧ', 'θ', 'h', 'g', 'ʤ', 'ŋ', 'p', 'm', 'ʃ', 'f', 'j', 'r'];
    for (const consonant of allIpaConsonants) {
        const doubleConsonant = consonant + consonant;
        if (ipa.includes(doubleConsonant)) {
            ipa = ipa.replace(doubleConsonant, consonant);
        };
    };
    ipa = ipa.replace("ɛɛ", "i");
    ipa = ipa.replace("ɪɪ", "ɪ");
    ipa = ipa.replace("iɪ", "i");
    ipa = ipa.replace("ŋg", "ŋ");
    ipa = ipa.replace(",", "");

    if (!ipa) {
        ipa = "_";
    };

    return ipa;
}