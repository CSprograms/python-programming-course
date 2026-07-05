"""
Session 51 - Program 4: Single Number (Workout)

Every value appears twice except one; find the one. The trick: XOR of a
value with itself is 0, so the pairs cancel out. (LeetCode 136.)

Sample Output:
1

Try also: [4, 1, 2, 1, 2] gives 4.
"""

# Program 4: Find the element that appears only once
numbers = [2, 2, 1]
result = 0
for x in numbers:
    result ^= x      # XOR cancels equal pairs
print(result)
