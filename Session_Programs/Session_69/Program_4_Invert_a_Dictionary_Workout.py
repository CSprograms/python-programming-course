"""
Session 69 - Program 4: Invert a Dictionary (Workout)

Swap the keys and the values.

Sample Output:
{1: 'a', 2: 'b'}

Try also: {"x": 10, "y": 20} gives {10: 'x', 20: 'y'}.
"""

# Program 4: Swap keys and values
d = {"a": 1, "b": 2}
inverted = {value: key for key, value in d.items()}
print(inverted)
