"""
Session 71 - Assignment 5, Program 5: Word Frequency

Count how often each word appears in a sentence.

Sample Output:
Enter a sentence: a b a c b a
{'a': 3, 'b': 2, 'c': 1}

Try also: "python is fun" gives {'python': 1, 'is': 1, 'fun': 1}.
"""

# Assignment 5: Frequency of each word in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)
