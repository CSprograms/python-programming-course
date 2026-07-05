"""
Session 56 - Assignment 4, Program 5: Merge Lists Alternately

Build one list by taking items from two lists in turn.

Sample Output:
[1, 4, 2, 5, 3, 6]

Try also: ['a', 'b'] and ['x', 'y'] give ['a', 'x', 'b', 'y'].
"""

# Assignment 5: Merge two lists alternately
a = [1, 2, 3]
b = [4, 5, 6]
result = []
for i in range(len(a)):
    result.append(a[i])
    result.append(b[i])
print(result)
