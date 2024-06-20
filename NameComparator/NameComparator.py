from unidecode import unidecode
from functools import lru_cache
from fuzzywuzzy import fuzz
import re
import itertools
import json
import os

class NameComparator():
    """The class used for fuzzy comparing two names.
    """    
    def __init__(self) -> None:
        """Sets up the necessary attributes needed for most name comparisons.
        """        
        self.namesToIpa:dict = self._getDataFromJson('_ipa_all_names.json')
        self.syllableToIpa:dict = self._getDataFromJson('_ipa_common_word_parts.json')
        self.topSurnames:set = set([str(tup[0]) for tup in self._getDataFromJson('_top_surnames.json')])
        self.ipaRules:list = self._getDataFromJson('_rules_ipa.json')
        replacementRules = {
            "consonant_or_break": ["-", "l", "d", "z", "b", "t", "k", "n", "s", "w", "v", "ð", "ʒ", "ʧ", "θ", "h", "g", "ʤ", "ŋ", "p", "m", "ʃ", "f", "j", "r"],
            "consonant": ["l", "d", "z", "b", "t", "k", "n", "s", "w", "v", "ð", "ʒ", "ʧ", "θ", "h", "g", "ʤ", "ŋ", "p", "m", "ʃ", "f", "j", "r"],
            "vowel": ["ɑ", "a", "æ", "ɪ", "i", "ɛ", "e", "ə", "ɔ", "ʊ", "u", "o"]
        }
        for sublist in self.ipaRules:
            for i, item in enumerate(sublist):
                if not isinstance(item, str):
                    continue
                if item in replacementRules.keys():
                    sublist[i] = replacementRules[item]
        
        self.spellingRules:list = self._getDataFromJson('_rules_spelling.json')
        replacementRules = {
            "consonant": ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"],
            "vowel": ["a", "e", "i", "o", "u", "y"],
            "letter": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
            "letter_or_break": ["-", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        }
        for sublist in self.spellingRules:
            for i, item in enumerate(sublist):
                if not isinstance(item, str):
                    continue
                if item in replacementRules.keys():
                    sublist[i] = replacementRules[item]

        self.nicknameSets = self._getDataFromJson('_nickname_sets.json')
        self.nicknameToNicknameSetNum = {}
        for i, ns in enumerate(self.nicknameSets):
            for name in ns:
                if self.nicknameToNicknameSetNum.get(name):
                    self.nicknameToNicknameSetNum[name].append(i)
                else:
                    self.nicknameToNicknameSetNum[name] = [i]
    
    def _getDataFromJson(self, fileName:str) -> dict|list:
        """Accesses data stored in the specified file.

        Args:
            fileName (str): the specified json file

        Returns:
            dict|list: the json data
        """        
        pathToJsonFolder = os.path.join(os.path.dirname(__file__), 'jsonData')
        path = os.path.join(pathToJsonFolder, fileName)
        with open(path, encoding="utf-8") as file:
            return json.load(file)

    def compareTwoNames(self, name0:str, name1:str) -> dict:
        """Compares two names to identify whether they are a fuzzy match.

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            dict: the data gleaned from the comparison (whether they are a match, whether one or both names is too generic, whether one or both names is too short, along with the debugging attempt data)
        """        
        # Setup
        data = {
            'match': False,
            'tooGeneric': False,
            'tooShort': False,
            'attempt1': None,
            'attempt2': None,
            'attempt3': None,
            'attempt4': None
        }

        # Clean names
        name0 = self._cleanNameByItself(name0)
        name1 = self._cleanNameByItself(name1)
        name0, name1 = self._cleanNamesTogether(name0, name1)

        # Check if either name is too short (one word or less)
        data['tooShort'] = self._eitherNameTooShort(name0, name1)

        # Check if either name is too generic
        data['tooGeneric'] = self._eitherNameTooGeneric(name0, name1)

        # Cleans away nicknames
        name0, name1 = self._removeNicknames(name0, name1)

        # 1st attempt: Checks if names are a match according to string comparison alone
        match, wordCombo = self._spellingComparison(name0, name1)
        data['attempt1'] = (name0, name1, wordCombo)
        if match:
            data['match'] = True
            return data

        # Failed first attempt. Check if names are even worth continuing
        if self._isWorthContinuing(name0, name1) is False:
            return data

        # 2nd attempt: Modify names via spelling rules, then check again if match according to string comparison
        modifiedName0, modifiedName1 = self._modifyNamesTogether(name0, name1)
        match, wordCombo = self._spellingComparison(modifiedName0, modifiedName1)
        data['attempt2'] = (modifiedName0, modifiedName1, wordCombo)
        if match:
            data['match'] = True
            return data
            
        # 3rd attempt: Checks if modified names are a match according to pronunciation
        match, wordCombo, ipaModifiedName0, ipaModifiedName1 = self._pronunciationComparison(modifiedName0, modifiedName1)
        data['attempt3'] = (ipaModifiedName0, ipaModifiedName1, wordCombo)
        if match:
            data['match'] = True
            return data

        # 4th attempt: Check if original names are a match according to pronunciation
        match, wordCombo, ipaName0, ipaName1 = self._pronunciationComparison(name0, name1)
        data['attempt4'] = (ipaName0, ipaName1, wordCombo)
        if match:
            data['match'] = True
            return data

        # If they are still not a match, returns false
        else:
            return data

    def _cleanNameByItself(self, name:str) -> str:
        """Cleans a singular name to get rid of extra or unhelpful data, or to standardize surnames.

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
        return name

    def _cleanNamesTogether(self, name0:str, name1:str) -> tuple[str, str]:
        """Cleans names by comparing them to one another, fixing common errors to standardize.

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            tuple[str, str]: the two cleaned names
        """        
        # Returns if either name is blank
        if (name0 == "" or name1 == ""):
            return name0, name1
        
        # Deal with dashes
        name0, name1 = self._dealWithDashes(name0, name1)
        
        # Deal with Scottish and Irish names
        name0, name1 = self._fixRelatedPrefixes(name0, name1, 'mac', 'mc')
        name0, name1 = self._fixMcMac(name0, name1)

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
            name0, name1 = self._removeIrishO(name0, name1, surname)

        # Deal with prefixes and optional intros that make the match worse
        name0, name1 = self._fixRelatedPrefixes(name0, name1, 'de', 'di')
        name0, name1 = self._fixRelatedPrefixes(name0, name1, 'del', 'dil')
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "d'")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "de")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "fi")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "santa")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "san")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "de la")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "de los")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "del")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "la")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "le")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "du")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "dela")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "los")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "der")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "den")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "vanden")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "vander")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "vande")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "van")
        name0, name1 = self._removeUnnecessaryPrefixes(name0, name1, "von")
        name0, name1 = self._combinePrefixWithSurnameifInBoth(name0, name1, "de")
        name0, name1 = self._combinePrefixWithSurnameifInBoth(name0, name1, "van")

        # Combine words that are one word in the other name
        while True:
            combined, name0, name1 = self._combineSplitWords(name0, name1)
            if not combined:
                break
        while True:
            combined, name1, name0 = self._combineSplitWords(name1, name0)
            if not combined:
                break

        # Remove extra spaces
        name0 = re.sub(r'\s+', ' ', name0)
        name1 = re.sub(r'\s+', ' ', name1)
        name0 = name0.strip()
        name1 = name1.strip()

        # Return the cleaned names
        return name0, name1

    def _dealWithDashes(self, name0:str, name1:str) -> tuple[str, str]:
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
        _, name0Edited, name1Edited = self._combineSplitWords(name0Edited, name1Edited)

        # Return old if the score did not improve
        diff, _, _ = self._calculateEditImprovement(name0, name1, name0Edited, name1Edited)
        if diff <= 0:
            return name0, name1
        
        # Return the edited names
        return name0Edited, name1Edited
    
    def _calculateEditImprovement(self, name0:str, name1:str, name0Edited:str, name1Edited:str) -> tuple[float, tuple, tuple]:
        """Calculates how much editing a name or both names improved the score in comparison to the original names.

        Args:
            name0 (str): the original first name
            name1 (str): the original second name
            name0Edited (str): the edited first name
            name1Edited (str): the edited second name

        Returns:
            tuple[float, tuple, tuple]: the score of how much the edits improved the comparison (can be negative), 
            the word combo of the original, the word combo of the edited verison
        """        
        ogWordCombo = self._findWhichWordsMatchAndHowWell(name0, name1)
        editedWordCombo = self._findWhichWordsMatchAndHowWell(name0Edited, name1Edited)
        ogAverageScore = sum(tup[2] for tup in ogWordCombo) / len(ogWordCombo)
        editedAverageScore = sum(tup[2] for tup in editedWordCombo) / len(editedWordCombo)
        diff = editedAverageScore - ogAverageScore
        return diff, ogWordCombo, editedWordCombo

    def _getPairIndicesAndWords(self, name0:str, name1:str) -> list[tuple[int, int, str, str]]:
        """Identifies which words in the names match.

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            list[tuple[int, int, str, str]]: the list of which words match. Tuples of: the index of word in name0, the index of word in name1, in word in name0, the word in name1
        """        
        combo = self._findWhichWordsMatchAndHowWell(name0, name1)
        words0 = name0.split()
        words1 = name1.split()
        matchIndices = [(int(tup[0]), int(tup[1])) for tup in combo]
        matchIndicesWithWords = [(tup[0], tup[1], words0[tup[0]], words1[tup[1]]) for tup in matchIndices]
        return matchIndicesWithWords

    class NameEditor():
        """ A class used for ease of editing specific words in names. TODO implement more where possible
        """        
        def __init__(self, name0:str, name1:str) -> None:
            """Splits the words for later editing

            Args:
                name0 (str): a name
                name1 (str): a name
            """            
            self.words0 = name0.split()
            self.words1 = name1.split()
        
        def updateName0(self, index:int, updatedWord:str) -> None:
            """Replaces the stored word for name0 at the specified index

            Args:
                index (int): the specified index
                updatedWord (str): the replacement string
            """
            self.words0[index] = updatedWord

        def updateName1(self, index:int, updatedWord:str) -> None:
            """Replaces the stored word for name1 at the specified index

            Args:
                index (int): the specified index
                updatedWord (str): the replacement string
            """
            self.words1[index] = updatedWord

        def getModifiedNames(self) -> tuple[str, str]:
            """Retrieves the modified names

            Returns:
                tuple[str, str]: the modified names
            """            
            return ' '.join(self.words0), ' '.join(self.words1)
    
    def _fixRelatedPrefixes(self, name0:str, name1:str, prefixA:str, prefixB:str) -> tuple[str, str]:
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
    
    def _fixMcMac(self, name0:str, name1:str) -> tuple[str, str]:
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
        _, name0, name1 = self._combineSplitWords(name0, name1)
        
        # Edit the names, if necessary
        ne = self.NameEditor(name0, name1)
        for prefix in ['mc', 'mac']:
            for index0, index1, word0, word1 in self._getPairIndicesAndWords(name0, name1):
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
                    updatedWord0 = word0.replace(prefix, "", 1)
                    updatedWord1 = word1
                else:
                    updatedWord0 = word0
                    updatedWord1 = word1.replace(prefix, "", 1)
                if fuzz.ratio(updatedWord0, updatedWord1) < 75:
                    continue

                # Update the words
                ne.updateName0(index0, updatedWord0)
                ne.updateName1(index1, updatedWord1)

        # Return the edited (or not) names
        return ne.getModifiedNames()

    def _removeIrishO(self, name0:str, name1:str, surname:str) -> tuple[str, str]:
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

    def _removeUnnecessaryPrefixes(self, name0:str, name1:str, prefix:str) -> tuple[str,str]:
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
        name1 = re.sub(r"\s+", " ", name1)
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

        # If no edits were made, try removing spacePrefix if in just one name and it's a long word
        if (name0 == name0Edited) and (name1 == name1Edited):
            pattern = r'\b{}\w*\b'.format(spacePrefix)
            if (spacePrefix in name0) and (spacePrefix not in name1):
                match = re.search(pattern, name0)
                matchedWord = match.group()
                length = len(matchedWord)
                if length > len(prefix) + 4:
                    name0Edited = name0.replace(spacePrefix, " ")
            elif(spacePrefix in name1) and (spacePrefix not in name0):
                match = re.search(pattern, name1)
                matchedWord = match.group()
                length = len(matchedWord)
                if length > len(prefix) + 4:
                    name1Edited = name1.replace(spacePrefix, " ")

        # If the edits were significantly beneficial (or pass spell), return the edited versions
        improvement, _, _= self._calculateEditImprovement(name0, name1, name0Edited, name1Edited)
        if (improvement >= 10) or (self._spellingComparison(name0Edited, name1Edited)[0] and not self._spellingComparison(name0, name1)[0]):
            return name0Edited, name1Edited
        
        # Finally, if the words are identical other than the prefix, remove the prefix
        ne = self.NameEditor(name0, name1)
        for index0, index1, word0, word1 in self._getPairIndicesAndWords(name0, name1):
            if (word0.startswith(prefix)) and (word0[len(prefix):] == word1) and (len(word1) > 2):
                ne.updateName0(index0, word0[len(prefix):])
            elif (word1.startswith(prefix)) and (word1[len(prefix):] == word0) and (len(word0) > 2):
                ne.updateName1(index1, word1[len(prefix):])
        name0, name1 = ne.getModifiedNames()

        # Otherwise, return originals
        return name0, name1

    def _combinePrefixWithSurnameifInBoth(self, name0:str, name1:str, prefix:str) -> tuple[str, str]:
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

    def _combineSplitWords(self, name0:str, name1:str) -> tuple[str, str]:
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
        if self._spellingComparison(name0, name1)[0]:
            return False, name0, name1
        
        for index0, _, word0, word1 in self._getPairIndicesAndWords(name0, name1):
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
            ne = self.NameEditor(name0, name1)
            ne.updateName0(index0, compound)
            ne.updateName0(indexN, '')
            name0Edited, _ = ne.getModifiedNames()

            # If the edited name0 is better (or only slightly worse), go with the edited version
            improvement = self._calculateEditImprovement(name0, name1, name0Edited, name1)[0]
            if improvement > -1:
                return True, name0Edited, name1

        # If no edits were beneficial, just return the original words
        return False, name0, name1

    def _eitherNameTooShort(self, name0:str, name1:str) -> bool:
        """Identifies if either of the names is too short.

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            bool: whether either was too short
        """        
        combo = self._findWhichWordsMatchAndHowWell(name0, name1)
        shortestWordCount = len(combo)
        if shortestWordCount < 2:
            return True
        else:
            return False

    def _findWhichWordsMatchAndHowWell(self, name0:str, name1:str) -> list[tuple[str, str, int]]:
        """Identifies which words in either name are a match, and how well they match.

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            list[tuple[str, str, int]]: a list of tuples idenifying the index of the word in the first name,
              the index of the word in the second name, and the score of how well they match
        """
        # Split strings into lists of words
        words0 = name0.split()
        words1 = name1.split()

        # Initialize empty list to store scores
        scores = []

        # Loops through each word in words1 and compare to each word in words2
        for i, word0 in enumerate(words0):
            for j, word1 in enumerate(words1):
                # Gets the score for how well the words match by using fuzzywuzzy
                rScore = fuzz.ratio(word0, word1)
                prScore = fuzz.partial_ratio(word0, word1)
                score = max(rScore, prScore)
                if word0[0] != word1[0]:
                    score = rScore

                # Unless word1 or word2 is only an initial,
                if (len(word0) == 1) or (len(word1) == 1):
                    # If the initial matches the first letter of the other word, give it a near perfect score
                    if (word0[0] == word1[0]):
                        score = 100
                    # Otherwise the score is 0
                    else:
                        score = 0

                # Add the score to scores
                scores.append((f"{i} words1", f"{j} words2", score))

        # Gets the length of the shortest word
        minLength = min(len(words0), len(words1))

        # Generate all combinations of tuples with length equal to the number of words in string2
        combinations = itertools.combinations(scores, minLength)

        # Filter the combinations to include only valid combinations
        validCombinations = [c for c in combinations if len(set(x[0] for x in c)) == len(c) and len(set(x[1] for x in c)) == len(c)]

        # Cleans the valid combinations
        cleanedValidCombinations = []
        for validCombo in validCombinations:
            cleanedValidCombo = []
            for tup in validCombo:
                cleanedTup = tuple([s.replace(' words1', '').replace(' words2', '') for s in tup[:2]] + [tup[2]])
                cleanedValidCombo.append(cleanedTup)
            cleanedValidCombinations.append(cleanedValidCombo)

        # Find the combination(s) with the maximum sum
        maxSum = sum(y[2] for y in max(cleanedValidCombinations, key=lambda x: sum(y[2] for y in x)))
        maxCombinations = []
        for combo in cleanedValidCombinations:
            if (sum(y[2] for y in combo)) == maxSum:
                maxCombinations.append(combo)

        # Assigns the max score combination with the most letters to be best_combo
        bestCombo = []
        maxLetterCount = 0
        for combo in maxCombinations:
            letterCount = 0
            for tup in combo:
                x, y, _ = map(int, (tup[0], tup[1], tup[2]))
                letterCount += len(words0[x]) + len(words1[y])
            if letterCount > maxLetterCount:
                maxLetterCount = letterCount
                bestCombo = combo

        # Returns the combination of word matches that are the closest match
        return bestCombo

    def _eitherNameTooGeneric(self, name0:str, name1:str) -> bool:
        """Identifies if either name is too generic.

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            bool: whether the name is too generic
        """        
        # Finds the length of the shortest of the two words
        combo = self._findWhichWordsMatchAndHowWell(name0, name1)
        shortestWordCount = len(combo)

        # If both last names are very rare, returns False
        if self._hasRareSurname(name0) and self._hasRareSurname(name1):
            return False

        # Checks if the initials between the two names make a match too uncertain
        words0 = name0.split()
        words2 = name1.split()
        nonInitialMatchCount = 0
        for match in combo:
            index1, index2, _ = match
            word0 = words0[int(index1)]
            word1 = words2[int(index2)]
            initialInWord1 = len(word0) == 1
            initialInWord2 = len(word1) == 1
            if initialInWord1 or initialInWord2:
                nonInitialMatchCount += 1

        if shortestWordCount <= nonInitialMatchCount + 1:
            return True
        else:
            return False

    def _hasRareSurname(self, name:str) -> bool:
        """Identifies if a name has a rare surname.

        Args:
            name (str): a name

        Returns:
            bool: whether the name's surname is rare
        """        
        # Isolates the last name
        name = name.lower()
        surname = name.split()[-1]

        # If the last name is not in the list of surnames, returns true
        if surname not in self.topSurnames:
            return True
        else:
            return False

    def _removeNicknames(self, name0:str, name1:str) -> tuple[str, str]:
        """Replaces the nickname in one name for the official name found in the other.

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            tuple[str, str]: the modified names
        """        
        words0 = name0.split()
        words1 = name1.split()
        for word0 in words0:
            # Skip if the word is also a word in name1
            if word0 in words1:
                continue

            # Skip if the word does not have an nickname
            if self.nicknameToNicknameSetNum.get(word0) is None:
                continue

            # Replace the word with a nickname if the nickname is in name1
            # (and nickname not also in name0)
            setNumbers = self.nicknameToNicknameSetNum[word0]
            breaking = False
            for num in setNumbers:
                nicknames = set(self.nicknameSets[num])
                nicknames.remove(word0)
                for nickname in nicknames:
                    if (nickname in words0) and (nickname in words1):
                        continue
                    if nickname in words1:
                        name0 = re.sub(rf"\b{word0}\b", nickname, name0, flags=re.IGNORECASE)
                        breaking = True
                        break
                if breaking:
                    break

        return name0, name1

    def _spellingComparison(self, name0:str, name1:str) -> tuple[bool, list]:
        """Identifies if two names are a match according to a comparison based soley on spelling.

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            tuple[bool, list]: whether the names are a match, and the resulting word combo
        """        
        # Compares the combination of words that match the best, and to what extent
        wordCombo = self._findWhichWordsMatchAndHowWell(name0, name1)

        # Loops through the tuples and counts the number of times the score is greater than 80
        count = sum(1 for tup in wordCombo if tup[2] > 80)

        # If at least three of the scores are greater than 80, or, 
        # if the number of name matches is the same as the number of words in the shortest name, it's a match
        minLength = min(len(name0.split()), len(name1.split()))
        if (count >= 3) or (count == minLength):
            return True, wordCombo

        # If that didn't work, do a consonant check
        if self._consonantComparison(name0, name1):
            return True, wordCombo

        # If that didn't work, spelling check returns false
        return False, wordCombo

    def _consonantComparison(self, name0:str, name1:str) -> bool:
        """Identifies if two names are a match according to consonant comparison.

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            bool: whether the two names are a match according to consonant comparison
        """        
        # Setup
        wordCombo = self._findWhichWordsMatchAndHowWell(name0, name1)
        minRequiredMatches = len(wordCombo)
        numWordConsonantMatches = 0
        def reduceToSimpleConsonants(string:str) -> str:
            """Reduces a string to the simple consonant componants

            Args:
                string (str): a string

            Returns:
                str: the consonant componants
            """            
            string = re.sub("a|e|i|o|u|y", "*", string)
            string = string.replace("**", "*")
            string = re.sub(r'(.)\1+', r'\1', string)
            return string

        # Loop through every word match in the combo
        for tup in wordCombo:
            # Get the matching word data
            word0:str = name0.split()[int(tup[0])]
            word1:str = name1.split()[int(tup[1])]
            originalScoreForWords:int = int(tup[2])

            # Get the words as consonants
            consonantsName0 = reduceToSimpleConsonants(word0)
            consonantsName1 = reduceToSimpleConsonants(word1)
            consonantsRatio = fuzz.ratio(consonantsName0, consonantsName1)

            # Continue if bad match
            if originalScoreForWords <= 30:
                continue
            if (len(word0) != 1) and (len(word1) != 1): #if neither word is initial
                lowestSyllableCount = min(consonantsName0.count("*"), consonantsName1.count("*"))
                if lowestSyllableCount < 2:
                    continue
            if (consonantsRatio <= 80 or originalScoreForWords <= 60) and consonantsRatio != 100:
                continue

            # If not rejected, increment the number of matches
            numWordConsonantMatches += 1

        # If enough matches, return true. Otherwise return false.
        if (numWordConsonantMatches > minRequiredMatches) or (numWordConsonantMatches >= 3):
            return True
        else:
            return False

    def _isWorthContinuing(self, name0:str, name1:str) -> bool:
        """Identifies if a name comparison will always prove false.

        Args:
            name0 (str): _description_
            name1 (str): _description_

        Returns:
            bool: whether the names are worth working on further
        """        
        wordCombo = self._findWhichWordsMatchAndHowWell(name0, name1)
        oneLetterMatchFailCount = 0

        for match in wordCombo:
            word0 = name0[int(match[0])]
            word1 = name1[int(match[1])]
            score = match[2]
            if (score == 0) and ((len(word0) == 1) or ((len(word1) == 1))):
                oneLetterMatchFailCount += 1

        if (oneLetterMatchFailCount >= 1) and (len(wordCombo) <= 3):
            return False
        else:
            return True

    def _modifyNamesTogether(self, name0:str, name1:str) -> tuple[str,str]:
        """Modifies the name together (changing them in a way that is much more intense than simply cleaning together).

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            tuple[str,str]: the modified names
        """        
        # Replaces 'ie' endings with 'y' endings
        name0 = re.sub(r'ie\b', 'y', name0)
        name1 = re.sub(r'ie\b', 'y', name1)

        # Fix when records are indexed with " or " in the name
        name0, name1 = self._removeOrInNames(name0, name1)

        # Deal with names longer than 5 that are off by one specific char
        name0, name1 = self._fixVowelMistakes(name0, name1)

        # Deal with names longer than 5 that have swapped letters
        name0, name1 = self._fixSwappedChars(name0, name1)

        # Deal with longer names that are identical except for the first char
        name0, name1 = self._dealWithWrongFirstChar(name0, name1)

        # Use spelling rules to modify both
        for rule in self.spellingRules:
            name0, name1 = self._replaceSubstringSandwichMeatIfMatchingBread(name0, name1, rule[0], rule[1], rule[2], rule[3], rule[4])

        # Remove extra spaces
        name0 = re.sub(r'\s+', ' ', name0)
        name1 = re.sub(r'\s+', ' ', name1)
        name0 = name0.strip()
        name1 = name1.strip()

        # Return modified names
        return name0, name1

    def _removeOrInNames(self, name0:str, name1:str) -> tuple[str, str]:
        """Removes the word 'or' from a name (assuming that the name could have been 
        poorly indexed so that the indexer's guesses for a specific word of the name is still within the string).

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            tuple[str, str]: the modified names
        """        
        name0, name1 = name0.lower(), name1.lower()
        # if or in neither
        if (not " or " in name0) and (not " or " in name1):
            return name0, name1
        # if or in both
        elif (" or " in name0) and (" or " in name1):
            return name0, name1
        # if or in 1, not 2
        elif " or " in name0:
            # Gets the score for if the word before 'or' is removed
            name0EditedA = re.sub("[a-z]+ or ", " ", name0)
            wordComboA = self._findWhichWordsMatchAndHowWell(name0EditedA, name1)
            averageScoreA = sum(tup[2] for tup in wordComboA) / len(wordComboA)

            # Gets the score for if the word after 'or' is removed
            name0EditedB = re.sub(" or [a-z]+", " ", name0)
            wordComboB =  self._findWhichWordsMatchAndHowWell(name0EditedB, name1)
            averageScoreB = sum(tup[2] for tup in wordComboB) / len(wordComboB)

            # If the before score is greater, returns A
            if averageScoreA >= averageScoreB:
                return name0EditedA, name1
            # Otherwise returns B
            else:
                return name0EditedB, name1
        # if or in 2, not 1
        elif " or " in name1:
            name1EditedA = re.sub("[a-z]+ or ", " ", name1)
            wordComboA = self._findWhichWordsMatchAndHowWell(name1EditedA, name0)
            averageScoreA = sum(tup[2] for tup in wordComboA) / len(wordComboA)

            # Gets the score for if the word after 'or' is removed
            name1EditedB = re.sub(" or [a-z]+", " ", name1)
            wordComboB =  self._findWhichWordsMatchAndHowWell(name1EditedB, name0)
            averageScoreB = sum(tup[2] for tup in wordComboB) / len(wordComboB)

            # If the before score is greater, returns A
            if averageScoreA >= averageScoreB:
                return name0, name1EditedA
            # Otherwise returns B
            else:
                return name0, name1EditedB

    def _fixVowelMistakes(self, name0:str, name1:str) -> tuple[str, str]:
        """Modifies two matching words in a name so that they are the same if 
        they are only different by one vowel and 5 letters or more.

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            tuple[str, str]: the two modified names
        """        
        ne = self.NameEditor(name0, name1)
        for index0, _, word0, word1 in self._getPairIndicesAndWords(name0, name1):
            # Continue if either word is less than 5 chars
            len0 = len(word0)
            if len0 < 5:
                continue
            len1 = len(word1)
            if len1 < 5:
                continue

            # Continue if they are not the same length
            if len0 != len1:
                continue

            # Check if there is only one difference
            mismatchedIndex = None
            tooManyDiffs = False
            for i in range(len0):
                # Skip matching chars
                if word0[i] == word1[i]:
                    continue

                # Check if there are already too many differences
                if mismatchedIndex:
                    tooManyDiffs = True
                    break

                # Append the index if the chars were not the same
                mismatchedIndex = i
            
            # Continue if there was not exactly one difference
            if (tooManyDiffs) or (mismatchedIndex is None):
                continue

            # Replace one of the letters to be the other if they are cooresponding
            charWord0 = word0[mismatchedIndex]
            charWord1 = word1[mismatchedIndex]
            cooresponding = ['ao', 'ea', 'iy']
            if (f'{charWord0}{charWord1}' in cooresponding) or (f'{charWord1}{charWord0}' in cooresponding):
                ne.updateName0(index0, word1)
        
        # Return the modified (or not) names
        return ne.getModifiedNames()

    def _fixSwappedChars(self, name0:str, name1:str) -> tuple[str, str]:
        """If two matching words (of 5 letters of more) for the two names are the same barring swapped letters (typo), makes the words the same.

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            tuple[str, str]: the modified names
        """        
        ne = self.NameEditor(name0, name1)
        for index0, _, word0, word1 in self._getPairIndicesAndWords(name0, name1):
            # Skip if the words are not 5 long
            if len(word0) != 5:
                continue
            
            # Skip if lengths are different
            if len(word0) != len(word1):
                continue

            # Skip if already a match, or could not be fixed by the swap
            if fuzz.ratio(word1, word0) != 80:
                continue

            # Find how many differences and where
            diffCount = 0
            diffPositions = []
            for i in range(len(word0)):
                if word0[i] != word1[i]:
                    diffCount += 1
                    diffPositions.append(i)
            
            # Skip if there are not two differences
            if diffCount != 2:
                continue

            # Skip if the differences are not sequential
            posI, posJ = diffPositions
            if abs(posI - posJ) != 1:
                continue

            # Skip if the differences are not swappable
            if (word0[posI] != word1[posJ]) or (word0[posI] != word1[posJ]):
                continue

            # Update the word
            ne.updateName0(index0, word1)
        
        # Return the modified (or not) names
        return ne.getModifiedNames()
                    
    def _dealWithWrongFirstChar(self, name0, name1):
        """If two matching words (of 5 letters or more) are the same barring the first letter, makes the same.

        Args:
            name0 (_type_): _description_
            name1 (_type_): _description_

        Returns:
            _type_: _description_
        """        
        ne = self.NameEditor(name0, name1)
        for index1, _, word1, word2 in self._getPairIndicesAndWords(name0, name1):
            if word1 == word2:
                continue
            if (word1[1:] == word2[1:]) and (len(word1) > 4) and (len(word2) > 4):
                ne.updateName0(index1, word2)
        name0, name1 = ne.getModifiedNames()
        return name0, name1

    def _replaceSubstringSandwichMeatIfMatchingBread(self, name0:str, name1:str, meatOption1:str, meatOption2:str, bottomBreadOptions:list[str], topBreadOptions:list[str], minRequiredLetters:int) -> tuple[str,str]:
        """For any given matching word pair, replaces a specific substring in one of the words, with a similar substring found in the other word.

        Args:
            name0 (str): a name
            name1 (str): a name
            meatOption1 (str): the first possible middle of the substring
            meatOption2 (str): the second possible middle of the substring
            bottomBreadOptions (list[str]): a list of possible beginnings to the substring. Whichever beginning is found in the one must be found in the other in order for the replacement to work
            topBreadOptions (list[str]): a list of possible endings to the substring. Whichever ending is found in the one must be found in the other in order for the replacement to work
            minRequiredLetters (int): the minimum required letters to be found in both words in order for the replacement to work

        Returns:
            tuple[str,str]: the modified names
        """        
        # Setup
        def overwriteWithSubstring(string:str, replacement:str, startIndex:int, endIndex:int) -> str:
            """Overwrites a specific index range of a string with the replacement string

            Args:
                string (str): the string to replace
                replacement (str): the replacement string
                startIndex (int): the start index for the replacement
                endIndex (int): the end index for the replacement

            Returns:
                _type_: _description_
            """
            stringList = list(string)
            stringList[startIndex:endIndex] = replacement
            newString = ''.join(stringList)
            return newString

        # Return if both middles not in different words
        if (meatOption1 not in name0 and meatOption2 not in name0) or (meatOption1 not in name1 and meatOption2 not in name1):
            return name0, name1

        # Initialize the name editor
        ne = self.NameEditor(name0, name1)

        # Iterate through the word matches
        for index0, index1, word0, word1 in self._getPairIndicesAndWords(name0, name1):
            # Skip words that are not long enough for the given rule
            if len(word0) < minRequiredLetters or len(word1) < minRequiredLetters:
                continue

            # Add clear word breaks
            word0 = f"-{word0}-"
            word1 = f"-{word1}-"

            # For every bread1
            for bottomBread in bottomBreadOptions:
                # Skip the bread if it doesn't appear in both matching words
                if bottomBread not in word0 or bottomBread not in word1:
                    continue

                # For every bread2
                for topBread in topBreadOptions:
                    # Skip the bread if it doesn't appear in both matching words
                    if topBread not in word0 or topBread not in word1:
                        continue

                    # Skip the bread if the pattern is not found in both
                    pattern = f"{bottomBread}({meatOption1}|{meatOption2}){topBread}"
                    results1 = re.search(pattern, word0)
                    results2 = re.search(pattern, word1)
                    if not results1 or not results2:
                        continue

                    # Skip the bread if the two patterns are identical (middles are the same)
                    if results1.group(0) == results2.group(0):
                        continue

                    # Skip the bread if the two patterns are too far apart
                    spanA1, spanB1 = results1.span()
                    spanA2, spanB2 = results2.span()
                    if not (abs(spanA1 - spanA2) <= 2 and abs(spanB1 - spanB2) <= 2):
                        continue

                    # Update the words by replacing matching (different) middles with the meat option 2
                    startIndexString1, endIndexString1 = results1.span()
                    startIndexString2, endIndexString2 = results2.span()
                    middleCoordsString1 = startIndexString1 + len(bottomBread), endIndexString1 - len(topBread)
                    middleCoordsString2 = startIndexString2 + len(bottomBread), endIndexString2 - len(topBread)
                    word0 = overwriteWithSubstring(word0, meatOption2, middleCoordsString1[0], middleCoordsString1[1])
                    word1 = overwriteWithSubstring(word1, meatOption2, middleCoordsString2[0], middleCoordsString2[1])

            # Update the words for that match (though a change may not have occured)
            word0 = word0.replace("-", "")
            word1 = word1.replace("-", "")
            ne.updateName0(index0, word0)
            ne.updateName1(index1, word1)

        # concatonates the two lists together back into strings
        name0, name1 = ne.getModifiedNames()
        return name0, name1

    def _pronunciationComparison(self, name0:str, name1:str) -> tuple[bool, list, str, str]:
        """Identifies whether two names are a match according to a pronunciation comparison.

        Args:
            name0 (str): a name
            name1 (str): a name

        Returns:
            tuple[bool, list, str, str]: whether the name was a match, the word combo, the ipa of name0, the ipa of name1
        """        
        # Necessary for pronunciation comparison
        wordCombo = self._findWhichWordsMatchAndHowWell(name0, name1)

        # Gets Ipas
        ipaOfName0 = self._getPronunciation(name0)
        ipaOfName1 = self._getPronunciation(name1)

        # Cleans Ipas
        ipaOfName0 = self._cleanIpa(ipaOfName0)
        ipaOfName1 = self._cleanIpa(ipaOfName1)
        ipaOfName0, ipaOfName1 = self._modifyIpasTogether(ipaOfName0, ipaOfName1)

        # Matches the ipa words within the two names
        # Splits strings into lists of words
        ipaWords0 = ipaOfName0.split()
        ipaWords1 = ipaOfName1.split()

        # Initializes an empty list to store scores
        scores = []

        # Loop through each word in words1 and compare to each word in words2
        for i in range(len(ipaWords0)):
            ipaWord0 = ipaWords0[i]
            for j in range(len(ipaWords1)):
                ipaWord1 = ipaWords1[j]

                # Use fuzz.ratio to compare the words and store the score
                score = fuzz.ratio(ipaWord0, ipaWord1)

                # Updates the score if one of the words was an initial
                for k in range(len(wordCombo)):
                    index1, index2, initialScore = wordCombo[k]
                    if i == int(index1) and j == int(index2) and (initialScore == 100 or initialScore == 0):
                        score = initialScore

                # Add the score to scores
                scores.append([f"{i} ipaWords0", f"{j} ipaWords1", score])

        # Gets the length of the shortest word
        minLength = min(len(ipaWords0), len(ipaWords1))

        # Generates all combinations of tuples with length equal to the number of words in string2
        combinations = itertools.combinations(scores, minLength)

        # Filters the combinations to include only valid combinations
        validCombinations = [c for c in combinations if len(set(x[0] for x in c)) == len(c) and len(set(x[1] for x in c)) == len(c)]

        # Finds the word combination with the maximum sum
        maxCombination = max(validCombinations, key=lambda x: sum(y[2] for y in x))

        # Cleans the max combo
        cleanedMaxCombination = []

        # Cleans the max combo
        cleanedMaxCombination = [(
            tup[0].replace(" ipaWords0", "").replace(" ipaWords1", ""),
            tup[1].replace(" ipaWords0", "").replace(" ipaWords1", ""),
            tup[2]) for tup in maxCombination]

        # Gets the smallest score in the max combination
        lowestScore = min(cleanedMaxCombination, key=lambda tuple: tuple[2])[2]

        # If the shortest name is two words in length
        if minLength <= 2:
            # If the lowest score match is greater than or equal to 80, it's a good pronunciation match
            if lowestScore >= 80:
                return True, cleanedMaxCombination, ipaOfName0, ipaOfName1
            # Otherwise, it's probably not a match
            return False, cleanedMaxCombination, ipaOfName0, ipaOfName1

        # If the shortest name is more than two words
        if minLength > 2:
            # If the lowest score match is greater than 75, it's a good pronunciation match
            if lowestScore > 75:
                return True, cleanedMaxCombination, ipaOfName0, ipaOfName1
            # Otherwise, it's probably not a match
            return False, cleanedMaxCombination, ipaOfName0, ipaOfName1

    def _getPronunciation(self, name:str) -> str:
        """Gets the pronunciation of the name.

        Args:
            name (str): a name

        Returns:
            str: the ipa of the name
        """        
        pList = []
        for word in name.split():
            pList.append(self._getIpaOfOneWord(word))
        pronunciationOfName = " ".join(pList)
        return pronunciationOfName

    @lru_cache(maxsize=1000)
    def _getIpaOfOneWord(self, word:str) -> str:
        """Gets the pronunciation of one word.

        Args:
            word (str): a word

        Returns:
            str: the ipa of the word
        """
        # Setup
        word = word.replace(" ", "")
        word = unidecode(word)
        word = word.lower()
        pronunciationList = [""] * len(word)
        def substringSplitsTh(substring:str, word:str, i:int, j:int) -> bool:
            """Helps to identify poor substring choices for words for ipa

            Args:
                substring (str): the ipa dissection
                word (str): the full word
                i (int): the start index of the substring
                j (int): the end index of the substring

            Returns:
                bool: whether it was a good substring
            """            
            if i == j:
                return False
            if i >= 0 and substring[0] == 'h' and word[i - 1] == 't':
                return True
            if j <= len(word) - 1 and substring[-1] == 't' and word[j] == 'h':
                return True
            return False

        # Tries to get the ipa from the plain word
        firstAttempt = self._pronunciationHailMary(word)
        if "*" not in firstAttempt:
            return firstAttempt

        # While there are still letters in the word
        substringAdded = True
        while substringAdded:
            # Initialize variables to store the largest matching substring and its length
            substringAdded = False
            largestSubstring = ""
            pronunciationOfLargestSubstring = ""
            largestSubstringLen = 0
            beginningIndexOfSubstring = 0
            endIndexOfSubstring = 0

            # Iterate over every possible substring
            for i in range(len(word)):
                for j in range(i + 1, len(word) + 1):
                    substring = word[i:j]

                    if len(substring) <= largestSubstringLen:
                        continue
                    if " " in substring:
                        continue
                    if len(substring) > 1:
                        substringIpa = self._convert(substring)
                        if ("*" in substringIpa) or (len(substringIpa) >= len(substring) * 2) or (substringSplitsTh(substring, word, i, j)):
                            continue
                        else:
                            pronunciationOfLargestSubstring = substringIpa
                    elif len(substring) == 1:
                        letterToPronunciation = {
                            "a": "æ", "b": "b", "c": "k", "d": "d", "e": "ɛ", "f": "f", "g": "g", "h": "h", "i": "ɪ",
                            "j": "ʤ", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "k", "r": "r",
                            "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "ks", "y": "j", "z": "z"
                        }
                        pronunciationOfLargestSubstring = letterToPronunciation.get(substring, largestSubstring)

                    largestSubstring = substring
                    substringAdded = True
                    largestSubstringLen = len(substring)
                    beginningIndexOfSubstring = i
                    endIndexOfSubstring = j

            # Adds the substring to the list
            if substringAdded:
                pronunciationList[beginningIndexOfSubstring] = pronunciationOfLargestSubstring
            spaces = " " * largestSubstringLen
            word = word.rstrip()
            word = word[:beginningIndexOfSubstring] + spaces + word[endIndexOfSubstring:]

        # Concatenates the list together at the end to get the pronunciation
        pronunciation = "".join(pronunciationList)
        return pronunciation

    def _pronunciationHailMary(self, word:str) -> str:
        """Tries to get the pronunciation from the predefined ipa dictionary.

        Args:
            word (str): the regular word

        Returns:
            str: the ipa of the word, or just the word with an asterix if no pronunciation found
        """        
        namePronuncation = self.namesToIpa.get(word)
        if namePronuncation != None:
            return namePronuncation
        return word + "*"

    def _convert(self, word:str) -> str:
        """Helper function of _getIpaOfOneWord.
        Gets the ipa of a word (with more than one letter).

        Args:
            word (str): a word (with more than one letter)

        Returns:
            str: the ipa of that word
        """        
        ipaPronunciation = self.syllableToIpa.get(word)
        if ipaPronunciation != None:
            return ipaPronunciation
        return word + "*"

    def _cleanIpa(self, ipa:str) -> str:
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
        return ipa

    def _modifyIpasTogether(self, ipa0:str, ipa1:str) -> tuple[str,str]:
        """Modifies two ipas by comparing each to one another.

        Args:
            ipa1 (str): the first ipa name
            ipa2 (str): the second ipa name

        Returns:
            tuple[str,str]: the two modified names
        """
        for rule in self.ipaRules:
            ipa0, ipa1 = self._replaceSubstringSandwichMeatIfMatchingBread(ipa0, ipa1, rule[0], rule[1], rule[2], rule[3], rule[4])
        return ipa0, ipa1