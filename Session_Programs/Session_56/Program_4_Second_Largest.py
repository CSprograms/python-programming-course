"""
Session 56 - Assignment 4, Program 4: Second Largest

Find the second largest element in a list.

Sample Output:
20

Try also: [1, 2, 3, 4, 5] gives 4.
"""

# Assignment 4: Second largest element
numbers = [10, 5, 20, 15, 25]
largest = max(numbers)
second = -float("inf")
for x in numbers:
    if x != largest and x > second:
        second = x
print(second)
