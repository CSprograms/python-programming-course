"""
Session 40 - Program 1: try-except-else-finally

Read a number safely and always report completion.

Sample Output:
Enter a number: 10
Number is 10. Execution complete.

Try also: "xyz" gives Invalid. Execution complete.
"""

# Program 1: try-except-else-finally
s = input("Enter a number: ")
try:
    n = int(s)
except ValueError:
    print("Invalid.", end=" ")
else:
    print(f"Number is {n}.", end=" ")
finally:
    print("Execution complete.")
