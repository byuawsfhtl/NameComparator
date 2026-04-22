from rapidfuzz.fuzz import partial_ratio_alignment

result = partial_ratio_alignment("aurel", "albert")

s = "albert"
print(f"window: '{s[result.dest_start:result.dest_end]}'")
print(f"window with +1: '{s[result.dest_start:result.dest_end+1]}'")
print(len(s))

# Also check what score this gives directly
from rapidfuzz import fuzz
print(fuzz.ratio("aurel", s[result.dest_start:result.dest_end]))
print(fuzz.ratio("aurel", "albert"))