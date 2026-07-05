"""
Session 18 - Program 2: Simple Calculator

Perform one of the four basic operations chosen by the user.

Sample Output:
Enter first number: 10
Enter second number: 5
Enter operator (+, -, *, /): +
15

Try also: 20, 4, / gives 5.0 (division always produces a float).
"""

# Program 2: Simple calculator (+, -, *, /)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")
