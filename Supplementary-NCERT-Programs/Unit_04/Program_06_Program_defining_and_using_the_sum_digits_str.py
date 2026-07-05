"""
NCERT Supplementary Program - Unit 4: Strings

Program defining and using the 'sum_digits_str' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def sum_digits_str(s):
    return sum(int(c) for c in s if c.isdigit())

s = input('Enter string with digits: ')
print('Sum of digits:', sum_digits_str(s))
