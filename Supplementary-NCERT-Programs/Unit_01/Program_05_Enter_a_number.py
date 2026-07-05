"""
NCERT Supplementary Program - Unit 1: Getting Started with Python

Enter a number

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
num = int(input('Enter a number: '))
if num % 2 == 0:
    print(num, 'is Even')
else:
    print(num, 'is Odd')
