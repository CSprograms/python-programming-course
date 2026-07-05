"""
Session 17 - Program 1: Even or Odd

A number is even when dividing it by 2 leaves remainder 0.

Sample Output:
Enter a number: 10
Even

Try also: 7 gives Odd.
"""

# Program 1: Even or odd
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
