"""
Session 17 - Program 3: Driver Eligibility (Workout)

Print Can Drive if age is at least 18, otherwise Cannot Drive.

Sample Output:
Enter age: 20
Can Drive

Try also: 16 gives Cannot Drive.
"""

# Program 3: Can Drive / Cannot Drive
age = int(input("Enter age: "))
if age >= 18:
    print("Can Drive")
else:
    print("Cannot Drive")
