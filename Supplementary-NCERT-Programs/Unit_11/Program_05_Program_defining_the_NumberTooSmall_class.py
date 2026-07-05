"""
NCERT Supplementary Program - Unit 11: Exception Handling

Program defining the 'NumberTooSmall' class

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
class NumberTooSmall(Exception): pass
class NumberTooBig(Exception):   pass

cubes = {}
for i in range(10):
    try:
        n = int(input(f'Integer {i+1}: '))
        if n < 3:  raise NumberTooSmall(f'{n} < 3 (min 3)')
        if n > 30: raise NumberTooBig(f'{n} > 30 (max 30)')
        cubes[n] = n**3
    except (NumberTooSmall, NumberTooBig) as e:
        print('Error:', e)
print('Cubes:', cubes)
