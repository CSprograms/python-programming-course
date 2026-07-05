"""
Session 70 - Program 1: Nested Dictionary

Store a student record as a nested dictionary and read its fields.

Sample Output:
Ravi, 85

Try also: {"S2": {"name": "Meera", "mark": 92}} gives Meera, 92.
"""

# Program 1: Nested dictionary for a student record
students = {"S1": {"name": "Ravi", "mark": 85}}
print(students["S1"]["name"], students["S1"]["mark"], sep=", ")
