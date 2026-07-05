"""
Session 64 - Program 4: Sort Tuples by Mark (Workout)

Sort a list of (name, mark) tuples by mark, highest first.

Sample Output:
[('Sita', 90), ('Ravi', 85), ('Ram', 75)]

Try also: [("A", 60), ("B", 80), ("C", 70)] gives [('B', 80), ('C', 70), ('A', 60)].
"""

# Program 4: Sort (name, mark) tuples by mark, descending
records = [("Ravi", 85), ("Sita", 90), ("Ram", 75)]
records.sort(key=lambda r: r[1], reverse=True)
print(records)
