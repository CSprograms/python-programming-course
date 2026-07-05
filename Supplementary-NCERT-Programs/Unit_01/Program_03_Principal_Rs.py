"""
NCERT Supplementary Program - Unit 1: Getting Started with Python

Principal (Rs)

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
P = float(input('Principal (Rs): '))
R = float(input('Rate (% per year): '))
T = float(input('Time (years): '))
SI    = (P * R * T) / 100
total = P + SI
print(f'Simple Interest = Rs. {SI:.2f}')
print(f'Total Payable   = Rs. {total:.2f}')
