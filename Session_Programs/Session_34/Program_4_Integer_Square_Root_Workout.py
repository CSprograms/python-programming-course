"""
Session 34 - Program 4: Integer Square Root (Workout)

Return the whole-number part of the square root. (LeetCode 69.)

Sample Output:
Enter a non-negative integer: 8
2

Try also: 4 gives 2 as well, since sqrt(4)=2.
"""

# Program 4: Integer square root (floor of the square root)
import math

x = int(input("Enter a non-negative integer: "))
print(int(math.sqrt(x)))
