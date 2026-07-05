"""
NCERT Supplementary Program - Unit 6: Tuples and Dictionaries

Number of employees

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
n = int(input('Number of employees: '))
employee = {}
for _ in range(n):
    name   = input('Name: ')
    salary = int(input('Salary: '))
    employee[name] = salary
print('\nEMPLOYEE_NAME\t\tSALARY')
for k, v in employee.items():
    print(f'{k:<20}{v}')
