"""
Session 38 - Program 3: Sort by Length (Workout)

Sort a list of strings by their length using a lambda as the key.

Sample Output:
['kiwi', 'apple', 'banana']

Try also: ["hi", "bye", "okay"] gives ['hi', 'bye', 'okay'].
"""

# Program 3: Sort strings by their length
words = ["apple", "kiwi", "banana"]
words.sort(key=lambda w: len(w))
print(words)
