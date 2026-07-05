"""
Session 31 - Program 3: Print N Stars (Workout)

A function that prints N stars on one line.

Sample Output:
* * * * *

Try also: print_stars(3) prints * * *.
"""

# Program 3: Print N stars on a single line (function)
def print_stars(n):
    for i in range(n):
        print("*", end=" ")
    print()

print_stars(5)
