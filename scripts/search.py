"""Rerun the final PubMed search (S10) and compare with the screened set.

Usage: python scripts/search.py
Needs internet access to NCBI E-utilities. PubMed grows over time, so a later
rerun can return more records; the check reports any difference.
"""
import csv
import json
import urllib.parse
import urllib.request
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
log = list(csv.DictReader(open(DATA / "EM-001-search-log.csv", encoding="utf-8-sig")))
query = next(r["string_or_terms"] for r in log if r["search"].startswith("S10"))

body = urllib.parse.urlencode({"db": "pubmed", "term": query, "retmax": 5000, "retmode": "json"}).encode()
result = json.load(urllib.request.urlopen("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", body))["esearchresult"]
found = set(result["idlist"])
screened = {r["pmid"] for r in csv.DictReader(open(DATA / "EM-001-screening-decisions.csv", encoding="utf-8-sig"))}

print(f"PubMed returns {len(found)}; screened set {len(screened)}")
print(f"In PubMed result but not screened: {sorted(found - screened)}")
print(f"Screened but not in PubMed result: {sorted(screened - found)}")
