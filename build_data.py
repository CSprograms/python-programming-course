#!/usr/bin/env python3
"""
Extracts every session's Python programs (docstring + code) from
Session_Programs/ into web-app/data/sessions.json for the static
code-viewer web app.
"""
import ast
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
SESSIONS_DIR = os.path.join(ROOT, "Session_Programs")
OUT_PATH = os.path.join(ROOT, "web-app", "data", "sessions.json")

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
    """Parse a .py file: return (docstring_text, code_text)."""
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source)
    docstring = ast.get_docstring(tree)
    code = source
    if tree.body and isinstance(tree.body[0], ast.Expr):
        first = tree.body[0]
        end_lineno = getattr(first, "end_lineno", None)
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

    session_dirs = sorted(
        (d for d in os.listdir(SESSIONS_DIR) if d.startswith("Session_")),
        key=lambda d: int(d.split("_")[1]),
    )

    for dirname in session_dirs:
        session_num = int(dirname.split("_")[1])
        session_path = os.path.join(SESSIONS_DIR, dirname)
        py_files = sorted(
            (f for f in os.listdir(session_path) if f.endswith(".py")),
            key=natural_program_key,
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
                with open(readme_path, "r", encoding="utf-8") as f:
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
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total_programs = sum(len(s["programs"]) for s in sessions_out.values())
    no_code = sum(1 for s in sessions_out.values() if not s["programs"])
    print(f"Wrote {OUT_PATH}")
    print(f"Sessions: {len(sessions_out)}, Programs: {total_programs}, No-code sessions: {no_code}")


if __name__ == "__main__":
    build()
