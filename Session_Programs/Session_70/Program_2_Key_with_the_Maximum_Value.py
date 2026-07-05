"""
Session 70 - Program 2: Key with the Maximum Value

Find which key holds the largest value.

Sample Output:
b

Try also: {"Ravi": 80, "Sita": 95, "Ram": 85} gives Sita.
"""

# Program 2: Key with the maximum value
d = {"a": 5, "b": 9, "c": 3}
max_key = max(d, key=d.get)
print(max_key)
