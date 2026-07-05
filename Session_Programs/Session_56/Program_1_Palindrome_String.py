"""
Session 56 - Assignment 4, Program 1: Palindrome String

A string is a palindrome if it reads the same forwards and backwards.

Sample Output:
Enter a string: madam
Palindrome

Try also: "python" gives Not a Palindrome.
"""

# Assignment 1: Check whether a string is a palindrome
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
