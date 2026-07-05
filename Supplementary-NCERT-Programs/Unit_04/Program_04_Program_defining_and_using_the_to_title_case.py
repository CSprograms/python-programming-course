"""
NCERT Supplementary Program - Unit 4: Strings

Program defining and using the 'to_title_case' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def to_title_case(s):
    return ' '.join(w[0].upper() + w[1:].lower()
                    for w in s.split())

print(to_title_case(input('Enter string: ')))
