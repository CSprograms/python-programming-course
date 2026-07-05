"""
Session 22 - Program 1: Odd Numbers

Print the first N odd numbers using a step of 2.

Sample Output:
Enter N: 5
1 3 5 7 9

Try also: N = 3 gives 1 3 5.
"""

# Program 1: First N odd numbers (for)
N = int(input("Enter N: "))
for i in range(1, 2 * N, 2):
    print(i, end=" ")
print()
