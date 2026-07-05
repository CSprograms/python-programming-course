"""
Session 22 - Program 3: Sum 1 to N (Workout)

Add the first N natural numbers.

Sample Output:
Enter N: 10
55

Try also: N = 5 gives 15.
"""

# Program 3: Sum of first N natural numbers (for)
N = int(input("Enter N: "))
total = 0
for i in range(1, N + 1):
    total += i
print(total)
