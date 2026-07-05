"""
NCERT Supplementary Program - Unit 8: Introduction to NumPy

NCERT-aligned practice program

This example continues from earlier setup code in this unit's exercises (included above so the file runs standalone).

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import numpy as np
ones = np.ones((2, 5), dtype=int)
myarray1 = np.array([[2.7,-2,-19],
                     [0, 3.4, 99.9],
                     [10.6, 0, 13]])
myarray2 = np.arange(4, 64, 4, dtype=float).reshape(3, 5)

print(ones / 3)                         # a
print(myarray1 + myarray2)              # b
print(np.dot(myarray1, myarray2))       # c
print(myarray1 ** 3 / 2)               # d
print((np.sqrt(myarray2) / 2).round(2))# e
