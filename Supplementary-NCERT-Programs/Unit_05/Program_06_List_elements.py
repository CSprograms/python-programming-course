"""
NCERT Supplementary Program - Unit 5: Lists

List elements

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
lst  = list(map(int, input('List elements: ').split()))
elem = int(input('Element to count: '))
print(f'{elem} occurs {lst.count(elem)} time(s)')
