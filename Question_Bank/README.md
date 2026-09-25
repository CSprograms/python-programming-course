# Question Bank (previous-year questions)

This folder is the source for the **Question Bank** page of the Session Viewer (`/#qb`).

| File | Purpose |
|---|---|
| `QuestionBank_Analysis.xlsx` | The full analysis of the end-semester papers (November 2023 to November 2025): every question with Unit, KL, CO, PO, PSO and its syllabus status. Kept for reference. |
| `question_bank.csv` | **In-syllabus questions only**: one row per question per exam. `build_data.py` reads this file. |

## What was left out

The 22 questions marked **OUT OF SYLLABUS** in the analysis (File Handling and Arrays) are not
in `question_bank.csv`: 11 from Part A, 5 from Part B and 6 from Part C.

The **PARTIAL** question (April 2025, Part B, Q19: "Explain the following (i) append () (ii) write lines ().")
keeps only its in-syllabus part, as the analysis recommends. It appears as "Explain the append() method of a
list with an example." (Unit IV, CO4), with a note on the page saying it was reframed.

## CSV columns

`Part` (A/B/C), `Unit` (I–V; use `IV/V` for a question spanning two units), `Question`, `KL`, `CO`, `PO`,
`PSO`, `Exam` (for example `November 2025`), `QNo`, `Note` (optional, shown under the question).

## Adding a new question paper

1. Add one row per in-syllabus question to `question_bank.csv` (Excel works; save as **CSV UTF-8**).
2. Run `python build_data.py`. The same question in another exam is merged automatically and shown
   as "Asked 2×" (case, spacing and punctuation are ignored when matching).
3. Commit `question_bank.csv` and `web-app/data/question_bank.json`, then push.
