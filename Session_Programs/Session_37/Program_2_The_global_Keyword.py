"""
Session 37 - Program 2: The global Keyword

Modify a global variable from inside a function.

Sample Output:
20

Try also: Starting from count = 0 and setting count = 5 prints 5.
"""

# Program 2: Modify a global variable with 'global'
x = 10

def change():
    global x
    x = 20

change()
print(x)
