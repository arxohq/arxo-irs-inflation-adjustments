# IRS inflation adjustments rebuilt from the Internal Revenue Code

Arxo Law · contact: hi@arxo.io

This repository reconstructs the annual inflation-adjusted amounts that the IRS publishes
in its revenue procedures. Each amount is rebuilt from the Internal Revenue Code, the
administrative sources it refers to, and the C-CPI-U as published by the Bureau of Labor
Statistics. The reconstruction is then compared with the published figures.

Not legal advice. Not affiliated with the IRS, the Treasury or BLS.

## What is here

**2026 — Rev. Proc. 2025-32.** All 295 rows of section 4 (all 63 items) were rebuilt:

- 216 rows match the published figures numerically, 213 of them without qualification.
- Two amounts cannot result from the statute's own rounding rule. The head-of-household
  standard deduction is published as $24,150; §63(c)(7)(B)(ii) gives $24,175. The §6334(d)(4)(B)
  per-dependent amount is published as $5,300; §6334(d)(4)(C) gives $5,250.
- The other findings are questions of basis or timing, one amount published for a
  provision that does not apply, drafting issues in the Code, and errors the IRS has
  already corrected.

The findings, with statutory text and arithmetic, are in [FINDINGS.md](FINDINGS.md). The
row-by-row table is [2026-recompute/TABLE.md](2026-recompute/TABLE.md).

**2027 — forecast.** We built all 307 amounts for 2027 before the general 2027 revenue
procedure appeared: the 295 rows above plus 12 amounts first indexed under P.L. 119-21. The
table is [2027-forecast/FORECAST.md](2027-forecast/FORECAST.md).

| | |
|---|---|
| File | `2027-forecast/forecast-2027.json` |
| SHA-256 | `07119073d7e96fadc072f07976a533a5e7aa666ed79fcd85da61b0f772d3ba8f` |
| Recorded locally | 2026-10-21 11:53:53 UTC |
| Public record | this repository, first published 2026-10-21; OpenTimestamps proof in `2027-forecast/forecast-2027.json.ots` (submitted 2026-10-21 to three calendars; Bitcoin attestation pending — `ots upgrade`, then `ots verify`) |
| Checked before publication | no general 2027 revenue procedure on irs.gov/pub/irs-drop (rp-26-31 and rp-26-33…60 returned 404) |

`PIN.sha256` is the original working record of the hash; its comments are in Russian. The
pinned object is `forecast-2027.json`.

## Reproduce

You need Python 3.10 or later. Only the standard library is used.

```sh
cd 2026-recompute
python3 -I scripts/compute.py      # writes results.json
python3 -I scripts/table_en.py     # writes TABLE.md
shasum -a 256 results.json         # 6f9a39da8216312002775800d7ac8f8478dde43365df7f43ff71bc94078c4ed8
python3 -I scripts/hsa_control.py  # control: the 2018 HSA episode, $6,900 (CPI-U) vs $6,850 (C-CPI-U)

cd ../2027-forecast
python3 -I scripts/make_specs27.py
python3 -I scripts/compute27.py
python3 -I scripts/table27.py      # working table (Russian); the English view is below
python3 -I scripts/forecast_en.py  # writes FORECAST.md
shasum -a 256 forecast-2027.json   # 07119073d7e96fadc072f07976a533a5e7aa666ed79fcd85da61b0f772d3ba8f
```

The 2027 scripts read the 2026 indexing records from `../2026-recompute`.

## Method

- **Law.** The law as in effect on October 9, 2025, the date the revenue procedure names: the
  official 2024 edition of Title 26 (govinfo, USCODE-2024-title26) with P.L. 119-21 applied.
  P.L. 119-29, 119-39, 119-64, 119-75 and 119-86 were checked and do not amend the indexing
  provisions.
- **Index.** The cost-of-living adjustment follows §1(f)(3)–(7). As §1(f)(6)(A) requires,
  C-CPI-U values are those available when the August value was first released; for 2026,
  the release of September 11, 2025. Archived releases come from ALFRED (Federal Reserve Bank
  of St. Louis), monthly series from the BLS public API.
- **Arithmetic.** Python `decimal` at 50-digit precision.
- **Indexing records.** One record per row, in `specs/*.json`. Each record gives the base
  amount, base year, COLA year, rounding rule and the quoted statutory text.
- **Inferred conventions.** A few conventions are inferred from published IRS figures and
  marked as such: rounding of the EIC maximum credit and phaseout endpoints, and the base
  year of Rev. Proc. 98-19 §5.05.
- **Control.** The 2018 HSA family limit is reproduced on both sides of that episode: Rev.
  Proc. 2017-37 and Rev. Proc. 2018-18.
- **External check.** The four figures the IRS changed between the October 9 and October 17,
  2025 versions of Rev. Proc. 2025-32 equal our computation.

Working annotations in the indexing records and code comments are partly in Russian. All
amounts, citations and statutory quotations are in English.

## Layout

| Path | Contents |
|---|---|
| `FINDINGS.md` | findings for Rev. Proc. 2025-32, with text and arithmetic |
| `2026-recompute/` | scripts, indexing records (`specs/`), index series (`data/`), `results.json`, `TABLE.md`, HSA control outputs |
| `2027-forecast/` | scripts, indexing records, index series up to the September 2026 release, `forecast-2027.json`, `PIN.sha256`, `FORECAST.md`, HSA 2027 check against Rev. Proc. 2026-24 |
| `sources/irs/` | revenue procedures, notices and the announcement cited, including both versions of Rev. Proc. 2025-32 |
| `sources/usc/` | text of the 58 Code sections cited, extracted from the govinfo USCODE-2024 HTML (the HTML is the authority) |
| `sources/public-law/` | P.L. 119-21 (govinfo USLM XML) |
| `sources/ecfr/` | 26 CFR 1.148-3, 1.148-5, 1.45R-2, 1.45R-3 (eCFR, as of 2025-10-01) |
| `SHA256SUMS` | SHA-256 of every file in this repository |

## Sources and licence

- IRS, Treasury and govinfo documents are works of the United States Government.
- BLS index data are in the public domain.
- Archived vintages were retrieved from ALFRED.
- Code and tables of this repository: Apache License 2.0 (see `LICENSE`).
