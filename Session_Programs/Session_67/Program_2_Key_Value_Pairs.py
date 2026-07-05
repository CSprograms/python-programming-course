"""
Session 67 - Program 2: Key-Value Pairs

Print each pair using items().

Sample Output:
a-1, b-2

Try also: {"Tamil": 80, "English": 75} gives Tamil-80, English-75.
"""

# Program 2: Print all key-value pairs using items()
d = {"a": 1, "b": 2}
pairs = []
for key, value in d.items():
    pairs.append(f"{key}-{value}")
print(", ".join(pairs))
