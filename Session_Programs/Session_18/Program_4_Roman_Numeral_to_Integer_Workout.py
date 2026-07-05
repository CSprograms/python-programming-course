"""
Session 18 - Program 4: Roman Numeral to Integer (Workout)

Convert a single Roman numeral character to its value. (LeetCode 13, single
symbol.)

Sample Output:
Enter a Roman numeral (I,V,X,L,C,D,M): V
5

Try also: X gives 10.
"""

# Program 4: Roman numeral character to integer
ch = input("Enter a Roman numeral (I,V,X,L,C,D,M): ")
if ch == "I":
    print(1)
elif ch == "V":
    print(5)
elif ch == "X":
    print(10)
elif ch == "L":
    print(50)
elif ch == "C":
    print(100)
elif ch == "D":
    print(500)
elif ch == "M":
    print(1000)
else:
    print("Invalid")
