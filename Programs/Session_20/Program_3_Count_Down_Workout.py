"""
Session 20 - Program 3: Count Down (Workout)

Print from N down to 1.

Sample Output:
Enter N: 5
5 4 3 2 1

Try also: N = 3 gives 3 2 1.
"""

# Program 3: Count down from N to 1 (while)
N = int(input("Enter N: "))
i = N
while i >= 1:
    print(i, end=" ")
    i -= 1
print()
