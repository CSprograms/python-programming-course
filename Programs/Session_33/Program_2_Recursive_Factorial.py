"""
Session 33 - Program 2: Recursive Factorial

The factorial of n is n x (n-1)!, with 0! = 1! = 1 as the base case.

Sample Output:
Enter a number: 5
120

Try also: 6 gives 720.
"""

# Program 2: Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(factorial(num))
