"""
Session 7 - Program 3: Triangle Validity (Workout)

Given three sides, decide whether they can form a valid triangle (the sum of
any two sides must be greater than the third), printing the boolean result
directly.

Sample Output:
True

Try also: a, b, c = 1, 1, 5 gives False.
"""

# Program 3: valid triangle?
a, b, c = 3, 4, 5
print(a + b > c and b + c > a and a + c > b)
