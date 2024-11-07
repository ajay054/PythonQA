# Find the Kth Smallest and Kth Largest Element in a List
def kth_smallest_largest(arr, k):
    arr.sort()
    return arr[k-1], arr[-k]

# Sorting the array, then returning the Kth elements from start and end gives the Kth smallest and largest.
print(kth_smallest_largest([7, 10, 4, 3, 20, 15], 3))