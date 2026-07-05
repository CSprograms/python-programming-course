"""
Session 55 - Program 4: Transpose a Matrix (Workout)

Swap rows and columns of a matrix. (LeetCode 867.)

Sample Output:
[[1, 4], [2, 5], [3, 6]]

Try also: [[1, 2], [3, 4]] gives [[1, 3], [2, 4]].
"""

# Program 4: Transpose of a 2D matrix
matrix = [[1, 2, 3], [4, 5, 6]]
rows = len(matrix)
cols = len(matrix[0])
result = []
for c in range(cols):
    new_row = []
    for r in range(rows):
        new_row.append(matrix[r][c])
    result.append(new_row)
print(result)
