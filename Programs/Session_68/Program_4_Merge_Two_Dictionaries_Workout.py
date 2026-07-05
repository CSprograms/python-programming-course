"""
Session 68 - Program 4: Merge Two Dictionaries (Workout)

Merge two dictionaries into one.

Sample Output:
{'a': 1, 'b': 2, 'c': 3}

Try also: {"x": 10} merged with {"y": 20} gives {'x': 10, 'y': 20}.
"""

# Program 4: Merge two dictionaries into one
a = {"a": 1}
b = {"b": 2, "c": 3}
a.update(b)
print(a)
