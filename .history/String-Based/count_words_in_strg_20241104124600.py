# Count the Occurrences of Each Word in a String
def count_words(s):
    word_counts = {}
    words = s.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts
# This splits the string into words, counting occurrences with a dictionary.

text = "this is a test this is only a test"
print(count_words(text))
