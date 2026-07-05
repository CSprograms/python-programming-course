"""
NCERT Supplementary Program - Unit 8: Introduction to NumPy

Demonstration using the numpy library

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import numpy as np

# a) 1-D array 'zeros' with 10 elements, all 0
zeros = np.zeros(10)

# b) 1-D array 'vowels' = ['a','e','i','o','u']
vowels = np.array(['a','e','i','o','u'])

# c) 2-D array 'ones': 2 rows, 5 cols, dtype=int
ones = np.ones((2, 5), dtype=int)

# d) 2-D array 'myarray1' from nested list (3x3)
myarray1 = np.array([[2.7,-2,-19],
                     [0, 3.4, 99.9],
                     [10.6, 0, 13]])

# e) 2-D array 'myarray2': arange, start=4, step=4,
#    reshape to 3 rows x 5 cols, dtype=float
myarray2 = np.arange(4, 64, 4, dtype=float).reshape(3, 5)
