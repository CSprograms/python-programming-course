"""
NCERT Supplementary Program - Unit 2: Flow of Control

Enter a number

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
n = int(input('Enter a number: '))
for i in range(1, 11):
    print(f'{n} x {i:2d} = {n*i}')
