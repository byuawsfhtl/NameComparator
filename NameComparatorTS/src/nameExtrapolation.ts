import { compareTwoNames } from "../nameComparator.js";

/**
 * This function takes in a list of names for a single person
 * and then determines what the most likely best full name is based on 
 * that list, favoring having full names instead of initials or 
 * abbreviations when possible.
 * 
 * @param inputListOfNames - A list of names that contains variations 
 *          of a name for a particular person
 * @param multiplePossibleMatchesDictionary - A dictionary of all of 
 *          the possible name fragment matches and positions that are 
 *          undetermined for a particular name at the time of the start 
 *          of this function
 * @param nameFragmentsAndFrequency - A dictionary of all of the name 
 *          fragments that have been used for the name so far, their 
 *          positions, and their frequencies
 * 
 * @returns A string representing the best or most complete version of 
 *          a name, based on all of the input names and a dictionary 
 *          containing all of the name fragments that haven't been used yet. 
 *          Then a dictionary of all of the unused possible matches for name 
 *          fragments. Then a list of all the name fragments and how 
 *          frequently they appear
 */
export function extrapolateBestFullName(inputListOfNames: string[], multiplePossibleMatchesDictionary: Record<number, NameFragment[]> | null = null, nameFragmentsAndFrequency: NameFragment[] | null = null): [string, Record<number, NameFragment[]>, NameFragment[]]{
    // If variables are None at the start of the function, set them to
    // a more appropriate empty dictionary or list
    if (multiplePossibleMatchesDictionary === null){
        multiplePossibleMatchesDictionary = {};
    };

    if (nameFragmentsAndFrequency === null){
        nameFragmentsAndFrequency = [];
    };

    // If there is nothing in the list of names, we can't
    // determine the best name so return an empty string
    if (inputListOfNames.length === 0){
        return ['', {}, []];
    };

    var cleanedListOfNames = cleanNameList(inputListOfNames);

    // If there is only one name in the cleaned names, we can
    // safely say that's the best name in the list. Just
    // return it
    if(cleanedListOfNames.length === 1){
        return [cleanedListOfNames[0], {}, []];
    };

    // Break all of the names into a collection of pieces I'm calling fragments
    var brokenNameList: BrokenNameDictionary[]
    var indexOfNameWithMostFragments: number;
    [brokenNameList, indexOfNameWithMostFragments, nameFragmentsAndFrequency] = _breakNamesIntoFragments(cleanedListOfNames, nameFragmentsAndFrequency);

    // Order the list of names according to the number of fragments in each name (from
    // largest to smalles) to ensure that the names are sorted as expected
    brokenNameList = [...brokenNameList].sort((a, b) => Number(b['total_fragments']) - Number(a['total_fragments']));

    // Populate an initial array of strings equal to the length of the name with the most
    // fragments, using the fragments from that name as the starting point
    const fragmentCountOfNameWithMostFragments = (brokenNameList[indexOfNameWithMostFragments]['fragment_list']).length; // Note that the as unknown[] isn't an issue since we can guarantee this field is always a list
    var bestNameAsFragments: NameFragment[] = [];
    for (const initialNameFragment of (brokenNameList[indexOfNameWithMostFragments]['fragment_list'])){
        bestNameAsFragments.push(initialNameFragment);
    };

    // Go through each of the name fragments and compare them to the current list of best fragments
    // to determine if there is a better possible name. Store unknown data to parse through later
    for (const brokenName of brokenNameList){
        // If the number of fragments matches the max number of fragments, we can probably safely assume that
        // the names have similar positions as long as their first letters match
        if (brokenName['fragment_list'].length === fragmentCountOfNameWithMostFragments){
            [bestNameAsFragments, multiplePossibleMatchesDictionary] = _extrapolateNamesFromEqualLengthFragments(brokenName, bestNameAsFragments, multiplePossibleMatchesDictionary, nameFragmentsAndFrequency);
        } else {
        // If the number of fragments doesn't match the max number of fragments, we'll need to handle the logic
        // a little bit differently
            [bestNameAsFragments, multiplePossibleMatchesDictionary] = _extrapolateNamesFromDifferentLengthFragments(brokenName, bestNameAsFragments, multiplePossibleMatchesDictionary);
        };
    };

    // After everything else is done, recompile the name fragments into one complete name and return it as a string
    var completeExtrapolatedName = "";
    var addSpacesIndexChecker = 1;
    for (const bestFragment of bestNameAsFragments){
        completeExtrapolatedName = completeExtrapolatedName + bestFragment['edited_fragment'];
        if (addSpacesIndexChecker < bestNameAsFragments.length){
            completeExtrapolatedName = completeExtrapolatedName + " ";
        }
    };

    return [completeExtrapolatedName.trim(), multiplePossibleMatchesDictionary, nameFragmentsAndFrequency];
};

/**
 * This function takes in a list of cleaned names and breaks them
 * up based on spaces and punctuation into their various parts, which
 * are being labelled as fragments. It also determines which of those
 * names has the most total fragments.
 * 
 * @param cleanedListOfNames - A list of names, cleaned by using one of 
 *          the cleaning functions, that contains variations of a name 
 *          for a particular person
 * @param nameFragmentsAndFrequency - A list of all of the name fragments 
 *          that have been used for the name so far, their positions, and 
 *          their frequencies
 * 
 * @returns A list of dictionaries where each entry is a name and the
 *          dictionary within it contains all of the info on the name
 *          fragments. It also returns an integer representing the
 *          index of the name inside of the list that has the most
 *          total fragments in it and a list of all the name fragments 
 *          and how frequently they appear
 */
function _breakNamesIntoFragments(cleanedListOfNames: string[], nameFragmentsAndFrequency: NameFragment[]): [BrokenNameDictionary[], number, NameFragment[]]{
    var brokenNameList = [];
    var currentIndexInNameList = 0;
    var indexOfNameWithMostFragments = 0;
    var fragmentsInNameWithMostFragments = 0;
    for (const name of cleanedListOfNames){
        // Split the name by likely indicators of different names (eg, surname, first name, etc)
        const unfilteredSplitName = name.split(/[. ,]\s*/).map(item => item.trim());
        const splitName = unfilteredSplitName.filter(item => item.trim() !== "");
        const totalNameFragments = splitName.length;

        if (fragmentsInNameWithMostFragments < totalNameFragments){
            fragmentsInNameWithMostFragments = totalNameFragments;
            indexOfNameWithMostFragments = currentIndexInNameList;
        };

        // Create a dictionary to add to a list for later comparison of fragments
        const emptyList: NameFragment[] = [];
        var dictionaryToAddToBrokenNameList: BrokenNameDictionary = {
            'complete_name': name,
            'complete_name_position_in_list': currentIndexInNameList,
            'total_fragments': totalNameFragments,
            'fragment_list': emptyList
        };

        // Remove spaces, commas, and periods from name fragments to get accurate info on them
        for (const nameFragment of splitName){
            const initialFragment = nameFragment;
            var editedNameFragment = nameFragment.trim();
            editedNameFragment = editedNameFragment.replaceAll('.', '');
            editedNameFragment = editedNameFragment.replaceAll(',', '');
            const lengthOfFragment = nameFragment.length;
            const lengthOfEditedFragment = editedNameFragment.length;

            // Add the fragment to the list of fragments in the name
            var fragmentToAdd: NameFragment = {
                'unedited_fragment': initialFragment,
                'edited_fragment': editedNameFragment,
                'length_of_unedited_fragment': lengthOfFragment,
                'edited_fragment_length': lengthOfEditedFragment,
                'fragment_frequency': 1
            };
            dictionaryToAddToBrokenNameList['fragment_list'].push(fragmentToAdd);

            var foundFrequencyFragment = false;
            for (const frequencyFragment of nameFragmentsAndFrequency){
                if (fragmentToAdd['edited_fragment'] === frequencyFragment['edited_fragment']){
                    frequencyFragment['fragment_frequency'] = Number(frequencyFragment['fragment_frequency']) + 1;
                    foundFrequencyFragment = true;
                };
            };

            if (foundFrequencyFragment === false){
                nameFragmentsAndFrequency.push(fragmentToAdd);
            };
        };

        // Add the fully constructed dictionary to the list of broken up names
        brokenNameList.push(dictionaryToAddToBrokenNameList);

        // Update this so we know where we are in the cleaned list of names
        currentIndexInNameList = currentIndexInNameList + 1;
    };

    return [brokenNameList, indexOfNameWithMostFragments, nameFragmentsAndFrequency];
};

/**
 * This function is a helper function for extrapolate_best_full_name that will take in a 
 * name that's been broken into it's name fragments and the currently determined best name,
 * also broken into it's fragments. Then it compares the fragments to each other to 
 * determine if the fragment from the broken name is a better match than the currently known 
 * best fragment.
 * 
 * @param brokenName - A dictionary containing all of the info on a specific name and all 
 *                     of it's fragments
 * @param bestNameAsFragments - A list of name fragments (which are dictionaries) for the 
 *                              best final name result as calculated so far
 * @param multiplePossibleMatchesDictionary - A dictionary containing all of the name 
 *                              fragments that have multiple possible locations that they 
 *                              could fit in. It's used to help determine locations of 
 *                              names later on
 * @param nameFragmentsAndFrequency - A dictionary of all of the name fragments that have 
 *                                    been used for the name so far, their positions, and 
 *                                    their frequencies
 * 
 * @returns A list of name fragments (which are dictionaries) representing the newly updated
 *          calculation for the best final name result. It also returns a list of all of the 
 *          fragments that have multiple possible locations or matches as updated during this 
 *          call of the function
 */
function _extrapolateNamesFromEqualLengthFragments(brokenName: BrokenNameDictionary, bestNameAsFragments: NameFragment[], multiplePossibleMatchesDictionary: Record<number, NameFragment[]>, nameFragmentsAndFrequency: NameFragment[]): [NameFragment[], Record<number, NameFragment[]>]{
    for (const [fragmentIndex, specificFragment] of brokenName['fragment_list'].entries()){
        if (specificFragment['edited_fragment'][0] === bestNameAsFragments[fragmentIndex]['edited_fragment'][0] && specificFragment['edited_fragment_length'] > bestNameAsFragments[fragmentIndex]['edited_fragment_length'] && compareTwoNames(specificFragment['edited_fragment'], bestNameAsFragments[fragmentIndex]['edited_fragment']).match === true){
            bestNameAsFragments[fragmentIndex] = specificFragment;
            for (const currentIndex in multiplePossibleMatchesDictionary){
                if (multiplePossibleMatchesDictionary[currentIndex].includes(specificFragment)){
                    multiplePossibleMatchesDictionary[currentIndex] = removeItemFromList(multiplePossibleMatchesDictionary[currentIndex], specificFragment);
                };
            };
        } else {
        //In the event that it isn't a great match but has the same positioning, it might be good to look
        // at it's occurence count in the name_fragments_and_frequency list. If another name has a higher
        // frequency, it's more likely to be correct so we'll take that one

            //Find the frequency of both names
            var bestNameFragmentFrequency = 0;
            var brokenNameFragmentFrequency = 0;
            for (const frequencyFragment of nameFragmentsAndFrequency){
                if (frequencyFragment['edited_fragment'] === specificFragment['edited_fragment']){
                    brokenNameFragmentFrequency = frequencyFragment['fragment_frequency'];
                };
                if (frequencyFragment['edited_fragment'] === bestNameAsFragments[fragmentIndex]['edited_fragment']){
                    bestNameFragmentFrequency = frequencyFragment['fragment_frequency'];
                };
            };
            // If the new fragment is an initial, we'll just ignore it since we'd want a better name than an initial anyways
            if (specificFragment['edited_fragment'].length === 1 || specificFragment['edited_fragment'] === bestNameAsFragments[fragmentIndex]['edited_fragment']){
                continue;
            };
            // If the new fragment option has more versions, take that
            if (brokenNameFragmentFrequency > bestNameFragmentFrequency){
                bestNameAsFragments[fragmentIndex] = specificFragment;
                for (const currentIndex in multiplePossibleMatchesDictionary){
                    if (multiplePossibleMatchesDictionary[currentIndex].includes(specificFragment)){
                        multiplePossibleMatchesDictionary[currentIndex] = removeItemFromList(multiplePossibleMatchesDictionary[currentIndex], specificFragment);
                    };
                };
            } else if (brokenNameFragmentFrequency === bestNameFragmentFrequency && specificFragment['edited_fragment'][0] === bestNameAsFragments[fragmentIndex]['edited_fragment'][0]) {
            // If they have an equal number and the same initial, just leave an empty intial
            // fragment and add them both to the multiple possible matches dictionary
                if (fragmentIndex in multiplePossibleMatchesDictionary){
                    multiplePossibleMatchesDictionary[fragmentIndex].push(specificFragment);
                } else {
                    multiplePossibleMatchesDictionary[fragmentIndex] = [specificFragment];
                };

                multiplePossibleMatchesDictionary[fragmentIndex].push(bestNameAsFragments[fragmentIndex]);
                var tempIndexTypeEnforcer: NameFragment = {
                    'unedited_fragment': specificFragment['edited_fragment'][0],
                    'edited_fragment': specificFragment['edited_fragment'][0],
                    'length_of_unedited_fragment': 1,
                    'edited_fragment_length': 1,
                    'fragment_frequency': 0
                };
                bestNameAsFragments[fragmentIndex] = tempIndexTypeEnforcer;
            };

            // If the best name one has more versions do nothing and leave the best name as is
        };
    };

    return [bestNameAsFragments, multiplePossibleMatchesDictionary];

};

/**
 * This is a helper function for extrapolate_best_full_name that's used to determine which name
 * fragments belong in the best final name conclusion when the fragments have a different length.
 * It uses a collection of logic to determine if a name fragment is better than a currently accepted
 * one, if there's a conflict, and to determine the order of fragments. This is all used to return
 * an updated list of the best fragments to be included in the conclusion for the final full name.
 * 
 * @param brokenName - A dictionary containing all of the info on a specific name and all 
 *                     of it's fragments
 * @param bestNameAsFragments - A list of name fragments (which are dictionaries) for the 
 *                              best final name result as calculated so far
 * @param multiplePossibleMatchesDictionary - A dictionary containing all of the name 
 *                              fragments that have multiple possible locations that they 
 *                              could fit in. It's used to help determine locations of 
 *                              names later on
 * 
 * 
 * In the future, it will also include:
 * @param nameFragmentsAndFrequency - A dictionary of all of the name fragments that have 
 *                                    been used for the name so far, their positions, and 
 *                                    their frequencies
 * 
 * @returns A list of name fragments (which are dictionaries) representing the newly updated
 *          calculation for the best final name result. It also returns a list of all of the 
 *          fragments that have multiple possible locations or matches as updated during this 
 *          call of the function
 */
function _extrapolateNamesFromDifferentLengthFragments(brokenName: BrokenNameDictionary, bestNameAsFragments: NameFragment[], multiplePossibleMatchesDictionary: Record<number, NameFragment[]>): [NameFragment[], Record<number, NameFragment[]>]{
    var firstAcceptedIndexOfPreviousFragment = -1;
    for (const specificFragment of brokenName['fragment_list']){
        var possibleNameMatchesForSpecificFragment = [];
        var foundFirstAcceptedIndex = false;

        if (bestNameAsFragments.includes(specificFragment)){
            continue;
        };

        // If the first letter of the fragment matches the first letter of a fragment from the best
        // name option, list it as a possible match. If it doesn't match any, list it as an
        // unknown location
        for (const [indexOfFragmentInBestNameList, fragmentOfBestName] of bestNameAsFragments.entries()){
            var acceptedAFragmentThisIteration = false;
            if ((indexOfFragmentInBestNameList > firstAcceptedIndexOfPreviousFragment) && (specificFragment['edited_fragment'][0] === fragmentOfBestName['edited_fragment'][0]) && (specificFragment['edited_fragment'] !== fragmentOfBestName['edited_fragment']) && (compareTwoNames(specificFragment['edited_fragment'], fragmentOfBestName['edited_fragment']).match === true) && ((indexOfFragmentInBestNameList in Object.keys(multiplePossibleMatchesDictionary).map(Number)) && (multiplePossibleMatchesDictionary[indexOfFragmentInBestNameList].includes(specificFragment) === false))){
                possibleNameMatchesForSpecificFragment.push(indexOfFragmentInBestNameList); // Note that this only tracks the possible fragment location matches (by thier indices)
                acceptedAFragmentThisIteration = true;
            };
            if (foundFirstAcceptedIndex === false && acceptedAFragmentThisIteration === true){
                firstAcceptedIndexOfPreviousFragment = indexOfFragmentInBestNameList;
                foundFirstAcceptedIndex = true;
            };
        };

        // If there's only one possible matching slot, we're just going to take that one given that the new fragment is better
        if (possibleNameMatchesForSpecificFragment.length === 1){
            if (specificFragment['edited_fragment'].length > bestNameAsFragments[possibleNameMatchesForSpecificFragment[0]]['edited_fragment'].length){
                if (compareTwoNames(specificFragment['edited_fragment'], bestNameAsFragments[possibleNameMatchesForSpecificFragment[0]]['edited_fragment']).match === true){
                    bestNameAsFragments[possibleNameMatchesForSpecificFragment[0]] = specificFragment;
                };
            };
        }

        // If there are several possible matching slots, we need to store that info for later use
        else if (possibleNameMatchesForSpecificFragment.length > 1) {
            for (const index of possibleNameMatchesForSpecificFragment){
                if (index in multiplePossibleMatchesDictionary) {
                    multiplePossibleMatchesDictionary[index].push(specificFragment);
                } else {
                    multiplePossibleMatchesDictionary[index] = [specificFragment];
                };
            };
        };

        // Now that we have more info, we need to go through each name fragment with an unknown slot
        // and determine if any of them have a more clear location or if they have something equivalent
        // that's been figured out
        [bestNameAsFragments, multiplePossibleMatchesDictionary] = _checkForNewlyDiscoveredMatches(bestNameAsFragments, multiplePossibleMatchesDictionary);

    };

    return [bestNameAsFragments, multiplePossibleMatchesDictionary];
};

/**
 * This is a helper function for _extrapolate_names_from_different_length_fragments
 * that takes in a list of all of the matches with more than one possible location for
 * a name and deteremines if we have the information to place them in a proper
 * place in the final name yet or not.
 * 
 * @param bestNameAsFragments - A list of name fragments (which are dictionaries) for 
 *                              the best final name result as calculated so far
 * @param multiplePossibleMatchesDictionary - A dictionary containing all of the name 
 *                                            fragments that have multiple possible 
 *                                            locations that they could fit in
 * 
 * @returns A list of name fragments (which are dictionaries) representing the newly 
 *          updated calculation for the best final name result. It also returns a 
 *          dictionary containing all the possible remaining name fragments (if any) 
 *          with an unkown location in the final name calculation
 */
function _checkForNewlyDiscoveredMatches(bestNameAsFragments: NameFragment[], multiplePossibleMatchesDictionary: Record<number, NameFragment[]>): [NameFragment[], Record<number, NameFragment[]>]{
    for (const indexKey of Object.keys(multiplePossibleMatchesDictionary).map(Number)){
        // If the item in the name fragments is still an initial, we should definitely look at it
        var checkForInitialInNameFragment = bestNameAsFragments[indexKey]['edited_fragment'];
        if (checkForInitialInNameFragment.length === 1){
            // We need to make sure there are no other names that are an initial that matches the letter
            // that the index key names start with
            var twoOrMoreFragmentsAreTheSameInitial = false;
            for (const [indexOfOtherNameFragment, otherNameFragment] of bestNameAsFragments.entries()){
                // Make sure that we aren't accidentally reading in the same fragment a second time
                if (indexOfOtherNameFragment === indexKey){
                    continue;
                };

                // If it's not, find out if the other name fragment in an initial. If it's not, we can move on. If it is
                // we need to note that there's another name that could possibly have this one as a match that's just an
                // initial, so we'll need to move on and skip this particular name fragment check for now.
                var checkForInitialInOtherNameFragment = otherNameFragment['edited_fragment'];
                if (checkForInitialInOtherNameFragment.length > 1){
                    continue;
                };
                if (checkForInitialInOtherNameFragment[0] === checkForInitialInNameFragment[0]){
                    twoOrMoreFragmentsAreTheSameInitial = true;
                    break;
                };
            };

            // If there are two or more fragments with the same initial, we'll want to shelve the rest of the
            // efforts to determine this segment of the name for now
            if (twoOrMoreFragmentsAreTheSameInitial === true){
                continue;
            };

            // If there are no others that are just an initial, we can check each item inside of the index
            // key to see if it matches the other name fragments that are currently accepted
            var foundAnInitialReplacement = false;
            for (const fragmentToTestForBelonging of multiplePossibleMatchesDictionary[indexKey]){
                // Search to see if there's another fragment that matches this particular name
                var foundMatchingFragmentInOtherLocation = false;
                for (const currentlyAcceptedNameFragment of bestNameAsFragments){
                    const fragmentsAreLikelyTheSame = compareTwoNames(fragmentToTestForBelonging['edited_fragment'], currentlyAcceptedNameFragment['edited_fragment']).match;
                    if (fragmentsAreLikelyTheSame === true && currentlyAcceptedNameFragment['edited_fragment'].length > 1){
                        foundMatchingFragmentInOtherLocation = true;
                        break;
                    };
                };
                // If there is another matching fragment, we don't really want to put it here since it's
                // unlikely to belong in this slot
                if (foundMatchingFragmentInOtherLocation === true){
                    for (const currentIndex of Object.keys(multiplePossibleMatchesDictionary).map(Number)){
                        if (multiplePossibleMatchesDictionary[currentIndex].includes(fragmentToTestForBelonging) === true){
                            var fragmentToRemoveIndex = multiplePossibleMatchesDictionary[currentIndex].indexOf(fragmentToTestForBelonging);
                            multiplePossibleMatchesDictionary[currentIndex].splice(1, fragmentToRemoveIndex);
                        };
                    };
                    continue;
                }
                // If it doesn't match anything else, it probably does go in that slot NOTE: (unless there's 
                // a more frequent alternative maybe?)
                else {
                    bestNameAsFragments[indexKey] = fragmentToTestForBelonging;
                    foundAnInitialReplacement = true;
                    for (const currentIndex of Object.keys(multiplePossibleMatchesDictionary).map(Number)){
                        if (multiplePossibleMatchesDictionary[currentIndex].includes(fragmentToTestForBelonging)){
                            var fragmentToRemoveIndex = multiplePossibleMatchesDictionary[currentIndex].indexOf(fragmentToTestForBelonging);
                            multiplePossibleMatchesDictionary[currentIndex].splice(1, fragmentToRemoveIndex);
                        };
                    };
                    break;
                };
            };

            // If we found any replacements in the previous step, we need to iterate through the remaining
            // possible matches in the dictionary to determine if any of them are a more complete version
            // of the name than the one we took in as a replacement for the initial
            if (foundAnInitialReplacement === true){
                for (const fragmentToTestAsBetterOption of multiplePossibleMatchesDictionary[indexKey]){
                    if (fragmentToTestAsBetterOption['edited_fragment'].length > bestNameAsFragments[indexKey]['edited_fragment'].length) {
                        if (compareTwoNames(fragmentToTestAsBetterOption['edited_fragment'], bestNameAsFragments[indexKey]['edited_fragment']).match === true){
                            bestNameAsFragments[indexKey] = fragmentToTestAsBetterOption;
                        };
                        for (const currentIndex of Object.keys(multiplePossibleMatchesDictionary).map(Number)){
                            if (multiplePossibleMatchesDictionary[currentIndex].includes(fragmentToTestAsBetterOption)){
                                 var fragmentToRemoveIndex = multiplePossibleMatchesDictionary[currentIndex].indexOf(fragmentToTestAsBetterOption);
                                multiplePossibleMatchesDictionary[currentIndex].splice(1, fragmentToRemoveIndex);
                            };
                        };
                    };
                };
            };
        };

        // At the end of this, if there is nothing left in the key, we want to completely remove the key
        if (multiplePossibleMatchesDictionary[indexKey].length === 0){
            delete multiplePossibleMatchesDictionary[indexKey];
        };
    };

    return [bestNameAsFragments, multiplePossibleMatchesDictionary];

};

/**
 * This function takes in a list of names to prepare for name extrapolation,
 * then standardizes them by doing a few initial comparisons to each other and
 * removing any unusual punctuation that's in them.
 * 
 * @param inputListOfNames - A list of names that need to be cleaned
 * 
 * @returns A list of all of the names, now cleaned and ready to be used for
 *          name extrapolation
 */
function cleanNameList(inputListOfNames: string[]): string[]{

    var listOfMatches: string[] = [];
    var listOfNonMatches: string[] = [];
    var indexCount: number = 0;

    // If the list is 2 items long or less, it will be inconclusive since we can't determine
    // which names are going to be the most significant using this method so return an empty
    // list of matches. This also establishes a base case for recursion, which is important
    if (inputListOfNames.length <= 2){
        return [];
    };

    for (const item of inputListOfNames){
        if (indexCount === 0){ // Skip the first name because there isn't anything to compare to yet
            indexCount = indexCount + 1;
            continue;
        } else if (indexCount === 1){ // For the second name, compare it to the first name
            const resultOfComparison = compareTwoNames(inputListOfNames[0], item).match;
            if (resultOfComparison === true){ // If they're a match, start building a list of matches
                listOfMatches.push(inputListOfNames[0]);
                listOfMatches.push(item);
            } else { // If they're not a match, start building a list of non-matches
                listOfNonMatches.push(inputListOfNames[0]);
                listOfMatches.push(item);
            };
            indexCount = indexCount + 1;
        } else { // After the second name we can apply this logic repeatedly
            // If there haven't been any matches, compare to the list of non-matches
            // to see if this name matches any of them
            if (listOfMatches === null || listOfMatches.length === 0){
                var gotAnInitialMatch = false;

                for(const notAMatch of listOfNonMatches){
                    // If we already found a basis from which to create a match list, we don't need to run this anymore
                    if (gotAnInitialMatch === true){
                        break;
                    };

                    const resultOfComparisonWithNonMatch = compareTwoNames(item, notAMatch).match;
                    
                    // If the name matches something in the list of non-matches so far, add them to the
                    // list of matches
                    if (resultOfComparisonWithNonMatch === true){
                        gotAnInitialMatch = true;
                        listOfMatches.push(notAMatch);
                        listOfMatches.push(item);
                        listOfNonMatches = removeItemFromList(listOfNonMatches, notAMatch);
                    };
                };

                // If there are still no more matches, add the name to the list of non-matches since it didn't match anything
                if (gotAnInitialMatch === false){
                    listOfNonMatches.push(item);
                };

            } else { // Otherwise, compare the new name to the list of matches to see if it matches any of the ones there
                var matchesAnotherMatch = false;

                for (const alreadyAMatch of listOfMatches){
                    // If it already matches something, we can just skip the rest of the cycle
                    if (matchesAnotherMatch === true){
                        break;
                    };

                    const resultOfComparisonWithMatch = compareTwoNames(item, alreadyAMatch).match;

                    // If the name matches another match, add it into the list of matches
                    if (resultOfComparisonWithMatch === true){
                        matchesAnotherMatch = true;
                        listOfMatches.push(item);
                    };
                };

                // If the name doesn't match any of the other matches, add it to the list of non-matches
                if (matchesAnotherMatch === false){
                    listOfNonMatches.push(item);
                };
            };
        };
    };

    // Run this function again on the list of non-matches to make sure that there isn't a better list
    // of matches that could be returned
    var checkForBetterMatchList = cleanNameList(listOfNonMatches);

    // If the returned match list has more matches than the initial match list, determine that one
    // is the better match between the two since it matches more things. Return that one instead
    if(checkForBetterMatchList.length > listOfMatches.length){
        listOfMatches = checkForBetterMatchList;
    };

    return listOfMatches;
};

/**
 * Removing an item from a list is fairly intuitive in Python but
 * requires a bit more effort in TypeScript. This function bundles
 * that code into one place for easy reusability. Note that this
 * will only have the right types to work with the items that are
 * inside of this file.
 * 
 * @param listToRemoveFrom - A list of names that contains variations 
 *          of a name for a particular person
 * @param itemToRemove - A dictionary of all of 
 *          the possible name fragment matches and positions that are 
 *          undetermined for a particular name at the time of the start 
 *          of this function
 * 
 * @returns A list of items that is equivalent to the input
 *          listToRemoveFrom, but without itemToRemove inside of it
 */
function removeItemFromList<T>(listToRemoveFrom: T[], itemToRemove: T): T[]{

    const indexOfItemToRemove = listToRemoveFrom.indexOf(itemToRemove);

    listToRemoveFrom.splice(indexOfItemToRemove, 1);

    return listToRemoveFrom;
};

// This interface guarantees that the typing works to prevent errors with typing
// in any section of this code involving a name fragment
interface NameFragment{
    unedited_fragment: string,
    edited_fragment: string,
    length_of_unedited_fragment: number,
    edited_fragment_length: number,
    fragment_frequency: number
}

// This interface guarantees that the typing works to prevent errors with typing
// in any section of this code involving a dictionary for a broken name
interface BrokenNameDictionary{
    complete_name: string,
    complete_name_position_in_list: number,
    total_fragments: number,
    fragment_list: NameFragment[]
}