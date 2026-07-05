"""
Session 21 - Program 4: Climbing Stairs (Workout)

Count the ways to climb n steps taking 1 or 2 steps at a time. The answer
follows the Fibonacci pattern. (LeetCode 70.)

Sample Output:
Enter number of steps n: 3
3

Try also: n = 5 gives 8.
"""

# Program 4: Climbing stairs (1 or 2 steps)
n = int(input("Enter number of steps n: "))
a = 1    # ways to reach the ground
b = 1    # ways to reach step 1
count = 1
while count < n:
    a, b = b, a + b
    count += 1
print(b)
