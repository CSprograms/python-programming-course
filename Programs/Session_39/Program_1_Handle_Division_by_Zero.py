"""
Session 39 - Program 1: Handle Division by Zero

Catch ZeroDivisionError when dividing two numbers.

Sample Output:
Enter numerator: 10
Enter denominator: 0
Cannot divide by zero

Try also: 10, 2 gives 5.0.
"""

# Program 1: Handle division by zero
a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
try:
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
