"""
NCERT Supplementary Program - Unit 4: Strings

Program defining and using the 'charCount' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def charCount(ch, st):
    return sum(1 for c in st if c == ch)

st = input('String: ')
ch = input('Character: ')
print(f'{ch!r} occurs {charCount(ch, st)} time(s)')
