"""
Session 33 - Program 4: Recursive Sum (Workout)

Add the first N natural numbers using recursion.

Sample Output:
15

Try also: rec_sum(10) gives 55.
"""

# Program 4: Sum of first N natural numbers using recursion
def rec_sum(n):
    if n == 0:
        return 0
    return n + rec_sum(n - 1)

print(rec_sum(5))
