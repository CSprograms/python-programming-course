"""
Session 47 - Program 4: First and Last Three (Workout)

Print the first three and last three characters.

Sample Output:
Enter a string: Programming
Pro, ing

Try also: "Saveetha" gives Sav, tha.
"""

# Program 4: First 3 and last 3 characters
s = input("Enter a string: ")
print(s[:3] + ", " + s[-3:])
