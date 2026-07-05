"""
Session 69 - Program 2: Character Frequency

Count how many times each character appears.

Sample Output:
Enter a string: banana
{'b': 1, 'a': 3, 'n': 2}

Try also: "hello" gives {'h': 1, 'e': 1, 'l': 2, 'o': 1}.
"""

# Program 2: Frequency of each character
s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
