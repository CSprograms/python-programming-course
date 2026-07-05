"""
Session 4 - Program 3: Boolean of a Value (Workout)

Print the bool() result for several values.

Sample Output:
[False, True, True, False, False, True]
"""

# Program 3: bool() of different values
values = [0, 1, -5, 0.0, '', 'Hi']
print([bool(v) for v in values])
