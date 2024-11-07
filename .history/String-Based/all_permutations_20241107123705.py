# Find All Permutations of a Given String
from itertools import permutations

def all_permutations(s):
    return [''.join(p) for p in permutations(s)]
# Using itertools.permutations generates all possible orders of the characters.
print(all_permutations("abcd")) 

# output : ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']