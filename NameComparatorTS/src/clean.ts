import unidecode from 'unidecode';
import * as fuzzball from 'fuzzball';

import { calculateEditImprovement, getMatchingWordsAndIndices, NameEditor } from './usefulTools';
import { compare_spelling } from './comparisons';

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
    const nameOnesList = []
    for (const word of name.split(/\s+/)) {
        nameOnesList.push(commonAbreviations[word as keyof typeof commonAbreviations] || word)
    }
    name = nameOnesList.join(' ')

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
 * @param nameOne - The first name to clean
 * @param nameTwo - The second name to clean
 * @returns The two cleaned names
 */
export function cleanNamesByComparison(nameOne: string, nameTwo: string): [string, string] {

    // Return if either name is blank
    if (nameOne == "") {
        nameOne = "_"
    }
    if (nameTwo == "") {
        nameTwo = "_"
    }

    // Deal with dashes
    const [newNameOne, newNameTwo] = _dealWithDashes(nameOne, nameTwo);
    nameOne = newNameOne;
    nameTwo = newNameTwo;

    // Deal with Scottish and Irish names
    const [fixedNameOne1, fixedNameTwo1] = _fixRelatedPrefixes(nameOne, nameTwo, 'mac', 'mc');
    nameOne = fixedNameOne1;
    nameTwo = fixedNameTwo1;
    
    const [fixedNameOne2, fixedNameTwo2] = _fixMcAndMacNames(nameOne, nameTwo);
    nameOne = fixedNameOne2;
    nameTwo = fixedNameTwo2;

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
    ]
    for (const surname of irishNamesStartingWithO) {
        const [newNameOne, newNameTwo] = _removeIrishO(nameOne, nameTwo, surname);
        nameOne = newNameOne;
        nameTwo = newNameTwo;
    }

    // Deal with prefixes and optional intros that make the match worse
    const [nameOne1, nameTwo1] = _fixRelatedPrefixes(nameOne, nameTwo, 'de', 'di');
    const [nameOne2, nameTwo2] = _fixRelatedPrefixes(nameOne1, nameTwo1, 'del', 'dil');
    const [nameOne3, nameTwo3] = _removeUnnecessaryPrefixes(nameOne2, nameTwo2, "d'");
    const [nameOne4, nameTwo4] = _removeUnnecessaryPrefixes(nameOne3, nameTwo3, "de");
    const [nameOne5, nameTwo5] = _removeUnnecessaryPrefixes(nameOne4, nameTwo4, "fi");
    const [nameOne6, nameTwo6] = _removeUnnecessaryPrefixes(nameOne5, nameTwo5, "santa");
    const [nameOne7, nameTwo7] = _removeUnnecessaryPrefixes(nameOne6, nameTwo6, "san");
    const [nameOne8, nameTwo8] = _removeUnnecessaryPrefixes(nameOne7, nameTwo7, "de la");
    const [nameOne9, nameTwo9] = _removeUnnecessaryPrefixes(nameOne8, nameTwo8, "de los");
    const [nameOne10, nameTwo10] = _removeUnnecessaryPrefixes(nameOne9, nameTwo9, "del");
    const [nameOne11, nameTwo11] = _removeUnnecessaryPrefixes(nameOne10, nameTwo10, "la");
    const [nameOne12, nameTwo12] = _removeUnnecessaryPrefixes(nameOne11, nameTwo11, "le");
    const [nameOne13, nameTwo13] = _removeUnnecessaryPrefixes(nameOne12, nameTwo12, "du");
    const [nameOne14, nameTwo14] = _removeUnnecessaryPrefixes(nameOne13, nameTwo13, "dela");
    const [nameOne15, nameTwo15] = _removeUnnecessaryPrefixes(nameOne14, nameTwo14, "los");
    const [nameOne16, nameTwo16] = _removeUnnecessaryPrefixes(nameOne15, nameTwo15, "der");
    const [nameOne17, nameTwo17] = _removeUnnecessaryPrefixes(nameOne16, nameTwo16, "den");
    const [nameOne18, nameTwo18] = _removeUnnecessaryPrefixes(nameOne17, nameTwo17, "vanden");
    const [nameOne19, nameTwo19] = _removeUnnecessaryPrefixes(nameOne18, nameTwo18, "vander");
    const [nameOne20, nameTwo20] = _removeUnnecessaryPrefixes(nameOne19, nameTwo19, "vande");
    const [nameOne21, nameTwo21] = _removeUnnecessaryPrefixes(nameOne20, nameTwo20, "van");
    const [nameOne22, nameTwo22] = _removeUnnecessaryPrefixes(nameOne21, nameTwo21, "van der");
    const [nameOne23, nameTwo23] = _removeUnnecessaryPrefixes(nameOne22, nameTwo22, "van den");
    const [nameOne24, nameTwo24] = _removeUnnecessaryPrefixes(nameOne23, nameTwo23, "van de");
    const [nameOne25, nameTwo25] = _removeUnnecessaryPrefixes(nameOne24, nameTwo24, "van");
    const [nameOne26, nameTwo26] = _removeUnnecessaryPrefixes(nameOne25, nameTwo25, "von");
    const [nameOne27, nameTwo27] = _combinePrefixWithSurnameifInBoth(nameOne26, nameTwo26, "de");
    const [nameOne28, nameTwo28] = _combinePrefixWithSurnameifInBoth(nameOne27, nameTwo27, "van");
    nameOne = nameOne28;
    nameTwo = nameTwo28;

    // Combine words that are one word in the other name
    while (true) {
        const [combined, splitNameOne, splitNameTwo] = _combineSplitWords(nameOne, nameTwo);
        if (!combined) {
            break;
        }
        nameOne = splitNameOne;
        nameTwo = splitNameTwo;
    }
    while (true) {
        const [combined, splitNameTwo, splitNameOne] = _combineSplitWords(nameTwo, nameOne);
        if (!combined) {
            break;
        }
        nameOne = splitNameOne;
        nameTwo = splitNameTwo;
    }

    // Remove extra spaces
    nameOne = nameOne.replace(/\s+/g, ' ').trim()
    nameTwo = nameTwo.replace(/\s+/g, ' ').trim()

    // Return if either name is blank
    if (nameOne == "") {
        nameOne = "_"
    }
    if (nameTwo == "") {
        nameTwo = "_"
    }

    return [nameOne, nameTwo]
}

/**
 * Cleans both names in order to deal with dashes in names.
 * 
 * @param nameOne - The first name to clean
 * @param nameTwo - The second name to clean
 * @returns The two cleaned names
 */
function _dealWithDashes(nameOne: string, nameTwo: string): [string, string] {

    // Return old if no dash in either
    if (!nameOne.includes('-') && !nameTwo.includes('-')) {
        return [nameOne, nameTwo]
    }

    // Return old if dash in both
    if (nameOne.includes('-') && nameTwo.includes('-')) {
        return [nameOne, nameTwo]
    }

    // Try replacing the dash with a space, and combine words if necessary
    var nameOneEdited = nameOne.replace('-', ' ');
    var nameTwoEdited = nameTwo.replace('-', ' ');
    if (!nameOneEdited) {
        nameOneEdited = "_";
    }
    if (!nameTwoEdited) {
        nameTwoEdited = "_";
    }
    var [combined, nameOneEdited, nameTwoEdited] = _combineSplitWords(nameOneEdited, nameTwoEdited);
    
    // Return old if the score did not improve
    const [diff, useless, uselessTwo] = calculateEditImprovement(nameOne, nameTwo, nameOneEdited, nameTwoEdited);
    if (diff <= 0) {
        return [nameOne, nameTwo]
    }

    return [nameOneEdited, nameTwoEdited]
}

/**
 * Combines words within one of the names if that combination is one word in the other name.
 * 
 * @param nameOne - The first name to clean
 * @param nameTwo - The second name to clean
 * @returns The two cleaned names
 */
function _combineSplitWords(nameOne: string, nameTwo: string): [boolean, string, string] {

    const wordsInNameOne = nameOne.split(/\s+/);

    // Do not combine words that are only two in length
    if (wordsInNameOne.length < 3) {
        return [false, nameOne, nameTwo]
    }

    // Do not combine words that are already a good spelling match
    if (compare_spelling(nameOne, nameTwo)[0]) {
        return [false, nameOne, nameTwo]
    }
    
    for (const [indexOne, indexTwo, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        // Skip if wordOne and wordTwo are not a good match
        if (fuzzball.partial_ratio(wordOne, wordTwo) < 75) {
            continue;
        }

        // Skip if either word is only an initial
        if (wordOne.length == 1 || wordTwo.length == 1) {
            continue;
        }

        // Find the left and right neighbors
        var leftNeighbor = wordsInNameOne[indexOne - 1] || '';
        var rightNeighbor = wordsInNameOne[indexOne + 1] || '';

        // Skip neighbors if they are initials
        leftNeighbor = leftNeighbor.length > 1 ? leftNeighbor : '';
        rightNeighbor = rightNeighbor.length > 1 ? rightNeighbor : '';
        if (!leftNeighbor && !rightNeighbor) {
            return [false, nameOne, nameTwo]
        }

        // Choose the neighbor that best matches wordOne's match
        let wasLeftChosen = false;
        if (!leftNeighbor) {
            wasLeftChosen = false;
        }
        else if (!rightNeighbor) {
            wasLeftChosen = true;
        }
        else {
            const leftScore = fuzzball.partial_ratio(leftNeighbor, wordTwo);
            const rightScore = fuzzball.partial_ratio(rightNeighbor, wordTwo);
            if (leftScore > rightScore) {
                wasLeftChosen = true;
            }
            else {
                wasLeftChosen = false;
            }
        }

        // Initialize the chosen neighbor, compound, and neighbor index
        let chosenNeighbor = '';
        let compound = '';
        let neighborIndex = 0;
        if (wasLeftChosen) {
            chosenNeighbor = leftNeighbor;
            compound = `${leftNeighbor}${wordOne}`;
            neighborIndex = indexOne - 1;
        }
        else {
            chosenNeighbor = rightNeighbor;
            compound = `${wordOne}${rightNeighbor}`;
            neighborIndex = indexOne + 1;
        }

        // Skip if the neighbor is a bad partial match to wordTwo's match
        if (fuzzball.partial_ratio(chosenNeighbor, wordTwo) < 65) {
            continue;
        }

        // Check if the compound is significantly better than the original
        const originalScore = fuzzball.ratio(wordOne, wordTwo);
        const compoundScore = fuzzball.ratio(compound, wordTwo);
        if (compoundScore < originalScore + 20) {
            continue;
        }
        const differenceOfOriginalLengths = Math.abs(wordTwo.length - wordOne.length);
        const differenceOfCompoundLengths = Math.abs(wordTwo.length - compound.length);
        if (differenceOfOriginalLengths < differenceOfCompoundLengths) {
            continue;
        }

        // If the compound was a better match, use a name editor to create an edited nameOne where the words are combined
        const ne = new NameEditor(nameOne, nameTwo);
        ne.updateNameOne(indexOne, compound);
        ne.updateNameOne(neighborIndex, '');
        const [nameOneEdited, notUsed] = ne.getModifiedNames();

        // If the edited nameOne is better (or only slightly worse), go with the edited version
        const [diff, useless, useless2] = calculateEditImprovement(nameOne, nameTwo, nameOneEdited, nameTwo);
        if (diff > -1) {
            return [true, nameOneEdited, nameTwo];
        }
    }

    return [false, nameOne, nameTwo];
}

/**
 * Cleans names to deal with prefixes that are different by spelling, but functionally the same.
 * 
 * @param nameOne - The first name to clean
 * @param nameTwo - The second name to clean
 * @param prefixVariantOne - The first prefix to check
 * @param prefixVariantTwo - The second prefix to check
 * @returns The two cleaned names
 */
function _fixRelatedPrefixes(nameOne: string, nameTwo: string, prefixVariantOne: string, prefixVariantTwo: string): [string, string] {

    // Return if prefixVariantOne in neither or prefixVariantTwo in neither
    if (!nameOne.includes(` ${prefixVariantOne}`) && !nameTwo.includes(` ${prefixVariantOne}`)) {
        return [nameOne, nameTwo];
    }
    if (!nameOne.includes(` ${prefixVariantTwo}`) && !nameTwo.includes(` ${prefixVariantTwo}`)) {
        return [nameOne, nameTwo];
    }

    // Return if prefixVariantOne in both or prefixVariantTwo in both
    if (nameOne.includes(` ${prefixVariantOne}`) && nameTwo.includes(` ${prefixVariantOne}`)) {
        return [nameOne, nameTwo];
    }
    if (nameOne.includes(` ${prefixVariantTwo}`) && nameTwo.includes(` ${prefixVariantTwo}`)) {
        return [nameOne, nameTwo];
    }

    // Replace prefixVariantTwo with prefixVariantOne
    if (nameOne.includes(` ${prefixVariantTwo}`)) {
        nameOne = nameOne.replace(` ${prefixVariantTwo}`, ` ${prefixVariantOne}`);
    }
    else {
        nameTwo = nameTwo.replace(` ${prefixVariantTwo}`, ` ${prefixVariantOne}`);
    }

    return [nameOne, nameTwo];
}

/**
 * Modified names to fix problems where mc or mac are in either names and don't match when they should.
 * 
 * @param nameOne - The first name to clean
 * @param nameTwo - The second name to clean
 * @returns The two modified names 
 */
function _fixMcAndMacNames(nameOne: string, nameTwo: string): [string, string] {

    // Return for most names
    if (!nameOne.includes('mc') && !nameOne.includes('mac') && !nameTwo.includes('mc') && !nameTwo.includes('mac')) {
        return [nameOne, nameTwo];
    }

    // Combine split words (if any)
    const [combined, splitNameOne, splitNameTwo] = _combineSplitWords(nameOne, nameTwo);
    nameOne = splitNameOne;
    nameTwo = splitNameTwo;

    // Edit the names, if necessary
    const ne = new NameEditor(nameOne, nameTwo);
    let score = null;
    for (const prefix of ['mc', 'mac']) {
        for (const [indexOne, indexTwo, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
            // Skip pair if the prefix is in both words
            if (wordOne.startsWith(prefix) && wordTwo.startsWith(prefix)) {
                continue;
            }

            // Skip pair if the prefix is not in either of them
            if (wordOne.startsWith(prefix) && wordTwo.startsWith(prefix)) {
                continue;
            }

            // Skip pair if either word is a firstname
            if (indexOne < 1 || indexTwo < 1) {
                continue;
            }

            // Skip pair if the shortest word is only 4 long
            if (Math.min(wordOne.length, wordTwo.length) < 3) {
                continue;
            }

            // Skip pair if they are already a solid match
            if (fuzzball.ratio(wordOne, wordTwo) > 80) {
                continue;
            }

            // Skip pair if the prefix is removed and not a good fuzzy match
            if (wordOne.startsWith(prefix)) {
                var updatedWordOne = wordOne.replace(prefix, '');
                var updatedWordTwo = wordTwo;
            }
            else {
                updatedWordOne = wordOne;
                updatedWordTwo = wordTwo.replace(prefix, '');
            }
            if (fuzzball.ratio(updatedWordOne, updatedWordTwo) < 75) {
                continue;
            }

            if(score === null || (score !== null && score < fuzzball.ratio(updatedWordOne, updatedWordTwo))){
                score = fuzzball.ratio(updatedWordOne, updatedWordTwo);
                // Update the words
                ne.updateNameOne(indexOne, updatedWordOne);
                ne.updateNameTwo(indexTwo, updatedWordTwo);
            }
        }
    }

    // Return the edited (or not) names
    return ne.getModifiedNames();
}

/**
 * Removes the irish O if needed for easier name comparison.
 * 
 * @param nameOne - The first name to clean
 * @param nameTwo - The second name to clean
 * @param surname - one of the irish surnames that often starts with O'
 * @returns The two modified names
 */
function _removeIrishO(nameOne: string, nameTwo: string, surname: string): [string, string] {

    // Skip non applicable names
    if (!nameOne.includes(" o ") && !nameOne.includes(" o") && !nameTwo.includes(" o") && !nameTwo.includes(" o ")) {
        return [nameOne, nameTwo];
    }
    if (!nameOne.includes(surname) && !nameTwo.includes(surname)) {
        return [nameOne, nameTwo];
    }

    // Edit the names
    const surnameOne = nameOne.split(/\s+/).pop() || '';
    if (fuzzball.ratio(surnameOne, surname) > 75) {
        if (surnameOne[0] == 'o') {
            nameOne = nameOne.replace(surnameOne, surname);
        }
        else {
            nameOne = nameOne.replace(`o ${surnameOne}`, surname);
        }
    }
    const surnameTwo = nameTwo.split(/\s+/).pop() || '';
    if (fuzzball.ratio(surnameTwo, surname) > 75) {
        if (surnameTwo[0] == 'o') {
            nameTwo = nameTwo.replace(surnameTwo, surname);
        }
        else {
            nameTwo = nameTwo.replace(`o ${surnameTwo}`, surname);
        }
    }

    return [nameOne, nameTwo];
}

/**
 * Removes an unnecessary prefix from either or both of the names.
 * 
 * @param nameOne - The first name to clean
 * @param nameTwo - The second name to clean
 * @param prefix - The prefix to (probably) remove
 * @returns The two modified names
 */
function _removeUnnecessaryPrefixes(nameOne: string, nameTwo: string, prefix: string): [string, string] {

    // Return if the prefix is not in either name
    nameOne = nameOne.replace(/\s+/, ' ').trim()
    nameTwo = nameTwo.replace(/\s+/, ' ').trim()
    if (!nameOne.includes(` ${prefix}`) && !nameTwo.includes(` ${prefix}`)) {
        return [nameOne, nameTwo];
    }
    
    // If the names are already a good match, return the names
    if (compare_spelling(nameOne, nameTwo)[0]) {
        return [nameOne, nameTwo];
    }

    // Setup
    let nameOneEdited = nameOne;
    let nameTwoEdited = nameTwo;
    const spaceThenPrefixThenSpace = ` ${prefix} `;
    const spaceThenPrefix = ` ${prefix}`;

    // Make the edited names different
    if (nameOne.includes(spaceThenPrefixThenSpace) && nameTwo.includes(spaceThenPrefixThenSpace)) {
        // No action needed when both names have the same prefix format
    }
    else if (nameOne.includes(spaceThenPrefixThenSpace) && nameTwo.includes(spaceThenPrefix)) {
        nameOneEdited = nameOneEdited.replace(spaceThenPrefixThenSpace, spaceThenPrefix);
    }
    else if (nameOne.includes(spaceThenPrefix) && nameTwo.includes(spaceThenPrefixThenSpace)) {
        nameTwoEdited = nameTwoEdited.replace(spaceThenPrefixThenSpace, spaceThenPrefix);
    }
    nameOneEdited = nameOneEdited.replace(spaceThenPrefixThenSpace, " ");
    nameTwoEdited = nameTwoEdited.replace(spaceThenPrefixThenSpace, " ");
    nameOneEdited = nameOneEdited.replace(/\s+/, " ");
    nameTwoEdited = nameTwoEdited.replace(/\s+/, " ");
    
    // If no edits were made, try removing spaceThenPrefix if only in nameOne and it's a long word
    const pattern = new RegExp(`\\b${spaceThenPrefix}\\w*\\b`, 'g');
    var noEditsMade = (nameOne == nameOneEdited) && (nameTwo == nameTwoEdited);
    const spaceThenPrefixOnlyInNameOne = (nameOne.includes(spaceThenPrefix)) && (!nameTwo.includes(spaceThenPrefix));
    const matchInNameOne = nameOne.match(pattern);
    if (noEditsMade && spaceThenPrefixOnlyInNameOne && matchInNameOne) {
        const matchedWord = matchInNameOne[0];
        if (matchedWord.length > prefix.length + 4) {
            nameOneEdited = nameOne.replace(spaceThenPrefix, " ");
        }
    }

    // If no edits were made, try removing spaceThenPrefix if only in nameTwo and it's a long word
    noEditsMade = (nameOne == nameOneEdited) && (nameTwo == nameTwoEdited);
    const spaceThenPrefixOnlyInNameTwo = (nameTwo.includes(spaceThenPrefix)) && (!nameOne.includes(spaceThenPrefix));
    const matchInNameTwo = nameTwo.match(pattern);
    if (noEditsMade && spaceThenPrefixOnlyInNameTwo && matchInNameTwo) {
        const matchedWord = matchInNameTwo[0];
        if (matchedWord.length > prefix.length + 4) {
            nameTwoEdited = nameTwo.replace(spaceThenPrefix, " ");
        }
    }

    // Safety
    if (!nameOneEdited) {
        nameOneEdited = '_';
    }
    if (!nameTwoEdited) {
        nameTwoEdited = '_';
    }

    // If the edits were significantly beneficial (or pass spell), return the edited versions
    const [improvement, useless, useless2] = calculateEditImprovement(nameOne, nameTwo, nameOneEdited, nameTwoEdited);
    if (improvement >= 10 || compare_spelling(nameOneEdited, nameTwoEdited)[0]) {
        return [nameOneEdited, nameTwoEdited];
    }

    // Finally, if the words are identical other than the prefix, remove the prefix
    const ne = new NameEditor(nameOne, nameTwo);
    for (const [indexOne, indexTwo, wordOne, wordTwo] of getMatchingWordsAndIndices(nameOne, nameTwo)) {
        if (wordOne.startsWith(prefix) && wordOne.slice(prefix.length) == wordTwo && wordTwo.length > 2) {
            ne.updateNameOne(indexOne, wordOne.slice(prefix.length));
        }
        else if (wordTwo.startsWith(prefix) && wordTwo.slice(prefix.length) == wordOne && wordOne.length > 2) {
            ne.updateNameTwo(indexTwo, wordTwo.slice(prefix.length));
        }
    }

    [nameOne, nameTwo] = ne.getModifiedNames();
    return [nameOne, nameTwo];
}

/**
 * Combines the prefix with the surname in both of the names if the prefix exists in both.
 * 
 * @param nameOne - The first name to clean
 * @param nameTwo - The second name to clean
 * @param prefix - The prefix to combine with the surname
 * @returns The two modified names
 */
function _combinePrefixWithSurnameifInBoth(nameOne: string, nameTwo: string, prefix: string): [string, string] {

    // Return if ' prefix ' in neither
    if (!nameOne.includes(` ${prefix} `) || !nameTwo.includes(` ${prefix} `)) {
        return [nameOne, nameTwo];
    }

    // Get the letter after ' prefix '
    const letterOne = nameOne[nameOne.indexOf(` ${prefix} `) + 4];
    const letterTwo = nameTwo[nameTwo.indexOf(` ${prefix} `) + 4];

    // If the letter after matches, replace ' prefix ' with ' prefix'
    if (letterOne == letterTwo) {
        nameOne = nameOne.replace(` ${prefix} `, ` ${prefix}`);
        nameTwo = nameTwo.replace(` ${prefix} `, ` ${prefix}`);
    }

    return [nameOne, nameTwo];
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