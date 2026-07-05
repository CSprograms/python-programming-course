"""
Session 5 - Program 3: Bill Receipt (Workout)

Print a formatted bill receipt with item name, quantity, unit price and
total amount.

Sample Output:
Item name : Pen
Quantity  : 5
Unit price: 10
Item: Pen, Qty: 5, Total: 50.00
"""

# Program 3: Bill receipt
item  = input("Item name : ")
qty   = int(input("Quantity  : "))
price = float(input("Unit price: "))
total = qty * price
print(f"Item: {item}, Qty: {qty}, Total: {total:.2f}")
