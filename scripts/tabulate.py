"""Rebuild every figure in EM-001 from data/EM-001-included-studies.csv.

Usage: python scripts/tabulate.py
"""
import csv
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
rows = list(csv.DictReader(open(DATA / "EM-001-included-studies.csv", encoding="utf-8-sig")))

studies, people = Counter(), Counter()
for r in rows:
    studies[r["region"]] += 1
    if r["counted_in_participant_total"] == "yes" and r["n_trans_participants"]:
        people[r["region"]] += int(r["n_trans_participants"])

total = sum(people.values())
korea = sum(int(r["n_trans_participants"]) for r in rows if "Korea" in r["country"])
named = sum(r["named_published_questionnaire"] == "yes" for r in rows)
asia = sum(people[k] for k in ("East Asia", "Southeast Asia", "South Asia"))

print(f"Included studies: {len(rows)}   Participants: {total:,}")
for region, n in people.most_common():
    print(f"  {region:<26}{studies[region]:>4} studies {n:>7,} people {100 * n / total:5.1f}%")
print(f"Europe + North America: {100 * (people['Europe'] + people['North America']) / total:.1f}%")
print(f"East, Southeast and South Asia: {100 * asia / total:.1f}%")
print(f"Korea: {sum('Korea' in r['country'] for r in rows)} studies, {korea} people, {100 * korea / total:.2f}%")
print(f"Named, published sexual-function questionnaire: {named}/{len(rows)} ({100 * named / len(rows):.0f}%)")
print(f"Sensitivity, KITE counted in (824 people): Korea {100 * (korea + 824) / (total + 824):.1f}%")
