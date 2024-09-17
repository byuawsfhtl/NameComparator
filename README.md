# Name Comparator

This package is used for fuzzy name comparisons.

## Problem

With most historic records, there is the problem of messy data: nicknames are common, abbreviations are prevalent, mishearings are not rare, and misspellings are everywhere. Because of these and other factors, it is very difficult to automate name comparisons.

## Solution

This package attempts to minimize that difficulty. By tokenizing names into their individual words, names can be compared using simple algorithms. Not only that, but this package cleans common indexing errors, understands most common nicknames, takes into account diverse spelling and pronunciation rules, and more in order to better compare messy name data.

## The Code

```python
from NameComparator import NameComparator

results = NameComparator.compareTwoNames(nameA='Johnny Christians', nameB='Christian, Jean')

print(results)
# ResultsOfNameComparison(nameA='Johnny Christians', nameB='Christian, Jean', 
# tooShort=False, tooGeneric=False, match=True,
# attempt1WordCombo=[('0', '1', 100.0), ('1', '0', 100.0)], attempt1NameA='jean christians', attempt1NameB='christian jean', 
# attempt2WordCombo=None, attempt2NameA=None, attempt2NameB=None,
# attempt3WordCombo=None, attempt3NameA=None, attempt3NameB=None,
# attempt4WordCombo=None, attempt4NameA=None, attempt4NameB=None)
```

The above code snippet shows possible example usage of the package. The results variable is a dictionary with various attributes. The attributes relevant to most users will be ```match```, ```tooGeneric```, and ```tooShort```. 
- ```match``` identifies whether the comparison was a match
- ```tooGeneric``` identifies whether either of the names was too generic (e.g. 'john smith')
- ```tooShort``` identifies whether either name was too short in regards to number of words (e.g. 'justin').

If you are interrested in the debugging portion of the returned namedtuple, each attempt is the use of different methods to identify if the names are a match or not. Two names might fail one or two methods but eventually be proven to be a match. A simple spelling comparison would fail for 'Maurice' and 'Morris'. The first attempt is this simple spelling comparison after minimal cleaning. The second attempt is a heavier edit of the tokens in order to try to get a closer spelling comparison. The third attempt checks if the modified tokens from attempt two are a match according to pronunciation. The fourth and last attempt identifies if the original tokens from the attempt one are a match according to pronunciation comparison. (Attempts 2 through 4 will not be undertaken if the names have no chance at matching.)

Each attempt's word combo is a list of tuples
```python
[('0', '0', 80), ('1', '1', 100), ('3', '2', 100)]
```
Each tuple in the list represents the best pairing of one word in nameA, with another word in nameB. Each tuple has three values: a string of the index number of the word in the first provided name, a string of the index number of the word in the second provided name, and a score of how well they matched (0-100). 
In the above example:
- the 1st word in the nameA matched with the 1st word in the nameB, with a score of 80.
- the 2nd word in the nameA matched with the 2nd word in the nameB, with a score of 100.
- the 4th word in the nameA matched with the 3rd word in the nameB, with a score of 100.

The algorithm finds all possible word pairs and chooses the word pairs that result in the highest overall score for the comparison. ```match``` can be ```True``` even if one of the names is only one word long. It is important to note, though, that the requirements for ```match``` to be evaluated as ```True``` changes depending number of words in the name with the shortest words. For example, if the minimum number of words in each name is three or more, the theshold for a good word pair is lower in order to achieve a match, than if there were only two words in the shortest name. This is because there is a much lower chance of a false negative when more words are present that are decent matches. Initials are also taken into account.

Enjoy!