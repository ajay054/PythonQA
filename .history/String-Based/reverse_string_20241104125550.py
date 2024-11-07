# Reverse a String Without Using Built-In Functions


# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str 
# print(reverse_string("Hello"))


def reverse_string(s): # s[::-1] creates a reversed version of the string s by using Python’s slicing feature. This is concise, efficient, and commonly used in Python for reversing sequences.
    return s[::-1]
print(reverse_string("hello"))
