"""
NCERT Supplementary Program - Unit 10: Plotting Data using Matplotlib

Demonstration using the numpy library

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulated data
np.random.seed(42)
min_t = np.random.uniform(15, 25, 30)
max_t = np.random.uniform(28, 40, 30)
df = pd.DataFrame({'Min Temp':min_t, 'Max Temp':max_t})
df.plot(kind='hist', bins=10, alpha=0.7,
        title='Monthly Temperature Distribution')
plt.xlabel('Temperature (C)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
