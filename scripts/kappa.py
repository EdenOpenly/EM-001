"""Cohen's kappa for the blinded author check (data/EM-001-author-check.csv).

Usage: python scripts/kappa.py
"""
import csv
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
rows = list(csv.DictReader(open(DATA / "EM-001-author-check.csv", encoding="utf-8-sig")))


def kappa(pairs, categories):
    n = len(pairs)
    observed = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    expected = sum(ca[c] * cb[c] for c in categories) / n / n
    return observed, (observed - expected) / (1 - expected)


def report(label, subset):
    pairs = [(r["ai_decision_title_abstract"], r["author_decision_blinded"]) for r in subset]
    agree, k3 = kappa(pairs, "YNU")
    binary = [("Y" if a == "Y" else "x", "Y" if b == "Y" else "x") for a, b in pairs]
    _, k2 = kappa(binary, "Yx")
    print(f"{label}: {sum(a == b for a, b in pairs)}/{len(pairs)} agree; kappa {k3:.2f} (Y/N/U), {k2:.2f} (include vs not)")


report("All", rows)
report("First sample", [r for r in rows if r["sample"].startswith("first")])
report("Second sample", [r for r in rows if r["sample"].startswith("second")])
