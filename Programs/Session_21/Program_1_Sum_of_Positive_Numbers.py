"""
Session 21 - Program 1: Sum of Positive Numbers

Keep adding numbers until a negative number is entered (the sentinel).

Sample Output:
Enter a number: 3
Enter a number: 4
Enter a number: 5
Enter a number: -1
12

Try also: 2, 4, 6, -5 gives 12.
"""

# Program 1: Sum numbers until a negative is entered
total = 0
num = int(input("Enter a number: "))
while num >= 0:
    total += num
    num = int(input("Enter a number: "))
print(total)
