"""
Session 25 - Program 4: Pascal's Triangle (Workout)

Each row starts and ends with 1; every inner number is the sum of the two
numbers above it. (LeetCode 118.)

Sample Output:
Enter n: 4
1
1 1
1 2 1
1 3 3 1

Try also: n = 3 prints the first three rows.
"""

# Program 4: Pascal's triangle (first n rows)
n = int(input("Enter n: "))
row = [1]
for r in range(n):
    print(*row)
    next_row = [1]
    for k in range(len(row) - 1):
        next_row.append(row[k] + row[k + 1])
    next_row.append(1)
    row = next_row
