"""
Session 18 - Program 1: Student Grade

Assign a grade from the average marks.

Sample Output:
Enter average marks: 85
Grade A

Try also: 45 gives Grade D (it is below 50 but at least 40).
"""

# Program 1: Grade from average marks
marks = int(input("Enter average marks: "))
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")
