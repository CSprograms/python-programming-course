"""
Session 3 - Program 4: Numeric Type Check (Workout)

Indicate whether a value is an int, a float, or neither, using isinstance().

Sample Output:
int

Try also: x = 3.14 gives float.
"""

# Program 4: int, float or neither
x = 25
if isinstance(x, int):
    print("int")
elif isinstance(x, float):
    print("float")
else:
    print("neither")
