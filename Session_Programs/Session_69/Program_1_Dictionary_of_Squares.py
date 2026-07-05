"""
Session 69 - Program 1: Dictionary of Squares

Build a dictionary of numbers and their squares.

Sample Output:
Enter N: 5
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

Try also: N = 3 gives {1: 1, 2: 4, 3: 9}.
"""

# Program 1: Dictionary of squares using comprehension
N = int(input("Enter N: "))
squares = {i: i * i for i in range(1, N + 1)}
print(squares)
