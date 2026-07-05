"""
Session 18 - Program 3: Day of Week (Workout)

Map a number 1-7 to the day of the week.

Sample Output:
Enter a number (1-7): 3
Wednesday

Try also: 6 gives Saturday.
"""

# Program 3: Day of week (1=Mon ... 7=Sun)
n = int(input("Enter a number (1-7): "))
if n == 1:
    print("Monday")
elif n == 2:
    print("Tuesday")
elif n == 3:
    print("Wednesday")
elif n == 4:
    print("Thursday")
elif n == 5:
    print("Friday")
elif n == 6:
    print("Saturday")
elif n == 7:
    print("Sunday")
else:
    print("Invalid number")
