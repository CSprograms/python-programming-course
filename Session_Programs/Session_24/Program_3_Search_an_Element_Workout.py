"""
Session 24 - Program 3: Search an Element (Workout)

Search a list and report the index, or Not Found.

Sample Output:
Found at index 2

Try also: numbers = [1, 2, 3], target = 4 gives Not Found.
"""

# Program 3: Search an element in a list (break)
numbers = [5, 3, 8, 1]
target = 8
found = False
for index in range(len(numbers)):
    if numbers[index] == target:
        print("Found at index", index)
        found = True
        break
if not found:
    print("Not Found")
