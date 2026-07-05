"""
Session 56 - Assignment 4, Program 3: Sort a List Without sort()

Sort in ascending order using a simple bubble sort.

Sample Output:
[1, 2, 3, 4, 5]

Try also: [10, 4, 15, 6] gives [4, 6, 10, 15].
"""

# Assignment 3: Sort a list ascending without sort() (bubble sort)
numbers = [5, 3, 1, 4, 2]
n = len(numbers)
for i in range(n):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)
