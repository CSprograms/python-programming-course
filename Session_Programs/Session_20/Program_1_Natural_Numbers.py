"""
Session 20 - Program 1: Natural Numbers

Print the first N natural numbers.

Sample Output:
Enter N: 5
1 2 3 4 5

Try also: N = 3 gives 1 2 3.
"""

# Program 1: First N natural numbers (while)
N = int(input("Enter N: "))
i = 1
while i <= N:
    print(i, end=" ")
    i += 1
print()
