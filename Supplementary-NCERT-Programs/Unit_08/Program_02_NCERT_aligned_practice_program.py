"""
NCERT Supplementary Program - Unit 8: Introduction to NumPy

NCERT-aligned practice program

This example continues from earlier setup code in this unit's exercises (included above so the file runs standalone).

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import numpy as np
vowels = np.array(['a','e','i','o','u'])
ones = np.ones((2, 5), dtype=int)
myarray1 = np.array([[2.7,-2,-19],
                     [0, 3.4, 99.9],
                     [10.6, 0, 13]])

print(ones.shape, ones.ndim, ones.size)    # a
print(ones.reshape(1, 10))                 # b
print(vowels[1:3])                         # c
print(myarray1[1:3, :])                    # d
print(myarray1[:, 0:2])                    # e
print(myarray1[1:3, 0])                    # f
print(vowels[::-1])                        # g
