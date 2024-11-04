# Group Elements of a List Based on Their Frequency
from collections import defaultdict

def group_by_frequency(lst):
    freq = defaultdict(list)
    for item in lst:
        freq[item].append(item)
    return list(freq.values())
# This groups items by their frequency into lists.
print(group_by_frequency([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))  


