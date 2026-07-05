"""
Session 6 - Program 1: Rectangle

Find the area and perimeter of a rectangle.

Sample Output:
Enter length : 10
Enter breadth: 5
Area      = 50
Perimeter = 30
"""

# Program 1: Area and perimeter of a rectangle
length  = int(input("Enter length : "))
breadth = int(input("Enter breadth: "))
area      = length * breadth
perimeter = 2 * (length + breadth)
print("Area      =", area)
print("Perimeter =", perimeter)
