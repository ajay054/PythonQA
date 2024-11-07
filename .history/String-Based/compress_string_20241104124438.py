# String Compression (e.g., "aaabb" -> "a3b2")
def compress_string(s):
    compressed, count = "", 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1
    compressed += s[-1] + str(count)
    return compressed
# This counts consecutive characters, appending character and count pairs.
print(compress_string("aabcccccaaa"))