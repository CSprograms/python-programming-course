"""
NCERT Supplementary Program - Unit 3: Functions and Modules

Program defining and using the 'add' function

Adapted from NCERT-aligned Computer Science / Informatics Practices
coursework (Classes XI-XII). This file contains only the runnable
Python solution; the original NCERT exercise text is not reproduced.
"""
import math

def add(a,b): return a + b
def sub(a,b): return a - b
def mul(a,b): return a * b
def div(a,b): return a/b if b != 0 else 'Error: Zero'

print('1.Add  2.Sub  3.Mul  4.Div  5.log10  6.sin  7.cos')
ch = int(input('Choice: '))
if ch in [1,2,3,4]:
    a, b = float(input('a: ')), float(input('b: '))
    ops = {1:add, 2:sub, 3:mul, 4:div}
    print('Result:', ops[ch](a, b))
else:
    x = float(input('x: '))
    ops = {5:math.log10, 6:lambda v: math.sin(math.radians(v)),
           7:lambda v: math.cos(math.radians(v))}
    print('Result:', ops[ch](x))
