"""
Session 62 - Program 4: Sum of Tuple Squares (Workout)

Add up the squares of all elements.

Sample Output:
14

Try also: (2, 4) gives 20.
"""

# Program 4: Sum of squares of tuple elements
t = (1, 2, 3)
total = 0
for x in t:
    total += x * x
print(total)
