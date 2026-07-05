"""
Session 50 - Program 3: Trim and Capitalise (Workout)

Strip surrounding spaces, then capitalise only the first letter.

Sample Output:
Enter a string:   hello world
Hello world

Try also: " python " gives Python.
"""

# Program 3: Strip whitespace and capitalise the first letter
s = input("Enter a string: ")
print(s.strip().capitalize())
