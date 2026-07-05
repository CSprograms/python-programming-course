"""
Session 9 - Program 1: Explicit Conversion

Demonstrate explicit conversion from string to int and from int to float.

Sample Output:
25 <class 'int'>
30.0 <class 'float'>
"""

# Program 1: Explicit type conversion
s = "25"
n = int(s)          # str -> int
print(n, type(n))

i = 30
f = float(i)        # int -> float
print(f, type(f))
