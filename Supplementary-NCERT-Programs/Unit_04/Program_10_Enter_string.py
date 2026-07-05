"""
NCERT Supplementary Program - Unit 4: Strings

Enter string

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
st = input('Enter string: ')
for i in range(-1, -len(st)-1, -1):
    print(st[i], end='')
print()
