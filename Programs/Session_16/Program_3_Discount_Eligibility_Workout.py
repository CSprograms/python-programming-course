"""
Session 16 - Program 3: Discount Eligibility (Workout)

Print Discount Applied if the purchase amount is greater than 1000;
otherwise do nothing.

Sample Output:
Enter purchase amount: 1500
Discount Applied

Try also: 800 prints nothing.
"""

# Program 3: Discount if amount > 1000
amount = int(input("Enter purchase amount: "))
if amount > 1000:
    print("Discount Applied")
