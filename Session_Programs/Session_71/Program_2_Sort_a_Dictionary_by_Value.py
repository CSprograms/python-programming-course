"""
Session 71 - Assignment 5, Program 2: Sort a Dictionary by Value

Sort a dictionary by its values, highest first.

Sample Output:
{'a': 3, 'c': 2, 'b': 1}

Try also: {"x": 10, "y": 5, "z": 15} gives {'z': 15, 'x': 10, 'y': 5}.
"""

# Assignment 2: Sort a dictionary by value (descending)
d = {"a": 3, "b": 1, "c": 2}
sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
result = dict(sorted_items)
print(result)
