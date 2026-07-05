"""
Session 20 - Program 4: GCD Using While (Workout)

Find the GCD (Greatest Common Divisor) of two positive integers using a
while loop, applying Euclid's method via repeated subtraction.

Sample Output:
Enter first number: 12
Enter second number: 18
6

Try also: 48, 60 gives 12.
"""

# Program 4: GCD using repeated subtraction (while)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)
