#!/usr/bin/env python3
"""
Builds the data files for the static Session Viewer web app:

* web-app/data/sessions.json       from Session_Programs/ (docstring + code)
* web-app/data/question_bank.json  from Question_Bank/Unit_<1-5>_Part_<A-C>.txt
                                   (previous-year questions, in syllabus only,
                                   with optional answers)
"""
import ast
import hashlib
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
SESSIONS_DIR = os.path.join(ROOT, "Session_Programs")
OUT_PATH = os.path.join(ROOT, "web-app", "data", "sessions.json")
QB_DIR = os.path.join(ROOT, "Question_Bank")
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
MONTHS = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11,
    "december": 12,
}
ROMAN = ["I", "II", "III", "IV", "V"]           # Unit_1 ... Unit_5 -> I ... V
VALID_UNITS = {u["number"] for u in UNITS}

# Field lines allowed inside a question block ("Key: value"), in the order
# they are usually written. "Answer:" must be the last one: everything after
# it, up to the next "=== Q<n>" line, is the answer text, kept as written.
QB_FIELDS = {
    "question": "question",
    "kl": "kl",
    "co": "co",
    "po": "po",
    "pso": "pso",
    "asked": "asked",
    "also in unit": "also_in",
    "note": "note",
}
BLOCK_START = re.compile(r"^===\s*Q\s*\d+\s*$", re.I)
FIELD_LINE = re.compile(r"^([A-Za-z][A-Za-z ]*?)\s*:\s?(.*)$")
ASKED_ITEM = re.compile(r"^(.+?)\s+Q\s*(\d+)$", re.I)


def exam_sort_key(exam):
    """'November 2023' -> (2023, 11) so exams sort chronologically."""
    parts = exam.split()
    try:
        return (int(parts[-1]), MONTHS.get(parts[0].lower(), 0))
    except (ValueError, IndexError):
        return (0, 0)


def normalise_question(text):
    """Case, spacing and punctuation are ignored when spotting duplicates."""
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def parse_qb_file(path, unit, part):
    """Parse one Question_Bank/Unit_N_Part_X.txt file into question dicts."""
    rel = os.path.relpath(path, ROOT)

    def fail(line_no, msg):
        raise SystemExit(f"ERROR: {rel}, line {line_no}: {msg}")

    with open(path, "r", encoding="utf-8-sig") as f:   # BOM-safe, CRLF-safe
        lines = f.read().split("\n")

    questions = []
    current = None
    in_answer = False

    def finish(q):
        if q is None:
            return
        if not q.get("question"):
            fail(q["_line"], "question block has no 'Question:' line")
        answer = "\n".join(q.pop("_answer")).strip("\n")
        # Remove trailing spaces on each line but keep indentation for code.
        q["answer"] = "\n".join(ln.rstrip() for ln in answer.split("\n")).strip("\n")
        questions.append(q)

    for n, raw in enumerate(lines, start=1):
        line = raw.rstrip("\r")
        if BLOCK_START.match(line.strip()):
            finish(current)
            current = {"_line": n, "_answer": []}
            in_answer = False
            continue
        if current is None:
            # File header: only comments and blank lines are allowed here.
            if line.strip() and not line.lstrip().startswith("#"):
                fail(n, "text before the first '=== Q1' line (header lines must start with #)")
            continue
        if in_answer:
            current["_answer"].append(line)
            continue
        if not line.strip():
            continue
        m = FIELD_LINE.match(line.strip())
        if not m:
            fail(n, f"expected 'Key: value' or 'Answer:', found: {line.strip()[:60]}")
        key, value = m.group(1).strip().lower(), m.group(2).strip()
        if key == "answer":
            in_answer = True
            if value:
                current["_answer"].append(value)
            continue
        if key not in QB_FIELDS:
            fail(n, f"unknown field '{m.group(1)}:' (allowed: Question, KL, CO, PO, PSO, Asked, Also in unit, Note, Answer)")
        current[QB_FIELDS[key]] = value
    finish(current)

    out = []
    seen = {}
    for q in questions:
        line_no = q.pop("_line")
        asked = []
        for item in filter(None, (a.strip() for a in q.get("asked", "").split(";"))):
            m = ASKED_ITEM.match(item)
            if not m:
                fail(line_no, f"'Asked:' entry '{item}' must look like 'November 2025 Q7'")
            asked.append({"exam": m.group(1).strip(), "qno": int(m.group(2))})
        asked.sort(key=lambda a: exam_sort_key(a["exam"]))

        units = [unit]
        for extra in filter(None, (u.strip().upper() for u in q.get("also_in", "").split(","))):
            if extra not in VALID_UNITS:
                fail(line_no, f"'Also in unit: {extra}' must be one of I, II, III, IV, V")
            if extra not in units:
                units.append(extra)

        key = normalise_question(q["question"])
        if key in seen:
            fail(line_no, f"same question as the block at line {seen[key]}; "
                          "merge them and list both exams on one 'Asked:' line")
        seen[key] = line_no

        out.append({
            "part": part,
            "units": units,
            "question": q["question"],
            "kl": q.get("kl", ""),
            "co": q.get("co", ""),
            "po": q.get("po", ""),
            "pso": q.get("pso", ""),
            "note": q.get("note", ""),
            "asked": asked,
            "answer": q["answer"],
        })
    return out


def build_question_bank():
    """Read the 15 Question_Bank/Unit_<1-5>_Part_<A-C>.txt files and write
    web-app/data/question_bank.json (order within a file is kept)."""
    if not os.path.isdir(QB_DIR):
        print("Question bank: Question_Bank/ not found, skipped")
        return

    questions = []
    missing = []
    for i, roman in enumerate(ROMAN, start=1):
        for part in QB_PARTS:
            path = os.path.join(QB_DIR, f"Unit_{i}_Part_{part}.txt")
            if not os.path.exists(path):
                missing.append(os.path.basename(path))
                continue
            questions.extend(parse_qb_file(path, roman, part))
    if missing:
        print("Question bank: WARNING, missing file(s): " + ", ".join(missing))

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

    answered = sum(1 for q in questions if q["answer"])
    repeated = sum(1 for q in questions if len(q["asked"]) > 1)
    print(f"Wrote {QB_OUT_PATH}")
    print(
        f"Question bank: {len(questions)} questions ({answered} with answers, "
        f"{repeated} asked more than once), exams: {', '.join(exams)}"
    )


# ---------------------------------------------------------------------------
# Cache-busting: index.html / 404.html load css/style.css?v=<hash> and
# js/app.js?v=<hash>. The hash changes whenever the file changes, so every
# browser downloads the new version at once instead of using an old cached
# copy (earlier deploys told browsers to cache these files for a year).
# ---------------------------------------------------------------------------
WEB_DIR = os.path.join(ROOT, "web-app")
ASSETS = ["css/style.css", "js/app.js"]
HTML_PAGES = ["index.html", "404.html"]


def stamp_asset_versions():
    versions = {}
    for asset in ASSETS:
        with open(os.path.join(WEB_DIR, asset), "rb") as f:
            versions[asset] = hashlib.sha1(f.read()).hexdigest()[:10]
    for page in HTML_PAGES:
        path = os.path.join(WEB_DIR, page)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8", newline="") as f:
            html = f.read()
        new_html = html
        for asset, v in versions.items():
            pattern = r'((?:href|src)="/?' + re.escape(asset) + r')(?:\?v=[0-9a-f]*)?(")'
            new_html = re.sub(pattern, r"\g<1>?v=" + v + r"\g<2>", new_html)
        if new_html != html:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(new_html)
    print("Asset versions: " + ", ".join(f"{a}?v={v}" for a, v in versions.items()))


if __name__ == "__main__":
    build()
    build_question_bank()
    stamp_asset_versions()
