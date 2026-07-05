"""
Session 55 - Program 3: Matrix Sum (Workout)

Add up every element of a 2D matrix.

Sample Output:
10

Try also: [[1, 2, 3], [4, 5, 6]] gives 21.
"""

# Program 3: Sum of all elements of a 2D matrix
matrix = [[1, 2], [3, 4]]
total = 0
for row in matrix:
    for x in row:
        total += x
print(total)
