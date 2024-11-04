# Find the Key With the Maximum Value in a Dictionary
def max_value_key(d):
    return max(d, key=d.get)

# Uses max() with d.get to find the key with the maximum value.


d = {'a': 10, 'b': 25, 'c': 7}
print(max_value_key(d))  

d2 = {'apple': 5, 'banana': 3, 'cherry': 8}
print(max_value_key(d2))  
