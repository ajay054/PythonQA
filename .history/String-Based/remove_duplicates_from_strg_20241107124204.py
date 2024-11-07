# Remove Duplicate Characters From a String While Maintaining Order

# def remove_duplicates(s):
#     seen = set()
#     result = ""
#     for char in s:
#         if char not in seen:
#             seen.add(char)
#             result += char
#     return result
# # This keeps track of seen characters using a set to maintain order.
# print(remove_duplicates("hello loop"))

# Time Complexity: 𝑂 ( 𝑛 ) O(n), where 𝑛 n is the length of s, since each character is processed once
# Space Complexity: 𝑂 ( 𝑘 ) O(k), where 𝑘 k is the number of unique characters in s (to store characters in seen and result).

def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
print(remove_duplicates("hello loop")) 

#  output : helo p

# This is more efficient because list appending is faster than string concatenation in Python.