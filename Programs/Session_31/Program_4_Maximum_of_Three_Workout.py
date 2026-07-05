"""
Session 31 - Program 4: Maximum of Three (Workout)

A function that returns the largest of three numbers.

Sample Output:
25

Try also: maximum(5, 5, 8) gives 8.
"""

# Program 4: Return the maximum of three numbers
def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

print(maximum(10, 25, 20))
