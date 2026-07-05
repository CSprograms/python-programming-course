"""
Session 71 - Assignment 5, Program 4: Tuple to Dictionary

Convert a tuple of (key, value) pairs into a dictionary.

Sample Output:
{'a': 1, 'b': 2, 'c': 3}

Try also: (("x", 10), ("y", 20)) gives {'x': 10, 'y': 20}.
"""

# Assignment 4: Convert a tuple of pairs into a dictionary
pairs = (("a", 1), ("b", 2), ("c", 3))
d = dict(pairs)
print(d)
