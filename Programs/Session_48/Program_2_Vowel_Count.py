"""
Session 48 - Program 2: Vowel Count

Count the vowels in a string.

Sample Output:
Enter a string: Hello World
3

Try also: "Programming" also gives 3.
"""

# Program 2: Count the vowels in a string
s = input("Enter a string: ")
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print(count)
