"""
NCERT Supplementary Program - Unit 11: Exception Handling

Program defining and using the 'safe_divide' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Denominator cannot be zero!')
    return a / b

try:
    n1 = float(input('Numerator: '))
    n2 = float(input('Denominator: '))
    print('Quotient:', safe_divide(n1, n2))
except ZeroDivisionError as e:
    print('Error:', e)
