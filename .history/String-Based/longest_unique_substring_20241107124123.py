# Find the Longest Substring Without Repeating Characters
def longest_unique_substring(s):
    start, max_length, used_chars = 0, 0, {}
    for end, char in enumerate(s):
        if char in used_chars and start <= used_chars[char]:
            start = used_chars[char] + 1
        used_chars[char] = end
        max_length = max(max_length, end - start + 1)
    return max_length
# Sliding window technique keeps track of the start index and character positions to avoid repeats.

print(longest_unique_substring("abddcabcbb")) # output : 4

# This approach has a time complexity of 𝑂 ( 𝑛 ) O(n), where 𝑛 n is the length of s, making it efficient for this type of problem.