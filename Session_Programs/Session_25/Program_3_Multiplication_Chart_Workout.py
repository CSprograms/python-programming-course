"""
Session 25 - Program 3: Multiplication Chart (Workout)

Print a chart where entry (i,j) is i x j.

Sample Output:
Enter N: 3
1   2   3
2   4   6
3   6   9

Try also: N = 2 prints a 2x2 chart.
"""

# Program 3: Multiplication chart 1..N (nested loops)
N = int(input("Enter N: "))
for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(i * j, end="\t")
    print()
