"""
NCERT Supplementary Program - Unit 3: Functions and Modules

Program defining and using the 'prefix_name' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
def prefix_name(name, gender):
    return f"{'Mr.' if gender.upper()=='M' else 'Ms.'} {name}"

print(prefix_name(input('Name: '), input('Gender (M/F): ')))
