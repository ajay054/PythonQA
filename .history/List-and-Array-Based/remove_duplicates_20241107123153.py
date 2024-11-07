# # Remove Duplicates from a List Without Using set()
# def remove_duplicates(lst):
#     unique_list = []
#     for item in lst:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list
# # This builds a new list only adding unseen elements.

# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
# print(remove_duplicates(["apple", "banana", "apple", "cherry"]))


# v2
def remove_duplicates(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list
# This approach maintains the order and reduces the time complexity to 𝑂 ( 𝑛 ) O(n), as checking membership in a set is 𝑂 ( 1 ) O(1) on average.
print(remove_duplicates(["apple", "banana", "apple", "cherry"]))
#  output : ['apple', 'banana', 'cherry']