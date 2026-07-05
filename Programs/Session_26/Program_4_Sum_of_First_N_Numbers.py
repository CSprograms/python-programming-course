"""
Session 26 - Assignment 2, Program 4: Sum of First N Numbers

Add the first N natural numbers with a while loop.

Sample Output:
Enter N: 10
55

Try also: N = 5 gives 15.
"""

# Assignment 4: Sum of first N natural numbers (while)
N = int(input("Enter N: "))
total = 0
i = 1
while i <= N:
    total += i
    i += 1
print(total)
