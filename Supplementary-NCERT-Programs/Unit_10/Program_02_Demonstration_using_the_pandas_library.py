"""
NCERT Supplementary Program - Unit 10: Plotting Data using Matplotlib

Demonstration using the pandas library

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import pandas as pd
import matplotlib.pyplot as plt

data = {'College':  ['CollegeA','CollegeB','CollegeC','CollegeD'],
        'Science':  [15, 12, 18, 10],
        'Commerce': [ 8, 10,  7, 12],
        'Humanities':[10, 9, 11,  8]}
df = pd.DataFrame(data)
df.plot(kind='bar', x='College',
        title='Courses Offered by Colleges')
plt.xlabel('College')
plt.ylabel('Number of Courses')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
