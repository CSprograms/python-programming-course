"""
NCERT Supplementary Program - Unit 4: Strings

NCERT-aligned practice program

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
mySubject = 'Computer Science'
print(mySubject[0:len(mySubject)])    # i
print(mySubject[-7:-1])               # ii
print(mySubject[::2])                 # iii
print(mySubject[len(mySubject)-1])    # iv
print(2 * mySubject)                  # v
print(mySubject[::-2])                # vi
print(mySubject[:3] + mySubject[3:])  # vii
print(mySubject.swapcase())           # viii
print(mySubject.startswith('Comp'))   # ix
print(mySubject.isalpha())            # x
