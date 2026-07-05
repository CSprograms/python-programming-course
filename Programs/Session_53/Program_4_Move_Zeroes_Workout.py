"""
Session 53 - Program 4: Move Zeroes (Workout)

Move every zero to the end while keeping the order of the non-zero items.
(LeetCode 283.)

Sample Output:
[1, 3, 12, 0, 0]

Try also: [0] stays [0].
"""

# Program 4: Move all zeroes to the end (in place)
numbers = [0, 1, 0, 3, 12]
pos = 0                          # next slot for a non-zero value
for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[pos] = numbers[i]
        pos += 1
while pos < len(numbers):
    numbers[pos] = 0
    pos += 1
print(numbers)
