# Count the Frequency of Characters in a String Using a Dictionary
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
# This counts occurrences of each character using a dictionary.
print(char_frequency("hello"))
print(char_frequency("aabbccdd"))