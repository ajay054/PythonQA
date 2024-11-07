def count_pairs_with_sum(arr, target):
    seen = {}
    count = 0
    for num in arr:
        diff = target - num
        if diff in seen:
            count += seen[diff]
        seen[num] = seen.get(num, 0) + 1
    return count
# Using a dictionary to track occurrences, this counts pairs efficiently.
# print(count_pairs_with_sum([1, 5, 7, -1], 6))  # output : 2
print(count_pairs_with_sum([1, 1, 1, 1], 2)) 