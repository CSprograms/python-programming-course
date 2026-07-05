"""
Session 33 - Program 1: Rectangle (Two Return Values)

Return both the area and the perimeter of a rectangle.

Sample Output:
50 30

Try also: rectangle(8, 4) gives 32 24.
"""

# Program 1: Area and perimeter of a rectangle (two values)
def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

a, p = rectangle(10, 5)
print(a, p)
