# Merge Two Dictionaries, Combining Values for Common Keys
def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    for k, v in dict2.items():
        merged[k] = merged.get(k, 0) + v
    return merged
# This merges by adding values for common keys.
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

print(merge_dictionaries(dict1, dict2))  


