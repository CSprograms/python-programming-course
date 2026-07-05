"""
NCERT Supplementary Program - Unit 5: Lists

How many integers?

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
n   = int(input('How many integers? '))
lst = [int(input()) for _ in range(n)]
pos = [x for x in lst if x > 0]
neg = [x for x in lst if x < 0]
print('Original:', lst)
print('Positives:', pos)
print('Negatives:', neg)
