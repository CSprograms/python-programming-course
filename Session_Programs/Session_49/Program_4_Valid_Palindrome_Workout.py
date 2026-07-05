"""
Session 49 - Program 4: Valid Palindrome (Workout)

Test whether a string reads the same both ways, ignoring case and keeping
only letters and digits. (LeetCode 125.)

Sample Output:
Enter a string: A man a plan a canal: Panama
True

Try also: "race a car" gives False.
"""

# Program 4: Valid palindrome (alphanumeric only, ignore case)
s = input("Enter a string: ")
cleaned = ""
for ch in s:
    if ch.isalnum():
        cleaned += ch.lower()
print(cleaned == cleaned[::-1])
