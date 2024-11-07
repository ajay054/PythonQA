# Reverse a List In-Place
def reverse_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left, right = left + 1, right - 1
    return lst
# Uses two-pointer technique to swap elements from both ends.
print(reverse_list([1, 2, 3, 4, 5])) # output : [5, 4, 3, 2, 1]
print(reverse_list(["a", "b", "c", "d"])) # output : ['d', 'c', 'b', 'a']