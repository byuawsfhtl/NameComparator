import re
from unidecode import unidecode
from fuzzywuzzy import fuzz

from NameComparator.dataProcessors.usefulTools import NameEditor, calculateEditImprovement, getPairIndicesAndWords
from NameComparator.dataProcessors.comparisons import spellingComparison

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

    # Remove more than one space again
    name = re.sub(r" +", " ", name)

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

def cleanNamesTogether(name0:str, name1:str) -> tuple[str, str]:
    """Cleans names by comparing them to one another, fixing common errors to standardize.

    Args:
        name0 (str): a name
        name1 (str): a name

    Returns:
        tuple[str, str]: the two cleaned names
    """        
    # Return if either name is blank
    if not name0:
        name0 = '_'
    if not name1:
        name1 = '_'
    if (name0 == "_") or (name1 == "_"):
        return name0, name1
    
    # Deal with dashes
    name0, name1 = _dealWithDashes(name0, name1)
    
    # Deal with Scottish and Irish names
    name0, name1 = _fixRelatedPrefixes(name0, name1, 'mac', 'mc')
    name0, name1 = _fixMcMac(name0, name1)

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
        name0, name1 = _removeIrishO(name0, name1, surname)

    # Deal with prefixes and optional intros that make the match worse
    name0, name1 = _fixRelatedPrefixes(name0, name1, 'de', 'di')
    name0, name1 = _fixRelatedPrefixes(name0, name1, 'del', 'dil')
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "d'")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "de")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "fi")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "santa")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "san")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "de la")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "de los")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "del")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "la")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "le")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "du")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "dela")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "los")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "der")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "den")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "vanden")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "vander")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "vande")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "van")
    name0, name1 = _removeUnnecessaryPrefixes(name0, name1, "von")
    name0, name1 = _combinePrefixWithSurnameifInBoth(name0, name1, "de")
    name0, name1 = _combinePrefixWithSurnameifInBoth(name0, name1, "van")

    # Combine words that are one word in the other name
    while True:
        combined, name0, name1 = _combineSplitWords(name0, name1)
        if not combined:
            break
    while True:
        combined, name1, name0 = _combineSplitWords(name1, name0)
        if not combined:
            break

    # Remove extra spaces
    name0 = re.sub(r'\s+', ' ', name0)
    name1 = re.sub(r'\s+', ' ', name1)
    name0 = name0.strip()
    name1 = name1.strip()
    if not name0:
        name0 = '_'
    if not name1:
        name1 = '_'

    # Return the cleaned names
    return name0, name1

def _dealWithDashes(name0:str, name1:str) -> tuple[str, str]:
    """Cleans both names in order to deal with dashes in names.

    Args:
        name0 (str): a name
        name1 (str): a name

    Returns:
        tuple[str, str]: the cleaned names
    """        
    # Return old if no dash in either
    if ('-' not in name0) and ('-' not in name1):
        return name0, name1

    # Return old if dash in both
    if ('-' in name0) and ('-' in name1):
        return name0, name1
    
    # Try replacing the dash with a space, and combine words if necessary
    name0Edited = name0.replace('-', ' ')
    name1Edited = name1.replace('-', ' ')
    if not name0Edited:
        name0Edited = '_'
    if not name1Edited:
        name1Edited = '_'
    _, name0Edited, name1Edited = _combineSplitWords(name0Edited, name1Edited)

    # Return old if the score did not improve
    diff, _, _ = calculateEditImprovement(name0, name1, name0Edited, name1Edited)
    if diff <= 0:
        return name0, name1
    
    # Return the edited names
    return name0Edited, name1Edited

def _combineSplitWords(name0:str, name1:str) -> tuple[str, str]:
    """Combines words within one of the names if that combination is one word in the other name.

    Args:
        name0 (str): a name
        name1 (str): a name

    Returns:
        tuple[str, str]: the modified names
    """        
    words0 = name0.split()

    # Do not combine words that are only two in length
    if len(words0) < 3:
        return False, name0, name1
    
    # Do not combine words that are already a good spelling match
    if spellingComparison(name0, name1)[0]:
        return False, name0, name1
    
    for index0, _, word0, word1 in getPairIndicesAndWords(name0, name1):
        # Skip if word0 and word1 are not a good match
        if (fuzz.partial_ratio(word0, word1) < 75):
            continue

        # Skip if either word is only an initial
        if (len(word0) == 1) or (len(word1) == 1):
            continue

        # Find the left and right neighbors
        leftNeighbor = words0[index0 - 1] if index0 - 1 >= 0 else ''
        rightNeighbor = words0[index0 + 1] if index0 + 1 < len(words0) else ''

        # Skip neighbors if they are initials
        leftNeighbor = leftNeighbor if len(leftNeighbor) > 1 else ''
        rightNeighbor = rightNeighbor if len(rightNeighbor) > 1 else ''
        if (not leftNeighbor) and (not rightNeighbor):
            return False, name0, name1

        # Choose the neighbor that best matches word0's match (word1)
        if not leftNeighbor:
            leftWasChosen = False
        elif not rightNeighbor:
            leftWasChosen = True
        else:
            leftScore = fuzz.partial_ratio(leftNeighbor, word1)
            rightScore = fuzz.partial_ratio(rightNeighbor, word1)
            if leftScore > rightScore:
                leftWasChosen = True
            else:
                leftWasChosen = False

        # Initialize the chosen neighbor, compound, and neighbor index
        if leftWasChosen:
            chosenNeighbor = leftNeighbor
            compound = f'{leftNeighbor}{word0}'
            indexN = index0 - 1
        else:
            chosenNeighbor = rightNeighbor
            compound = f'{word0}{rightNeighbor}'
            indexN = index0 + 1

        # Skip if the neighbor is a bad partial match to word0's match
        if fuzz.partial_ratio(chosenNeighbor, word1) < 65:
            continue

        # Check if the compound is significantly better than the original
        ogScore = fuzz.ratio(word0, word1)
        compoundScore = fuzz.ratio(compound, word1)
        if compoundScore < ogScore + 20:
            continue
        diffLength0 = abs(len(word1) - len(word0))
        diffLengthCompound = abs(len(word1) - len(compound))
        if diffLength0 < diffLengthCompound:
            continue

        # If the compound was a better match, use a name editor to create an edited name0 where the words are combined
        ne = NameEditor(name0, name1)
        ne.updateName0(index0, compound)
        ne.updateName0(indexN, '')
        name0Edited, _ = ne.getModifiedNames()

        # If the edited name0 is better (or only slightly worse), go with the edited version
        improvement = calculateEditImprovement(name0, name1, name0Edited, name1)[0]
        if improvement > -1:
            return True, name0Edited, name1

    # If no edits were beneficial, just return the original words
    return False, name0, name1

def _fixRelatedPrefixes(name0:str, name1:str, prefixA:str, prefixB:str) -> tuple[str, str]:
    """Cleans names to deal with prefixes that are different by spelling, but functionally the same.

    Args:
        name0 (str): a name
        name1 (str): a name
        prefixA (str): the first related prefix
        prefixB (str): the second related prefix

    Returns:
        tuple[str, str]: the two modified names
    """        
    # Return if prefix1 in neither or prefix2 in neither
    if (f' {prefixA}' not in name0) and (f' {prefixA}' not in name1):
        return name0, name1
    if (f' {prefixB}' not in name0) and (f' {prefixB}' not in name1):
        return name0, name1

    # Return if prefix1 or prefix2 is found in both
    if (f' {prefixA}' in name0) and (f' {prefixA}' in name1):
        return name0, name1
    if (f' {prefixB}' in name0) and (f' {prefixB}' in name1):
        return name0, name1
    
    # Replace prefix2 with prefix1
    if f' {prefixB}' in name0:
        name0 = name0.replace(f' {prefixB}', f' {prefixA}')
    else:
        name1 = name1.replace(f' {prefixB}', f' {prefixA}')
    return name0, name1

def _fixMcMac(name0:str, name1:str) -> tuple[str, str]:
    """Modified names to fix problems where mc or mac are in either names and don't match when they should.

    Args:
        name0 (str): a name
        name1 (str): a name

    Returns:
        tuple[str, str]: the two modified names 
    """        
    # Return for most names
    if ("mc" not in name0) and ("mac" not in name0) and ("mc" not in name1) and ("mac" not in name1):
        return name0, name1
    
    # Combine split words (if any)
    _, name0, name1 = _combineSplitWords(name0, name1)
    
    # Edit the names, if necessary
    ne = NameEditor(name0, name1)
    for prefix in ['mc', 'mac']:
        for index0, index1, word0, word1 in getPairIndicesAndWords(name0, name1):
            # Skip pair if the prefix is in both words
            if (word0.startswith(prefix)) and (word1.startswith(prefix)):
                continue

            # Skip pair if the prefix is not in either of them
            if (not word0.startswith(prefix)) and (not word1.startswith(prefix)):
                continue

            # Skip pair if either word is a firstname
            if (index0 < 1) or (index1 < 1):
                continue

            # Skip pair if the shortest word is only 4 long
            if min(len(word0), len(word1)) < 3:
                continue

            # Skip pair if they are already a solid match
            if fuzz.ratio(word0, word1) > 80:
                continue

            # Skip pair if the prefix is removed and not a good fuzzy match
            if word0.startswith(prefix):
                updatedWord0 = word0.replace(prefix, '', 1)
                updatedWord1 = word1
            else:
                updatedWord0 = word0
                updatedWord1 = word1.replace(prefix, '', 1)
            if fuzz.ratio(updatedWord0, updatedWord1) < 75:
                continue

            # Update the words
            ne.updateName0(index0, updatedWord0)
            ne.updateName1(index1, updatedWord1)

    # Return the edited (or not) names
    return ne.getModifiedNames()


def _removeIrishO(name0:str, name1:str, surname:str) -> tuple[str, str]:
    """Removes the irish O if needed for easier name comparison.

    Args:
        name0 (str): a name
        name1 (str): a name
        surname (str): one of the irish surnames that often starts with O'

    Returns:
        tuple[str, str]: the modified names
    """        
    # Skip non applicable names
    if (' o ' not in name0) and (" o" not in name0) and (" o" not in name1) and (' o ' not in name1):
        return name0, name1
    if (surname not in name0) and (surname not in name1):
        return name0, name1
    # Edit the names
    lastname0 = name0.split()[-1]
    if fuzz.ratio(lastname0, surname) > 75:
        if lastname0[0] == 'o':
            name0 = name0.replace(f'{lastname0}', surname)
        else:
            name0 = name0.replace(f'o {lastname0}', surname)
    lastname1 = name1.split()[-1]
    if fuzz.ratio(lastname1, surname) > 75:
        if lastname1[0] == 'o':
            name1 = name1.replace(f'{lastname1}', surname)
        else:
            name1 = name1.replace(f'o {lastname1}', surname)
    return name0, name1


def _removeUnnecessaryPrefixes(name0:str, name1:str, prefix:str) -> tuple[str,str]:
    """Removes an unnecessary prefix from either or both of the names.

    Args:
        name0 (str): a name
        name1 (str): a name
        prefix (str): the prefix to (probably) remove

    Returns:
        tuple[str,str]: the modified names
    """        
    # If the prefix is not in either names, return the names
    name0 = re.sub(r"\s+", " ", name0)
    name0 = name0.strip()
    name1 = re.sub(r"\s+", " ", name1)
    name1 = name1.strip()
    if (f" {prefix}" not in name0) and (f" {prefix}" not in name1):
        return name0, name1

    # Setup
    name0Edited = name0
    name1Edited = name1
    spPrefixSp = f" {prefix} "
    spacePrefix = f" {prefix}"

    # Make the edited names different
    if (spPrefixSp in name0) and (spPrefixSp in name1):
        pass
    elif (spPrefixSp in name0) and (spacePrefix in name1):
        name0Edited = name0Edited.replace(spPrefixSp, spacePrefix)
    elif (spacePrefix in name0) and (spPrefixSp in name1):
        name1Edited = name1Edited.replace(spPrefixSp, spacePrefix)
    name0Edited = name0Edited.replace(spPrefixSp, " ")
    name1Edited = name1Edited.replace(spPrefixSp, " ")
    name0Edited = re.sub(r"\s+", " ", name0Edited)
    name1Edited = re.sub(r"\s+", " ", name1Edited)

    # If no edits were made, try removing spacePrefix if only in name0 and it's a long word
    pattern = r'\b{}\w*\b'.format(spacePrefix)
    noEditsMade = (name0 == name0Edited) and (name1 == name1Edited) 
    spPreOnlyInName0 = (spacePrefix in name0) and (spacePrefix not in name1) 
    matchOf0 = re.search(pattern, name0)
    if (noEditsMade) and (spPreOnlyInName0) and (matchOf0 is not None):
        matchedWord = matchOf0.group()
        if len(matchedWord) > len(prefix) + 4:
            name0Edited = name0.replace(spacePrefix, " ")

    # If no edits were made, try removing spacePrefix if only in name1 and it's a long word
    pattern = r'\b{}\w*\b'.format(spacePrefix)
    noEditsMade = (name0 == name0Edited) and (name1 == name1Edited) 
    spPreOnlyInName1 = (spacePrefix in name1) and (spacePrefix not in name0)
    matchOf1 = re.search(pattern, name1)
    if (noEditsMade) and (spPreOnlyInName1) and (matchOf1 is not None):
        matchedWord = matchOf1.group()
        if len(matchedWord) > len(prefix) + 4:
            name1Edited = name1.replace(spacePrefix, " ")

    # Safety
    if not name0Edited:
        name0Edited = '_'
    if not name1Edited:
        name1Edited = '_'

    # If the edits were significantly beneficial (or pass spell), return the edited versions
    improvement, _, _= calculateEditImprovement(name0, name1, name0Edited, name1Edited)
    if (improvement >= 10) or (spellingComparison(name0Edited, name1Edited)[0] and not spellingComparison(name0, name1)[0]):
        return name0Edited, name1Edited
    
    # Finally, if the words are identical other than the prefix, remove the prefix
    ne = NameEditor(name0, name1)
    for index0, index1, word0, word1 in getPairIndicesAndWords(name0, name1):
        if (word0.startswith(prefix)) and (word0[len(prefix):] == word1) and (len(word1) > 2):
            ne.updateName0(index0, word0[len(prefix):])
        elif (word1.startswith(prefix)) and (word1[len(prefix):] == word0) and (len(word0) > 2):
            ne.updateName1(index1, word1[len(prefix):])
    name0, name1 = ne.getModifiedNames()

    # Whatever happened, just return
    return name0, name1

def _combinePrefixWithSurnameifInBoth(name0:str, name1:str, prefix:str) -> tuple[str, str]:
    """Combines the prefix with the surname in both of the names if the prefix exists in both.

    Args:
        name0 (str): a name
        name1 (str): a name
        prefix (str): the prefix to combine with the surname

    Returns:
        tuple[str, str]: the modified names
    """        
    # Return if ' prefix ' in neither
    if (not re.search(f' {prefix} .', name0)) or (not re.search(f' {prefix} .', name1)):
        return name0, name1
    
    # Get the letter after ' prefix '
    letter0 = name0[name0.index(f' {prefix} ') + 4]
    letter1 = name1[name1.index(f' {prefix} ') + 4]

    # If the letter after matches, replace ' prefix ' with ' prefix'
    if letter0 == letter1:
        name0 = name0.replace(f' {prefix} ', f' {prefix}')
        name1 = name1.replace(f' {prefix} ', f' {prefix}')
    return name0, name1