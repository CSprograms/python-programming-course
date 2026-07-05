"""
Session 11 - Assignment 1, Program 4: Total Bill with GST

Add GST to a bill amount.

Sample Output:
1180.0

Try also: bill = 500, gst = 5 gives 525.0.
"""

bill = 1000
gst = 18
total = bill + bill * gst / 100
print(total)
