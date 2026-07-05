"""
Session 56 - Assignment 4, Program 2: Vowel and Consonant Count

Count vowels and consonants, ignoring spaces and punctuation.

Sample Output:
Enter a string: Hello World
Vowels = 3, Consonants = 7

Try also: "Python" gives Vowels = 1, Consonants = 5.
"""

# Assignment 2: Count vowels and consonants
s = input("Enter a string: ")
vowels = 0
consonants = 0
for ch in s:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1
print(f"Vowels = {vowels}, Consonants = {consonants}")
