"""
Session 23 - Program 2: Factorial

The factorial of n is the product 1 x 2 x x n.

Sample Output:
Enter a number: 5
120

Try also: 3 gives 6.
"""

# Program 2: Factorial of a number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
