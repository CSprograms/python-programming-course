"""
NCERT Supplementary Program - Unit 4: Strings

Program defining and using the 'replaceVowel' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def replaceVowel(st):
    return ''.join('*' if c in 'aeiouAEIOU' else c
                   for c in st)

print(replaceVowel(input('String: ')))
