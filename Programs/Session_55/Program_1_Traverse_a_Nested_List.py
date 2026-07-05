"""
Session 55 - Program 1: Traverse a Nested List

Print every element of a nested list.

Sample Output:
1 2 3 4 5 6

Try also: [['a', 'b'], ['c', 'd']] prints a b c d.
"""

# Program 1: Traverse a nested list
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for x in row:
        print(x, end=" ")
print()
