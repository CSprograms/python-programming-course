"""
NCERT Supplementary Program - Unit 9: Data Handling using Pandas

Demonstration using the pandas library

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import pandas as pd
data = {
  'Name':['Raman','Raman','Raman',
          'Zuhaire','Zuhaire','Zuhaire',
          'Ashravy','Ashravy','Ashravy',
          'Mishti','Mishti','Mishti'],
  'UT': [1,2,3,1,2,3,1,2,3,1,2,3],
  'Maths':  [22,21,14,20,23,22,23,24,12,15,18,17],
  'Science':[21,20,19,17,15,18,19,22,25,22,21,18],
  'S.St':   [18,17,15,22,21,19,20,24,19,25,25,20],
  'Hindi':  [20,22,24,24,25,23,15,17,21,22,24,25],
  'Eng':    [21,24,23,19,15,13,22,21,23,22,23,20]
}
df = pd.DataFrame(data)

# Descriptive statistics
print(df.max(numeric_only=True))
print(df.min(numeric_only=True))
print(df.mean(numeric_only=True))
print(df.median(numeric_only=True))

# Average Maths marks for Zuhaire
dfZ = df[df['Name']=='Zuhaire'].loc[:,'Maths':'Eng']
print(dfZ.mean(axis=1))

# Sort by Maths descending
print(df.sort_values('Maths', ascending=False))

# Mean, var, std, quantile per student
print(df.groupby('Name')['Maths'].agg(
      ['mean','var','std','quantile']))
