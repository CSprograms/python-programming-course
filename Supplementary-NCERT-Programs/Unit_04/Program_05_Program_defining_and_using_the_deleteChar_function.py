"""
NCERT Supplementary Program - Unit 4: Strings

Program defining and using the 'deleteChar' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def deleteChar(st, ch):
    return st.replace(ch, '')

s = input('String: ')
c = input('Character to delete: ')
print('Result:', deleteChar(s, c))
