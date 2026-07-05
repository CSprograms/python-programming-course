"""
Session 68 - Program 2: Merge Dictionaries

Combine two dictionaries with update().

Sample Output:
{'a': 1, 'b': 2, 'c': 3}

Try also: {"x": 10} merged with {"y": 20} gives {'x': 10, 'y': 20}.
"""

# Program 2: Merge two dictionaries with update()
a = {"a": 1}
b = {"b": 2, "c": 3}
a.update(b)
print(a)
