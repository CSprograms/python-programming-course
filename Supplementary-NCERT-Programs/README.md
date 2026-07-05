# Supplementary NCERT Programs

92 supplementary practice programs extracted from `NCERT_Programs.tex`, a
compendium of NCERT-aligned Computer Science / Informatics Practices
exercises (Classes XI-XII) used alongside the main course. These are
**supplementary** to [`../Session_Programs/`](../Session_Programs/) (the
75-session course itself) -- extra practice material mapped to the same
units, not part of the graded session plan.

Only the runnable Python solutions were extracted; the original NCERT
exercise/question text is not reproduced in these files. Each program's
docstring gives a short, code-derived description instead.

## Layout

One folder per unit, `Unit_01` ... `Unit_11`, each with numbered
`Program_NN_description.py` files:

| Unit | Title                                  | Programs |
|------|-----------------------------------------|----------|
| 1    | Getting Started with Python             | 5        |
| 2    | Flow of Control                         | 10       |
| 3    | Functions and Modules                   | 12       |
| 4    | Strings                                 | 10       |
| 5    | Lists                                   | 12       |
| 6    | Tuples and Dictionaries                 | 11       |
| 7    | Understanding Data and Statistics       | 0 (conceptual only, see `Unit_07/README.md`) |
| 8    | Introduction to NumPy                   | 13       |
| 9    | Data Handling using Pandas              | 8        |
| 10   | Plotting Data using Matplotlib          | 5        |
| 11   | Exception Handling                      | 6        |

**Total: 92 programs across 10 code-bearing units.**

## Multi-part exercises

Some NCERT exercises build a data structure in one step and then query/modify
it in later steps (e.g. a Unit 8 NumPy array created in one program, then
sliced and operated on in the next few). Where a program depends on
variables set up earlier in the same unit, the required setup code is
automatically included at the top of the file (with a docstring note saying
so) so every file runs standalone -- you never need to run another file
first.

## Known caveats (by design, not bugs)

A handful of programs behave unusually on purpose or need something this
repository doesn't include; each has a `Note:` line in its docstring:

- **External data files** -- a few Unit 8 (NumPy) and Unit 10 (Matplotlib)
  programs load `Iris.txt` or `Marks.csv` from the NCERT dataset, which
  isn't bundled here. Supply your own copy at the referenced path to run
  them.
- **Intentional error demonstrations** -- a couple of programs (Unit 4
  string methods, Unit 6 tuples) deliberately end in a `ValueError` /
  `TypeError` to illustrate a common mistake, exactly as annotated in the
  original comments.
- **Two Unit 8 array-shape exercises** (`Program_03`, and `Program_04`/`05`)
  reproduce a shape mismatch present in the original source material itself
  (e.g. adding a 3x3 array to a 3x5 array) -- this is inherited from
  `NCERT_Programs.tex` as written, not introduced by this extraction.

## Verification

All 92 files were checked with `ast.parse` (0 syntax errors) and executed;
every non-interactive, no-external-file program runs cleanly except the
known cases listed above.
