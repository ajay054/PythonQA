#  Replace All Spaces in a String With "%20"
def replace_spaces(s):
    return ''.join('%20' if char == ' ' else char for char in s)
# This constructs a new string, replacing spaces with %20.
print(replace_spaces("Hello World")) # output : Hello%20World
print(replace_spaces("NoSpacesHere"))