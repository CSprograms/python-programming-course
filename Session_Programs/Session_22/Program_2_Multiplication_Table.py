"""
Session 22 - Program 2: Multiplication Table

Print the table of a number from 1 to 10.

Sample Output:
Enter a number: 5
5 10 15 20 25 30 35 40 45 50

Try also: 3 gives 3 6 9 12 15 18 21 24 27 30.
"""

# Program 2: Multiplication table of a number
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i, end=" ")
print()
