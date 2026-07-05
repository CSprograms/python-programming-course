"""
NCERT Supplementary Program - Unit 2: Flow of Control

Enter a number

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
num = int(input('Enter a number: '))
fact = 1
if num < 0:
    print('Factorial not defined for negative numbers')
elif num == 0:
    print('Factorial of 0 is 1')
else:
    for i in range(1, num + 1):
        fact *= i
    print(f'Factorial of {num} is {fact}')
