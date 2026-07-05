"""
Session 37 - Program 4: Variable Shadowing (Workout)

Use the same name as a local and a global variable, and print both.

Sample Output:
Inside: 5
Outside: 10
"""

# Program 4: Variable shadowing (local hides global)
g = 10

def demo():
    g = 5           # local g shadows the global g
    print("Inside:", g)

demo()
print("Outside:", g)
