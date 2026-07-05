"""
Session 40 - Program 3: Multi-Exception Calculator (Workout)

Handle several error types in one calculator function.

Sample Output:
Cannot divide by zero
Invalid operand type
"""

# Program 3: Calculator handling several exceptions
def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "/":
            return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid operand type"

print(calculate(10, 0, "/"))
print(calculate("a", 5, "+"))
