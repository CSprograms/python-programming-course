"""
NCERT Supplementary Program - Unit 3: Functions and Modules

Program defining and using the 'div_by_7' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def div_by_7(n):
    return n % 7 == 0

n = int(input('Enter a number: '))
print(n, 'IS' if div_by_7(n) else 'is NOT', 'divisible by 7')
