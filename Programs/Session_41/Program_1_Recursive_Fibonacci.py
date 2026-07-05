"""
Session 41 - Assignment 3, Program 1: Recursive Fibonacci

Each Fibonacci number is the sum of the previous two, with the first two
equal to 1.

Sample Output:
8

Try also: fib(8) gives 21.
"""

# Assignment 1: Nth Fibonacci number (recursive)
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(6))
