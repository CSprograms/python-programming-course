"""
NCERT Supplementary Program - Unit 3: Functions and Modules

Program defining and using the 'login' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def login(uid, pwd):
    attempts = 0
    while attempts < 3:
        u = input('User ID: ')
        p = input('Password: ')
        if u == uid and p == pwd:
            print('Login successful')
            return
        print('Incorrect credentials')
        attempts += 1
    print('Account blocked after 3 wrong attempts')

login('ADMIN', 'St0rE@1')
