# Check if Two Strings Are Anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)    #  Sorting both strings and comparing them helps check if both strings have the same characters in any order.
print(are_anagrams("listen", "silent"))
print(are_anagrams("apple", "pale"))