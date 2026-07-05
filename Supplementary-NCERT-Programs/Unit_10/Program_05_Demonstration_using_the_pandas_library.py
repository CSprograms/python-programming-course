"""
NCERT Supplementary Program - Unit 10: Plotting Data using Matplotlib

Demonstration using the pandas library

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {'mass':   [0.330, 4.87, 5.97],
     'radius': [2439.7, 6051.8, 6378.1]},
    index=['Mercury','Venus','Earth'])
df.plot(kind='pie', y='mass',
        title='Planets by Mass Proportion')
plt.ylabel('')
plt.show()
