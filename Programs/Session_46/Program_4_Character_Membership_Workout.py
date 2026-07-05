"""
Session 46 - Program 4: Character Membership (Workout)

Check whether a character is present in a string.

Sample Output:
Enter a string: Hello
Enter a character: e
Found

Try also: "Hello", "z" gives Not Found.
"""

# Program 4: Check whether a character is present (using 'in')
s = input("Enter a string: ")
ch = input("Enter a character: ")
if ch in s:
    print("Found")
else:
    print("Not Found")
