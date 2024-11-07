# Split a String Based on a Delimiter Without Using split()
def split_string(s, delimiter):
    result, temp = [], ""
    for char in s:
        if char == delimiter:
            result.append(temp)
            temp = ""
        else:
            temp += char
    if temp:
        result.append(temp)
    return result
# This builds substrings manually, adding them when the delimiter is encountered.
print(split_string("a,b,c", ","))
print(split_string("hello world test", " "))