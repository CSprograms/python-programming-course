"""
Session 20 - Program 2: Sum of Digits

Add up the digits of a number by repeatedly taking the last digit.

Sample Output:
Enter a number: 123
6

Try also: 456 gives 15.
"""

# Program 2: Sum of digits
n = int(input("Enter a number: "))
total = 0
while n > 0:
    total += n % 10      # add the last digit
    n //= 10             # drop the last digit
print(total)
