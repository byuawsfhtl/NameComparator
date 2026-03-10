import unidecode from 'unidecode';
import * as fuzzball from 'fuzzball';

import { calculateEditImprovement, getPairIndicesAndWords, NameEditor } from './usefulTools';
import { spellingComparison } from './comparisons';

/**
 * Cleans a singular name to get rid of extra or unhelpful data, and to standardize surnames.
 * 
 * @param name - The name to clean
 * @returns The cleaned name
 */
export function cleanName(name: string): string {

    // Deal with blank names
    if (name == "" ||typeof name !== 'string') {
        return "_"
    }

    // Deal with whitespace
    name = name.replace(/[^\S ]/g, ' ')
    name = name.replace(/\s+/g, ' ')
    name = name.trim()

    // Standardize name into ascii
    name = unidecode(name)
    name = name.toLowerCase()

    // Deal with blank names again
    if (name == "") {
        return "_"
    }

    // Remove Punctiation
    name = name.replace(/[.,?;\"*()]/g, '')

    // Remove spaces after apostrophe
    name = name.replace(/' +/g, "'")

    // Remove jr and sr
    name = name.replace(/\bjr\b/gi, "").replace(/\bjunior\b/gi, "");
    name = name.replace(/\bsr\b/gi, "").replace(/\bsenior\b/gi, "");

    // Remove titles
    name = name.replace(/\bprof\b/g, '').replace(/\bprofessor\b/g, '')
    name = name.replace(/\bmr\b/g, '').replace(/\bmister\b/g, '')
    name = name.replace(/\bmrs\b/g, '').replace(/\bmissus\b/g, '')
    name = name.replace(/\bmiss\b/g, '').replace(/\bms\b/g, '')
    name = name.replace(/\bdr\b/g, '').replace(/\bdoctor\b/g, '')
    name = name.replace(/\bstudent\b/g, '')
    name = name.replace(/\brev\b/g, '').replace(/reverend/g, '')

    // Remove family relations
    name = name.replace(/\bsister\b/g, '').replace(/\bbrother\b/g, '').replace(/\bmother\b/g, '').replace(/\bfather\b/g, '')
    name = name.replace(/ in law/g, '')

    // Remove "head of household"
    name = name.replace(/head of household/g, '')

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
    }
    const nameAsList = []
    for (const word of name.split(/\s+/)) {
        nameAsList.push(commonAbreviations[word as keyof typeof commonAbreviations] || word)
    }
    name = nameAsList.join(' ')

    // Remove stuff like 'the 3rd'
    name = name.replace(/the [1-9][a-z]2,6/g, '').replace(" the ", "")

    // Remove Roman numerals
    name = name.split(/\s+/)
    .map(word => word.replace(/\b(ii|iii|iv)\b/, ''))  // Remove Roman numerals ii, iii, iv
    .join(' ');

    // remove 'no suffix'
    name = name.replace("no suffix", "")

    // Deal with Dutch names
    name = name.replace(/\bvan de\b/g, 'vande').replace(/\bvan den\b/g, 'vanden').replace(/\bvan der\b/g, 'vander')
    
    // Deal with whitespace one last time, then return
    name = name.replace(/\s+/g, ' ').trim()
    if (name == "") {
        return "_"
    }
    return name
}

/**
 * Cleans two names together, fixing common errors to standardize.
 * 
 * @param nameA - The first name to clean
 * @param nameB - The second name to clean
 * @returns The two cleaned names
 */
export function cleanNamesTogether(nameA: string, nameB: string): [string, string] {

    // Return if either name is blank
    if (nameA == "") {
        nameA = "_"
    }
    if (nameB == "") {
        nameB = "_"
    }

    // Deal with dashes
    const [newNameA, newNameB] = _dealWithDashes(nameA, nameB);
    nameA = newNameA;
    nameB = newNameB;

    // Deal with Scottish and Irish names
    const [fixedNameA1, fixedNameB1] = _fixRelatedPrefixes(nameA, nameB, 'mac', 'mc');
    nameA = fixedNameA1;
    nameB = fixedNameB1;
    
    const [fixedNameA2, fixedNameB2] = _fixMcMac(nameA, nameB);
    nameA = fixedNameA2;
    nameB = fixedNameB2;

    // Deal with just Irish names
    const oNames = [
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
    ]
    for (const surname of oNames) {
        const [newNameA, newNameB] = _removeIrishO(nameA, nameB, surname);
        nameA = newNameA;
        nameB = newNameB;
    }

    // Deal with prefixes and optional intros that make the match worse
    const [nameA1, nameB1] = _fixRelatedPrefixes(nameA, nameB, 'de', 'di');
    const [nameA2, nameB2] = _fixRelatedPrefixes(nameA1, nameB1, 'del', 'dil');
    const [nameA3, nameB3] = _removeUnnecessaryPrefixes(nameA2, nameB2, "d'");
    const [nameA4, nameB4] = _removeUnnecessaryPrefixes(nameA3, nameB3, "de");
    const [nameA5, nameB5] = _removeUnnecessaryPrefixes(nameA4, nameB4, "fi");
    const [nameA6, nameB6] = _removeUnnecessaryPrefixes(nameA5, nameB5, "santa");
    const [nameA7, nameB7] = _removeUnnecessaryPrefixes(nameA6, nameB6, "san");
    const [nameA8, nameB8] = _removeUnnecessaryPrefixes(nameA7, nameB7, "de la");
    const [nameA9, nameB9] = _removeUnnecessaryPrefixes(nameA8, nameB8, "de los");
    const [nameA10, nameB10] = _removeUnnecessaryPrefixes(nameA9, nameB9, "del");
    const [nameA11, nameB11] = _removeUnnecessaryPrefixes(nameA10, nameB10, "la");
    const [nameA12, nameB12] = _removeUnnecessaryPrefixes(nameA11, nameB11, "le");
    const [nameA13, nameB13] = _removeUnnecessaryPrefixes(nameA12, nameB12, "du");
    const [nameA14, nameB14] = _removeUnnecessaryPrefixes(nameA13, nameB13, "dela");
    const [nameA15, nameB15] = _removeUnnecessaryPrefixes(nameA14, nameB14, "los");
    const [nameA16, nameB16] = _removeUnnecessaryPrefixes(nameA15, nameB15, "der");
    const [nameA17, nameB17] = _removeUnnecessaryPrefixes(nameA16, nameB16, "den");
    const [nameA18, nameB18] = _removeUnnecessaryPrefixes(nameA17, nameB17, "vanden");
    const [nameA19, nameB19] = _removeUnnecessaryPrefixes(nameA18, nameB18, "vander");
    const [nameA20, nameB20] = _removeUnnecessaryPrefixes(nameA19, nameB19, "vande");
    const [nameA21, nameB21] = _removeUnnecessaryPrefixes(nameA20, nameB20, "van");
    const [nameA22, nameB22] = _removeUnnecessaryPrefixes(nameA21, nameB21, "van der");
    const [nameA23, nameB23] = _removeUnnecessaryPrefixes(nameA22, nameB22, "van den");
    const [nameA24, nameB24] = _removeUnnecessaryPrefixes(nameA23, nameB23, "van de");
    const [nameA25, nameB25] = _removeUnnecessaryPrefixes(nameA24, nameB24, "van");
    const [nameA26, nameB26] = _removeUnnecessaryPrefixes(nameA25, nameB25, "von");
    const [nameA27, nameB27] = _combinePrefixWithSurnameifInBoth(nameA26, nameB26, "de");
    const [nameA28, nameB28] = _combinePrefixWithSurnameifInBoth(nameA27, nameB27, "van");
    nameA = nameA28;
    nameB = nameB28;

    // Combine words that are one word in the other name
    while (true) {
        const [combined, splitNameA, splitNameB] = _combineSplitWords(nameA, nameB);
        if (!combined) {
            break;
        }
        nameA = splitNameA;
        nameB = splitNameB;
    }
    while (true) {
        const [combined, splitNameB, splitNameA] = _combineSplitWords(nameB, nameA);
        if (!combined) {
            break;
        }
        nameA = splitNameA;
        nameB = splitNameB;
    }

    // Remove extra spaces
    nameA = nameA.replace(/\s+/g, ' ').trim()
    nameB = nameB.replace(/\s+/g, ' ').trim()

    // Return if either name is blank
    if (nameA == "") {
        nameA = "_"
    }
    if (nameB == "") {
        nameB = "_"
    }

    return [nameA, nameB]
}

/**
 * Cleans both names in order to deal with dashes in names.
 * 
 * @param nameA - The first name to clean
 * @param nameB - The second name to clean
 * @returns The two cleaned names
 */
function _dealWithDashes(nameA: string, nameB: string): [string, string] {

    // Return old if no dash in either
    if (!nameA.includes('-') && !nameB.includes('-')) {
        return [nameA, nameB]
    }

    // Return old if dash in both
    if (nameA.includes('-') && nameB.includes('-')) {
        return [nameA, nameB]
    }

    // Try replacing the dash with a space, and combine words if necessary
    var nameAEdited = nameA.replace('-', ' ');
    var nameBEdited = nameB.replace('-', ' ');
    if (!nameAEdited) {
        nameAEdited = "_";
    }
    if (!nameBEdited) {
        nameBEdited = "_";
    }
    var [combined, nameAEdited, nameBEdited] = _combineSplitWords(nameAEdited, nameBEdited);
    
    // Return old if the score did not improve
    const [diff, useless, useless2] = calculateEditImprovement(nameA, nameB, nameAEdited, nameBEdited);
    if (diff <= 0) {
        return [nameA, nameB]
    }

    return [nameAEdited, nameBEdited]
}

/**
 * Combines words within one of the names if that combination is one word in the other name.
 * 
 * @param nameA - The first name to clean
 * @param nameB - The second name to clean
 * @returns The two cleaned names
 */
function _combineSplitWords(nameA: string, nameB: string): [boolean, string, string] {

    const wordsInA = nameA.split(/\s+/);

    // Do not combine words that are only two in length
    if (wordsInA.length < 3) {
        return [false, nameA, nameB]
    }

    // Do not combine words that are already a good spelling match
    if (spellingComparison(nameA, nameB)[0]) {
        return [false, nameA, nameB]
    }
    
    for (const [indexA, indexB, wordA, wordB] of getPairIndicesAndWords(nameA, nameB)) {
        // Skip if wordA and wordB are not a good match
        if (fuzzball.partial_ratio(wordA, wordB) < 75) {
            continue;
        }

        // Skip if either word is only an initial
        if (wordA.length == 1 || wordB.length == 1) {
            continue;
        }

        // Find the left and right neighbors
        var leftNeighbor = wordsInA[indexA - 1] || '';
        var rightNeighbor = wordsInA[indexA + 1] || '';

        // Skip neighbors if they are initials
        leftNeighbor = leftNeighbor.length > 1 ? leftNeighbor : '';
        rightNeighbor = rightNeighbor.length > 1 ? rightNeighbor : '';
        if (!leftNeighbor && !rightNeighbor) {
            return [false, nameA, nameB]
        }

        // Choose the neighbor that best matches wordA's match
        let leftWasChosen = false;
        let rightWasChosen = false;
        if (!leftNeighbor) {
            leftWasChosen = false;
        }
        else if (!rightNeighbor) {
            leftWasChosen = true;
        }
        else {
            const leftScore = fuzzball.partial_ratio(leftNeighbor, wordB);
            const rightScore = fuzzball.partial_ratio(rightNeighbor, wordB);
            if (leftScore > rightScore) {
                leftWasChosen = true;
            }
            else {
                leftWasChosen = false;
            }
        }

        // Initialize the chosen neighbor, compound, and neighbor index
        let chosenNeighbor = '';
        let compound = '';
        let neighborIndex = 0;
        if (leftWasChosen) {
            chosenNeighbor = leftNeighbor;
            compound = `${leftNeighbor}${wordA}`;
            neighborIndex = indexA - 1;
        }
        else {
            chosenNeighbor = rightNeighbor;
            compound = `${wordA}${rightNeighbor}`;
            neighborIndex = indexA + 1;
        }

        // Skip if the neighbor is a bad partial match to wordB's match
        if (fuzzball.partial_ratio(chosenNeighbor, wordB) < 65) {
            continue;
        }

        // Check if the compound is significantly better than the original
        const ogScore = fuzzball.ratio(wordA, wordB);
        const compoundScore = fuzzball.ratio(compound, wordB);
        if (compoundScore < ogScore + 20) {
            continue;
        }
        const diffLengthOriginal = Math.abs(wordB.length - wordA.length);
        const diffLengthCompound = Math.abs(wordB.length - compound.length);
        if (diffLengthOriginal < diffLengthCompound) {
            continue;
        }

        // If the compound was a better match, use a name editor to create an edited nameA where the words are combined
        const ne = new NameEditor(nameA, nameB);
        ne.updateNameA(indexA, compound);
        ne.updateNameA(neighborIndex, '');
        const [nameAEdited, notUsed] = ne.getModifiedNames();

        // If the edited nameA is better (or only slightly worse), go with the edited version
        const [diff, useless, useless2] = calculateEditImprovement(nameA, nameB, nameAEdited, nameB);
        if (diff > -1) {
            return [true, nameAEdited, nameB];
        }
    }

    return [false, nameA, nameB];
}

/**
 * Cleans names to deal with prefixes that are different by spelling, but functionally the same.
 * 
 * @param nameA - The first name to clean
 * @param nameB - The second name to clean
 * @param prefixX - The first prefix to check
 * @param prefixY - The second prefix to check
 * @returns The two cleaned names
 */
function _fixRelatedPrefixes(nameA: string, nameB: string, prefixX: string, prefixY: string): [string, string] {

    // Return if prefixX in neither or prefixY in neither
    if (!nameA.includes(` ${prefixX}`) && !nameB.includes(` ${prefixX}`)) {
        return [nameA, nameB];
    }
    if (!nameA.includes(` ${prefixY}`) && !nameB.includes(` ${prefixY}`)) {
        return [nameA, nameB];
    }

    // Return if prefixX in both or prefixY in both
    if (nameA.includes(` ${prefixX}`) && nameB.includes(` ${prefixX}`)) {
        return [nameA, nameB];
    }
    if (nameA.includes(` ${prefixY}`) && nameB.includes(` ${prefixY}`)) {
        return [nameA, nameB];
    }

    // Replace prefixY with prefixX
    if (nameA.includes(` ${prefixY}`)) {
        nameA = nameA.replace(` ${prefixY}`, ` ${prefixX}`);
    }
    else {
        nameB = nameB.replace(` ${prefixY}`, ` ${prefixX}`);
    }

    return [nameA, nameB];
}

/**
 * Modified names to fix problems where mc or mac are in either names and don't match when they should.
 * 
 * @param nameA - The first name to clean
 * @param nameB - The second name to clean
 * @returns The two modified names 
 */
function _fixMcMac(nameA: string, nameB: string): [string, string] {

    // Return for most names
    if (!nameA.includes('mc') && !nameA.includes('mac') && !nameB.includes('mc') && !nameB.includes('mac')) {
        return [nameA, nameB];
    }

    // Combine split words (if any)
    const [combined, splitNameA, splitNameB] = _combineSplitWords(nameA, nameB);
    nameA = splitNameA;
    nameB = splitNameB;

    // Edit the names, if necessary
    const ne = new NameEditor(nameA, nameB);
    let score = null;
    for (const prefix of ['mc', 'mac']) {
        for (const [indexA, indexB, wordA, wordB] of getPairIndicesAndWords(nameA, nameB)) {
            // Skip pair if the prefix is in both words
            if (wordA.startsWith(prefix) && wordB.startsWith(prefix)) {
                continue;
            }

            // Skip pair if the prefix is not in either of them
            if (wordA.startsWith(prefix) && wordB.startsWith(prefix)) {
                continue;
            }

            // Skip pair if either word is a firstname
            if (indexA < 1 || indexB < 1) {
                continue;
            }

            // Skip pair if the shortest word is only 4 long
            if (Math.min(wordA.length, wordB.length) < 3) {
                continue;
            }

            // Skip pair if they are already a solid match
            if (fuzzball.ratio(wordA, wordB) > 80) {
                continue;
            }

            // Skip pair if the prefix is removed and not a good fuzzy match
            if (wordA.startsWith(prefix)) {
                var updatedWordA = wordA.replace(prefix, '');
                var updatedWordB = wordB;
            }
            else {
                updatedWordA = wordA;
                updatedWordB = wordB.replace(prefix, '');
            }
            if (fuzzball.ratio(updatedWordA, updatedWordB) < 75) {
                continue;
            }

            if(score === null || (score !== null && score < fuzzball.ratio(updatedWordA, updatedWordB))){
                score = fuzzball.ratio(updatedWordA, updatedWordB);
                // Update the words
                ne.updateNameA(indexA, updatedWordA);
                ne.updateNameB(indexB, updatedWordB);
            }
        }
    }

    // Return the edited (or not) names
    return ne.getModifiedNames();
}

/**
 * Removes the irish O if needed for easier name comparison.
 * 
 * @param nameA - The first name to clean
 * @param nameB - The second name to clean
 * @param surname - one of the irish surnames that often starts with O'
 * @returns The two modified names
 */
function _removeIrishO(nameA: string, nameB: string, surname: string): [string, string] {

    // Skip non applicable names
    if (!nameA.includes(" o ") && !nameA.includes(" o") && !nameB.includes(" o") && !nameB.includes(" o ")) {
        return [nameA, nameB];
    }
    if (!nameA.includes(surname) && !nameB.includes(surname)) {
        return [nameA, nameB];
    }

    // Edit the names
    const surnameA = nameA.split(/\s+/).pop() || '';
    if (fuzzball.ratio(surnameA, surname) > 75) {
        if (surnameA[0] == 'o') {
            nameA = nameA.replace(surnameA, surname);
        }
        else {
            nameA = nameA.replace(`o ${surnameA}`, surname);
        }
    }
    const surnameB = nameB.split(/\s+/).pop() || '';
    if (fuzzball.ratio(surnameB, surname) > 75) {
        if (surnameB[0] == 'o') {
            nameB = nameB.replace(surnameB, surname);
        }
        else {
            nameB = nameB.replace(`o ${surnameB}`, surname);
        }
    }

    return [nameA, nameB];
}

/**
 * Removes an unnecessary prefix from either or both of the names.
 * 
 * @param nameA - The first name to clean
 * @param nameB - The second name to clean
 * @param prefix - The prefix to (probably) remove
 * @returns The two modified names
 */
function _removeUnnecessaryPrefixes(nameA: string, nameB: string, prefix: string): [string, string] {

    // Return if the prefix is not in either name
    nameA = nameA.replace(/\s+/, ' ').trim()
    nameB = nameB.replace(/\s+/, ' ').trim()
    if (!nameA.includes(` ${prefix}`) && !nameB.includes(` ${prefix}`)) {
        return [nameA, nameB];
    }
    
    // If the names are already a good match, return the names
    if (spellingComparison(nameA, nameB)[0]) {
        return [nameA, nameB];
    }

    // Setup
    let nameAEdited = nameA;
    let nameBEdited = nameB;
    const spPrefixSp = ` ${prefix} `;
    const spacePrefix = ` ${prefix}`;

    // Make the edited names different
    if (nameA.includes(spPrefixSp) && nameB.includes(spPrefixSp)) {
        // No action needed when both names have the same prefix format
    }
    else if (nameA.includes(spPrefixSp) && nameB.includes(spacePrefix)) {
        nameAEdited = nameAEdited.replace(spPrefixSp, spacePrefix);
    }
    else if (nameA.includes(spacePrefix) && nameB.includes(spPrefixSp)) {
        nameBEdited = nameBEdited.replace(spPrefixSp, spacePrefix);
    }
    nameAEdited = nameAEdited.replace(spPrefixSp, " ");
    nameBEdited = nameBEdited.replace(spPrefixSp, " ");
    nameAEdited = nameAEdited.replace(/\s+/, " ");
    nameBEdited = nameBEdited.replace(/\s+/, " ");
    
    // If no edits were made, try removing spacePrefix if only in nameA and it's a long word
    const pattern = new RegExp(`\\b${spacePrefix}\\w*\\b`, 'g');
    var noEditsMade = (nameA == nameAEdited) && (nameB == nameBEdited);
    const spPreOnlyInNameA = (nameA.includes(spacePrefix)) && (!nameB.includes(spacePrefix));
    const matchOfA = nameA.match(pattern);
    if (noEditsMade && spPreOnlyInNameA && matchOfA) {
        const matchedWord = matchOfA[0];
        if (matchedWord.length > prefix.length + 4) {
            nameAEdited = nameA.replace(spacePrefix, " ");
        }
    }

    // If no edits were made, try removing spacePrefix if only in nameB and it's a long word
    noEditsMade = (nameA == nameAEdited) && (nameB == nameBEdited);
    const spPreOnlyInNameB = (nameB.includes(spacePrefix)) && (!nameA.includes(spacePrefix));
    const matchOfB = nameB.match(pattern);
    if (noEditsMade && spPreOnlyInNameB && matchOfB) {
        const matchedWord = matchOfB[0];
        if (matchedWord.length > prefix.length + 4) {
            nameBEdited = nameB.replace(spacePrefix, " ");
        }
    }

    // Safety
    if (!nameAEdited) {
        nameAEdited = '_';
    }
    if (!nameBEdited) {
        nameBEdited = '_';
    }

    // If the edits were significantly beneficial (or pass spell), return the edited versions
    const [improvement, useless, useless2] = calculateEditImprovement(nameA, nameB, nameAEdited, nameBEdited);
    if (improvement >= 10 || spellingComparison(nameAEdited, nameBEdited)[0]) {
        return [nameAEdited, nameBEdited];
    }

    // Finally, if the words are identical other than the prefix, remove the prefix
    const ne = new NameEditor(nameA, nameB);
    for (const [indexA, indexB, wordA, wordB] of getPairIndicesAndWords(nameA, nameB)) {
        if (wordA.startsWith(prefix) && wordA.slice(prefix.length) == wordB && wordB.length > 2) {
            ne.updateNameA(indexA, wordA.slice(prefix.length));
        }
        else if (wordB.startsWith(prefix) && wordB.slice(prefix.length) == wordA && wordA.length > 2) {
            ne.updateNameB(indexB, wordB.slice(prefix.length));
        }
    }

    [nameA, nameB] = ne.getModifiedNames();
    return [nameA, nameB];
}

/**
 * Combines the prefix with the surname in both of the names if the prefix exists in both.
 * 
 * @param nameA - The first name to clean
 * @param nameB - The second name to clean
 * @param prefix - The prefix to combine with the surname
 * @returns The two modified names
 */
function _combinePrefixWithSurnameifInBoth(nameA: string, nameB: string, prefix: string): [string, string] {

    // Return if ' prefix ' in neither
    if (!nameA.includes(` ${prefix} `) || !nameB.includes(` ${prefix} `)) {
        return [nameA, nameB];
    }

    // Get the letter after ' prefix '
    const letterA = nameA[nameA.indexOf(` ${prefix} `) + 4];
    const letterB = nameB[nameB.indexOf(` ${prefix} `) + 4];

    // If the letter after matches, replace ' prefix ' with ' prefix'
    if (letterA == letterB) {
        nameA = nameA.replace(` ${prefix} `, ` ${prefix}`);
        nameB = nameB.replace(` ${prefix} `, ` ${prefix}`);
    }

    return [nameA, nameB];
}

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
        }
    }
    ipa = ipa.replace("ɛɛ", "i");
    ipa = ipa.replace("ɪɪ", "ɪ");
    ipa = ipa.replace("iɪ", "i");
    ipa = ipa.replace("ŋg", "ŋ");
    ipa = ipa.replace(",", "");

    if (!ipa) {
        ipa = "_";
    }

    return ipa;
}