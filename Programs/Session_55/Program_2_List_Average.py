"""
Session 55 - Program 2: List Average

Pass a list to a function that returns its average.

Sample Output:
20.0

Try also: [5, 15, 25, 35] also gives 20.0.
"""

# Program 2: Average of a list (passed to a function)
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([10, 20, 30]))
