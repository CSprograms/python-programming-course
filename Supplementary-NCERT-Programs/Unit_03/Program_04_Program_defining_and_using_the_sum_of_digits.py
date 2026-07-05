"""
NCERT Supplementary Program - Unit 3: Functions and Modules

Program defining and using the 'sum_of_digits' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def sum_of_digits(n):
    n, total = abs(n), 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print('Sum of digits:', sum_of_digits(int(input('Enter: '))))
