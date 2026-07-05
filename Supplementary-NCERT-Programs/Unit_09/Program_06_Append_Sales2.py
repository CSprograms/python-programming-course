"""
NCERT Supplementary Program - Unit 9: Data Handling using Pandas

Append Sales2

This example continues from earlier setup code in this unit's exercises (included above so the file runs standalone).

Note: this program reads an external data file ('SalesFigures.csv') from the NCERT dataset, which is not bundled in this repository. Supply your own copy at that path (or adjust the path) to run it.

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import pandas as pd
data = {
    2014: [100.5,  150.8,  200.9, 30000, 40000],
    2015: [12000,  18000,  22000, 30000, 45000],
    2016: [20000,  50000,  70000,100000,125000],
    2017: [50000,  60000,  70000, 80000, 90000]
}
Sales = pd.DataFrame(data,
        index=['Madhu','Kusum','Kinshuk','Ankit','Shruti'])
Sales2 = pd.DataFrame({'2018':[160000,110000,500000,340000,900000]},
                       index=Sales.index)

# Append Sales2
Sales = pd.concat([Sales, Sales2], axis=1)
# Transpose
print(Sales.T)
# Display 2017 sales for all
print(Sales[2017])
# Delete year 2014
Sales.drop(columns=[2014], inplace=True)
# Rename Ankit to Vivaan
Sales.rename(index={'Ankit':'Vivaan'}, inplace=True)
# Write to CSV (no labels)
Sales.to_csv('SalesFigures.csv',
             header=False, index=False)
# Read back
SalesRetrieved = pd.read_csv('SalesFigures.csv',
                              header=None)
