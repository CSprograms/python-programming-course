"""
Session 36 - Program 4: Maximum of Many (Workout)

Find the maximum of a variable number of arguments with *args.

Sample Output:
12

Try also: maximum(1, 2) gives 2.
"""

# Program 4: Maximum of many numbers using *args
def maximum(*numbers):
    big = numbers[0]
    for x in numbers:
        if x > big:
            big = x
    return big

print(maximum(10, 5, 8, 12, 3))
