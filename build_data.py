#!/usr/bin/env python3
"""
Builds the data files for the static Session Viewer web app:

* web-app/data/sessions.json       from Session_Programs/ (docstring + code)
* web-app/data/question_bank.json  from Question_Bank/question_bank.csv
                                   (previous-year questions, in syllabus only)
"""
import ast
import csv
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
SESSIONS_DIR = os.path.join(ROOT, "Session_Programs")
OUT_PATH = os.path.join(ROOT, "web-app", "data", "sessions.json")
QB_CSV = os.path.join(ROOT, "Question_Bank", "question_bank.csv")
QB_OUT_PATH = os.path.join(ROOT, "web-app", "data", "question_bank.json")

UNITS = [
    {"number": "I", "title": "Introduction to Python", "start": 1, "end": 15},
    {"number": "II", "title": "Flow Control", "start": 16, "end": 30},
    {"number": "III", "title": "Functions and Exception Handling", "start": 31, "end": 45},
    {"number": "IV", "title": "Strings and Lists", "start": 46, "end": 60},
    {"number": "V", "title": "Tuples and Dictionaries", "start": 61, "end": 75},
]


def unit_for_session(n):
    for u in UNITS:
        if u["start"] <= n <= u["end"]:
            return u["number"]
    return None


def parse_program_file(filepath):
    """Parse a .py file: return (docstring_text, code_text).

    * "utf-8-sig" strips a byte-order mark that Windows editors (Notepad,
      some VS Code settings) may add; ast.parse() rejects a leading BOM.
    * Text mode with universal newlines turns CRLF (Windows) into LF.
    * Only a real module docstring is removed from the displayed code; a
      file that starts with an ordinary expression (e.g. print(...)) keeps it.
    """
    with open(filepath, "r", encoding="utf-8-sig") as f:
        source = f.read()
    try:
        tree = ast.parse(source, filename=filepath)
    except SyntaxError as exc:
        rel = os.path.relpath(filepath, ROOT)
        raise SystemExit(
            "ERROR: syntax error in {} (line {}): {}".format(rel, exc.lineno, exc.msg)
        )
    docstring = ast.get_docstring(tree)
    code = source
    if docstring is not None:
        end_lineno = getattr(tree.body[0], "end_lineno", None)
        if end_lineno is not None:
            lines = source.split("\n")
            code = "\n".join(lines[end_lineno:])
    return docstring, code.strip("\n")


def extract_fields(docstring):
    """Pull header/title/description/sample_output/try_also out of a
    cleaned module docstring following the course's documented format."""
    if not docstring:
        return {
            "header": "",
            "title": "Untitled",
            "description": "",
            "sample_output": None,
            "try_also": None,
        }
    text = docstring.strip("\n")
    lines = text.split("\n")
    header = lines[0].strip()
    rest = "\n".join(lines[1:])

    marker = "Sample Output:"
    if marker in rest:
        before, after = rest.split(marker, 1)
        description = before.strip("\n").strip()
        after = after.lstrip("\n")
        m = re.search(r"\n\s*\nTry also:(.*)", after, re.S)
        if m:
            sample_output = after[: m.start()].rstrip("\n")
            try_also = m.group(1).strip()
        else:
            sample_output = after.rstrip("\n")
            try_also = None
    else:
        description = rest.strip()
        sample_output = None
        try_also = None

    title = header.split(":", 1)[1].strip() if ":" in header else header
    return {
        "header": header,
        "title": title,
        "description": description,
        "sample_output": sample_output,
        "try_also": try_also,
    }


def classify_session(header_text, has_programs):
    if not has_programs:
        return None  # determined from README instead
    h = header_text.lower()
    if "class test" in h:
        return "class-test"
    if "assignment" in h:
        return "assignment"
    return "teaching"


def natural_program_key(filename):
    m = re.match(r"Program_(\d+)_", filename)
    return int(m.group(1)) if m else 0


def build():
    sessions_out = {}

    if not os.path.isdir(SESSIONS_DIR):
        raise SystemExit("ERROR: folder not found: {}".format(SESSIONS_DIR))

    # Only real session folders (Session_01 ... Session_75); ignore anything
    # else such as README.md or a stray "Session_Plan" folder.
    session_dirs = sorted(
        (
            d for d in os.listdir(SESSIONS_DIR)
            if re.fullmatch(r"Session_\d+", d)
            and os.path.isdir(os.path.join(SESSIONS_DIR, d))
        ),
        key=lambda d: int(d.split("_")[1]),
    )

    for dirname in session_dirs:
        session_num = int(dirname.split("_")[1])
        session_path = os.path.join(SESSIONS_DIR, dirname)
        py_files = sorted(
            (f for f in os.listdir(session_path) if f.endswith(".py")),
            key=lambda f: (natural_program_key(f), f),
        )

        entry = {
            "number": session_num,
            "unit": unit_for_session(session_num),
            "programs": [],
        }

        if not py_files:
            # Seminar / Discussion session — read README.md for the note
            readme_path = os.path.join(session_path, "README.md")
            note = ""
            session_type = "note"
            if os.path.exists(readme_path):
                with open(readme_path, "r", encoding="utf-8-sig") as f:
                    readme_text = f.read()
                m = re.search(r"This is a \*\*(.+?)\*\*", readme_text)
                if m:
                    label = m.group(1)
                    if "seminar" in label.lower():
                        session_type = "seminar"
                    elif "discussion" in label.lower():
                        session_type = "discussion"
                body_lines = [
                    ln for ln in readme_text.split("\n")
                    if ln.strip() and not ln.strip().startswith("#")
                ]
                note = "\n".join(body_lines).strip()
            entry["type"] = session_type
            entry["note"] = note
            sessions_out[str(session_num)] = entry
            continue

        session_type = "teaching"
        for fname in py_files:
            fpath = os.path.join(session_path, fname)
            docstring, code = parse_program_file(fpath)
            fields = extract_fields(docstring)
            t = classify_session(fields["header"], True)
            if t:
                session_type = t
            entry["programs"].append(
                {
                    "file": fname,
                    "title": fields["title"],
                    "header": fields["header"],
                    "description": fields["description"],
                    "sample_output": fields["sample_output"],
                    "try_also": fields["try_also"],
                    "code": code,
                }
            )

        entry["type"] = session_type
        sessions_out[str(session_num)] = entry

    data = {
        "course": {
            "code": "UCAM11I",
            "title": "Python Programming",
            "institution": "Sri Sankara Arts and Science College (Autonomous), Enathur",
            "section": "BCA Section 1",
        },
        "units": UNITS,
        "sessions": sessions_out,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    # newline="\n" keeps the file byte-identical on Windows and Linux (CI /
    # Netlify), so re-running the script never produces a line-ending diff.
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    total_programs = sum(len(s["programs"]) for s in sessions_out.values())
    no_code = sum(1 for s in sessions_out.values() if not s["programs"])
    print(f"Wrote {OUT_PATH}")
    print(f"Sessions: {len(sessions_out)}, Programs: {total_programs}, No-code sessions: {no_code}")


# ---------------------------------------------------------------------------
# Question Bank
# ---------------------------------------------------------------------------
QB_PARTS = {
    "A": "Part A",
    "B": "Part B",
    "C": "Part C",
}
QB_REQUIRED = ["Part", "Unit", "Question", "KL", "CO", "PO", "PSO", "Exam", "QNo"]
MONTHS = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11,
    "december": 12,
}
VALID_UNITS = {u["number"] for u in UNITS}


def exam_sort_key(exam):
    """'November 2023' -> (2023, 11) so exams sort chronologically."""
    parts = exam.split()
    try:
        return (int(parts[-1]), MONTHS.get(parts[0].lower(), 0))
    except (ValueError, IndexError):
        return (0, 0)


def normalise_question(text):
    """Key used to merge the same question asked in several exams:
    case, spacing and punctuation are ignored."""
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def build_question_bank():
    """Read Question_Bank/question_bank.csv (one row per question per exam,
    in-syllabus questions only) and write question_bank.json with repeated
    questions merged and their exam history listed."""
    if not os.path.exists(QB_CSV):
        print(f"Question bank: {os.path.relpath(QB_CSV, ROOT)} not found, skipped")
        return

    with open(QB_CSV, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        missing = [c for c in QB_REQUIRED if c not in (reader.fieldnames or [])]
        if missing:
            raise SystemExit(f"ERROR: {QB_CSV} is missing column(s): {', '.join(missing)}")
        rows = list(reader)

    merged = {}
    order = []
    for line_no, row in enumerate(rows, start=2):
        row = {k: (v or "").strip() for k, v in row.items() if k}
        if not row["Question"]:
            continue
        part = row["Part"].upper()
        if part not in QB_PARTS:
            raise SystemExit(f"ERROR: question_bank.csv line {line_no}: Part must be A, B or C")
        units = [u.strip() for u in row["Unit"].split("/") if u.strip()]
        bad = [u for u in units if u not in VALID_UNITS]
        if not units or bad:
            raise SystemExit(
                f"ERROR: question_bank.csv line {line_no}: Unit '{row['Unit']}' "
                f"must be I-V (use I/II for a question spanning two units)"
            )

        key = (part, normalise_question(row["Question"]))
        if key not in merged:
            merged[key] = {
                "part": part,
                "units": units,
                "question": row["Question"],
                "kl": row["KL"],
                "co": row["CO"],
                "po": row["PO"],
                "pso": row["PSO"],
                "note": row.get("Note", ""),
                "asked": [],
            }
            order.append(key)
        entry = merged[key]
        if row.get("Note") and not entry["note"]:
            entry["note"] = row["Note"]
        qno = row["QNo"]
        entry["asked"].append({"exam": row["Exam"], "qno": int(qno) if qno.isdigit() else qno})

    questions = []
    for key in order:
        q = merged[key]
        q["asked"].sort(key=lambda a: exam_sort_key(a["exam"]))
        questions.append(q)

    unit_rank = {u["number"]: i for i, u in enumerate(UNITS)}
    questions.sort(
        key=lambda q: (unit_rank[q["units"][0]], q["part"], -len(q["asked"]), q["question"].lower())
    )
    for i, q in enumerate(questions, start=1):
        q["id"] = i

    exams = sorted({a["exam"] for q in questions for a in q["asked"]}, key=exam_sort_key)
    data = {
        "title": "Previous-year Question Bank",
        "source": "End-semester question papers, analysed against the current syllabus",
        "excluded": "Out-of-syllabus questions (File Handling, Arrays) are not included.",
        "parts": QB_PARTS,
        "exams": exams,
        "questions": questions,
    }
    with open(QB_OUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    occurrences = sum(len(q["asked"]) for q in questions)
    repeated = sum(1 for q in questions if len(q["asked"]) > 1)
    print(f"Wrote {QB_OUT_PATH}")
    print(
        f"Question bank: {len(rows)} rows -> {len(questions)} unique questions "
        f"({occurrences} exam occurrences, {repeated} repeated), exams: {', '.join(exams)}"
    )


if __name__ == "__main__":
    build()
    build_question_bank()
