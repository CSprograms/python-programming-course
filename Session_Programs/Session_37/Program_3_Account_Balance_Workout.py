"""
Session 37 - Program 3: Account Balance (Workout)

Track a bank balance in a global variable across function calls.

Sample Output:
Balance: 800

Try also: Deposit 500 then withdraw 100 gives Balance: 400.
"""

# Program 3: Track a balance with a global variable
balance = 0

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount

deposit(1000)
withdraw(200)
print("Balance:", balance)
