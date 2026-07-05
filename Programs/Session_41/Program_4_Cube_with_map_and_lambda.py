"""
Session 41 - Assignment 3, Program 4: Cube with map and lambda

Cube each element of a list.

Sample Output:
[1, 8, 27, 64]

Try also: [2, 3, 5] gives [8, 27, 125].
"""

# Assignment 4: Cube each element using map() and lambda
numbers = [1, 2, 3, 4]
cubes = list(map(lambda x: x ** 3, numbers))
print(cubes)
