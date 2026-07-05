"""
NCERT Supplementary Program - Unit 4: Strings

NCERT-aligned practice program

Note: as annotated in the comments, this example intentionally demonstrates a runtime error case; running it to completion will raise that exception.

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
myAddress = 'WZ-1,New Ganga Nagar,New Delhi'
print(myAddress.lower())              # i
print(myAddress.upper())              # ii
print(myAddress.count('New'))         # iii
print(myAddress.find('New'))          # iv
print(myAddress.rfind('New'))         # v
print(myAddress.split(','))           # vi
print(myAddress.split(' '))           # vii
print(myAddress.replace('New','Old')) # viii
print(myAddress.partition(','))       # ix
print(myAddress.index('Agra'))        # x  -> ValueError
