"""
Session 52 - Program 1: Largest in a List

Find the largest element without using max().

Sample Output:
8

Try also: [10, 4, 15, 6] gives 15.
"""

# Program 1: Largest element without max()
numbers = [3, 7, 2, 8, 5]
largest = numbers[0]
for x in numbers:
    if x > largest:
        largest = x
print(largest)
