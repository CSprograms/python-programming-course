"""
Session 34 - Program 3: Circle Circumference (Workout)

Return the circumference of a circle, 2 pi r.

Sample Output:
43.98

Try also: circumference(10) gives 62.83.
"""

# Program 3: Circumference of a circle using math.pi
import math

def circumference(r):
    return 2 * math.pi * r

print(f"{circumference(7):.2f}")
