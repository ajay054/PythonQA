# Check if a String Is a Palindrome
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("racecar")) # True
print(is_palindrome("12345")) # False

# This checks if the string is equal to its reverse.