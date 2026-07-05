"""
Session 32 - Program 3: Cylinder Volume (Workout)

Return the volume of a cylinder, pi r^2 h, using two parameters.

Sample Output:
785.40

Try also: cylinder_volume(3, 7) gives 197.92.
"""

# Program 3: Volume of a cylinder (pi * r * r * h)
import math

def cylinder_volume(r, h):
    return math.pi * r * r * h

print(f"{cylinder_volume(5, 10):.2f}")
