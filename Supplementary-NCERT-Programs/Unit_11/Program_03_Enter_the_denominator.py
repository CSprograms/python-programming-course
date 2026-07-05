"""
NCERT Supplementary Program - Unit 11: Exception Handling

Enter the denominator

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
print('Handling multiple exceptions')
try:
    numerator = 50
    denom = int(input('Enter the denominator: '))
    print(numerator / denom)
    print('Division performed successfully')
except ZeroDivisionError:
    print('Denominator as ZERO is not allowed')
except ValueError:
    print('Only INTEGERS should be entered')
