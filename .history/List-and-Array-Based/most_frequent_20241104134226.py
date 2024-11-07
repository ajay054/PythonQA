# Find the Most Frequent Element in an Array
from collections import Counter

def most_frequent(arr):
    count = Counter(arr)
    return count.most_common(1)[0][0]

# Counter counts occurrences, and most_common(1) retrieves the element with the highest count.

print(most_frequent([1, 3, 2, 1, 4, 1, 2, 3, 1]))
print(most_frequent(["apple", "banana", "apple", "cherry", "banana", "apple"]))

# Time Complexity: 𝑂 ( 𝑛 ) O(n), where 𝑛 n is the length of arr, as Counter counts each element in a single pass. Space Complexity: 𝑂 ( 𝑛 ) O(n), for storing the count of each unique element in arr.
