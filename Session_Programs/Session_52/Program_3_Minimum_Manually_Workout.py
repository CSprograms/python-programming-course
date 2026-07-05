"""
Session 52 - Program 3: Minimum Manually (Workout)

Find the smallest element without using min().

Sample Output:
2

Try also: [10, 4, 15, 6] gives 4.
"""

# Program 3: Minimum element without min()
numbers = [3, 7, 2, 8, 5]
smallest = numbers[0]
for x in numbers:
    if x < smallest:
        smallest = x
print(smallest)
