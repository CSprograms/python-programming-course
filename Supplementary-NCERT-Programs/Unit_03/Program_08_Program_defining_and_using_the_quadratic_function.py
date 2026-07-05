"""
NCERT Supplementary Program - Unit 3: Functions and Modules

Program defining and using the 'quadratic' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def quadratic(a, b, c):
    disc = b**2 - 4*a*c
    if disc > 0:
        r1 = (-b + disc**0.5) / (2*a)
        r2 = (-b - disc**0.5) / (2*a)
        print(f'Two real roots: {r1:.4f} and {r2:.4f}')
    elif disc == 0:
        print(f'Equal roots: {-b/(2*a):.4f}')
    else:
        print('Complex roots (no real roots)')

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
quadratic(a, b, c)
