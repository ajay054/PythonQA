# Find the Top N Most Frequent Words in a Text File
from collections import Counter

def top_n_words(text, n):
    words = text.split()
    counts = Counter(words)
    return counts.most_common(n)
# Splits text into words, counts occurrences, and retrieves the top N words.
text = "apple banana apple orange banana apple cherry banana"
print(top_n_words(text, 2))  # Output: [('apple', 3), ('banana', 3)]