"""
Session 21 - Program 2: Reverse a Number

Build the reversed number one digit at a time.

Sample Output:
Enter a number: 1234
4321

Try also: 567 gives 765.
"""

# Program 2: Reverse the digits of a number
n = int(input("Enter a number: "))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)
