"""
Session 36 - Program 1: Default Arguments

Compute the area of a rectangle, with the breadth defaulting to 1.

Sample Output:
50
8
"""

# Program 1: Area with a default argument
def area(length, breadth=1):
    return length * breadth

print(area(10, 5))    # both given
print(area(8))        # breadth defaults to 1
