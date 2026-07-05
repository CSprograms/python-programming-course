"""
Session 29 - Class Test 2, Q3: Program - check whether a number is prime.

A number is prime when no value from 2 up to n-1 divides it exactly.

Sample Output:
Enter a number: 7
Prime
"""

# Class Test: prime check
n = int(input("Enter a number: "))
if n <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    print("Prime" if is_prime else "Not Prime")
