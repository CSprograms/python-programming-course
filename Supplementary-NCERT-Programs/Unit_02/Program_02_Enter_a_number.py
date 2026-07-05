"""
NCERT Supplementary Program - Unit 2: Flow of Control

Enter a number

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
num = int(input('Enter a number: '))
if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
else:
    print('Zero')
