# Group a List of Dictionaries by a Common Key
from collections import defaultdict

def group_by_key(dicts, key):
    grouped = defaultdict(list)
    for d in dicts:
        grouped[d[key]].append(d)
    return grouped
# Groups dictionaries in a list based on a shared key.


dicts = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'David', 'age': 30, 'city': 'New York'},
    {'name': 'Eve', 'age': 35, 'city': 'San Francisco'}
]

# Group by age
print(group_by_key(dicts, 'age'))
# Output:
# {
#   25: [{'name': 'Alice', 'age': 25, 'city': 'New York'}, {'name': 'Charlie', 'age': 25, 'city': 'Los Angeles'}],
#   30: [{'name': 'Bob', 'age': 30, 'city': 'San Francisco'}, {'name': 'David', 'age': 30, 'city': 'New York'}],
#   35: [{'name': 'Eve', 'age': 35, 'city': 'San Francisco'}]
# }

# Group by city
print(group_by_key(dicts, 'city'))
# Output:
# {
#   'New York': [{'name': 'Alice', 'age': 25, 'city': 'New York'}, {'name': 'David', 'age': 30, 'city': 'New York'}],
#   'San Francisco': [{'name': 'Bob', 'age': 30, 'city': 'San Francisco'}, {'name': 'Eve', 'age': 35, 'city': 'San Francisco'}],
#   'Los Angeles': [{'name': 'Charlie', 'age': 25, 'city': 'Los Angeles'}]
# }

# When grouping by 'age', dictionaries with the same age are grouped together.
# When grouping by 'city', dictionaries with the same city are grouped together.