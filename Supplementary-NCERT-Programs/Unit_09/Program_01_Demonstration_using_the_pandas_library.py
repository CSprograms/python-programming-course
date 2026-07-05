"""
NCERT Supplementary Program - Unit 9: Data Handling using Pandas

Demonstration using the pandas library

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import pandas as pd
import numpy as np

EngAlph   = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
Vowels    = pd.Series([0,0,0,0,0], index=['a','e','i','o','u'])
Friends   = pd.Series({'Arnab':1,'Samridhi':2,
                        'Ramit':3,'Divyam':4,'Kritika':5})
MTseries  = pd.Series([], dtype=float)
MonthDays = pd.Series(
    np.array([31,28,31,30,31,30,31,31,30,31,30,31]),
    index=range(1,13))

print(Vowels.empty)     # Check if empty
print(MTseries.empty)
