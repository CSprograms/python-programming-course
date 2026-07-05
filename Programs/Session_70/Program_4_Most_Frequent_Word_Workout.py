"""
Session 70 - Program 4: Most Frequent Word (Workout)

Find the word that appears most often in a sentence.

Sample Output:
Enter a sentence: a b a c b a
a (count=3)

Try also: "go go go run" gives go (count=3).
"""

# Program 4: Most frequent word in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
top = max(freq, key=freq.get)
print(f"{top} (count={freq[top]})")
