"""
NCERT Supplementary Program - Unit 5: Lists

After removing duplicates

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
lst, unique = list(map(int, input('List: ').split())), []
for x in lst:
    if x not in unique:
        unique.append(x)
print('After removing duplicates:', unique)
