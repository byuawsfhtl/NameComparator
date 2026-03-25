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
# ResultsOfNameComparison(
#     nameA='Johnny Christians',
#     nameB='Christian, Jean',
#     match=True,
#     uniqueness=100,
#     tooShort=False,
#     attempt1=Attempt(nameA='jean christians', nameB='christian jean', wordCombo=[('0', '1', 100.0), ('1', '0', 100.0)]),
#     attempt2=None,
#     attempt3=None,
#     attempt4=None
# )
```

The above code snippet shows possible example usage of the package. The results variable is a dictionary with various attributes. The attributes relevant to most users will be ```match```, ```tooGeneric```, and ```tooShort```. 
- ```match``` identifies whether the comparison was a match
- ```uniqueness``` gives a score out of 100 to the uniqueness of the two names compared to one another. (e.g. 'john smith' compared to 'j smith' would have a very low uniqueness score).
- ```tooShort``` identifies whether either name was too short in regards to number of words (e.g. 'justin').

If you are interrested in debugging or looking deeper at what factors went into the comparison being a match or not, please see the attempt attributes. Each attempt is the use of different methods to identify if the names are a match or not. These include cleaning names in reference to one another and spelling rules, and using the names' pronunciation instead of spelling. An attempt is None if a previous attempt discovered the names were a match, as there is no further reason to continue the comparison. This is because two names might fail one or two methods but eventually be proven to be a match. 

Let's look at the example of the name comparison of 'Maurice' and 'Morris'. 
* ```attempt1``` is this simple spelling comparison after minimal cleaning. This would fail to identify a match.
* ```attempt2``` is a heavier edit of the spelling in reference to the other name and to spelling rules. This would also prove ineffective.
* ```attempt3``` checks if the modified tokens from attempt two are a match according to pronunciation. This would work!
* ```attempt4```, the last attempt, (not reached in this scenerio) identifies if the original tokens from the attempt one are a match according to pronunciation comparison.

Finally, when debugging, it is important to understand any attempt after attempt1 will not be undertaken if the names have no chance at matching. This is thanks to the ```isWorthContinuing``` function. If it fails this function or gets through all four attempts without passing any attempt, then match is considered false.

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