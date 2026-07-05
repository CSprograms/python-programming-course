"""
Session 41 - Assignment 3, Program 5: Division with Exception Handling

Divide two numbers, handling division by zero and wrong types.

Sample Output:
5.0
Cannot divide by zero
"""

# Assignment 5: Safe division with exception handling
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid operand type"

print(divide(10, 2))
print(divide(10, 0))
