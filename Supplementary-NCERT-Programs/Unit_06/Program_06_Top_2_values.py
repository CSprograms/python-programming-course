"""
NCERT Supplementary Program - Unit 6: Tuples and Dictionaries

Top 2 values

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
d = {'Raman':85,'Priya':92,'Arjun':78,'Sneha':95,'Kiran':88}
top2 = sorted(d.values(), reverse=True)[:2]
print('Top 2 values:', top2)
