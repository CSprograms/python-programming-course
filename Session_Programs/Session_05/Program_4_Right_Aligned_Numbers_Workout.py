"""
Session 5 - Program 4: Right-Aligned Numbers (Workout)

Print three numbers right-justified in a field of width~8.

Sample Output:
       5     100    1234
"""

# Program 4: right-justified numbers (width 8)
nums = [5, 100, 1234]
for n in nums:
    print(f"{n:>8}", end="")
print()
