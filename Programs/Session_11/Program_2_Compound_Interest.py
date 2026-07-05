"""
Session 11 - Assignment 1, Program 2: Compound Interest

A = P(1 + R/(100n))^nT and CI = A - P.

Sample Output:
CI = 102.5

Try also: P = 5000, T = 3, R = 10, n = 1 gives CI = 1655.0.
"""

P, T, R, n = 1000, 2, 5, 1
A = P * (1 + R / (100 * n)) ** (n * T)
CI = A - P
print("CI =", CI)
