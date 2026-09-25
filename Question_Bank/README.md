# Question Bank (previous-year questions)

This folder is the source for the **Question Bank** pages of the Session Viewer: an overview at `/#qb`, one page
per unit (`/#qb/unit-I` … `/#qb/unit-V`), and Part A / B / C tabs inside each (`/#qb/unit-I/part-A`).

It holds **15 plain-text files**, one for each unit and part:

```
Unit_1_Part_A.txt   Unit_1_Part_B.txt   Unit_1_Part_C.txt     Unit I   - Introduction to Python
Unit_2_Part_A.txt   Unit_2_Part_B.txt   Unit_2_Part_C.txt     Unit II  - Flow Control
Unit_3_Part_A.txt   Unit_3_Part_B.txt   Unit_3_Part_C.txt     Unit III - Functions and Exception Handling
Unit_4_Part_A.txt   Unit_4_Part_B.txt   Unit_4_Part_C.txt     Unit IV  - Strings and Lists
Unit_5_Part_A.txt   Unit_5_Part_B.txt   Unit_5_Part_C.txt     Unit V   - Tuples and Dictionaries
```

The file name decides the unit and part. Questions appear on the website in the order they are written.

## Format of a question

~~~text
=== Q1
Question: What is recursion?
KL: K1
CO: CO3
PO: PO1
PSO: PSO1
Asked: November 2023 Q6; April 2025 Q6
Answer:
Recursion is a technique in which a function calls itself to solve a smaller
instance of the same problem. Every recursive function needs a base case.

```python
def factorial(n):
    # base case
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120
```

Example: factorial(5) = 5 x 4 x 3 x 2 x 1 = 120.
~~~

Rules:

- Each question starts with a line `=== Q<number>`. The numbers are for your reference only.
- `Question:` is required. `KL`, `CO`, `PO`, `PSO` and `Asked` are optional, and so are:
  - `Note:` a remark shown under the question (for example why a question was reframed);
  - `Also in unit:` for a question that spans two units (for example `Also in unit: V`), so that it
    also appears on that unit's page.
- `Asked:` lists every exam the question appeared in, as `Month Year Q<number>`, separated by `;`.
  A question listed with two or more exams gets an "Asked 2×" badge on the site.
- **`Answer:` comes last.** Everything after it, up to the next `=== Q` line, is the answer, kept
  exactly as written (so Python `#` comments inside code are safe).
  - A blank line starts a new paragraph.
  - Put code between a line ```` ```python ```` and a line ```` ``` ```` to show it as highlighted code.
  - Put syntax templates or program output between ```` ```text ```` and ```` ``` ````; they are shown in a light box.
    The convention used in the answers is a line `Output:` followed by a ```` ```text ```` block.
  - A short first line of a paragraph with no full stop (for example `1. if-else statement` or `Syntax:`)
    is shown in bold as a small heading.
  - Leave the answer empty if it is not ready. The website then shows the question only; once you add
    an answer, an **Answer** link appears under the question.
- Lines starting with `#` are comments only in the header at the top of the file (before `=== Q1`).
- Save the files as **UTF-8** (Notepad: *Save as → Encoding: UTF-8*).

## After editing

```bash
python build_data.py
```

This checks all 15 files and rewrites `web-app/data/question_bank.json`. If something is wrong, it stops with the
file name, line number and the problem (for example an unknown field, or the same question written twice in one
file). Commit the `.txt` files and `web-app/data/question_bank.json`, then push. Netlify also runs
`build_data.py` on every deploy.

## What was left out

These files were created from the analysis of the end-semester papers (November 2023 to November 2025). The
22 questions marked **OUT OF SYLLABUS** (File Handling and Arrays) are not included.

The partly out-of-syllabus question (April 2025, Part B, Q19: "Explain the following (i) append () (ii) write lines ().")
is kept as "Explain the append() method of a list with an example." in `Unit_4_Part_B.txt`, with a note saying it was reframed.
Questions asked in more than one exam are written once, with all their exams listed on the `Asked:` line.
