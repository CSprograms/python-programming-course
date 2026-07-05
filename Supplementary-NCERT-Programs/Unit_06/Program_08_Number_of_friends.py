"""
NCERT Supplementary Program - Unit 6: Tuples and Dictionaries

Number of friends

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
friends = {}
n = int(input('Number of friends: '))
for _ in range(n):
    name  = input('Name: ')
    phone = input('Phone: ')
    friends[name] = phone

# Display sorted by name
print('\nPhonebook:')
for k in sorted(friends):
    print(f'  {k}: {friends[k]}')
