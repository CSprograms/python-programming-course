"""
Session 41 - Assignment 3, Program 3: Power with Default Argument

Compute base^exp, with the exponent defaulting to 2.

Sample Output:
32
9
"""

# Assignment 3: Power with a default exponent
def power(base, exp=2):
    return base ** exp

print(power(2, 5))
print(power(3))        # exp defaults to 2
