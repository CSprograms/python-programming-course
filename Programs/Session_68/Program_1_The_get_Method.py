"""
Session 68 - Program 1: The get Method

Safely retrieve a value, even when the key is absent.

Sample Output:
85
None
"""

# Program 1: Safely retrieve a value with get()
d = {"Ravi": 85}
print(d.get("Ravi"))
print(d.get("Sita"))
