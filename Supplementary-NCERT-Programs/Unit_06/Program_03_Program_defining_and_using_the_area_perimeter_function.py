"""
NCERT Supplementary Program - Unit 6: Tuples and Dictionaries

Program defining and using the 'area_perimeter' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def area_perimeter(l, b):
    return l*b, 2*(l+b)

l, b = float(input('Length: ')), float(input('Breadth: '))
area, peri = area_perimeter(l, b)
print(f'Area: {area}   Perimeter: {peri}')
