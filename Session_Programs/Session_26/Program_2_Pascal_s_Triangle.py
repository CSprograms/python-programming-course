"""
Session 26 - Assignment 2, Program 2: Pascal's Triangle

Print Pascal's triangle up to N rows.

Sample Output:
Enter N: 4
1
1 1
1 2 1
1 3 3 1

Try also: N = 3 prints the first three rows.
"""

# Assignment 2: Pascal's triangle (N rows)
N = int(input("Enter N: "))
row = [1]
for r in range(N):
    print(*row)
    next_row = [1]
    for k in range(len(row) - 1):
        next_row.append(row[k] + row[k + 1])
    next_row.append(1)
    row = next_row
