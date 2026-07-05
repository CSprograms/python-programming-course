"""
NCERT Supplementary Program - Unit 6: Tuples and Dictionaries

Enter a string

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
st = input('Enter a string: ')
freq = {}
for ch in st:
    freq[ch] = freq.get(ch, 0) + 1
for key, val in freq.items():
    print(f'{key} : {val}')
