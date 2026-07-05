"""
NCERT Supplementary Program - Unit 2: Flow of Control

Enter a year

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
year = int(input('Enter a year: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, 'is a Leap Year')
else:
    print(year, 'is NOT a Leap Year')
