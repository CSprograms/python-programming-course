"""
Session 17 - Program 4: Maximum of Two (Workout)

Find the maximum of two numbers using if-else, without the built-in max().

Sample Output:
Enter first number: 10
Enter second number: 5
10

Try also: 3, 7 gives 7.
"""

# Program 4: Maximum of two (no max())
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a >= b:
    largest = a
else:
    largest = b
print(largest)
