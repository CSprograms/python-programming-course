"""
Session 26 - Assignment 2, Program 1: Armstrong Number

A 3-digit number is an Armstrong number if the sum of the cubes of its
digits equals the number itself (for example, 1^3 + 5^3 + 3^3 = 153).

Sample Output:
Enter a number: 153
Armstrong Number

Try also: 123 gives Not an Armstrong Number.
"""

# Assignment 1: Armstrong number
n = int(input("Enter a number: "))
temp = n
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10
if total == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
