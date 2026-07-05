"""
Session 14 - Class Test 1, Q3: Swap two variables without using a third variable (program).

Sample Output:
Before: 5 10
After : 10 5
"""

# Method 1: tuple assignment (recommended)
a, b = 5, 10
print("Before:", a, b)
a, b = b, a
print("After :", a, b)
