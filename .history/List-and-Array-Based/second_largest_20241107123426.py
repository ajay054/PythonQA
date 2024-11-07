# Find the Second Largest Element in an Array
def second_largest(arr):
    first, second = float('-inf'), float('-inf')
    for num in arr:
        if num > first:
            second, first = first, num
        elif num > second and num != first:
            second = num
    return second
# Tracks the largest and second-largest elements in one pass.
print(second_largest([10, 20, 4, 45, 99])) # output : 45
