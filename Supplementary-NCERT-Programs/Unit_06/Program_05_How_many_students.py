"""
NCERT Supplementary Program - Unit 6: Tuples and Dictionaries

How many students?

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
n      = int(input('How many students? '))
emails = tuple(input(f'Email {i+1}: ') for i in range(n))
users  = tuple(e.split('@')[0] for e in emails)
doms   = tuple(e.split('@')[1] for e in emails)
print('Usernames:', users)
print('Domains:',   doms)
