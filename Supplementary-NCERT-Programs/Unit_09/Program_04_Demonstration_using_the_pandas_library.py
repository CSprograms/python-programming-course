"""
NCERT Supplementary Program - Unit 9: Data Handling using Pandas

Demonstration using the pandas library

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
print(Sales)
