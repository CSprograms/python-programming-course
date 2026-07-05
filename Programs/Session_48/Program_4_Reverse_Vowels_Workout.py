"""
Session 48 - Program 4: Reverse Vowels (Workout)

Reverse only the vowels, leaving every other character in place. (LeetCode
345.)

Sample Output:
Enter a string: hello
holle

Try also: "leetcode" gives leotcede.
"""

# Program 4: Reverse only the vowels in a string
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
chars = list(s)
i = 0
j = len(chars) - 1
while i < j:
    if chars[i] not in vowels:
        i += 1
    elif chars[j] not in vowels:
        j -= 1
    else:
        chars[i], chars[j] = chars[j], chars[i]
        i += 1
        j -= 1
print("".join(chars))
