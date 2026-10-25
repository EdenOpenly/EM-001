"""Cohen's kappa for the blinded author check (data/EM-001-author-check.csv)
and the full-text check by an independent human reviewer (data/EM-001-fulltext-check.csv, from v1.1).

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


ft_file = DATA / "EM-001-fulltext-check.csv"
if ft_file.exists():
    ft = list(csv.DictReader(open(ft_file, encoding="utf-8-sig")))
    pairs = [(r["ai_decision_full_text"], r["reviewer_decision_blinded"]) for r in ft]
    agree, k = kappa(pairs, ["include", "exclude", "unclear", "hold separately"])
    changed = sum(r["final_decision"] != r["ai_decision_full_text"] for r in ft)
    print(f"Full-text check (independent human reviewer, blind): {sum(a == b for a, b in pairs)}/{len(pairs)} agree; "
          f"kappa {k:.2f}; {changed} AI decisions changed after the author's ruling")
