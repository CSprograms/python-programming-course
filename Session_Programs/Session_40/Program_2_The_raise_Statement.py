"""
Session 40 - Program 2: The raise Statement

Raise an exception when the age is negative.

Sample Output:
Enter age: 25
Age is valid: 25

Try also: -5 gives ValueError: Age cannot be negative.
"""

# Program 2: Raise an exception for a negative age
age = int(input("Enter age: "))
try:
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age is valid:", age)
except ValueError as e:
    print("ValueError:", e)
