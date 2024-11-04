# Check if an Array Is a Palindrome
def is_palindrome(arr):
    return arr == arr[::-1]
# Checks if the array is equal to its reverse.
print(is_palindrome([1, 2, 3, 2, 1]))
print(is_palindrome([1, 2, 3]))
