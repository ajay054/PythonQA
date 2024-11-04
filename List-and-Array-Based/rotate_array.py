# Rotate an Array by k Positions
def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]
# Slicing the list and rearranging parts achieves rotation.
print(rotate_array([1, 2, 3, 4, 5], 2))

# For [1, 2, 3, 4, 5] with k = 2, the last 2 elements [4, 5] move to the front, producing [4, 5, 1, 2, 3].