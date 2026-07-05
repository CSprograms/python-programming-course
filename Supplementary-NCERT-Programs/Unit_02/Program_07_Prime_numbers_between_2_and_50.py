"""
NCERT Supplementary Program - Unit 2: Flow of Control

Prime numbers between 2 and 50

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
print('Prime numbers between 2 and 50:')
for i in range(2, 51):
    j = 2
    while j <= i/2:
        if i % j == 0:
            break
        j += 1
    if j > i/2:
        print(i, end=' ')
print()
