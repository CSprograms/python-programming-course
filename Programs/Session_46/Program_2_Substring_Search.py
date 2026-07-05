"""
Session 46 - Program 2: Substring Search

Check whether a substring occurs in a string using in.

Sample Output:
Enter a string: Hello, World!
Enter substring to find: World
Found

Try also: "Python", "Java" gives Not Found.
"""

# Program 2: Check whether a substring exists (using 'in')
text = input("Enter a string: ")
sub = input("Enter substring to find: ")
if sub in text:
    print("Found")
else:
    print("Not Found")
