"""
Session 35 - Program 4: Logarithm (Workout)

Find the natural log and the log base 10 of a number.

Sample Output:
Enter a number: 100
ln=4.605, log10=2.0

Try also: 1000 gives ln=6.908, log10=3.0.
"""

# Program 4: Natural log and log base 10
import math

n = float(input("Enter a number: "))
print(f"ln={math.log(n):.3f}, log10={math.log10(n)}")
