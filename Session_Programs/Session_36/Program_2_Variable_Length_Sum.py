"""
Session 36 - Program 2: Variable-Length Sum

Add any number of values using *args.

Sample Output:
15

Try also: total(10, 20) gives 30.
"""

# Program 2: Sum using variable-length arguments (*args)
def total(*numbers):
    s = 0
    for x in numbers:
        s += x
    return s

print(total(1, 2, 3, 4, 5))
