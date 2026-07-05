"""
NCERT Supplementary Program - Unit 6: Tuples and Dictionaries

Enter any number

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
numberNames = {0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',
               5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
num = input('Enter any number: ')
result = ' '.join(numberNames[int(d)] for d in num)
print(result)
