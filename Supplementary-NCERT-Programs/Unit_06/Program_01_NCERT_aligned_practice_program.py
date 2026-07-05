"""
NCERT Supplementary Program - Unit 6: Tuples and Dictionaries

NCERT-aligned practice program

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
tuple1 = (23,1,45,67,45,9,55,45)
tuple2 = (100,200)
print(tuple1.index(45))    # i
print(tuple1.count(45))    # ii
print(tuple1 + tuple2)     # iii
print(len(tuple2))         # iv
print(max(tuple1))         # v
print(min(tuple1))         # vi
print(sum(tuple2))         # vii
print(sorted(tuple1))      # viii -- does not modify tuple1
print(tuple1)
