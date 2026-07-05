"""
NCERT Supplementary Program - Unit 6: Tuples and Dictionaries

NCERT-aligned practice program

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
s = 'w3resource'
d = {}
for i, c in enumerate(s):
    if c not in d:
        d[c] = i
print(d)
