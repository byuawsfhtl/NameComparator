import re
from unidecode import unidecode
from fuzzywuzzy import fuzz

import NameComparator.src.usefulTools as usefulTools
import NameComparator.src.comparisons as comparisonsMod

def cleanName(name:str) -> str:
    """Cleans a singular name to get rid of extra or unhelpful data, and to standardize surnames.

    Args:
        name (str): the name being cleaned

    Returns:
        str: the cleaned name
    """        
    # Deal with blank names
    if (name == "") or (not isinstance(name, str)):
        return "_"

    # Deal with whitespace
    name = re.sub(r'[^\S ]', ' ', name)
    name = re.sub(r" +", " ", name)
    name = name.strip()

    # Standardize name into ascii
    name = unidecode(name)
    name = name.lower()

    # Deal with blank names again
    if name == "":
        return "_"

    # Remove Punctiation
    name = re.sub(r"[.,?;\"*()]", "", name)

    # Remove spaces after apostrophe
    name = re.sub("' +", "'", name)

    # Remove jr and sr
    name = re.sub(r"\bjr\b", "", name).replace(r"\bjunior\b", "")
    name = re.sub(r"\bsr\b", "", name).replace(r"\bsenior\b", "")

    # Remove titles
    name = re.sub(r"\bprof\b", "", name).replace(r"\bprofessor\b", "")
    name = re.sub(r"\bmr\b", "", name).replace(r"\bmister\b", "")
    name = re.sub(r"\bmrs\b", "", name).replace(r"\bmissus\b", "")
    name = re.sub(r"\bms\b", "", name).replace(r"\bmiss\b", "")
    name = re.sub(r"\bdr\b", "", name).replace(r"\bdoctor\b", "")
    name = re.sub(r"\bstudent\b", "", name)
    name = re.sub(r"\brev\b", "", name)
    name = name.replace("reverend", "")

    # Remove family relations
    name = re.sub(r"\bsister\b", "", name)
    name = re.sub(r"\bbrother\b", "", name)
    name = re.sub(r"\bmother\b", "", name)
    name = re.sub(r"\bfather\b", "", name)
    name = re.sub(r" in law", " ", name)

    # Removes "head of household"
    name = name.replace("head of household", "")

    # Remove Common Abbreviations
    commonAbreviations = {
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
    nameAsList = []
    for word in name.split():
        nameAsList.append(commonAbreviations.get(word, word))
    name = ' '.join(nameAsList)

    # Remove stuff like 'the 3rd'
    name = re.sub(r"[1-9][a-z]2,6", "", name).replace(" the ", "")

    # Remove Roman numerals
    name = ' '.join(re.sub(r'\b(ii|iii|iv)\b', '', word) for word in name.split())
    name = re.sub(r" +", " ", name)
    name = name.strip()

    # Remove 'no suffix'
    name = name.replace("no suffix", "")

    # Deal with Dutch names
    name = re.sub(r"\bvan de", "vande", name)
    name = re.sub(r"\bvan den", "vanden", name)
    name = re.sub(r"\bvan der", "vander", name)
    
    # Deal with whitespace one last time, then return
    name = re.sub(r" +", " ", name)
    name = name.strip()
    if not name:
        name = '_'
    return name

def cleanNamesTogether(nameA:str, nameB:str) -> tuple[str, str]:
    """Cleans names by comparing them to one another, fixing common errors to standardize.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        tuple[str, str]: the two cleaned names
    """        
    # Return if either name is blank
    if not nameA:
        nameA = '_'
    if not nameB:
        nameB = '_'
    if (nameA == "_") or (nameB == "_"):
        return nameA, nameB
    
    # Deal with dashes
    nameA, nameB = _dealWithDashes(nameA, nameB)
    
    # Deal with Scottish and Irish names
    nameA, nameB = _fixRelatedPrefixes(nameA, nameB, 'mac', 'mc')
    nameA, nameB = _fixMcMac(nameA, nameB)

    # Deal with just Irish names
    oNames = [
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
    for surname in oNames:
        nameA, nameB = _removeIrishO(nameA, nameB, surname)

    # Deal with prefixes and optional intros that make the match worse
    nameA, nameB = _fixRelatedPrefixes(nameA, nameB, 'de', 'di')
    nameA, nameB = _fixRelatedPrefixes(nameA, nameB, 'del', 'dil')
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "d'")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "de")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "fi")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "santa")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "san")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "de la")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "de los")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "del")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "la")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "le")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "du")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "dela")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "los")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "der")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "den")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "vanden")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "vander")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "vande")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "van")
    nameA, nameB = _removeUnnecessaryPrefixes(nameA, nameB, "von")
    nameA, nameB = _combinePrefixWithSurnameifInBoth(nameA, nameB, "de")
    nameA, nameB = _combinePrefixWithSurnameifInBoth(nameA, nameB, "van")

    # Combine words that are one word in the other name
    while True:
        combined, nameA, nameB = _combineSplitWords(nameA, nameB)
        if not combined:
            break
    while True:
        combined, nameB, nameA = _combineSplitWords(nameB, nameA)
        if not combined:
            break

    # Remove extra spaces
    nameA = re.sub(r'\s+', ' ', nameA)
    nameB = re.sub(r'\s+', ' ', nameB)
    nameA = nameA.strip()
    nameB = nameB.strip()
    if not nameA:
        nameA = '_'
    if not nameB:
        nameB = '_'

    # Return the cleaned names
    return nameA, nameB

def _dealWithDashes(nameA:str, nameB:str) -> tuple[str, str]:
    """Cleans both names in order to deal with dashes in names.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        tuple[str, str]: the cleaned names
    """        
    # Return old if no dash in either
    if ('-' not in nameA) and ('-' not in nameB):
        return nameA, nameB

    # Return old if dash in both
    if ('-' in nameA) and ('-' in nameB):
        return nameA, nameB
    
    # Try replacing the dash with a space, and combine words if necessary
    nameAEdited = nameA.replace('-', ' ')
    nameBEdited = nameB.replace('-', ' ')
    if not nameAEdited:
        nameAEdited = '_'
    if not nameBEdited:
        nameBEdited = '_'
    _, nameAEdited, nameBEdited = _combineSplitWords(nameAEdited, nameBEdited)

    # Return old if the score did not improve
    diff, _, _ = usefulTools.calculateEditImprovement(nameA, nameB, nameAEdited, nameBEdited)
    if diff <= 0:
        return nameA, nameB
    
    # Return the edited names
    return nameAEdited, nameBEdited

def _combineSplitWords(nameA:str, nameB:str) -> tuple[str, str]:
    """Combines words within one of the names if that combination is one word in the other name.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    wordsInA = nameA.split()

    # Do not combine words that are only two in length
    if len(wordsInA) < 3:
        return False, nameA, nameB
    
    # Do not combine words that are already a good spelling match
    if comparisonsMod.spellingComparison(nameA, nameB)[0]:
        return False, nameA, nameB
    
    for indexA, _, wordA, wordB in usefulTools.getPairIndicesAndWords(nameA, nameB):
        # Skip if wordA and wordB are not a good match
        if (fuzz.partial_ratio(wordA, wordB) < 75):
            continue

        # Skip if either word is only an initial
        if (len(wordA) == 1) or (len(wordB) == 1):
            continue

        # Find the left and right neighbors
        leftNeighbor = wordsInA[indexA - 1] if indexA - 1 >= 0 else ''
        rightNeighbor = wordsInA[indexA + 1] if indexA + 1 < len(wordsInA) else ''

        # Skip neighbors if they are initials
        leftNeighbor = leftNeighbor if len(leftNeighbor) > 1 else ''
        rightNeighbor = rightNeighbor if len(rightNeighbor) > 1 else ''
        if (not leftNeighbor) and (not rightNeighbor):
            return False, nameA, nameB

        # Choose the neighbor that best matches wordA's match
        if not leftNeighbor:
            leftWasChosen = False
        elif not rightNeighbor:
            leftWasChosen = True
        else:
            leftScore = fuzz.partial_ratio(leftNeighbor, wordB)
            rightScore = fuzz.partial_ratio(rightNeighbor, wordB)
            if leftScore > rightScore:
                leftWasChosen = True
            else:
                leftWasChosen = False

        # Initialize the chosen neighbor, compound, and neighbor index
        if leftWasChosen:
            chosenNeighbor = leftNeighbor
            compound = f'{leftNeighbor}{wordA}'
            indexN = indexA - 1
        else:
            chosenNeighbor = rightNeighbor
            compound = f'{wordA}{rightNeighbor}'
            indexN = indexA + 1

        # Skip if the neighbor is a bad partial match to wordB's match
        if fuzz.partial_ratio(chosenNeighbor, wordB) < 65:
            continue

        # Check if the compound is significantly better than the original
        ogScore = fuzz.ratio(wordA, wordB)
        compoundScore = fuzz.ratio(compound, wordB)
        if compoundScore < ogScore + 20:
            continue
        diffLengthOriginal = abs(len(wordB) - len(wordA))
        diffLengthCompound = abs(len(wordB) - len(compound))
        if diffLengthOriginal < diffLengthCompound:
            continue

        # If the compound was a better match, use a name editor to create an edited nameA where the words are combined
        ne = usefulTools.NameEditor(nameA, nameB)
        ne.updateNameA(indexA, compound)
        ne.updateNameA(indexN, '')
        nameAEdited, _ = ne.getModifiedNames()

        # If the edited nameA is better (or only slightly worse), go with the edited version
        improvement = usefulTools.calculateEditImprovement(nameA, nameB, nameAEdited, nameB)[0]
        if improvement > -1:
            return True, nameAEdited, nameB

    # If no edits were beneficial, just return the original words
    return False, nameA, nameB

def _fixRelatedPrefixes(nameA:str, nameB:str, prefixX:str, prefixY:str) -> tuple[str, str]:
    """Cleans names to deal with prefixes that are different by spelling, but functionally the same.

    Args:
        nameA (str): a name
        nameB (str): a name
        prefixX (str): the first related prefix
        prefixY (str): the second related prefix

    Returns:
        tuple[str, str]: the two modified names
    """        
    # Return if prefixX in neither or prefixY in neither
    if (f' {prefixX}' not in nameA) and (f' {prefixX}' not in nameB):
        return nameA, nameB
    if (f' {prefixY}' not in nameA) and (f' {prefixY}' not in nameB):
        return nameA, nameB

    # Return if prefixX or prefixY is found in both
    if (f' {prefixX}' in nameA) and (f' {prefixX}' in nameB):
        return nameA, nameB
    if (f' {prefixY}' in nameA) and (f' {prefixY}' in nameB):
        return nameA, nameB
    
    # Replace prefixY with prefixX
    if f' {prefixY}' in nameA:
        nameA = nameA.replace(f' {prefixY}', f' {prefixX}')
    else:
        nameB = nameB.replace(f' {prefixY}', f' {prefixX}')
    return nameA, nameB

def _fixMcMac(nameA:str, nameB:str) -> tuple[str, str]:
    """Modified names to fix problems where mc or mac are in either names and don't match when they should.

    Args:
        nameA (str): a name
        nameB (str): a name

    Returns:
        tuple[str, str]: the two modified names 
    """        
    # Return for most names
    if ("mc" not in nameA) and ("mac" not in nameA) and ("mc" not in nameB) and ("mac" not in nameB):
        return nameA, nameB
    
    # Combine split words (if any)
    _, nameA, nameB = _combineSplitWords(nameA, nameB)
    
    # Edit the names, if necessary
    ne = usefulTools.NameEditor(nameA, nameB)
    for prefix in ['mc', 'mac']:
        for indexA, indexB, wordA, wordB in usefulTools.getPairIndicesAndWords(nameA, nameB):
            # Skip pair if the prefix is in both words
            if (wordA.startswith(prefix)) and (wordB.startswith(prefix)):
                continue

            # Skip pair if the prefix is not in either of them
            if (not wordA.startswith(prefix)) and (not wordB.startswith(prefix)):
                continue

            # Skip pair if either word is a firstname
            if (indexA < 1) or (indexB < 1):
                continue

            # Skip pair if the shortest word is only 4 long
            if min(len(wordA), len(wordB)) < 3:
                continue

            # Skip pair if they are already a solid match
            if fuzz.ratio(wordA, wordB) > 80:
                continue

            # Skip pair if the prefix is removed and not a good fuzzy match
            if wordA.startswith(prefix):
                updatedWordA = wordA.replace(prefix, '', 1)
                updatedWordB = wordB
            else:
                updatedWordA = wordA
                updatedWordB = wordB.replace(prefix, '', 1)
            if fuzz.ratio(updatedWordA, updatedWordB) < 75:
                continue

            # Update the words
            ne.updateNameA(indexA, updatedWordA)
            ne.updateNameB(indexB, updatedWordB)

    # Return the edited (or not) names
    return ne.getModifiedNames()


def _removeIrishO(nameA:str, nameB:str, surname:str) -> tuple[str, str]:
    """Removes the irish O if needed for easier name comparison.

    Args:
        nameA (str): a name
        nameB (str): a name
        surname (str): one of the irish surnames that often starts with O'

    Returns:
        tuple[str, str]: the modified names
    """        
    # Skip non applicable names
    if (' o ' not in nameA) and (" o" not in nameA) and (" o" not in nameB) and (' o ' not in nameB):
        return nameA, nameB
    if (surname not in nameA) and (surname not in nameB):
        return nameA, nameB
    # Edit the names
    surnameA = nameA.split()[-1]
    if fuzz.ratio(surnameA, surname) > 75:
        if surnameA[0] == 'o':
            nameA = nameA.replace(f'{surnameA}', surname)
        else:
            nameA = nameA.replace(f'o {surnameA}', surname)
    surnameB = nameB.split()[-1]
    if fuzz.ratio(surnameB, surname) > 75:
        if surnameB[0] == 'o':
            nameB = nameB.replace(f'{surnameB}', surname)
        else:
            nameB = nameB.replace(f'o {surnameB}', surname)
    return nameA, nameB


def _removeUnnecessaryPrefixes(nameA:str, nameB:str, prefix:str) -> tuple[str,str]:
    """Removes an unnecessary prefix from either or both of the names.

    Args:
        nameA (str): a name
        nameB (str): a name
        prefix (str): the prefix to (probably) remove

    Returns:
        tuple[str,str]: the modified names
    """        
    # If the prefix is not in either names, return the names
    nameA = re.sub(r"\s+", " ", nameA)
    nameA = nameA.strip()
    nameB = re.sub(r"\s+", " ", nameB)
    nameB = nameB.strip()
    if (f" {prefix}" not in nameA) and (f" {prefix}" not in nameB):
        return nameA, nameB
    
    # If the names are already a good match, return the names
    if comparisonsMod.spellingComparison(nameA, nameB)[0]:
        return nameA, nameB

    # Setup
    nameAEdited = nameA
    nameBEdited = nameB
    spPrefixSp = f" {prefix} "
    spacePrefix = f" {prefix}"

    # Make the edited names different
    if (spPrefixSp in nameA) and (spPrefixSp in nameB):
        pass
    elif (spPrefixSp in nameA) and (spacePrefix in nameB):
        nameAEdited = nameAEdited.replace(spPrefixSp, spacePrefix)
    elif (spacePrefix in nameA) and (spPrefixSp in nameB):
        nameBEdited = nameBEdited.replace(spPrefixSp, spacePrefix)
    nameAEdited = nameAEdited.replace(spPrefixSp, " ")
    nameBEdited = nameBEdited.replace(spPrefixSp, " ")
    nameAEdited = re.sub(r"\s+", " ", nameAEdited)
    nameBEdited = re.sub(r"\s+", " ", nameBEdited)

    # If no edits were made, try removing spacePrefix if only in nameA and it's a long word
    pattern = r'\b{}\w*\b'.format(spacePrefix)
    noEditsMade = (nameA == nameAEdited) and (nameB == nameBEdited) 
    spPreOnlyInNameA = (spacePrefix in nameA) and (spacePrefix not in nameB) 
    matchOfA = re.search(pattern, nameA)
    if (noEditsMade) and (spPreOnlyInNameA) and (matchOfA is not None):
        matchedWord = matchOfA.group()
        if len(matchedWord) > len(prefix) + 4:
            nameAEdited = nameA.replace(spacePrefix, " ")

    # If no edits were made, try removing spacePrefix if only in nameB and it's a long word
    pattern = r'\b{}\w*\b'.format(spacePrefix)
    noEditsMade = (nameA == nameAEdited) and (nameB == nameBEdited) 
    spPreOnlyInNameB = (spacePrefix in nameB) and (spacePrefix not in nameA)
    matchOfB = re.search(pattern, nameB)
    if (noEditsMade) and (spPreOnlyInNameB) and (matchOfB is not None):
        matchedWord = matchOfB.group()
        if len(matchedWord) > len(prefix) + 4:
            nameBEdited = nameB.replace(spacePrefix, " ")

    # Safety
    if not nameAEdited:
        nameAEdited = '_'
    if not nameBEdited:
        nameBEdited = '_'

    # If the edits were significantly beneficial (or pass spell), return the edited versions
    improvement, _, _= usefulTools.calculateEditImprovement(nameA, nameB, nameAEdited, nameBEdited)
    if (improvement >= 10) or comparisonsMod.spellingComparison(nameAEdited, nameBEdited)[0]:
        return nameAEdited, nameBEdited
    
    # Finally, if the words are identical other than the prefix, remove the prefix
    ne = usefulTools.NameEditor(nameA, nameB)
    for indexA, indexB, wordA, wordB in usefulTools.getPairIndicesAndWords(nameA, nameB):
        if (wordA.startswith(prefix)) and (wordA[len(prefix):] == wordB) and (len(wordB) > 2):
            ne.updateNameA(indexA, wordA[len(prefix):])
        elif (wordB.startswith(prefix)) and (wordB[len(prefix):] == wordA) and (len(wordA) > 2):
            ne.updateNameB(indexB, wordB[len(prefix):])
    nameA, nameB = ne.getModifiedNames()
    return nameA, nameB

def _combinePrefixWithSurnameifInBoth(nameA:str, nameB:str, prefix:str) -> tuple[str, str]:
    """Combines the prefix with the surname in both of the names if the prefix exists in both.

    Args:
        nameA (str): a name
        nameB (str): a name
        prefix (str): the prefix to combine with the surname

    Returns:
        tuple[str, str]: the modified names
    """        
    # Return if ' prefix ' in neither
    if (not re.search(f' {prefix} .', nameA)) or (not re.search(f' {prefix} .', nameB)):
        return nameA, nameB
    
    # Get the letter after ' prefix '
    letterA = nameA[nameA.index(f' {prefix} ') + 4]
    letterB = nameB[nameB.index(f' {prefix} ') + 4]

    # If the letter after matches, replace ' prefix ' with ' prefix'
    if letterA == letterB:
        nameA = nameA.replace(f' {prefix} ', f' {prefix}')
        nameB = nameB.replace(f' {prefix} ', f' {prefix}')
    return nameA, nameB

def cleanIpa(ipa:str) -> str:
    """cleans ipa to get rid of double ipa-consonants and other mistakes.

    Args:
        ipa (str): the ipa of a word

    Returns:
        str: the cleaned ipa
    """        
    allIpaConsonants = ['l', 'd', 'z', 'b', 't', 'k', 'n', 's', 'w', 'v', 'ð', 'ʒ', 'ʧ', 'θ', 'h', 'g', 'ʤ', 'ŋ', 'p', 'm', 'ʃ', 'f', 'j', 'r']
    for consonant in allIpaConsonants:
        doubleConsonant = consonant + consonant
        if doubleConsonant in ipa:
            ipa = ipa.replace(doubleConsonant, consonant)
    ipa = ipa.replace("ɛɛ", "i")
    ipa = ipa.replace("ɪɪ", "ɪ")
    ipa = ipa.replace("iɪ", "i")
    ipa = ipa.replace("ŋg", "ŋ")
    ipa = ipa.replace(",", "")
    if not ipa:
        ipa = '_'
    return ipa