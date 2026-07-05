"""
NCERT Supplementary Program - Unit 2: Flow of Control

Enter numbers (negative to stop)

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
total = 0
print('Enter numbers (negative to stop):')
while True:
    n = int(input())
    if n < 0:
        break
    total += n
print('Sum =', total)
