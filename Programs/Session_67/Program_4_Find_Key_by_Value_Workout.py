"""
Session 67 - Program 4: Find Key by Value (Workout)

Given a value, find the matching key.

Sample Output:
b

Try also: {"A": 100, "B": 200} with val = 100 gives A.
"""

# Program 4: Find the key for a given value
d = {"a": 1, "b": 2, "c": 3}
val = 2
for key, value in d.items():
    if value == val:
        print(key)
        break
