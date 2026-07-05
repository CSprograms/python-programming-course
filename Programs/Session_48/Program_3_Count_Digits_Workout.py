"""
Session 48 - Program 3: Count Digits (Workout)

Count how many digit characters a string contains.

Sample Output:
Enter a string: Hello123World45
5

Try also: "abc" gives 0.
"""

# Program 3: Count the digit characters in a string
s = input("Enter a string: ")
count = 0
for ch in s:
    if ch.isdigit():
        count += 1
print(count)
