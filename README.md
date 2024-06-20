# Name Comparator

This package is used for fuzzy name comparisons.

## Problem

With most historic records, there is the problem of messy data: nicknames are common, abbreviations are prevalent, mishearings are not rare, and misspellings are everywhere. Because of these and other factors, it is very difficult to automate name comparisons.

## Solution

This package attempts to minimize that difficulty. By tokenizing names into their individual words, names can be compared using simple algorithms. Not only that, but this package cleans common indexing errors, understands most common nicknames, takes into account diverse spelling and pronunciation rules, and more in order to better compare messy name data.

## The Code

```python
from NameComparator.NameComparator import NameComparator

nc = NameComparator()
# it is recommended to reuse this object as it is expensive to initialize

results = nc.compareTwoNames('Johnny Christians', 'Christian, Jean')

print(results)
# {'match': True, 'tooGeneric': False, 'tooShort': False, 'attempt1': ('jean christians', 'christian jean', [('0', '1', 100), ('1', '0', 100)]), 'attempt2': None, 'attempt3': None, 'attempt4': None}
```

The above code snippet shows possible example usage of the package. The results variable is a dictionary with various attributes. The keys relevant to most users will be 'match', 'tooGeneric', and 'tooShort'. 'match' identifies whether the comparison was a match, 'tooGeneric' identifies whether either of the names was too generic (e.g. 'john smith'), and 'tooShort' identifies whether either name was too short in regards to number of words (e.g. 'justin').

If you are interrested in the debugging portion of the dictionary, each attempt is the use of different methods to identify if the names are a match or not. Two names might fail one or two methods but eventually be proven to be a match. A simple spelling comparison would fail for 'Maurice' and 'Morris'. The first attempt is simply cleaned up tokens being compared by spelling. The second attempt is a heavier edit of the tokens in order to try to get a cleaner spelling comparison. The third attempt checks if the tokens from attempt one are a match according to pronunciation. The fourth and last attempt identifies if the modified tokens from the second attempt are a match according to pronunciation comparison.

Each attempt's value is a list of tuples
```python
[('0', '0', 80), ('1', '1', 100), ('3', '2', 100)]
```
Each tuple represents the best pairing of one word in the first provided name, with another word in the second provided name. Each tuple has three values: a string of the index number of the word in the first provided name, a string of the index number of the word in the second provided name, and a score of how well they matched (0-100). 
In the above example:
- the 1st word in the 1st provided name matched with the 1st word in the 2nd provided name, with a score of 80.
- the 2nd word in the 1st provided name matched with the 2nd word in the 2nd provided name, with a score of 100.
- the 4th word in the 1st provided name matched with the 3rd word in the 2nd provided name, with a score of 100.

The algorithm finds all possible word pairs and chooses the word pairs that result in the highest overall score for the comparison. Names can be a match even if they are as low as 1 word in length each, but how these lists of tuples are interpreted for the boolean 'match' is very different depending on the minimum number of words in either name. For example, if the minimum number of words in each name is 3 or more, the theshold for scores is lower in order to achieve a match, than if there were only two names. This is because there is a much lower chance of a false negative when more words are present that are decent matches. Initials are also taken into account.

Enjoy!