"""
Session 54 - Program 3: Sort by Length (Workout)

Sort a list of strings from shortest to longest.

Sample Output:
['fig', 'kiwi', 'apple']

Try also: ["Hi", "Bye", "OK"] gives ['Hi', 'OK', 'Bye'].
"""

# Program 3: Sort strings by length (ascending)
words = ["apple", "kiwi", "fig"]
words.sort(key=len)
print(words)
