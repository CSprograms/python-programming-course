"""
NCERT Supplementary Program - Unit 5: Lists

Numbers

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
lst = sorted(map(int, input('Numbers: ').split()))
n = len(lst)
median = lst[n//2] if n%2 else (lst[n//2-1]+lst[n//2])/2
print('Median:', median)
