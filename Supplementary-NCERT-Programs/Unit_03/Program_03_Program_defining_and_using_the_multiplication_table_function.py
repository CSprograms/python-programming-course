"""
NCERT Supplementary Program - Unit 3: Functions and Modules

Program defining and using the 'multiplication_table' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def multiplication_table(n):
    for i in range(1, 11):
        print(f'{n} x {i:2d} = {n*i}')

multiplication_table(int(input('Enter a number: ')))
