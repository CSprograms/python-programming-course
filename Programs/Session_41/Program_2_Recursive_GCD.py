"""
Session 41 - Assignment 3, Program 2: Recursive GCD

Use Euclid's rule recursively: gcd(a, b) = gcd(b, a mod b).

Sample Output:
6

Try also: gcd(48, 60) gives 12.
"""

# Assignment 2: GCD of two numbers (recursive)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(12, 18))
