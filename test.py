from rapidfuzz.fuzz import partial_ratio_alignment
from rapidfuzz.fuzz import partial_ratio
from rapidfuzz.distance.Levenshtein import normalized_similarity
from rapidfuzz.distance import Levenshtein

result = partial_ratio_alignment("aurel", "albert")

s = "albert"
print(f"window: '{s[result.dest_start:result.dest_end]}'")
print(f"window with +1: '{s[result.dest_start:result.dest_end+1]}'")
print(len(s))

# Also check what score this gives directly
from rapidfuzz import fuzz
print(fuzz.ratio("aurel", s[result.dest_start:result.dest_end]))
print(fuzz.ratio("aurel", "albert"))

normal_partial_ratio_result = partial_ratio("aurel", "albert")
print("Normal Partial Ratio:")
print(f"window: '{s[result.dest_start:result.dest_end]}'")
print(f"window with +1: '{s[result.dest_start:result.dest_end+1]}'")
print(normal_partial_ratio_result)

# new_test_partial_ratio_result = partial_ratio("aurel", "albert", scorer=normalized_similarity)
# print("Test Partial Ratio:")
# print(new_test_partial_ratio_result)

levenshtein_result = Levenshtein.normalized_similarity("aurel", "albert")
print("Levenshtein Result:")
print(levenshtein_result)

def partial_levenshtein_ratio(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1  # ensure s1 is shorter
    best = 0
    for i in range(len(s2) - len(s1) + 1):
        window = s2[i:i+len(s1)]
        score = Levenshtein.normalized_similarity(s1, window) * 100
        best = max(best, score)
    return best

print("Partial Levenshtein Ratio:")
print(partial_levenshtein_ratio("aurel", "albert"))