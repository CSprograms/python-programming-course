"""
Session 54 - Program 4: Find Index or -1 (Workout)

Return the index of an element, or -1 when it is not present.

Sample Output:
1

Try also: target = 50 gives -1.
"""

# Program 4: Find the index of an element, or -1 if absent
numbers = [10, 20, 30]
target = 20
if target in numbers:
    print(numbers.index(target))
else:
    print(-1)
