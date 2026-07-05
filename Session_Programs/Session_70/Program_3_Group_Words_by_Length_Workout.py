"""
Session 70 - Program 3: Group Words by Length (Workout)

Group a list of words into a dictionary keyed by word length.

Sample Output:
{2: ['hi'], 3: ['bye', 'cat'], 4: ['door']}

Try also: ["apple", "fig", "kiwi"] gives {5: ['apple'], 3: ['fig'], 4: ['kiwi']}.
"""

# Program 3: Group words by their length
words = ["hi", "bye", "cat", "door"]
groups = {}
for word in words:
    length = len(word)
    if length not in groups:
        groups[length] = []
    groups[length].append(word)
print(groups)
