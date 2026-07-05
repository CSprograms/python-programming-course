"""
Session 40 - Program 4: Custom Exception (Workout)

Define and raise your own exception type.

Sample Output:
Valid: 25
NegativeNumberError: Value cannot be negative
"""

# Program 4: Define and raise a custom exception
class NegativeNumberError(Exception):
    pass

def check(value):
    if value < 0:
        raise NegativeNumberError("Value cannot be negative")
    return value

try:
    print("Valid:", check(25))
    print("Valid:", check(-7))
except NegativeNumberError as e:
    print("NegativeNumberError:", e)
