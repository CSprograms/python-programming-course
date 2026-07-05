"""
NCERT Supplementary Program - Unit 9: Data Handling using Pandas

NCERT-aligned practice program

This example continues from earlier setup code in this unit's exercises (included above so the file runs standalone).

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import pandas as pd
import numpy as np
MonthDays = pd.Series(
    np.array([31,28,31,30,31,30,31,31,30,31,30,31]),
    index=range(1,13))

print(MonthDays[3:8])
print(MonthDays[::-1])
