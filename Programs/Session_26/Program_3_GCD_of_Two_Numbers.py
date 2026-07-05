"""
Session 26 - Assignment 2, Program 3: GCD of Two Numbers

Use Euclid's method: replace the pair (a, b) by (b, a mod b) until b becomes
0.

Sample Output:
Enter first number: 12
Enter second number: 18
6

Try also: 24, 36 gives 12.
"""

# Assignment 3: GCD using a loop
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    a, b = b, a % b
print(a)
