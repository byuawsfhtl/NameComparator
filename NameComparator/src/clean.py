import re
from unidecode import unidecode
from fuzzywuzzy import fuzz

import NameComparator.src.usefulTools as useful_tools
import NameComparator.src.comparisons as comparisons_mod

def clean_name(name : str) -> str:
    """Cleans a singular name to get rid of extra or unhelpful data, and to standardize surnames.

    Args:
        name: the name being cleaned

    Returns:
        the cleaned-up name
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
    common_abreviations = {
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
    name_as_list = []
    for word in name.split():
        name_as_list.append(common_abreviations.get(word, word))
    name = ' '.join(name_as_list)

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

def clean_names_together(name_a : str, name_b : str) -> tuple[str, str]:
    """Cleans names by comparing them to one another, fixing common errors to standardize.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        the two cleaned names
    """        
    # Return if either name is blank
    if not name_a:
        name_a = '_'
    if not name_b:
        name_b = '_'
    if (name_a == "_") or (name_b == "_"):
        return name_a, name_b
    
    # Deal with dashes
    name_a, name_b = _deal_with_dashes(name_a, name_b)
    
    # Deal with Scottish and Irish names
    name_a, name_b = _fix_related_prefixes(name_a, name_b, 'mac', 'mc')
    name_a, name_b = _fix_mc_mac(name_a, name_b)

    # Deal with just Irish names
    o_names = [
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
    for surname in o_names:
        name_a, name_b = _remove_irish_o(name_a, name_b, surname)

    # Deal with prefixes and optional intros that make the match worse
    name_a, name_b = _fix_related_prefixes(name_a, name_b, 'de', 'di')
    name_a, name_b = _fix_related_prefixes(name_a, name_b, 'del', 'dil')
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "d'")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "de")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "fi")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "santa")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "san")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "de la")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "de los")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "del")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "la")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "le")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "du")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "dela")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "los")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "der")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "den")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "vanden")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "vander")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "vande")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "van")
    name_a, name_b = _remove_unnecessary_prefixes(name_a, name_b, "von")
    name_a, name_b = _combine_prefix_with_surname_if_in_both(name_a, name_b, "de")
    name_a, name_b = _combine_prefix_with_surname_if_in_both(name_a, name_b, "van")

    # Combine words that are one word in the other name
    while True:
        combined, name_a, name_b = _combine_split_words(name_a, name_b)
        if not combined:
            break
    while True:
        combined, name_b, name_a = _combine_split_words(name_b, name_a)
        if not combined:
            break

    # Remove extra spaces
    name_a = re.sub(r'\s+', ' ', name_a)
    name_b = re.sub(r'\s+', ' ', name_b)
    name_a = name_a.strip()
    name_b = name_b.strip()
    if not name_a:
        name_a = '_'
    if not name_b:
        name_b = '_'

    # Return the cleaned names
    return name_a, name_b

def _deal_with_dashes(name_a : str, name_b : str) -> tuple[str, str]:
    """Cleans both names in order to deal with dashes in names.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        the cleaned names
    """        
    # Return originals if no dash in either
    if ('-' not in name_a) and ('-' not in name_b):
        return name_a, name_b

    # Return originals if dash in both
    if ('-' in name_a) and ('-' in name_b):
        return name_a, name_b
    
    # Try replacing the dash with a space, and combine words if necessary
    name_a_edited = name_a.replace('-', ' ')
    name_b_edited = name_b.replace('-', ' ')
    if not name_a_edited:
        name_a_edited = '_'
    if not name_b_edited:
        name_b_edited = '_'
    _, name_a_edited, name_b_edited = _combine_split_words(name_a_edited, name_b_edited)

    # Return originals if the score did not improve
    diff, _, _ = useful_tools.calculate_edit_improvement(name_a, name_b, name_a_edited, name_b_edited)
    if diff <= 0:
        return name_a, name_b
    
    # Return the edited names
    return name_a_edited, name_b_edited

def _combine_split_words(name_a : str, name_b : str) -> tuple[str, str]:
    """Combines words within one of the names if that combination is one word in the other name.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        the modified names
    """        
    words_in_a = name_a.split()

    # Do not combine words that are only two in length
    if len(words_in_a) < 3:
        return False, name_a, name_b
    
    # Do not combine words that are already a good spelling match
    if comparisons_mod.spelling_comparison(name_a, name_b)[0]:
        return False, name_a, name_b
    
    for index_a, _, word_a, word_b in useful_tools.get_pair_indices_and_words(name_a, name_b):
        # Skip if wordA and wordB are not a good match
        if (fuzz.partial_ratio(word_a, word_b) < 75):
            continue

        # Skip if either word is only an initial
        if (len(word_a) == 1) or (len(word_b) == 1):
            continue

        # Find the left and right neighbors
        left_neighbor = words_in_a[index_a - 1] if index_a - 1 >= 0 else ''
        right_neighbor = words_in_a[index_a + 1] if index_a + 1 < len(words_in_a) else ''

        # Skip neighbors if they are initials
        left_neighbor = left_neighbor if len(left_neighbor) > 1 else ''
        right_neighbor = right_neighbor if len(right_neighbor) > 1 else ''
        if (not left_neighbor) and (not right_neighbor):
            return False, name_a, name_b

        # Choose the neighbor that best matches wordA's match
        if not left_neighbor:
            left_was_chosen = False
        elif not right_neighbor:
            left_was_chosen = True
        else:
            score_of_left = fuzz.partial_ratio(left_neighbor, word_b)
            score_of_right = fuzz.partial_ratio(right_neighbor, word_b)
            if score_of_left > score_of_right:
                left_was_chosen = True
            else:
                left_was_chosen = False

        # Initialize the chosen neighbor, compound, and neighbor index
        if left_was_chosen:
            chosen_neighbor = left_neighbor
            compound = f'{left_neighbor}{word_a}'
            index_n = index_a - 1
        else:
            chosen_neighbor = right_neighbor
            compound = f'{word_a}{right_neighbor}'
            index_n = index_a + 1

        # Skip if the neighbor is a bad partial match to wordB's match
        if fuzz.partial_ratio(chosen_neighbor, word_b) < 65:
            continue

        # Check if the compound is significantly better than the original
        og_score = fuzz.ratio(word_a, word_b)
        compound_score = fuzz.ratio(compound, word_b)
        if compound_score < og_score + 20:
            continue
        diff_length_original = abs(len(word_b) - len(word_a))
        diff_length_compound = abs(len(word_b) - len(compound))
        if diff_length_original < diff_length_compound:
            continue

        # If the compound was a better match, use a name editor to create an edited nameA where the words are combined
        ne = useful_tools.NameEditor(name_a, name_b)
        ne.update_name_a(index_a, compound)
        ne.update_name_a(index_n, '')
        name_a_edited, _ = ne.get_modified_names()

        # If the edited nameA is better (or only slightly worse), go with the edited version
        improvement = useful_tools.calculate_edit_improvement(name_a, name_b, name_a_edited, name_b)[0]
        if improvement > -1:
            return True, name_a_edited, name_b

    # If no edits were beneficial, just return the original words
    return False, name_a, name_b

def _fix_related_prefixes(name_a : str, name_b : str, prefix_x : str, prefix_y : str) -> tuple[str, str]:
    """Cleans names to deal with prefixes that are different by spelling, but functionally the same.

    Args:
        name_a: the name of a person
        name_b: the name of a person
        prefix_x: the first related prefix
        prefix_y: the second related prefix

    Returns:
        the two modified names
    """        
    # Return if prefixX in neither or prefixY in neither
    if (f' {prefix_x}' not in name_a) and (f' {prefix_x}' not in name_b):
        return name_a, name_b
    if (f' {prefix_y}' not in name_a) and (f' {prefix_y}' not in name_b):
        return name_a, name_b

    # Return if prefixX or prefixY is found in both
    if (f' {prefix_x}' in name_a) and (f' {prefix_x}' in name_b):
        return name_a, name_b
    if (f' {prefix_y}' in name_a) and (f' {prefix_y}' in name_b):
        return name_a, name_b
    
    # Replace prefixY with prefixX
    if f' {prefix_y}' in name_a:
        name_a = name_a.replace(f' {prefix_y}', f' {prefix_x}')
    else:
        name_b = name_b.replace(f' {prefix_y}', f' {prefix_x}')
    return name_a, name_b

def _fix_mc_mac(name_a : str, name_b : str) -> tuple[str, str]:
    """Modified names to fix problems where mc or mac are in either names and don't match when they should.

    Args:
        name_a: the name of a person
        name_b: the name of a person

    Returns:
        the two modified names 
    """        
    # Return for most names
    if ("mc" not in name_a) and ("mac" not in name_a) and ("mc" not in name_b) and ("mac" not in name_b):
        return name_a, name_b
    
    # Combine split words (if any)
    _, name_a, name_b = _combine_split_words(name_a, name_b)
    
    # Edit the names, if necessary
    ne = useful_tools.NameEditor(name_a, name_b)
    for prefix in ['mc', 'mac']:
        for index_a, index_b, word_a, word_b in useful_tools.get_pair_indices_and_words(name_a, name_b):
            # Skip pair if the prefix is in both words
            if (word_a.startswith(prefix)) and (word_b.startswith(prefix)):
                continue

            # Skip pair if the prefix is not in either of them
            if (not word_a.startswith(prefix)) and (not word_b.startswith(prefix)):
                continue

            # Skip pair if either word is a firstname
            if (index_a < 1) or (index_b < 1):
                continue

            # Skip pair if the shortest word is only 4 long
            if min(len(word_a), len(word_b)) < 3:
                continue

            # Skip pair if they are already a solid match
            if fuzz.ratio(word_a, word_b) > 80:
                continue

            # Skip pair if the prefix is removed and not a good fuzzy match
            if word_a.startswith(prefix):
                updated_word_a = word_a.replace(prefix, '', 1)
                updated_word_b = word_b
            else:
                updated_word_a = word_a
                updated_word_b = word_b.replace(prefix, '', 1)
            if fuzz.ratio(updated_word_a, updated_word_b) < 75:
                continue

            # Update the words
            ne.update_name_a(index_a, updated_word_a)
            ne.update_name_b(index_b, updated_word_b)

    # Return the edited (or not) names
    return ne.get_modified_names()


def _remove_irish_o(name_a : str, name_b : str, surname : str) -> tuple[str, str]:
    """Removes the irish O if needed for easier name comparison.

    Args:
        name_a: the name of a person
        name_b: the name of a person
        surname: one of the irish surnames that often starts with O'

    Returns:
        the modified names
    """        
    # Skip non applicable names
    if (' o ' not in name_a) and (" o" not in name_a) and (" o" not in name_b) and (' o ' not in name_b):
        return name_a, name_b
    if (surname not in name_a) and (surname not in name_b):
        return name_a, name_b
    # Edit the names
    surnameA = name_a.split()[-1]
    if fuzz.ratio(surnameA, surname) > 75:
        if surnameA[0] == 'o':
            name_a = name_a.replace(f'{surnameA}', surname)
        else:
            name_a = name_a.replace(f'o {surnameA}', surname)
    surnameB = name_b.split()[-1]
    if fuzz.ratio(surnameB, surname) > 75:
        if surnameB[0] == 'o':
            name_b = name_b.replace(f'{surnameB}', surname)
        else:
            name_b = name_b.replace(f'o {surnameB}', surname)
    return name_a, name_b


def _remove_unnecessary_prefixes(nameA : str, nameB : str, prefix : str) -> tuple[str,str]:
    """Removes an unnecessary prefix from either or both of the names.

    Args:
        name_a: the name of a person
        name_b: the name of a person
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
    if comparisons_mod.spelling_comparison(nameA, nameB)[0]:
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
    improvement, _, _= useful_tools.calculate_edit_improvement(nameA, nameB, nameAEdited, nameBEdited)
    if (improvement >= 10) or comparisons_mod.spelling_comparison(nameAEdited, nameBEdited)[0]:
        return nameAEdited, nameBEdited
    
    # Finally, if the words are identical other than the prefix, remove the prefix
    ne = useful_tools.NameEditor(nameA, nameB)
    for indexA, indexB, wordA, wordB in useful_tools.get_pair_indices_and_words(nameA, nameB):
        if (wordA.startswith(prefix)) and (wordA[len(prefix):] == wordB) and (len(wordB) > 2):
            ne.update_name_a(indexA, wordA[len(prefix):])
        elif (wordB.startswith(prefix)) and (wordB[len(prefix):] == wordA) and (len(wordA) > 2):
            ne.update_name_b(indexB, wordB[len(prefix):])
    nameA, nameB = ne.get_modified_names()
    return nameA, nameB

def _combine_prefix_with_surname_if_in_both(nameA : str, nameB : str, prefix : str) -> tuple[str, str]:
    """Combines the prefix with the surname in both of the names if the prefix exists in both.

    Args:
        name_a: the name of a person
        name_b: the name of a person
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

def clean_ipa(ipa : str) -> str:
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