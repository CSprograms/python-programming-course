"""
Session 37 - Program 1: Local vs Global

Show that a local variable is separate from a global one of the same name.

Sample Output:
Inside: 5
Outside: 10
"""

# Program 1: Local vs global scope
x = 10              # global variable

def show():
    x = 5           # local variable (separate from the global x)
    print("Inside:", x)

show()
print("Outside:", x)
