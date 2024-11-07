# Find All Permutations of a Given String
from itertools import permutations

def all_permutations(s):
    return [''.join(p) for p in permutations(s)]
# Using itertools.permutations generates all possible orders of the characters.
print(all_permutations("abcd")) 