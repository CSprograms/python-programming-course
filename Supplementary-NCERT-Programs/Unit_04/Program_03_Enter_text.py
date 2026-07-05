"""
NCERT Supplementary Program - Unit 4: Strings

Enter text

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
text = input('Enter text: ')
chars   = len(text)
alphas  = sum(1 for c in text if c.isalpha())
digits  = sum(1 for c in text if c.isdigit())
spaces  = sum(1 for c in text if c.isspace())
special = chars - alphas - digits - spaces
words   = len(text.split())
print(f'Characters: {chars}  Alphabets: {alphas}')
print(f'Digits: {digits}  Special: {special}  Words: {words}')
