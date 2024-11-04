# Check if a Dictionary Is a Subset of Another Dictionary
def is_subset(dict1, dict2):
    return all(item in dict2.items() for item in dict1.items())

# Checks if all items in dict1 are also in dict2.
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 2, 'c': 3}
print(is_subset(dict1, dict2))  # Output: True

dict3 = {'a': 1, 'b': 3}
print(is_subset(dict3, dict2))  # Output: False