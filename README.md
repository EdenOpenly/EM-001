# EM-001: Korean patients deserve Korean evidence

An evidence map of sexual health after gender-affirming care: where the evidence comes from, and how much of it comes from Korea.

**Finding.** Of 959 PubMed records, 188 primary studies (19,792 participants) reported a sexual outcome in transgender people after hormones or genital surgery. Europe and North America contributed 88.7% of participants; East, Southeast and South Asia 5.4%. Korea contributed 3 studies and 70 participants (0.35%), all case series from one centre, with outcomes collected by interview. 45 of 188 studies (24%) used a named, published sexual-function questionnaire; no Korean study did.

- Public page: https://edenopenly.com/korean-evidence-map/
- Archived deposit (the report PDF and the data files): Zenodo, https://doi.org/10.5281/zenodo.23646560
- Presented as an e-poster at the Korean Association for Sexual Health (대한성학회) 2026 autumn conference, 21 November 2026

## Reproduce the figures

Python 3.9 or later, standard library only.

```
python scripts/tabulate.py   # every figure on the poster and page, from data/EM-001-included-studies.csv
python scripts/kappa.py      # the blinded author check (80 records)
python scripts/search.py     # reruns the final PubMed search and compares it with the screened set
```

`search.py` needs internet access to NCBI E-utilities. PubMed grows, so a later rerun can return more records; the script reports any difference.

## Contents

| Path | What it is |
|---|---|
| `data/EM-001-search-log.csv` | Every search: database, date, exact string, records |
| `data/EM-001-screening-decisions.csv` | All 959 PubMed records: decision, basis, reason, country, author-check sample |
| `data/EM-001-included-studies.csv` | The 188 included studies: country, region, participants, intervention, outcomes, instrument |
| `data/EM-001-unresolved-records.csv` | The 13 records that could not be obtained |
| `data/EM-001-author-check.csv` | The 80-record blinded author check |
| `prompts/` | The fixed prompts used for AI-assisted screening (title/abstract and full text) |
| `scripts/` | Reproduction scripts |

## How the decisions were made

Screening and data extraction were AI-assisted, with fixed prompts (in `prompts/`). Each decision's basis is labelled in the screening file: "title and abstract, AI-assisted" or "full text, AI-assisted". The author re-screened 80 random records blind: 76 of 80 agreed with the AI's title-and-abstract decisions (κ = 0.90; 0.97 for include versus not). Full-text decisions were not independently checked by a human, and are not presented as such.

Country is where participants were recruited or treated. Participants are as stated by each study; Lawrence 2005 and 2006 report the same 232 patients and are counted once (`counted_in_participant_total`).

The KITE cohort (Lee ES et al. 2026, doi:10.1080/26895269.2026.2626839) was found outside the PubMed search and is reported beside the map rather than counted in it. Counted in, Korea would be 4.3% of participants. See Part 4 of the report in the Zenodo deposit.

## Corrections

Every correction and change of figure is listed, dated, in the report's correction record (Zenodo deposit) and in the page's revision history. Report errors to editor@edenopenly.com.

## Competing interests

The author is a transgender woman and a dermatologist, and the founder and sole funder of Eden Institute, a transgender health research institute being set up in Korea. The full, dated register is at https://edenopenly.com/about/declared-interests/. AI use: https://edenopenly.com/how-we-use-ai/.

## How to cite

Eden. Korean patients deserve Korean evidence: an evidence map of sexual health after gender-affirming care (EM-001), version 1.0. Eden Openly; 2026. doi:10.5281/zenodo.23646560

## Licence

Data, prompts and text: CC BY 4.0. Code (`scripts/`): MIT. See `LICENSE`.

Eden, Eden Openly · ORCID 0009-0001-2205-5702
