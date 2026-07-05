"""
NCERT Supplementary Program - Unit 3: Functions and Modules

Program defining and using the 'calculate_discount' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def calculate_discount(amount, is_member=False):
    if amount >= 2000:   disc = 10
    elif amount >= 1000: disc = 8
    elif amount >= 500:  disc = 5
    else:                disc = 0
    if is_member:
        disc += 5
    net = amount - (amount * disc / 100)
    return disc, net

amt = float(input('Shopping amount: '))
mem = input('Member? (y/n): ').lower() == 'y'
d, net = calculate_discount(amt, mem)
print(f'Discount: {d}%   Net: Rs.{net:.2f}')
