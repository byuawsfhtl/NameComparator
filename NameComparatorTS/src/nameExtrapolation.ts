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
function extrapolateBestFullName(inputListOfNames: string[], multiplePossibleMatchesDictionary: Record<number, NameFragment> | null, nameFragmentsAndFrequency: NameFragment[] | null): [string, Record<number, Record<string, string | number>>, Record<string, string | number>[]]{
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
            [bestNameAsFragments, multiplePossibleMatchesDictionary] = 
        }
    }
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

function _extrapolateNamesFromEqualLengthFragments(){
    
}

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
function removeItemFromList(listToRemoveFrom: string[], itemToRemove: string): string[]{

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