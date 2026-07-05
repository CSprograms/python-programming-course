"""
NCERT Supplementary Program - Unit 3: Functions and Modules

Program defining and using the 'compound_interest' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def compound_interest(P, r, t, n=1):
    amount = P * (1 + r/(100*n)) ** (n*t)
    return amount - P, amount

P = float(input('Principal: '))
r = float(input('Rate %: '))
t = float(input('Time (years): '))
n = int(input('Times compounded/year: '))
ci, amt = compound_interest(P, r, t, n)
print(f'CI = {ci:.2f}   Total = {amt:.2f}')
