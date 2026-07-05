"""
Session 38 - Program 4: Filter Positive (Workout)

Extract the positive numbers from a list using filter().

Sample Output:
[5, 8]

Try also: [1, -2, 3, -4] gives [1, 3].
"""

# Program 4: Extract positive numbers using filter()
numbers = [-3, 5, -1, 8, 0]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)
