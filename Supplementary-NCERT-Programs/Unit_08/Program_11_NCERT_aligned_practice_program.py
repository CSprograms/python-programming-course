"""
NCERT Supplementary Program - Unit 8: Introduction to NumPy

NCERT-aligned practice program

This example continues from earlier setup code in this unit's exercises (included above so the file runs standalone).

Note: this program reads an external data file ('C:/NCERT/Iris.txt') from the NCERT dataset, which is not bundled in this repository. Supply your own copy at that path (or adjust the path) to run it.

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import numpy as np
iris = np.genfromtxt('C:/NCERT/Iris.txt',
        skip_header=1, delimiter=',', dtype=float)
iris = iris[0:30, [0,1,2,3,5]]
iris1, iris2, iris3 = np.split(iris, [10, 20], axis=0)
iris_min = iris.min(axis=0)

iris1_min = iris1.min(axis=0)
print(iris1_min[0] > iris_min[0])  # sepal length
# repeat for other columns and species
