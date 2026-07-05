"""
Session 25 - Program 1: Prime Check

A number is prime if it has no divisor other than 1 and itself. The inner
loop tests for divisors; break stops early once one is found.

Sample Output:
Enter a number: 7
Prime

Try also: 12 gives Not Prime.
"""

# Program 1: Prime check
n = int(input("Enter a number: "))
if n <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
