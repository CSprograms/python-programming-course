"""
NCERT Supplementary Program - Unit 11: Exception Handling

Numerator

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
n1 = float(input('Numerator: '))
n2 = float(input('Denominator: '))
try:
    assert n2 != 0, 'Denominator must not be zero'
    print('Quotient:', n1 / n2)
except AssertionError as e:
    print('Assertion failed:', e)
