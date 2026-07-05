"""
Session 39 - Program 4: Index Error Handler (Workout)

Safely read a list element by index, catching IndexError.

Sample Output:
2
Index out of range
"""

# Program 4: Safely access a list element by index
def get_item(lst, idx):
    try:
        return lst[idx]
    except IndexError:
        return "Index out of range"

print(get_item([1, 2, 3], 1))
print(get_item([1, 2, 3], 5))
