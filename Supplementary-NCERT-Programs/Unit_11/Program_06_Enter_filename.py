"""
NCERT Supplementary Program - Unit 11: Exception Handling

Enter filename

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
filename = input('Enter filename: ')
try:
    with open(filename, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print(f'File "{filename}" not found.')
except IOError as e:
    print('I/O error:', e)
