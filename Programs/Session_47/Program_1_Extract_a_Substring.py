"""
Session 47 - Program 1: Extract a Substring

Use positive-index slicing to pull out part of a string.

Sample Output:
Enter a string: Programming
Enter start index: 0
Enter end index: 7
Program

Try also: "Python", 2, 6 gives thon.
"""

# Program 1: Extract a substring using s[start:end]
s = input("Enter a string: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
print(s[start:end])
