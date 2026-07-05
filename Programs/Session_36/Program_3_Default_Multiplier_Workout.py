"""
Session 36 - Program 3: Default Multiplier (Workout)

Multiply N by 2 by default, or by a value the caller provides.

Sample Output:
10
15
"""

# Program 3: Multiply N by m (default m = 2)
def multiply(n, m=2):
    return n * m

print(multiply(5))       # uses default m = 2
print(multiply(5, 3))    # m = 3
