"""
Session 23 - Program 3: Count Spaces in a String (Workout)

Count how many space characters a string contains.

Sample Output:
Enter a string: Hello World
1

Try also: I love Python gives 2.
"""

# Program 3: Count spaces in a string (for)
s = input("Enter a string: ")
count = 0
for ch in s:
    if ch == " ":
        count += 1
print(count)
