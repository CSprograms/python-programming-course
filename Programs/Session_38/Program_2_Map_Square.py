"""
Session 38 - Program 2: Map Square

Square every element of a list with map().

Sample Output:
[1, 4, 9, 16]

Try also: [5, 6, 7] gives [25, 36, 49].
"""

# Program 2: Square each element using map()
numbers = [1, 2, 3, 4]
squares = list(map(lambda n: n * n, numbers))
print(squares)
