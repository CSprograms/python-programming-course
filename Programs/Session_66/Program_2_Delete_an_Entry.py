"""
Session 66 - Program 2: Delete an Entry

Remove a key with del.

Sample Output:
{'a': 1, 'c': 3}

Try also: {"x": 10, "y": 20} after del d["x"] gives {'y': 20}.
"""

# Program 2: Delete an entry using del
d = {"a": 1, "b": 2, "c": 3}
del d["b"]
print(d)
