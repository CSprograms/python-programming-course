"""
NCERT Supplementary Program - Unit 5: Lists

Largest

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
lst = sorted(set(map(int, input('List: ').split())), reverse=True)
print('Largest:', lst[0])
if len(lst) > 1:
    print('Second Largest:', lst[1])
