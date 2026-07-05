"""
Session 24 - Program 4: Skip Multiples of 5 (Workout)

Print 1 to N but skip every multiple of 5.

Sample Output:
Enter N: 12
1 2 3 4 6 7 8 9 11 12

Try also: N = 7 gives 1 2 3 4 6 7.
"""

# Program 4: Print 1..N skipping multiples of 5 (continue)
N = int(input("Enter N: "))
for i in range(1, N + 1):
    if i % 5 == 0:
        continue
    print(i, end=" ")
print()
