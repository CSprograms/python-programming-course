"""
Session 19 - Program 2: Leap Year

A year is a leap year if it is divisible by 4, except century years, which
must be divisible by 400.

Sample Output:
Enter a year: 2024
Leap Year

Try also: 2023 gives Not a Leap Year; 1900 gives Not a Leap Year; 2000 gives Leap Year.
"""

# Program 2: Leap year (nested if)
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")
