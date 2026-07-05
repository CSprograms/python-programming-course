"""
NCERT Supplementary Program - Unit 10: Plotting Data using Matplotlib

Demonstration using the pandas library

Note: this program reads an external data file ('Marks.csv') from the NCERT dataset, which is not bundled in this repository. Supply your own copy at that path (or adjust the path) to run it.

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Marks.csv')
df   = pd.DataFrame(data)
df.plot(kind='box')
plt.title('Performance Analysis')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.show()
