"""
NCERT Supplementary Program - Unit 3: Functions and Modules

Program defining and using the 'fibonacci' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n-2):
        a, b = b, a + b
    return b

terms = int(input('How many terms? '))
for i in range(1, terms+1):
    print(fibonacci(i), end=' ')
print()
