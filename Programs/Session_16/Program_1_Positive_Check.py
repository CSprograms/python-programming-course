"""
Session 16 - Program 1: Positive Check

Check whether a number is positive. Print Positive only when it is.

Sample Output:
Enter a number: 15
Positive

Try also: -5 prints nothing, because the condition n > 0 is false.
"""

# Program 1: Check whether a number is positive
n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
