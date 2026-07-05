"""
Session 35 - Program 3: Round Up Currency (Workout)

Round a price up to the next whole rupee.

Sample Output:
Enter the price: 99.45
100

Try also: 250.99 gives 251.
"""

# Program 3: Round a price up to the next rupee
import math

price = float(input("Enter the price: "))
print(math.ceil(price))
