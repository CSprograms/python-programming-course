"""
Session 2 - Program 3: Keyword Check (Workout)

Use the keyword module to check whether a name is a reserved keyword.

Sample Output:
True

Try also: name = "hello" gives False.
"""

# Program 3: Is the name a keyword?
import keyword
name = "if"
print(keyword.iskeyword(name))
