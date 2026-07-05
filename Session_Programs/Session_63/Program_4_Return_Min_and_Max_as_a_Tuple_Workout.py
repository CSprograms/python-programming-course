"""
Session 63 - Program 4: Return Min and Max as a Tuple (Workout)

Return both the minimum and maximum of a list, bundled in a tuple.

Sample Output:
(1, 9)

Try also: [10, 20, 5] gives (5, 20).
"""

# Program 4: Return (min, max) of a list as a tuple
def min_max(numbers):
    return (min(numbers), max(numbers))

print(min_max([3, 1, 4, 1, 5, 9, 2, 6]))
