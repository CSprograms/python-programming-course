"""
Session 69 - Program 3: Letter Positions (Workout)

Map each letter of a word to its position using a comprehension.

Sample Output:
Enter a word: CAT
{'C': 0, 'A': 1, 'T': 2}

Try also: "ABCD" gives {'A': 0, 'B': 1, 'C': 2, 'D': 3}.
"""

# Program 3: Map each letter to its position (dict comprehension)
word = input("Enter a word: ")
positions = {word[i]: i for i in range(len(word))}
print(positions)
