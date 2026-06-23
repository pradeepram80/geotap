# -*- coding: utf-8 -*-
"""
Turn a simple questions list into a Blooket-ready import CSV.

Usage:
    python3 make_blooket.py questions.csv blooket.csv [time_limit]

Input CSV must have two columns with headers: Question, Answer
 - 'Question' = the full single-sentence clue, ending in '?'
 - 'Answer'   = the correct answer (state/country/etc.)

The script builds 3 random wrong answers for each question from the pool of all
correct answers in the file, shuffles the four choices, marks the correct number,
and writes a CSV that matches Blooket's 8-column import template.
"""
import csv, sys, random

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 make_blooket.py questions.csv blooket.csv [time_limit]")
        return
    infile, outfile = sys.argv[1], sys.argv[2]
    time_limit = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    random.seed(42)

    rows = []
    with open(infile, newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            q = (r.get("Question") or r.get("question") or "").strip()
            a = (r.get("Answer") or r.get("answer") or "").strip()
            if q and a:
                rows.append((q, a))

    if not rows:
        print("No rows found. Make sure the CSV has 'Question' and 'Answer' columns.")
        return

    pool = sorted({a for _, a in rows})
    if len(pool) < 4:
        print("Need at least 4 distinct answers to build 4-choice questions.")
        return

    header = ["Question #", "Question Text", "Answer 1", "Answer 2",
              "Answer 3", "Answer 4", "Time Limit (sec)", "Correct Answer(s)"]
    out = []
    for i, (q, a) in enumerate(rows, start=1):
        distractors = random.sample([x for x in pool if x != a], 3)
        opts = [a] + distractors
        random.shuffle(opts)
        correct = opts.index(a) + 1
        out.append([i, q, opts[0], opts[1], opts[2], opts[3], time_limit, correct])

    with open(outfile, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(out)

    print(f"Wrote {len(out)} questions to {outfile}")

if __name__ == "__main__":
    main()
