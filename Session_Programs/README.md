# Python Programming - Session & Workout Programs

Course: UCAM11I - Python Programming, BCA Section 1, Sri Sankara Arts and Science College.

This folder holds every runnable Python program from the 75-session course, one
subfolder per session (`Session_01` ... `Session_75`), extracted from the
Lecture Notes in `../LectureNotes/`.

## Layout

- **Teaching sessions** (e.g. `Session_01`-`Session_10`, `Session_16`-`Session_25`, ...):
  4 files each - Program 1-2 are the Session Programs demonstrated in class,
  Program 3-4 are the Workout Programs for practice.
- **Assignment sessions** (`Session_11`, `26`, `41`, `56`, `71`): 5 solved
  assignment programs for that unit.
- **Class Test sessions** (`Session_14`, `29`, `44`, `59`, `74`): the solved
  programming question from that unit's class test.
- **Seminar sessions** (e.g. `Session_12`, `13`, ...) and **Discussion sessions**
  (e.g. `Session_15`, `30`, ...): no programs - contains a `README.md` pointing
  back to the Session Plan for topic details.

## File format

Each program file has a docstring with the session/program number, a short
description, and the documented sample output, followed by the runnable code:

```python
"""
Session 1 - Program 3: Print Banner (Workout)

Print a banner with the word PYTHON between two rows of asterisks ...

Sample Output:
**********
* PYTHON *
**********
"""

print("**********")
...
```

## Coverage

- 75 session folders (matches the 75 one-hour sessions in the Session Plan)
- 230 individual `.py` program files
- 15 sessions are Seminar/Discussion with no code

All 230 files were verified to parse with no syntax errors, and a cross-unit
sample was executed against its documented sample input/output.
