"""
Session 24 - Program 2: First Divisible by 7 (using break)

Stop as soon as the first multiple of 7 is found.

Sample Output:
Enter start: 1
Enter end: 20
7

Try also: 10, 30 gives 14.
"""

# Program 2: First number divisible by 7 (break)
start = int(input("Enter start: "))
end = int(input("Enter end: "))
for i in range(start, end + 1):
    if i % 7 == 0:
        print(i)
        break
