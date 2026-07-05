"""
NCERT Supplementary Program - Unit 3: Functions and Modules

Program defining and using the 'swap_if_needed' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def swap_if_needed(a, b):
    return (b, a) if a > b else (a, b)

x, y = map(int, input('Enter two numbers: ').split())
x, y = swap_if_needed(x, y)
print(f'Result: {x}, {y}')
