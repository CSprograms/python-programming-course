"""
Session 44 - Class Test 3, Q3: Program - factorial using recursion.

The factorial of n is n x (n-1)!, stopping at the base case 0! = 1! = 1.

Sample Output:
Enter a number: 5
120
"""

# Class Test: factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(factorial(num))
