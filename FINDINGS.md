# Rev. Proc. 2025-32 reconstructed from the Internal Revenue Code: findings

Arxo Law · October 21, 2026 · contact: hi@arxo.io · reproduction package: https://github.com/arxohq/arxo-irs-inflation-adjustments

## Summary

We reconstructed 295 modelled rows covering all 63 items in section 4 of Rev. Proc.
2025-32 (the 2026 inflation-adjusted items), using statutory and administrative sources
and explicitly identified computational assumptions.

- **Match.** 216 rows match the published figures numerically. 213 of them match without
  qualification.
- **Rounding.** Two amounts cannot result from the statute's rounding rule, whatever
  index value is used. A third group, the long-term care figures, is consistent with the
  same convention.
- **Remaining findings:**
  - questions of basis or timing;
  - one amount published for a provision that does not apply;
  - drafting issues in the Code;
  - errors the IRS has already corrected.

Each finding can be checked in about ten minutes from the cited text and two index values.

The head-of-household deduction differs by $25; the annual levy component differs by $50
per dependent. Tax effects depend on individual circumstances; we have not estimated
aggregate effects. The point is the method and whether the published figures can be
verified from the statute.

**Method.**
- **Law.** The law as in effect on October 9, 2025, the date the revenue procedure names
  in its section 1: the official 2024 edition of Title 26 (govinfo, USCODE-2024-title26)
  with P.L. 119-21 applied. Later 2025 public laws (119-29, 119-39, 119-64, 119-75,
  119-86) do not affect the indexing provisions.
- **Numbering.** Item numbers follow the October 17, 2025 version posted on irs.gov.
- **Index values.** The cost-of-living adjustment follows §1(f)(3)–(7). As
  §1(f)(6)(A) requires, C-CPI-U values are those available when the August 2025 value was
  first released (September 11, 2025). Later revisions are not used.
- **Arithmetic.** Decimal arithmetic at 50-digit precision. Displayed intermediate values
  are rounded.
- **Inferred conventions.** A few are inferred from published IRS figures and labelled as
  such: rounding of the EIC maximum credit and phaseout endpoints, and the base year 1997
  for Rev. Proc. 98-19 §5.05.
- **Interpretive assumptions.** §45R(d)(3)(B)(ii) «multiplied by the cost-of-living
  adjustment» is read as 1 + COLA; §642(b)(2)(C)(iii)(II) «the $4,150 amount in
  subparagraph (A)» is read as the amount in subclause (I) of clause (iii).
- **Tools.** Standalone Python scripts.
- **Control case.** The 2018 HSA family limit is reproduced on both sides of that
  episode: $6,900 with CPI-U (Rev. Proc. 2017-37) and $6,850 with C-CPI-U
  (Rev. Proc. 2018-18).

**Index values used** (12-month averages ending August 31, C-CPI-U as available on
September 11, 2025):

| Series | Year | Value |
|---|---|---:|
| C-CPI-U | 2025 | 177.113750 |
| C-CPI-U | 2024 | 173.015833 |
| C-CPI-U | 2017 | 138.236750 |
| C-CPI-U | 2016 | 135.993000 |
| CPI-U | 2016 | 238.649 |

## A. Rounding discrepancies

**A1. Standard deduction, head of household — §63(c)(7)(B)(ii) (item 4.14(1)).**
- **Text** (as amended by P.L. 119-21 §70102). «In the case of a taxable year beginning
  after 2025, the $23,625 and $15,750 amounts in subparagraph (A) shall each be increased
  by an amount equal to— (I) such dollar amount, multiplied by (II) the cost-of-living
  adjustment determined under section 1(f)(3) for the calendar year in which the taxable
  year begins, determined by substituting "2024" for "2016" in subparagraph (A)(ii)
  thereof. If any increase under this clause is not a multiple of $50, such increase shall
  be rounded to the next lowest multiple of $50.»
- **Computation.** 177.113750 / 173.015833 = 1.0236852.
  Increase: 23,625 × 0.0236852 = 559.56, rounded down to 550. Amount **$24,175**.
- **Published: $24,150.**
  - The published increase, 24,150 − 23,625 = 525, is not a multiple of $50. It cannot
    result from the quoted increase-rounding rule, regardless of the index value.
  - The published figure is consistent with rounding the whole amount (24,184.56) down
    to a multiple of $50.
- **Other statuses.** Single ($16,100) and joint ($32,200 = 200%) match.

**A2. Per-dependent levy amount and qualified disability trust deduction —
§6334(d)(4)(B)–(C), §642(b)(2)(C)(iii)(II) (items 4.50 and 4.35).**
- **Text.** §6334(d)(4)(C): the $4,150 amount is increased by the COLA «determined by
  substituting "2017" for "2016"». «If any increase … is not a multiple of $100, such
  increase shall be rounded to the next lowest multiple of $100.»
  §642(b)(2)(C)(iii)(II) applies the same rule; for §642 the calculation assumes that its
  reference to «subparagraph (A)» means subclause (I) of clause (iii) (see D).
- **Computation for 2026.** 177.113750 / 138.236750 = 1.2812349.
  Increase 1,167.12, rounded down to 1,100. Amount **$5,250**.
- **Published: $5,300.** 5,300 − 4,150 = 1,150, which is not a multiple of $100.
- **2025** (Rev. Proc. 2024-40, item 2.51): $5,150 under the text, $5,100 published.
  - In both years the published figures are consistent with rounding the whole amount
    down to $100.
  - The difference changes sign from year to year. In 2025 the published figure was $50
    per dependent lower than the statutory figure, about $1 a week in the levy formula.

**A3. Long-term care premium limit for ages 41–50 and per diem — §213(d)(10)(B)(i),
§7702B(d)(5) (items 4.27 and 4.62).**
- **Text.** The rule rounds the *increase* to the nearest multiple of $10.
- **Published figures.** Under the medical-component index link described in B1, they are
  consistent with rounding the whole amount:

  | Item | Base × factor | Published | Increase rounding under the assumed medical-component link |
  |---|---|---:|---:|
  | Ages 41–50 | 375 × 2.48130 = 930.49 | $930 | $935 (increase 555.49 → 560) |
  | Per diem | 175 × 2.48130 = 434.23 | $430 | $435 |

- **Other premium limits.** For the other age bands both conventions give the published
  figure.
- These two amounts assume the reconstructed index link. Their basis is itself the
  question in B1.

## B. Questions of basis and timing

**B1. Basis of the medical care adjustment — §213(d)(10)(B)(ii).**
- **Text since P.L. 115-97.** The statutory adjustment compares two things:
  - the medical care component of the *C-CPI-U* for August of the preceding year;
  - the medical care component of the *CPI-U* for August 1996, multiplied by the
    *all-items* ratio of §1(f)(3)(B).
- **Literal reading.** It mixes two index scales and gives a factor of 1.683: $340
  against the published $500 for ages 40 and under, $635 against $930 for ages 41–50,
  $295 against $430 per diem.
- **What the published figures match.** A link through the medical care component
  itself (C-CPI-U/CPI-U medical, August 2016): factor 2.48130.
- **The clause** continues: «The Secretary shall, in consultation with the Secretary of
  Health and Human Services, prescribe an adjustment which the Secretary determines is
  more appropriate for purposes of this paragraph than the adjustment described in the
  preceding sentence, and the adjustment so prescribed shall apply in lieu of the
  adjustment described in the preceding sentence.»
- **The clause directs that an adjustment be prescribed after consultation with HHS. We
  have not located a published act defining the adjustment applied.** This is a question,
  not a claimed error.

**B2. Penalty amounts for returns and statements due in 2027 (items 4.52–4.59).**
- **Text.** §§6651(j), 6652(c)(7), 6695(h), 6698(e), 6699(e), 6721(f), 6722(f) and
  6726(d) index by the COLA «for the calendar year» of the relevant event. That event is
  the required filing, the actual filing or the required furnishing, depending on the
  section.
- **What the published figures use.** All 75 rows in items 4.52–4.59 are consistent with
  applying the 2026 adjustment where indexing applies.
- **Effect of the event-year reading.** Under that reading and the later-data scenario
  below, 57 rows differ and 18 remain unchanged. Examples: $555 instead of $535 (§6651(a)), $360 instead of $340 (§6721(a)(1)).
  These alternatives are conditional calculations: they use later BLS data and an
  eleven-month mean.
- **Labels.** Items 4.57–4.58 show «August 1, 2026» for returns and statements due in
  2027; Rev. Proc. 2024-40 shows the same date for returns due in 2026. The date appears to
  have been carried over; please confirm.
- **We ask** which reading of «for the calendar year» the Service applies, and whether
  that reading has been stated in published guidance.

**B3. Missing October 2025 C-CPI-U value.**
- **Fact.** BLS could not collect October 2025 survey data during the lapse in
  appropriations and published no all-items C-CPI-U value (SUUR0000SA0) for that month.
  According to its FAQ, final C-CPI-U estimates for October–December 2025 are scheduled
  for November 10, 2026. That is after the September 11, 2026 release of the initial August
  2026 value, which §1(f)(6)(A) fixes for the 2027 adjustments.
- **Effect on 2027.** In our 307-row dataset for 2027 (the 295-row dataset plus 12
  additional rows for amounts first indexed under P.L. 119-21):
  - 163 vary across missing-month treatments under at least one reading.
  - 158 vary under the reconstructed IRS conventions.
  - Example: the joint-return 12%/22% boundary is $104,050 with an eleven-month mean and
    $103,900 with linear interpolation.
- **We ask** that the method be stated in the 2027 revenue procedure.

**B4. Estates and trusts: boundary of the 10% and 24% brackets (item 4.01, Table 5).**
- **Text.** After P.L. 119-21 §70101(b), base year 2017 applies «solely for purposes of
  determining the dollar amounts at which any rate bracket higher than 12 percent ends and
  at which any rate bracket higher than 22 percent begins».
- **The ambiguity.** In Table 5 one amount is both the end of the 10% bracket (base 2016)
  and the start of the 24% bracket (base 2017).
- **Effect.** The published $3,300 uses 2016; base 2017 gives $3,250. The tax amounts at
  the 24%, 35% and 37% brackets follow: $330 / $2,346 / $3,851 against
  $325 / $2,353 / $3,858.

**B5. Rounding where the statute states none.** The published figures are rounded; the
rule is not in the text:
- §45R(d)(3)(B): $34,057.75 → $34,100 (reading «multiplied by the cost-of-living
  adjustment» as 1 + COLA; the wording itself is a separate interpretive question);
- §512(d)(2): $211.58 → $212;
- §513(h)(2)(C): $13.878 → $13.90;
- §6039F(d): $20,573.24 → $20,573.

The $25 and $50 guidelines of Rev. Proc. 90-12 are published as 5× and 10× of $13.90
($69.50, $139), not indexed separately ($69.39, $138.78).

## C. Amount published for a provision that does not apply

**§59(j), item 4.11.**
- **Statute.** §55(d)(4)(A)(iii), added by P.L. 116-94, provides that «subsection (j) of
  section 59 shall not apply». P.L. 119-21 §70107(a) made §55(d)(4)(A) permanent.
- **Published.** The $9,750 figure is computed correctly but continues to be published,
  as in Rev. Proc. 2024-40.

## D. Drafting issues and questions for legislative clarification

- **§642(b)(2)(C)(iii)(II)** refers to «the $4,150 amount in subparagraph (A)»; the
  amount is in subclause (I) of clause (iii).
- **§877(a)(2)** substitutes «2003» for «1992» in §1(f)(3)(B). After P.L. 115-97 that
  subparagraph no longer contains «1992».
  - Read as intended (base 2003): $211,000, as published.
  - Read literally (no substitution): $161,000.
- **«For the calendar year»** in the penalty indexing provisions (B2) and the **mixed
  index scales** of §213(d)(10)(B)(ii) (B1) may warrant clarification.

## E. Already corrected by the IRS, and reproduced

- **§4611.** Rev. Proc. 2025-32 published $0.27 per barrel. The Oil Spill Liability Trust
  Fund rate expired after December 31, 2025 (§4611(f)(2)), so the statutory rate is $0.18,
  as Announcement 2026-2 states.
- **October 9 and October 17, 2025 versions.** The October 17 version replaced the
  October 9 version at the same URL without a change note in the document. It added
  section 2.05 (§42(h)(3)(I)), renumbered the rest of section 2 and changed four figures;
  for each, our computation equals the October 17 value:
  - EIC completed phaseout, joint, three or more children: $70,224 → **$70,244**;
  - tax at the 24% bracket, married filing separately: $17,996 → **$17,966**;
  - head-of-household 24% bracket ceiling: $201,775 → **$201,750**;
  - low-income housing credit ceiling: $3.05 / $3,530,000 → **$3.416 / $3,953,600**.

## F. Reproduction

The package contains:
- the statute texts used, with SHA-256;
- both PDF versions of Rev. Proc. 2025-32;
- the C-CPI-U, CPI-U and medical care series as available on the stated dates, with
  their origin;
- one indexing record per row quoting its rule;
- scripts, expected outputs and SHA-256 of the result table.

Our 307-row 2027 forecast dataset was recorded locally; we have not located the general
annual inflation-adjustment revenue procedure for 2027:
- file `forecast-2027.json`;
- SHA-256 `07119073d7e96fadc072f07976a533a5e7aa666ed79fcd85da61b0f772d3ba8f`;
- 2026-10-21 11:53 UTC;
- public record of the hash: this repository (first published 2026-10-21) and the OpenTimestamps proof `2027-forecast/forecast-2027.json.ots`.

Package: https://github.com/arxohq/arxo-irs-inflation-adjustments.
