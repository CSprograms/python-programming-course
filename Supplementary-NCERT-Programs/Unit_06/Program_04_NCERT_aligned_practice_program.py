"""
NCERT Supplementary Program - Unit 6: Tuples and Dictionaries

NCERT-aligned practice program

Note: as annotated in the comments, this example intentionally demonstrates a runtime error case; running it to completion will raise that exception.

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
tuple1 = (5)       # NOT a tuple -- parentheses, not tuple
len(tuple1)        # TypeError: object of type 'int'
                   # Fix: tuple1 = (5,)
