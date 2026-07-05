"""
Session 19 - Program 1: Largest of Three (Nested)

Find the largest of three numbers using nested if.

Sample Output:
Enter first number: 10
Enter second number: 20
Enter third number: 15
20

Try also: 100, 50, 75 gives 100.
"""

# Program 1: Largest of three (nested if)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)
