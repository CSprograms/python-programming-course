"""
Session 19 - Program 4: Number Category (Workout)

Classify a given non-zero integer using nested if statements into one of:
Positive Even, Positive Odd, Negative Even, or Negative Odd.

Sample Output:
Enter a non-zero number: 6
Positive Even

Try also: -3 gives Negative Odd.
"""

# Program 4: Classify a number (nested if)
n = int(input("Enter a non-zero number: "))
if n > 0:
    if n % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if n % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
