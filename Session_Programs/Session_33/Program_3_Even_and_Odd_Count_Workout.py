"""
Session 33 - Program 3: Even and Odd Count (Workout)

Return how many even and how many odd numbers a list contains.

Sample Output:
even=3, odd=3

Try also: [10, 15, 20, 25] gives even=2, odd=2.
"""

# Program 3: Count even and odd numbers in a list
def count_even_odd(numbers):
    even = 0
    odd = 0
    for x in numbers:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

e, o = count_even_odd([1, 2, 3, 4, 5, 6])
print(f"even={e}, odd={o}")
