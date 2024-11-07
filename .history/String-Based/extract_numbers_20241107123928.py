# Extract All Numbers From a Given String
import re

def extract_numbers(s):
    return [int(num) for num in re.findall(r'\d+', s)]
# Regular expression \d+ finds all sequences of digits.

print(extract_numbers("There are 3 apples, 20 oranges, and 100 bananas.")) # output : [3, 20, 100]
print(extract_numbers("2023-10-05")) # output : [2023, 10, 5]