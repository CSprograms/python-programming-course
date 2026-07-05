"""
Session 51 - Program 3: Product of Elements (Workout)

Multiply all the numbers in a list together.

Sample Output:
24

Try also: [5, 5, 5] gives 125.
"""

# Program 3: Product of all elements in a list
numbers = [1, 2, 3, 4]
product = 1
for x in numbers:
    product *= x
print(product)
