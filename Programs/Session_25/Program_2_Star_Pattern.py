"""
Session 25 - Program 2: Star Pattern

Print a right-angled triangle of stars. Row i has i stars.

Sample Output:
Enter number of rows: 4
*
* *
* * *
* * * *

Try also: rows = 3 prints a 3-row triangle.
"""

# Program 2: Right-angled triangle of stars
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
