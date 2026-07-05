"""
Session 59 - Class Test 4, Q3: Program - reverse a string without built-in functions.

Build the result by placing each character in front of what has been
collected so far.

Sample Output:
Enter a string: Python
nohtyP
"""

# Class Test: reverse a string without built-in functions
s = input("Enter a string: ")
result = ""
for ch in s:
    result = ch + result      # prepend each character
print(result)
