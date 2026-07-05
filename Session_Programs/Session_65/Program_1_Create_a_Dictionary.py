"""
Session 65 - Program 1: Create a Dictionary

Create a dictionary of names and marks and print each pair.

Sample Output:
Ravi: 85, Sita: 90

Try also: {"A": 1, "B": 2} gives A: 1, B: 2.
"""

# Program 1: Create a dictionary and print it
marks = {"Ravi": 85, "Sita": 90}
pairs = []
for name, score in marks.items():
    pairs.append(f"{name}: {score}")
print(", ".join(pairs))
