"""
NCERT Supplementary Program - Unit 2: Flow of Control

Enter a number

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
num = int(input('Enter a number: '))
flag = 0
if num > 1:
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            flag = 1
            break
    print(num, 'is NOT prime' if flag else 'is prime')
else:
    print('Enter a number > 1')
