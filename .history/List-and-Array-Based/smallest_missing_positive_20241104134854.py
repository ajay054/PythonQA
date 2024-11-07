# Find the Smallest Missing Positive Integer in an Array
def smallest_missing_positive(arr):
    s = set(arr)
    i = 1
    while i in s:
        i += 1
    return i
# Using a set for quick lookup, this increments i until finding the first missing integer.
print(smallest_missing_positive([1, 2, 3, 4]))
