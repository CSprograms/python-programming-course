"""
Session 62 - Program 3: Tuple Membership (Workout)

Check whether a value exists in a tuple.

Sample Output:
Found

Try also: val = 5 gives Not Found.
"""

# Program 3: Check membership in a tuple (using 'in')
t = (1, 2, 3, 4)
val = 3
if val in t:
    print("Found")
else:
    print("Not Found")
