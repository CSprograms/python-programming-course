"""
Session 71 - Assignment 5, Program 1: Student Database

Display the students who scored above 80.

Sample Output:
Ravi, Ram

Try also: {"A": 75, "B": 95, "C": 82} gives B, C.
"""

# Assignment 1: Students who scored above 80
marks = {"Ravi": 85, "Sita": 72, "Ram": 90}
result = []
for name, score in marks.items():
    if score > 80:
        result.append(name)
print(", ".join(result))
