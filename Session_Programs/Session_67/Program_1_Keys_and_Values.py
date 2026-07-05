"""
Session 67 - Program 1: Keys and Values

Print all keys and all values.

Sample Output:
Keys: a b c
Values: 1 2 3
"""

# Program 1: Print all keys and all values
d = {"a": 1, "b": 2, "c": 3}
print("Keys:", *d.keys())
print("Values:", *d.values())
