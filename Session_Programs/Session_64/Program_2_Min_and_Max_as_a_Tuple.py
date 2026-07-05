"""
Session 64 - Program 2: Min and Max as a Tuple

A function that returns a tuple of the minimum and maximum.

Sample Output:
(1, 9)

Try also: [10, 20, 30] gives (10, 30).
"""

# Program 2: Function returning (min, max) of a list
def min_max(numbers):
    return (min(numbers), max(numbers))

print(min_max([3, 1, 4, 1, 5, 9, 2]))
