"""
NCERT Supplementary Program - Unit 5: Lists

How many students?

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
n    = int(input('How many students? '))
lst  = [int(input(f'Marks of student {i+1}: ')) for i in range(n)]
print(f'Average marks: {sum(lst)/n:.2f}')
