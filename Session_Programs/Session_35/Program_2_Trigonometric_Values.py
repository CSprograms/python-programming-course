"""
Session 35 - Program 2: Trigonometric Values

Find sine, cosine and tangent of an angle given in degrees.

Sample Output:
Enter an angle in degrees: 30
0.50, 0.87, 0.58

Try also: 45 gives 0.71, 0.71, 1.00.
"""

# Program 2: sin, cos, tan of an angle in degrees
import math

angle = float(input("Enter an angle in degrees: "))
r = math.radians(angle)
print(f"{math.sin(r):.2f}, {math.cos(r):.2f}, {math.tan(r):.2f}")
