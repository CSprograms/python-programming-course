"""
Session 2 - Program 1: List Keywords

List Python keywords using the keyword module.

Sample Output:
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
 'while', 'with', 'yield']
Total keywords: 35
"""

# Program 1: List all Python keywords
import keyword
print(keyword.kwlist)
print("Total keywords:", len(keyword.kwlist))
