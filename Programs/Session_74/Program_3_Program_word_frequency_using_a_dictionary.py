"""
Session 74 - Class Test 5, Q3: Program - word frequency using a dictionary.

Split the sentence into words, then count each with the get pattern.

Sample Output:
Enter a sentence: a b a c b a
{'a': 3, 'b': 2, 'c': 1}
"""

# Class Test: word frequency using a dictionary
sentence = input("Enter a sentence: ")
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)
