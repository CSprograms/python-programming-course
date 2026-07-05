"""
Session 50 - Program 4: CSV to List (Workout)

Split a comma-separated string into a list of fields.

Sample Output:
Enter a CSV string: Ravi,21,BCA,90
['Ravi', '21', 'BCA', '90']

Try also: "a,b,c" gives ['a', 'b', 'c'].
"""

# Program 4: Split a CSV string into a list of fields
s = input("Enter a CSV string: ")
fields = s.split(",")
print(fields)
