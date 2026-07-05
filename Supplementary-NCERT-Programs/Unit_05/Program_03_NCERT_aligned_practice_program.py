"""
NCERT Supplementary Program - Unit 5: Lists

NCERT-aligned practice program

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
myList = [1,2,3,4,5,6,7,8,9,10]
for i in range(0, len(myList)):
    if i % 2 == 0:
        print(myList[i])
