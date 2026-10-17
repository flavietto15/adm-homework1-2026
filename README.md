# Algorithmic Methods of Data Mining - Homework 1 (2026)

Python solutions for all **97 challenges listed in the assignment**: 91 Python
domain exercises and 6 algorithms. The earlier count of 107 was an arithmetic
error. Deadline stated in the assignment: **18 October 2026, 23:59**.

## Contents

- One independent `.py` file per challenge; `manifest.json` groups them by topic.
- `homework1.ipynb`: the same solutions, one exercise per code cell.
- `scripts.py`: runs a selected solution from the command line.
- `manifest.json`: complete exercise inventory and submission status.
- `check.py` and `cases.json`: local input/output checks, not HackerRank hidden tests.
- `printouts/`: location for genuine HackerRank submission evidence.
- `instructions/`: the original assignment and PDF-generation instructions.

| Topic | Exercises |
| --- | ---: |
| Introduction | 7 |
| Basic Data Types | 6 |
| Strings | 14 |
| Sets | 13 |
| Collections | 8 |
| Date and Time | 2 |
| Exceptions | 1 |
| Built-ins | 3 |
| Python Functionals | 1 |
| Regex and Parsing | 17 |
| XML | 2 |
| Closures and Decorators | 2 |
| NumPy | 15 |
| Algorithms (Problem 2) | 6 |
| **Total** | **97** |

## Run

Use Python 3. NumPy is required only for the 15 NumPy exercises.

```sh
python scripts.py birthday-cake-candles < input.txt
python check.py
```

Run notebook cells individually: each cell is a separate program and reads its
own input. For HackerRank, use the corresponding standalone file. Where the site
provides a locked driver, copy only the required function, definitions and imports
into the editable section, retaining the site's driver. Some regex challenges ask
only for named pattern variables.

The Tuples challenge prints Python's native tuple hash, which varies across
interpreter versions. Keep the requested `hash(tuple(...))` implementation; use
the interpreter expected by HackerRank rather than hard-coding a sample hash.

## Authorship and status

This initial solution set was **generated with OpenAI Codex assistance**, including
the code and local checks. It has not been represented as independently written
student work. The assignment requires individual writing: the student must review,
understand and adapt the work and verify that its use complies with course rules
before submitting it.

HackerRank editorials and other users' solution files were not used to produce
these solutions. Official challenge pages were consulted to check the inventory
and selected format requirements.

Local checks do not establish acceptance by HackerRank. The audit on 17 October 2026 verified 74 Accepted exercises, two previous unsuccessful submissions awaiting correction, and 21 exercises not yet submitted. Further updates will appear in this same repository. `manifest.json` records
verified submission status; no successful submissions or evidence are invented.
The Google Form must be completed only after the actual submission evidence is
available and reviewed.

## Assignment links

- [Assignment](http://aris.me/contents/teaching/data-mining-ds-2026/homeworks/homework1.pdf)
- [PDF instructions](http://aris.me/contents/teaching/data-mining-ds-2026/homeworks/generate-pdf.pdf)
- [HackerRank submissions](https://www.hackerrank.com/submissions/all)
- [Submission form](https://forms.gle/4qG2jWgreimWLTFX8)
