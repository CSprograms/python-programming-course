"""
NCERT Supplementary Program - Unit 8: Introduction to NumPy

NCERT-aligned practice program

This example continues from earlier setup code in this unit's exercises (included above so the file runs standalone).

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import numpy as np
myarray4 = np.arange(-1, 2.5, 0.25).reshape(14, 3)

print(myarray4.sum())          # total sum
print(myarray4.sum(axis=1))    # row-wise
print(myarray4.sum(axis=0))    # column-wise
print(myarray4.max(), myarray4.min())
print(myarray4.mean())
print(myarray4.std(),  myarray4.var())
