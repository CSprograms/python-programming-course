"""
Session 39 - Program 3: Safe Division (Workout)

A function that returns 0 when the denominator is 0.

Sample Output:
5.0
0
"""

# Program 3: Safe division (return 0 if denominator is 0)
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

print(safe_divide(10, 2))
print(safe_divide(10, 0))
