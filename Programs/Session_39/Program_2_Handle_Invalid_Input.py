"""
Session 39 - Program 2: Handle Invalid Input

Catch ValueError when converting text to a number.

Sample Output:
Enter a number: abc
Invalid input

Try also: "25" gives 25.
"""

# Program 2: Handle an invalid integer conversion
s = input("Enter a number: ")
try:
    n = int(s)
    print(n)
except ValueError:
    print("Invalid input")
