"""
Session 71 - Assignment 5, Program 3: Common Elements in Tuples

Find the values that appear in both tuples.

Sample Output:
(3, 4)

Try also: (10, 20, 30) and (20, 30, 40) give (20, 30).
"""

# Assignment 3: Common elements between two tuples
a = (1, 2, 3, 4)
b = (3, 4, 5, 6)
common = tuple(x for x in a if x in b)
print(common)
