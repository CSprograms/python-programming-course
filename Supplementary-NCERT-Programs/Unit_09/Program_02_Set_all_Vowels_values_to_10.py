"""
NCERT Supplementary Program - Unit 9: Data Handling using Pandas

Set all Vowels values to 10

This example continues from earlier setup code in this unit's exercises (included above so the file runs standalone).

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import pandas as pd
EngAlph   = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
Vowels    = pd.Series([0,0,0,0,0], index=['a','e','i','o','u'])

# Set all Vowels values to 10
Vowels[:] = 10
# Divide by 2
Vowels = Vowels / 2
# Create Vowels1 and add
Vowels1 = pd.Series([2,5,6,3,8], index=['a','e','i','o','u'])
Vowels3 = Vowels + Vowels1
# Display first/last 10 of EngAlph
print(EngAlph[:10])
print(EngAlph[-10:])
