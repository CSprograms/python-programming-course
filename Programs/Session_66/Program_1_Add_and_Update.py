"""
Session 66 - Program 1: Add and Update

Add a new key, and change the value of an existing one.

Sample Output:
{'a': 5, 'b': 2}

Try also: {"x": 10} with add ("y", 20) and update ("x", 15) gives {'x': 15, 'y': 20}.
"""

# Program 1: Add a new entry and update an existing one
d = {"a": 1}
d["b"] = 2        # add a new key
d["a"] = 5        # update an existing key
print(d)
