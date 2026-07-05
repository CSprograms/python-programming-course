"""
Session 63 - Program 3: Unpack a Student Record (Workout)

Unpack a tuple into three separate variables.

Sample Output:
Ravi, 21, BCA

Try also: ("Sita", 20, "BCA") gives Sita, 20, BCA.
"""

# Program 3: Unpack a tuple into separate variables
record = ("Ravi", 21, "BCA")
name, age, course = record
print(name, age, course, sep=", ")
