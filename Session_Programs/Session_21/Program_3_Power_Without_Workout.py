"""
Session 21 - Program 3: Power Without ** (Workout)

Compute a^b by multiplying a by itself b times.

Sample Output:
Enter base a: 2
Enter exponent b: 5
32

Try also: a = 3, b = 4 gives 81.
"""

# Program 3: Compute a to the power b without **
a = int(input("Enter base a: "))
b = int(input("Enter exponent b: "))
result = 1
count = 0
while count < b:
    result *= a
    count += 1
print(result)
