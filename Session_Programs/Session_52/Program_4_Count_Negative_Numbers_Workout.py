"""
Session 52 - Program 4: Count Negative Numbers (Workout)

Count how many elements are negative.

Sample Output:
3

Try also: [1, 2, 3] gives 0.
"""

# Program 4: Count negative numbers
numbers = [-3, 5, -1, 8, -7]
count = 0
for x in numbers:
    if x < 0:
        count += 1
print(count)
