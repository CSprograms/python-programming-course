"""
NCERT Supplementary Program - Unit 1: Getting Started with Python

Enter temperature in Celsius

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
celsius = float(input('Enter temperature in Celsius: '))
fahrenheit = celsius * 9/5 + 32
print(f'{celsius} C = {fahrenheit} F')
print('Boiling (100 C):', 100*9/5+32, 'F')
print('Freezing  (0 C):', 0*9/5+32,   'F')
