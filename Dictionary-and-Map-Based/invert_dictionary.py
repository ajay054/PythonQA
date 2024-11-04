# Invert a Dictionary (Swap Keys and Values)
def invert_dictionary(d):
    return {v: k for k, v in d.items()}
# This swaps each key with its value using a dictionary comprehension.
d = {'a': 1, 'b': 2, 'c': 3}
print(invert_dictionary(d))  
