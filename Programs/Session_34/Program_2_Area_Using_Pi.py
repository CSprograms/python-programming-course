"""
Session 34 - Program 2: Area Using Pi

Compute the area of a circle, pi r^2, using math.pi.

Sample Output:
Enter the radius: 10
314.159

Try also: r = 7 gives 153.938.
"""

# Program 2: Area of a circle using math.pi
import math

r = int(input("Enter the radius: "))
area = math.pi * r * r
print(round(area, 3))
