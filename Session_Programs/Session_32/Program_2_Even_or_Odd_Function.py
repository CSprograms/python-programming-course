"""
Session 32 - Program 2: Even or Odd Function

Return whether a number is even or odd.

Sample Output:
Enter a number: 10
Even

Try also: 11 gives Odd.
"""

# Program 2: Check even or odd using a function
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(even_odd(num))
