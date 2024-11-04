# Remove Key-Value Pairs from a Dictionary Based on a Condition
def remove_based_on_condition(d, condition):
    return {k: v for k, v in d.items() if condition(v)}
# This creates a new dictionary only with items meeting the condition.
# Example dictionary
d = {'a': 10, 'b': 25, 'c': 7, 'd': 30}

# Condition: Keep only values greater than 15
print(remove_based_on_condition(d, lambda x: x > 15))  
# Output: {'b': 25, 'd': 30}
