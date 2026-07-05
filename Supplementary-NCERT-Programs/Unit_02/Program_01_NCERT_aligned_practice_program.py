"""
NCERT Supplementary Program - Unit 2: Flow of Control

NCERT-aligned practice program

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
# (i)
a = 110
while a > 100:
    print(a)
    a -= 2

# (ii)
for i in range(5, 0, -1):
    print(i)

# (iii)
for i in range(1, 5):
    for j in range(1, i+1):
        print('*', end='')
    print()

# (iv)
for i in range(2, 7, 2):
    print(i)

# (v)
x = 2
for i in range(6):
    x *= 2
print(x)
