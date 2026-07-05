"""
Session 24 - Program 1: Even Numbers (using continue)

Skip the odd numbers and print only the even ones.

Sample Output:
Enter start: 1
Enter end: 10
2 4 6 8 10

Try also: 1, 5 gives 2 4.
"""

# Program 1: Even numbers in a range (continue)
start = int(input("Enter start: "))
end = int(input("Enter end: "))
for i in range(start, end + 1):
    if i % 2 != 0:
        continue          # skip odd numbers
    print(i, end=" ")
print()
