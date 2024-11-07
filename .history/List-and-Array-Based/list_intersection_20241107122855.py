# # Find the Intersection of Two Lists
# def list_intersection(list1, list2):
#     return [item for item in list1 if item in list2]
# # This finds common elements by checking membership in both lists.

# print(list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))
# print(list_intersection(["apple", "banana"], ["banana", "cherry"]))

# If list2 is large or if you want to improve efficiency, you could use a set for list2 to reduce the time complexity to 𝑂 ( 𝑛 ) O(n), as checking membership in a set is 𝑂 ( 1 ) O(1) on average

def list_intersection(list1, list2):
    set2 = set(list2)
    return [item for item in list1 if item in set2]
print(list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))  
#  output : [3, 4]