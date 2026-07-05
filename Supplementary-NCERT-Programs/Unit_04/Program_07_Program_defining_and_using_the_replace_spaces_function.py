"""
NCERT Supplementary Program - Unit 4: Strings

Program defining and using the 'replace_spaces' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def replace_spaces(sentence):
    return sentence.replace(' ', '-')

print(replace_spaces(input('Enter sentence: ')))
