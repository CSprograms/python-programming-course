"""
Session 64 - Program 3: Student Records (Workout)

Store records as a list of tuples and print each one.

Sample Output:
Ravi:85, Sita:90

Try also: [("A", 75), ("B", 82)] gives A:75, B:82.
"""

# Program 3: Store student records as a list of tuples
records = [("Ravi", 85), ("Sita", 90)]
output = []
for name, mark in records:
    output.append(f"{name}:{mark}")
print(", ".join(output))
