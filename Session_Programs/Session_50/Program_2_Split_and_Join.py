"""
Session 50 - Program 2: Split and Join

Split a sentence into words, then join them back with a double-hyphen
separator.

Sample Output:
Enter a sentence: Hello Python World
Hello--Python--World

Try also: "I love coding" gives I--love--coding.
"""

# Program 2: Split into words and join with "--"
s = input("Enter a sentence: ")
words = s.split()
print("--".join(words))
