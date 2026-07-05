"""
NCERT Supplementary Program - Unit 5: Lists

NCERT-aligned practice program

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
list1 = [12,32,65,26,80,10]
list1.sort();   print(list1)       # i

list1 = [12,32,65,26,80,10]
sorted(list1);  print(list1)       # ii -- note: no mutation!

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1[::-2])                 # iii
print(list1[:3] + list1[3:])

list1 = [1,2,3,4,5]
print(list1[len(list1)-1])         # iv
