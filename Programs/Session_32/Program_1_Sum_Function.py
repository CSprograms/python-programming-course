"""
Session 32 - Program 1: Sum Function

Find the sum of two numbers passed as positional arguments.

Sample Output:
Enter first number: 10
Enter second number: 15
25

Try also: 100, 200 gives 300.
"""

# Program 1: Sum of two numbers (positional arguments)
def add(a, b):
    return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(add(x, y))
