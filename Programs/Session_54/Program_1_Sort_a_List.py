"""
Session 54 - Program 1: Sort a List

Sort in ascending and then descending order.

Sample Output:
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
"""

# Program 1: Sort ascending and descending
numbers = [5, 3, 1, 4, 2]
numbers.sort()
print(numbers)               # ascending
numbers.sort(reverse=True)
print(numbers)               # descending
