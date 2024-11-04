# Sort a Dictionary by Its Values
def sort_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))
# Uses sorted() with a key function to sort by values.
d = {'apple': 3, 'banana': 1, 'cherry': 2}
print(sort_by_values(d))