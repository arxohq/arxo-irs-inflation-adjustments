# 2027 inflation-adjusted amounts: forecast built from the Code before the IRS publication

Rows: 307 (295 rows of Rev. Proc. 2025-32 section 4 plus 12 amounts first indexed under P.L. 119-21). Class occurrences (a row may carry several): ambiguity: 12, firm: 67, irs-rule: 17, new-base: 15, october: 163, year: 77.

Columns: **2027, text** — the statutory reading with an eleven-month mean for the September 2025–August 2026 C-CPI-U average (no all-items October 2025 value was published); **2027, IRS conventions** — the same with the conventions the 2026 figures are consistent with (amount rounding where observed, prior-year COLA for penalties, medical-component link for long-term care); **range** — the IRS-conventions value across four treatments of the missing month (eleven-month mean, geometric and linear interpolation, carry-forward of September).

Classes: `firm` — one value under every reading and missing-month treatment; `october` — depends on the missing-month treatment; `irs-rule` — text and IRS conventions differ (as found for 2026); `year` — penalty year reading; `ambiguity` — two readings of the text; `new-base` — first indexation of a base set by P.L. 119-21.

The SHA-256 of `forecast-2027.json` is recorded in `PIN.sha256`; this table is a view of that file.

| item | amount (id) | 2026 published | 2027, text | 2027, IRS conventions | range across missing-month treatments | class |
|---|---|---:|---:|---:|---:|---|
| 4.01 | Table 1 MFJ and surviving spouses: top of 10% bracket / start of 12% bracket (`rt_mfj_10_12`) | 24,800 | 25,600 | 25,600 | 25,550 – 25,600 | october |
| 4.01 | Table 1 MFJ and surviving spouses: top of 12% bracket / start of 22% bracket (`rt_mfj_12_22`) | 100,800 | 104,050 | 104,050 | 103,900 – 104,050 | october |
| 4.01 | Table 1 MFJ and surviving spouses: top of 22% bracket / start of 24% bracket (`rt_mfj_22_24`) | 211,400 | 218,250 | 218,250 | 217,950 – 218,250 | october |
| 4.01 | Table 1 MFJ and surviving spouses: top of 24% bracket / start of 32% bracket (`rt_mfj_24_32`) | 403,550 | 416,650 | 416,650 | 416,150 – 416,650 | october |
| 4.01 | Table 1 MFJ and surviving spouses: top of 32% bracket / start of 35% bracket (`rt_mfj_32_35`) | 512,450 | 529,100 | 529,100 | 528,450 – 529,100 | october |
| 4.01 | Table 1 MFJ and surviving spouses: top of 35% bracket / start of 37% bracket (`rt_mfj_35_37`) | 768,700 | 793,650 | 793,650 | 792,650 – 793,650 | october |
| 4.01 | Table 1 MFJ and surviving spouses: tax at start of 12% bracket (`rt_mfj_tax_at_12`) | 2,480 | 2,560 | 2,560 | 2,555 – 2,560 | october |
| 4.01 | Table 1 MFJ and surviving spouses: tax at start of 22% bracket (`rt_mfj_tax_at_22`) | 11,600 | 11,974 | 11,974 | 11,957 – 11,974 | october |
| 4.01 | Table 1 MFJ and surviving spouses: tax at start of 24% bracket (`rt_mfj_tax_at_24`) | 35,932 | 37,098 | 37,098 | 37,048 – 37,098 | october |
| 4.01 | Table 1 MFJ and surviving spouses: tax at start of 32% bracket (`rt_mfj_tax_at_32`) | 82,048 | 84,714 | 84,714 | 84,616 – 84,714 | october |
| 4.01 | Table 1 MFJ and surviving spouses: tax at start of 35% bracket (`rt_mfj_tax_at_35`) | 116,896 | 120,698 | 120,698 | 120,552 – 120,698 | october |
| 4.01 | Table 1 MFJ and surviving spouses: tax at start of 37% bracket (`rt_mfj_tax_at_37`) | 206583.50 | 213290.50 | 213290.50 | 213,022 – 213290.50 | october |
| 4.01 | Table 2 Heads of households: top of 10% bracket / start of 12% bracket (`rt_hoh_10_12`) | 17,700 | 18,250 | 18,250 | 18,250 | firm |
| 4.01 | Table 2 Heads of households: top of 12% bracket / start of 22% bracket (`rt_hoh_12_22`) | 67,450 | 69,650 | 69,650 | 69,550 – 69,650 | october |
| 4.01 | Table 2 Heads of households: top of 22% bracket / start of 24% bracket (`rt_hoh_22_24`) | 105,700 | 109,100 | 109,100 | 108,950 – 109,100 | october |
| 4.01 | Table 2 Heads of households: top of 24% bracket / start of 32% bracket (`rt_hoh_24_32`) | 201,750 | 208,300 | 208,300 | 208,050 – 208,300 | october |
| 4.01 | Table 2 Heads of households: top of 32% bracket / start of 35% bracket (`rt_hoh_32_35`) | 256,200 | 264,550 | 264,550 | 264,200 – 264,550 | october |
| 4.01 | Table 2 Heads of households: top of 35% bracket / start of 37% bracket (`rt_hoh_35_37`) | 640,600 | 661,350 | 661,350 | 660,550 – 661,350 | october |
| 4.01 | Table 2 Heads of households: tax at start of 12% bracket (`rt_hoh_tax_at_12`) | 1,770 | 1,825 | 1,825 | 1,825 | firm |
| 4.01 | Table 2 Heads of households: tax at start of 22% bracket (`rt_hoh_tax_at_22`) | 7,740 | 7,993 | 7,993 | 7,981 – 7,993 | october |
| 4.01 | Table 2 Heads of households: tax at start of 24% bracket (`rt_hoh_tax_at_24`) | 16,155 | 16,672 | 16,672 | 16,649 – 16,672 | october |
| 4.01 | Table 2 Heads of households: tax at start of 32% bracket (`rt_hoh_tax_at_32`) | 39,207 | 40,480 | 40,480 | 40,433 – 40,480 | october |
| 4.01 | Table 2 Heads of households: tax at start of 35% bracket (`rt_hoh_tax_at_35`) | 56,631 | 58,480 | 58,480 | 58,401 – 58,480 | october |
| 4.01 | Table 2 Heads of households: tax at start of 37% bracket (`rt_hoh_tax_at_37`) | 191,171 | 197,360 | 197,360 | 197123.50 – 197,360 | october |
| 4.01 | Table 3 Unmarried individuals: top of 10% bracket / start of 12% bracket (`rt_single_10_12`) | 12,400 | 12,800 | 12,800 | 12,775 – 12,800 | october |
| 4.01 | Table 3 Unmarried individuals: top of 12% bracket / start of 22% bracket (`rt_single_12_22`) | 50,400 | 52,025 | 52,025 | 51,950 – 52,025 | october |
| 4.01 | Table 3 Unmarried individuals: top of 22% bracket / start of 24% bracket (`rt_single_22_24`) | 105,700 | 109,125 | 109,125 | 108,975 – 109,125 | october |
| 4.01 | Table 3 Unmarried individuals: top of 24% bracket / start of 32% bracket (`rt_single_24_32`) | 201,775 | 208,325 | 208,325 | 208,075 – 208,325 | october |
| 4.01 | Table 3 Unmarried individuals: top of 32% bracket / start of 35% bracket (`rt_single_32_35`) | 256,225 | 264,550 | 264,550 | 264,225 – 264,550 | october |
| 4.01 | Table 3 Unmarried individuals: top of 35% bracket / start of 37% bracket (`rt_single_35_37`) | 640,600 | 661,375 | 661,375 | 660,550 – 661,375 | october |
| 4.01 | Table 3 Unmarried individuals: tax at start of 12% bracket (`rt_single_tax_at_12`) | 1,240 | 1,280 | 1,280 | 1277.50 – 1,280 | october |
| 4.01 | Table 3 Unmarried individuals: tax at start of 22% bracket (`rt_single_tax_at_22`) | 5,800 | 5,987 | 5,987 | 5978.50 – 5,987 | october |
| 4.01 | Table 3 Unmarried individuals: tax at start of 24% bracket (`rt_single_tax_at_24`) | 17,966 | 18,549 | 18,549 | 18,524 – 18,549 | october |
| 4.01 | Table 3 Unmarried individuals: tax at start of 32% bracket (`rt_single_tax_at_32`) | 41,024 | 42,357 | 42,357 | 42,308 – 42,357 | october |
| 4.01 | Table 3 Unmarried individuals: tax at start of 35% bracket (`rt_single_tax_at_35`) | 58,448 | 60,349 | 60,349 | 60,276 – 60,349 | october |
| 4.01 | Table 3 Unmarried individuals: tax at start of 37% bracket (`rt_single_tax_at_37`) | 192979.25 | 199237.75 | 199237.75 | 198989.75 – 199237.75 | october |
| 4.01 | Table 4 Married filing separately: top of 10% bracket / start of 12% bracket (`rt_mfs_10_12`) | 12,400 | 12,800 | 12,800 | 12,775 – 12,800 | october |
| 4.01 | Table 4 Married filing separately: top of 12% bracket / start of 22% bracket (`rt_mfs_12_22`) | 50,400 | 52,025 | 52,025 | 51,950 – 52,025 | october |
| 4.01 | Table 4 Married filing separately: top of 22% bracket / start of 24% bracket (`rt_mfs_22_24`) | 105,700 | 109,125 | 109,125 | 108,975 – 109,125 | october |
| 4.01 | Table 4 Married filing separately: top of 24% bracket / start of 32% bracket (`rt_mfs_24_32`) | 201,775 | 208,325 | 208,325 | 208,075 – 208,325 | october |
| 4.01 | Table 4 Married filing separately: top of 32% bracket / start of 35% bracket (`rt_mfs_32_35`) | 256,225 | 264,550 | 264,550 | 264,225 – 264,550 | october |
| 4.01 | Table 4 Married filing separately: top of 35% bracket / start of 37% bracket (`rt_mfs_35_37`) | 384,350 | 396,825 | 396,825 | 396,325 – 396,825 | october |
| 4.01 | Table 4 Married filing separately: tax at start of 12% bracket (`rt_mfs_tax_at_12`) | 1,240 | 1,280 | 1,280 | 1277.50 – 1,280 | october |
| 4.01 | Table 4 Married filing separately: tax at start of 22% bracket (`rt_mfs_tax_at_22`) | 5,800 | 5,987 | 5,987 | 5978.50 – 5,987 | october |
| 4.01 | Table 4 Married filing separately: tax at start of 24% bracket (`rt_mfs_tax_at_24`) | 17,966 | 18,549 | 18,549 | 18,524 – 18,549 | october |
| 4.01 | Table 4 Married filing separately: tax at start of 32% bracket (`rt_mfs_tax_at_32`) | 41,024 | 42,357 | 42,357 | 42,308 – 42,357 | october |
| 4.01 | Table 4 Married filing separately: tax at start of 35% bracket (`rt_mfs_tax_at_35`) | 58,448 | 60,349 | 60,349 | 60,276 – 60,349 | october |
| 4.01 | Table 4 Married filing separately: tax at start of 37% bracket (`rt_mfs_tax_at_37`) | 103291.75 | 106645.25 | 106645.25 | 106,511 – 106645.25 | october |
| 4.01 | Table 5 Estates and trusts: top of 10% bracket / start of 24% bracket (`rt_estate_10_24`) | 3,300 | 3,350 | 3,400 | 3,400 | ambiguity |
| 4.01 | Table 5 Estates and trusts: top of 24% bracket / start of 35% bracket (`rt_estate_24_35`) | 11,700 | 12,100 | 12,100 | 12,050 – 12,100 | october |
| 4.01 | Table 5 Estates and trusts: top of 35% bracket / start of 37% bracket (`rt_estate_35_37`) | 16,000 | 16,500 | 16,500 | 16,500 | firm |
| 4.01 | Table 5 Estates and trusts: tax at start of 24% bracket (`rt_estate_tax_at_24`) | 330 | 335 | 340 | 340 | ambiguity |
| 4.01 | Table 5 Estates and trusts: tax at start of 35% bracket (`rt_estate_tax_at_35`) | 2,346 | 2,435 | 2,428 | 2,416 – 2,428 | ambiguity+october |
| 4.01 | Table 5 Estates and trusts: tax at start of 37% bracket (`rt_estate_tax_at_37`) | 3,851 | 3,975 | 3,968 | 3,968 – 3973.50 | ambiguity+october |
| 4.02 | Kiddie tax: amount in §1(g)(4)(A)(ii)(I) (`kiddie_unearned_offset`) | 1,350 | 1,400 | 1,400 | 1,400 | firm |
| 4.02 | Kiddie tax: parental-election gross income ceiling (10 × §1(g)(4)(A)(ii)(I) amount) (`kiddie_parent_election_max`) | 13,500 | 14,000 | 14,000 | 14,000 | firm |
| 4.03 | Maximum zero rate amount, MFJ / surviving spouse (`cg0_mfj`) | 98,900 | 102,100 | 102,100 | 101,950 – 102,100 | october |
| 4.03 | Maximum zero rate amount, head of household (`cg0_hoh`) | 66,200 | 68,350 | 68,350 | 68,300 – 68,350 | october |
| 4.03 | Maximum zero rate amount, estates and trusts (`cg0_estate`) | 3,300 | 3,400 | 3,400 | 3,400 | firm |
| 4.03 | Maximum zero rate amount, MFS (`cg0_mfs`) | 49,450 | 51,050 | 51,050 | 50,975 – 51,050 | october |
| 4.03 | Maximum zero rate amount, all other individuals (`cg0_single`) | 49,450 | 51,050 | 51,050 | 50,975 – 51,050 | october |
| 4.03 | Maximum 15% rate amount, MFJ / surviving spouse (`cg15_mfj`) | 613,700 | 633,600 | 633,600 | 632,800 – 633,600 | october |
| 4.03 | Maximum 15% rate amount, head of household (`cg15_hoh`) | 579,600 | 598,400 | 598,400 | 597,650 – 598,400 | october |
| 4.03 | Maximum 15% rate amount, all other individuals (`cg15_single`) | 545,500 | 563,200 | 563,200 | 562,500 – 563,200 | october |
| 4.03 | Maximum 15% rate amount, estates and trusts (`cg15_estate`) | 16,250 | 16,750 | 16,750 | 16,750 | firm |
| 4.03 | Maximum 15% rate amount, MFS (`cg15_mfs`) | 306,850 | 316,800 | 316,800 | 316,400 – 316,800 | october |
| 4.10 | AMT exemption, joint return / surviving spouse (`amt_ex_mfj`) | 140,200 | 144,700 | 144,700 | 144,500 – 144,700 | october |
| 4.10 | AMT exemption, unmarried individuals (`amt_ex_single`) | 90,100 | 93,000 | 93,000 | 92,900 – 93,000 | october |
| 4.10 | AMT exemption, married filing separately (`amt_ex_mfs`) | 70,100 | 72,350 | 72,350 | 72,250 – 72,350 | october |
| 4.10 | AMT exemption, estates and trusts (`amt_ex_estate`) | 31,400 | 32,500 | 32,500 | 32,400 – 32,500 | october |
| 4.10 | AMT: excess taxable income above which 28% applies, all other taxpayers (`amt_28pct_other`) | 244,500 | 252,500 | 252,500 | 252,100 – 252,500 | october |
| 4.10 | AMT: 28% threshold, married filing separately (`amt_28pct_mfs`) | 122,250 | 126,250 | 126,250 | 126,050 – 126,250 | october |
| 4.10 | AMT exemption phaseout threshold, joint / surviving spouse (`amt_phaseout_mfj`) | 1,000,000 | 1,031,900 | 1,031,900 | 1,030,600 – 1,031,900 | new-base+october+ambiguity |
| 4.10 | AMT exemption phaseout threshold, unmarried individuals (`amt_phaseout_single`) | 500,000 | 515,950 | 515,950 | 515,300 – 515,950 | new-base+october |
| 4.10 | AMT exemption phaseout threshold, married filing separately (`amt_phaseout_mfs`) | 500,000 | 515,950 | 515,950 | 515,300 – 515,950 | new-base+october |
| 4.10 | AMT exemption phaseout threshold, estates and trusts (`amt_phaseout_estate`) | 104,800 | 108,200 | 108,200 | 108,050 – 108,200 | october |
| 4.10 | AMT exemption complete phaseout amount, mfj (`amt_complete_phaseout_mfj`) | 1,280,400 | 1,321,300 | 1,321,300 | 1,319,600 – 1,321,300 | october |
| 4.10 | AMT exemption complete phaseout amount, single (`amt_complete_phaseout_single`) | 680,200 | 701,950 | 701,950 | 701,100 – 701,950 | october |
| 4.10 | AMT exemption complete phaseout amount, mfs (`amt_complete_phaseout_mfs`) | 640,200 | 660,650 | 660,650 | 659,800 – 660,650 | october |
| 4.10 | AMT exemption complete phaseout amount, estate (`amt_complete_phaseout_estate`) | 167,600 | 173,200 | 173,200 | 172,850 – 173,200 | october |
| 4.11 | AMT exemption cap for child subject to kiddie tax: earned income plus (`amt_kiddie_exemption_addon`) | 9,750 | 10,050 | 10,050 | 10,050 | irs-rule |
| 4.14(1) | Basic standard deduction, unmarried (other than HoH/surviving spouse) (`std_deduction_single`) | 16,100 | 16,600 | 16,600 | 16,600 | firm |
| 4.14(1) | Basic standard deduction, head of household (`std_deduction_hoh`) | 24,150 | 24,925 | 24,950 | 24,900 – 24,950 | irs-rule+october |
| 4.14(1) | Basic standard deduction, MFJ / surviving spouse (`std_deduction_mfj`) | 32,200 | 33,200 | 33,200 | 33,200 | firm |
| 4.14(1) | Basic standard deduction, married filing separately (`std_deduction_mfs`) | 16,100 | 16,600 | 16,600 | 16,600 | firm |
| 4.14(2) | Dependent standard deduction floor (§63(c)(5)(A)) (`std_deduction_dependent_min`) | 1,350 | 1,400 | 1,400 | 1,400 | firm |
| 4.14(2) | Dependent standard deduction: earned income plus (§63(c)(5)(B)) (`std_deduction_dependent_earned_addon`) | 450 | 500 | 500 | 500 | firm |
| 4.14(3) | Additional standard deduction, aged or blind (married / surviving spouse) (`std_additional_aged_blind`) | 1,650 | 1,700 | 1,700 | 1,700 | firm |
| 4.14(3) | Additional standard deduction, aged or blind, unmarried and not surviving spouse (`std_additional_aged_blind_unmarried`) | 2,050 | 2,100 | 2,100 | 2,100 | firm |
| 4.23 | Qualifying relative gross income limit = exemption amount §151(d) (`qualifying_relative_gross_income_limit`) | 5,300 | 5,500 | 5,500 | 5,450 – 5,500 | october |
| 4.26 | §199A threshold amount, all other returns (`qbi_threshold_other`) | 201,750 | 208,300 | 208,300 | 208,050 – 208,300 | october |
| 4.26 | §199A threshold amount, married filing separately (`qbi_threshold_mfs`) | 201,775 | 208,325 | 208,325 | 208,075 – 208,325 | october |
| 4.26 | §199A threshold amount, MFJ (`qbi_threshold_mfj`) | 403,500 | 416,600 | 416,600 | 416,100 – 416,600 | october |
| 4.26 | §199A phase-in range end, MFJ (`qbi_phasein_end_mfj`) | 553,500 | 566,600 | 566,600 | 566,100 – 566,600 | october |
| 4.26 | §199A phase-in range end, MFS (`qbi_phasein_end_mfs`) | 276,775 | 283,325 | 283,325 | 283,075 – 283,325 | october |
| 4.26 | §199A phase-in range end, all other returns (`qbi_phasein_end_other`) | 276,750 | 283,300 | 283,300 | 283,050 – 283,300 | october |
| 4.35 | Qualified disability trust deduction §642(b)(2)(C)(i) (`qualified_disability_trust_exemption`) | 5,300 | 5,450 | 5,400 | 5,400 | irs-rule |
| 4.50 | Levy exempt amount: per-dependent amount §6334(d)(4)(B) (`levy_exempt_dependent_amount`) | 5,300 | 5,450 | 5,400 | 5,400 | irs-rule |
| 4.04(1) | Adoption credit, child with special needs (§23(a)(3)) (`adoption_credit_special_needs`) | 17,670 | 18,250 | 18,250 | 18,220 – 18,250 | october |
| 4.04(2) | Adoption credit, maximum qualified adoption expenses (§23(b)(1)) (`adoption_credit_dollar_limit`) | 17,670 | 18,250 | 18,250 | 18,220 – 18,250 | october |
| 4.04(2) | Adoption credit, MAGI phaseout threshold (§23(b)(2)(A)(i)) (`adoption_credit_phaseout_threshold`) | 265,080 | 273,680 | 273,680 | 273,340 – 273,680 | october |
| 4.04(2) | Adoption credit, MAGI at which fully phased out (`adoption_credit_phaseout_complete`) | 305,080 | 313,680 | 313,680 | 313,340 – 313,680 | october |
| 4.04(3) | Adoption credit, refundable portion (§23(a)(4)) (`adoption_credit_refundable_portion`) | 5,120 | 5,280 | 5,280 | 5,280 | firm |
| 4.05(1) | Child tax credit, maximum per qualifying child (§24(a) via §24(h)(2)) (`ctc_max_per_child`) | 2,200 | 2,300 | 2,300 | 2,300 | firm |
| 4.05(2) | Child tax credit, maximum refundable amount per child (§24(h)(5) / §24(d)(1)(A)) (`ctc_refundable_max`) | 1,700 | 1,800 | 1,800 | 1,800 | firm |
| 4.06(1) | EITC earned income amount, one qualifying child (`eitc_earned_income_amount_1`) | 13,020 | 13,450 | 13,450 | 13,430 – 13,450 | october |
| 4.06(1) | EITC maximum credit, one qualifying child (`eitc_max_credit_1`) | 4,427 | 4,573 | 4,573 | 4,566 – 4,573 | october |
| 4.06(1) | EITC threshold phaseout amount, one qualifying child, all other filing statuses (`eitc_phaseout_threshold_1_other`) | 23,890 | 24,660 | 24,660 | 24,630 – 24,660 | october |
| 4.06(1) | EITC threshold phaseout amount, one qualifying child, married filing jointly (`eitc_phaseout_threshold_1_mfj`) | 31,160 | 32,170 | 32,170 | 32,130 – 32,170 | october |
| 4.06(1) | EITC completed phaseout amount, one qualifying child, all other filing statuses (`eitc_phaseout_complete_1_other`) | 51,593 | 53,277 | 53,277 | 53,203 – 53,277 | october |
| 4.06(1) | EITC completed phaseout amount, one qualifying child, married filing jointly (`eitc_phaseout_complete_1_mfj`) | 58,863 | 60,787 | 60,787 | 60,703 – 60,787 | october |
| 4.06(1) | EITC earned income amount, two qualifying children (`eitc_earned_income_amount_2`) | 18,290 | 18,880 | 18,880 | 18,860 – 18,880 | october |
| 4.06(1) | EITC maximum credit, two qualifying children (`eitc_max_credit_2`) | 7,316 | 7,552 | 7,552 | 7,544 – 7,552 | october |
| 4.06(1) | EITC threshold phaseout amount, two qualifying children, all other filing statuses (`eitc_phaseout_threshold_2_other`) | 23,890 | 24,660 | 24,660 | 24,630 – 24,660 | october |
| 4.06(1) | EITC threshold phaseout amount, two qualifying children, married filing jointly (`eitc_phaseout_threshold_2_mfj`) | 31,160 | 32,170 | 32,170 | 32,130 – 32,170 | october |
| 4.06(1) | EITC completed phaseout amount, two qualifying children, all other filing statuses (`eitc_phaseout_complete_2_other`) | 58,629 | 60,519 | 60,519 | 60,451 – 60,519 | october |
| 4.06(1) | EITC completed phaseout amount, two qualifying children, married filing jointly (`eitc_phaseout_complete_2_mfj`) | 65,899 | 68,029 | 68,029 | 67,951 – 68,029 | october |
| 4.06(1) | EITC earned income amount, three or more qualifying children (`eitc_earned_income_amount_3`) | 18,290 | 18,880 | 18,880 | 18,860 – 18,880 | october |
| 4.06(1) | EITC maximum credit, three or more qualifying children (`eitc_max_credit_3`) | 8,231 | 8,496 | 8,496 | 8,487 – 8,496 | october |
| 4.06(1) | EITC threshold phaseout amount, three or more qualifying children, all other filing statuses (`eitc_phaseout_threshold_3_other`) | 23,890 | 24,660 | 24,660 | 24,630 – 24,660 | october |
| 4.06(1) | EITC threshold phaseout amount, three or more qualifying children, married filing jointly (`eitc_phaseout_threshold_3_mfj`) | 31,160 | 32,170 | 32,170 | 32,130 – 32,170 | october |
| 4.06(1) | EITC completed phaseout amount, three or more qualifying children, all other filing statuses (`eitc_phaseout_complete_3_other`) | 62,974 | 65,002 | 65,002 | 64,929 – 65,002 | october |
| 4.06(1) | EITC completed phaseout amount, three or more qualifying children, married filing jointly (`eitc_phaseout_complete_3_mfj`) | 70,244 | 72,512 | 72,512 | 72,429 – 72,512 | october |
| 4.06(1) | EITC earned income amount, no qualifying children (`eitc_earned_income_amount_0`) | 8,680 | 8,960 | 8,960 | 8,950 – 8,960 | october |
| 4.06(1) | EITC maximum credit, no qualifying children (`eitc_max_credit_0`) | 664 | 685 | 685 | 685 | firm |
| 4.06(1) | EITC threshold phaseout amount, no qualifying children, all other filing statuses (`eitc_phaseout_threshold_0_other`) | 10,860 | 11,210 | 11,210 | 11,200 – 11,210 | october |
| 4.06(1) | EITC threshold phaseout amount, no qualifying children, married filing jointly (`eitc_phaseout_threshold_0_mfj`) | 18,140 | 18,730 | 18,730 | 18,700 – 18,730 | october |
| 4.06(1) | EITC completed phaseout amount, no qualifying children, all other filing statuses (`eitc_phaseout_complete_0_other`) | 19,540 | 20,164 | 20,164 | 20,154 – 20,164 | october |
| 4.06(1) | EITC completed phaseout amount, no qualifying children, married filing jointly (`eitc_phaseout_complete_0_mfj`) | 26,820 | 27,684 | 27,684 | 27,654 – 27,684 | october |
| 4.06(2) | EITC disqualified (investment) income limit (§32(i)(1)) (`eitc_investment_income_limit`) | 12,200 | 12,600 | 12,600 | 12,600 | firm |
| 4.07 | LIHTC rehabilitation expenditures, per low-income unit qualified basis (§42(e)(3)(A)(ii)(II)) (`lihtc_rehab_per_unit_min`) | 8,700 | 9,000 | 9,000 | 9,000 | firm |
| 4.08 | LIHTC State housing credit ceiling, per-capita amount (`lihtc_state_ceiling_per_capita`) | 3.42 | 3.53 | 3.53 | 3.53 | firm |
| 4.08 | LIHTC State housing credit ceiling, minimum (small-State) amount (`lihtc_state_ceiling_minimum`) | 3,953,600 | 4,082,400 | 4,082,400 | 4,076,800 – 4,082,400 | october |
| 4.09 | Small employer health insurance credit, dollar amount (§45R(d)(3)(B)) (`sbhic_average_wage_amount`) | 34,100 | 35162.04 | 35,200 | 35,100 – 35,200 | irs-rule+october |
| 4.12 | Eligible educator expenses above-the-line deduction limit (§62(a)(2)(D)) (`educator_expense_limit`) | 350 | 350 | 350 | 350 | firm |
| 4.15 | Health FSA salary reduction limit (§125(i)) (`health_fsa_salary_reduction_limit`) | 3,400 | 3,500 | 3,500 | 3,500 | firm |
| 4.15 | Health FSA maximum carryover of unused amounts (`health_fsa_carryover_max`) | 680 | 700 | 700 | 700 | firm |
| 4.16 | Qualified transportation fringe monthly limit, commuter highway vehicle + transit pass (§132(f)(2)(A)) (`qtf_monthly_transit_vanpool`) | 340 | 350 | 350 | 350 | firm |
| 4.16 | Qualified transportation fringe monthly limit, qualified parking (§132(f)(2)(B)) (`qtf_monthly_parking`) | 340 | 350 | 350 | 350 | firm |
| 4.17 | Savings bond interest exclusion, MAGI phaseout threshold, joint return (`savings_bond_phaseout_joint`) | 152,650 | 157,600 | 157,600 | 157,400 – 157,600 | october |
| 4.17 | Savings bond interest exclusion, MAGI phaseout threshold, other returns (`savings_bond_phaseout_other`) | 101,800 | 105,100 | 105,100 | 104,950 – 105,100 | october |
| 4.17 | Savings bond interest exclusion, fully phased out, joint return (`savings_bond_phaseout_complete_joint`) | 182,650 | 187,600 | 187,600 | 187,400 – 187,600 | october |
| 4.17 | Savings bond interest exclusion, fully phased out, other returns (`savings_bond_phaseout_complete_other`) | 116,800 | 120,100 | 120,100 | 119,950 – 120,100 | october |
| 4.18 | Adoption assistance exclusion, child with special needs (§137(a)(2)) (`adoption_assistance_special_needs`) | 17,670 | 18,250 | 18,250 | 18,220 – 18,250 | october |
| 4.18 | Adoption assistance exclusion, maximum (§137(b)(1)) (`adoption_assistance_dollar_limit`) | 17,670 | 18,250 | 18,250 | 18,220 – 18,250 | october |
| 4.18 | Adoption assistance exclusion, MAGI phaseout threshold (§137(b)(2)(A)) (`adoption_assistance_phaseout_threshold`) | 265,080 | 273,680 | 273,680 | 273,340 – 273,680 | october |
| 4.18 | Adoption assistance exclusion, fully phased out (`adoption_assistance_phaseout_complete`) | 305,080 | 313,680 | 313,680 | 313,340 – 313,680 | october |
| 4.19 | Private activity bond volume cap, per-capita amount (`pab_volume_cap_per_capita`) | 135 | 135 | 135 | 135 | firm |
| 4.19 | Private activity bond volume cap, State minimum (`pab_volume_cap_minimum`) | 397,625,000 | 410,520,000 | 410,520,000 | 410,010,000 – 410,520,000 | october |
| 4.20 | Agricultural bonds, first-time farmer loan limit (§147(c)(2)(A)) (`ag_bond_first_time_farmer_limit`) | 682,700 | 704,800 | 704,800 | 704,000 – 704,800 | october |
| 4.21 | Arbitrage rebate computation credit (26 CFR 1.148-3(d)(4)) (`arbitrage_computation_credit`) | 2,170 | 2,240 | 2,240 | 2,240 | firm |
| 4.22 | GIC broker fee safe harbor, per-contract cap ((B)(1)(i)(A)) (`gic_broker_fee_cap`) | 51,000 | 53,000 | 53,000 | 53,000 | firm |
| 4.22 | GIC broker fee safe harbor, minimum ('if more') amount ((B)(1)(i)(B)) (`gic_broker_fee_floor`) | 5,000 | 5,000 | 5,000 | 5,000 | firm |
| 4.22 | GIC broker fee safe harbor, per-issue aggregate ((B)(1)(ii)) (`gic_broker_fee_per_issue`) | 145,000 | 149,000 | 149,000 | 149,000 | firm |
| 4.22 | GIC broker fee safe harbor, percentage of computational base (`gic_broker_fee_pct`) | 0.2 | 0.2 | 0.2 | 0.2 | firm |
| 4.24 | §179 expensing dollar limitation (§179(b)(1)) (`sec179_dollar_limit`) | 2,560,000 | 2,640,000 | 2,640,000 | 2,640,000 | firm |
| 4.24 | §179 investment phaseout threshold (§179(b)(2)) (`sec179_phaseout_threshold`) | 4,090,000 | 4,230,000 | 4,230,000 | 4,220,000 – 4,230,000 | october |
| 4.24 | §179 sport utility vehicle cost limit (§179(b)(5)(A)) (`sec179_suv_limit`) | 32,000 | 33,100 | 33,100 | 33,000 – 33,100 | october |
| 4.25 | §179D applicable dollar value, base ($0.50) (`sec179d_base_value`) | 0.59 | 0.61 | 0.61 | 0.61 | firm |
| 4.25 | §179D applicable dollar value, cap ($1.00) (`sec179d_base_cap`) | 1.19 | 1.23 | 1.23 | 1.23 | firm |
| 4.25 | §179D increment per percentage point ($0.02) (`sec179d_base_step`) | 0.02 | 0.02 | 0.02 | 0.02 | firm |
| 4.25 | §179D increased (prevailing wage/apprenticeship) value ($2.50) (`sec179d_pw_value`) | 2.97 | 3.07 | 3.07 | 3.06 – 3.07 | october |
| 4.25 | §179D increased cap ($5.00) (`sec179d_pw_cap`) | 5.94 | 6.13 | 6.13 | 6.13 | firm |
| 4.25 | §179D increased increment per percentage point ($0.10) (`sec179d_pw_step`) | 0.12 | 0.12 | 0.12 | 0.12 | firm |
| 4.13 | Pipeline rig-related expenses deemed substantiated, per hour (no fuel provided) (`pipeline_rig_hourly`) | 23 | 23 | 23 | 23 | firm |
| 4.13 | Pipeline rig-related expenses deemed substantiated, per hour (employer provides/reimburses fuel) (`pipeline_rig_hourly_fuel_provided`) | 14 | 14 | 14 | 14 | firm |
| 4.27 | Eligible LTC premium limit, age 40 or less (`ltc_premium_age_40_or_less`) | 500 | 340 | 500 | 500 | irs-rule |
| 4.27 | Eligible LTC premium limit, age >40 to 50 (`ltc_premium_age_41_to_50`) | 930 | 645 | 940 | 940 | irs-rule |
| 4.27 | Eligible LTC premium limit, age >50 to 60 (`ltc_premium_age_51_to_60`) | 1,860 | 1,280 | 1,890 | 1,890 | irs-rule |
| 4.27 | Eligible LTC premium limit, age >60 to 70 (`ltc_premium_age_61_to_70`) | 4,960 | 3,410 | 5,030 | 5,030 | irs-rule |
| 4.27 | Eligible LTC premium limit, age over 70 (`ltc_premium_age_over_70`) | 6,200 | 4,270 | 6,290 | 6,290 | irs-rule |
| 4.28 | Archer MSA HDHP self-only: minimum annual deductible (`msa_hdhp_self_deductible_min`) | 2,900 | 3,000 | 3,000 | 3,000 | firm |
| 4.28 | Archer MSA HDHP self-only: maximum annual deductible (`msa_hdhp_self_deductible_max`) | 4,400 | 4,550 | 4,550 | 4,500 – 4,550 | october |
| 4.28 | Archer MSA HDHP self-only: out-of-pocket maximum (`msa_hdhp_self_oop_max`) | 5,850 | 6,050 | 6,050 | 6,050 | firm |
| 4.28 | Archer MSA HDHP family: minimum annual deductible (`msa_hdhp_family_deductible_min`) | 5,850 | 6,050 | 6,050 | 6,050 | firm |
| 4.28 | Archer MSA HDHP family: maximum annual deductible (`msa_hdhp_family_deductible_max`) | 8,750 | 9,050 | 9,050 | 9,050 | firm |
| 4.28 | Archer MSA HDHP family: out-of-pocket maximum (`msa_hdhp_family_oop_max`) | 10,700 | 11,050 | 11,050 | 11,050 | firm |
| 4.29 | Student loan interest deduction maximum (`student_loan_interest_max_deduction`) | 2,500 | 2,500 | 2,500 | 2,500 | firm |
| 4.29 | Student loan interest phaseout begins (MAGI), other than joint (`student_loan_interest_phaseout_start`) | 85,000 | 90,000 | 90,000 | 90,000 | firm |
| 4.29 | Student loan interest phaseout begins (MAGI), joint return (`student_loan_interest_phaseout_start_joint`) | 175,000 | 180,000 | 180,000 | 180,000 | firm |
| 4.29 | Student loan interest fully phased out (MAGI), other than joint (`student_loan_interest_phaseout_end`) | 100,000 | 105,000 | 105,000 | 105,000 | firm |
| 4.29 | Student loan interest fully phased out (MAGI), joint return (`student_loan_interest_phaseout_end_joint`) | 205,000 | 210,000 | 210,000 | 210,000 | firm |
| 4.30 | Gross receipts test, §448(c) (3-year average) (`cash_method_gross_receipts_limit`) | 32,000,000 | 33,000,000 | 33,000,000 | 33,000,000 | firm |
| 4.31 | Excess business loss threshold (`excess_business_loss_threshold`) | 256,000 | 264,000 | 264,000 | 264,000 | firm |
| 4.31 | Excess business loss threshold, joint return (`excess_business_loss_threshold_joint`) | 512,000 | 528,000 | 528,000 | 528,000 | firm |
| 4.32 | Agricultural/horticultural organization annual dues limit (`ag_hort_dues_limit`) | 212 | 218.44 | 218 | 218 | irs-rule+october |
| 4.33(1) | Low cost article, §513(h)(2) (`low_cost_article`) | 13.90 | 14.33 | 14.30 | 14.30 | irs-rule+october |
| 4.33(2) | Rev. Proc. 90-12 $5 guideline (token items / low cost article) (`insubstantial_benefit_5`) | 13.90 | 14.33 | 14.30 | 14.30 | irs-rule+october |
| 4.33(2) | Rev. Proc. 90-12 $25 payment guideline (`insubstantial_benefit_25`) | 69.50 | 71.64 | 71.50 | 71.50 | irs-rule+october |
| 4.33(2) | Rev. Proc. 90-12 $50 benefit guideline (`insubstantial_benefit_50`) | 139 | 143.27 | 143 | 143 | irs-rule+october |
| 4.34 | ABLE account aggregate annual contribution limit (§529A(b)(2)(B)(i)) (`able_annual_contribution_limit`) | 20,000 | 20,000 | 20,000 | 20,000 | firm |
| 4.36 | §831(b) net/direct written premiums limit (`small_insurer_831b_premium_limit`) | 2,900,000 | 3,000,000 | 3,000,000 | 3,000,000 | firm |
| 4.37 | Covered expatriate average annual net income tax threshold (§877(a)(2)(A)) (`expatriate_avg_income_tax_threshold`) | 211,000 | 218,000 | 218,000 | 217,000 – 218,000 | ambiguity+october |
| 4.38 | Mark-to-market gain exclusion for covered expatriates (`expatriation_gain_exclusion`) | 910,000 | 940,000 | 940,000 | 939,000 – 940,000 | october |
| 4.39 | Foreign earned income exclusion amount (`foreign_earned_income_exclusion`) | 132,900 | 137,300 | 137,300 | 137,100 – 137,300 | october |
| 4.40 | Qualified debt instrument stated principal limit (§1274A(b)) (`qualified_debt_instrument_max`) | 7,462,600 | 7,704,600 | 7,704,600 | 7,695,000 – 7,704,600 | october |
| 4.40 | Cash method debt instrument stated principal limit (§1274A(c)(2)(A)) (`cash_method_debt_instrument_max`) | 5,330,500 | 5,503,300 | 5,503,300 | 5,496,500 – 5,503,300 | october |
| 4.41 | §2032A aggregate decrease limit (`special_use_valuation_max_decrease`) | 1,460,000 | 1,500,000 | 1,500,000 | 1,500,000 | firm |
| 4.42(1) | Annual gift tax exclusion per donee (`gift_annual_exclusion`) | 19,000 | 20,000 | 20,000 | 20,000 | firm |
| 4.42(2) | Annual exclusion for gifts to noncitizen spouse (§2523(i)(2)) (`gift_noncitizen_spouse_exclusion`) | 194,000 | 201,000 | 201,000 | 200,000 – 201,000 | october |
| 4.42(3) | §2801(c) exception for covered gifts/bequests from covered expatriate (`covered_gift_2801_exception`) | 19,000 | 20,000 | 20,000 | 20,000 | firm |
| 4.43 | Tax per arrow shaft (`arrow_shaft_tax`) | 0.65 | 0.67 | 0.67 | 0.67 | firm |
| 4.44 | Domestic segment tax per segment (`air_domestic_segment_tax`) | 5.30 | 5.50 | 5.50 | 5.50 | firm |
| 4.44 | International air transportation facilities tax (`air_international_tax`) | 23.40 | 24.10 | 24.10 | 24.10 | firm |
| 4.44 | International facilities tax rate for domestic segment beginning/ending in Alaska or Hawaii (departures) (`air_alaska_hawaii_tax`) | 11.70 | 12.10 | 12.10 | 12.10 | firm |
| 4.45 | Hazardous Substance Superfund financing rate on crude oil/petroleum, per barrel (`superfund_petroleum_rate`) | 0.18 | 0.18 | 0.18 | 0.18 | firm |
| 4.45 | Oil Spill Liability Trust Fund financing rate, per barrel (`oil_spill_liability_rate`) | 0.09 | 0 | 0 | 0 | year |
| 4.45 | §4611 total tax on crude oil/petroleum products, per barrel (as in Rev. Proc.) (`petroleum_tax_total`) | 0.27 | 0.18 | 0.18 | 0.18 | year |
| 4.46 | §6033(e)(3) reporting exception: annual dues per person/family/entity ($X or less), Rev. Proc. 98-19 §5.05 (`eo_lobbying_dues_limit_6033e3`) | 147 | 151 | 151 | 151 | ambiguity |
| 4.47 | §6039F foreign gifts reporting threshold (aggregate value exceeds) (`foreign_gift_reporting_threshold_6039F`) | 20,573 | 21240.31 | 21,240 | 21,214 – 21,240 | irs-rule+october |
| 4.48(1) | §6323(b)(4) casual sale of personal property: lien not valid if price less than (`lien_casual_sale_6323b4`) | 2,000 | 2,070 | 2,070 | 2,060 – 2,070 | october |
| 4.48(2) | §6323(b)(7) mechanic's lienor, residential repair: contract price not more than (`lien_mechanics_residential_6323b7`) | 10,010 | 10,340 | 10,340 | 10,320 – 10,340 | october |
| 4.49(1) | §6334(a)(2) levy-exempt fuel, provisions, furniture, personal effects, arms, livestock, poultry (value cap) (`levy_exempt_household_6334a2`) | 11,980 | 12,370 | 12,370 | 12,350 – 12,370 | october |
| 4.49(2) | §6334(a)(3) levy-exempt books and tools of trade (value cap) (`levy_exempt_tools_6334a3`) | 5,990 | 6,180 | 6,180 | 6,180 | firm |
| 4.51 | §6601(j)(2)(A) dollar amount for the '2-percent portion' (decedents dying in 2026) (`estate_installment_2pct_portion_amount_6601j`) | 1,940,000 | 2,010,000 | 2,010,000 | 2,000,000 – 2,010,000 | october |
| 4.52 | §6651(a) last sentence: minimum addition for failure to file income tax return >60 days late (lesser of $X or 100% of tax), returns required to be filed in 2027 (`ftf_min_addition_6651a`) | 535 | — | 555 | 550 – 555 | year+october |
| 4.53(1)(A) | §6652(c)(1)(A) exempt org / political org return: daily penalty — returns required to be filed in 2027 (`eo990_daily_6652c1A`) | 25 | — | 25 | 25 | year |
| 4.53(1)(A) | §6652(c)(1)(A) maximum per return (lesser of $X or 5% of gross receipts) — returns required to be filed in 2027 (`eo990_max_6652c1A`) | 13,000 | — | 13,500 | 13,500 | year |
| 4.53(1)(A) | §6652(c)(1)(A) gross receipts threshold for large-organization rule (exceeding) — returns required to be filed in 2027 (`eo990_large_gross_receipts_threshold_6652c1A`) | 1,339,500 | — | 1,383,000 | 1,381,000 – 1,383,000 | year+october |
| 4.53(1)(A) | §6652(c)(1)(A) large organization: daily penalty — returns required to be filed in 2027 (`eo990_large_daily_6652c1A`) | 130 | — | 135 | 135 | year |
| 4.53(1)(A) | §6652(c)(1)(A) large organization: maximum — returns required to be filed in 2027 (`eo990_large_max_6652c1A`) | 66,500 | — | 69,000 | 69,000 | year |
| 4.53(1)(B) | §6652(c)(1)(B)(ii) managers: daily penalty — returns required to be filed in 2027 (`eo990_managers_daily_6652c1B`) | 10 | — | 10 | 10 | year |
| 4.53(1)(B) | §6652(c)(1)(B)(ii) managers: maximum — returns required to be filed in 2027 (`eo990_managers_max_6652c1B`) | 6,500 | — | 6,500 | 6,500 | year |
| 4.53(1)(C) | §6652(c)(1)(C) public inspection of annual returns/reports: daily — returns required to be filed in 2027 (`eo_public_inspection_returns_daily_6652c1C`) | 25 | — | 25 | 25 | year |
| 4.53(1)(C) | §6652(c)(1)(C) public inspection of annual returns/reports: maximum — returns required to be filed in 2027 (`eo_public_inspection_returns_max_6652c1C`) | 13,000 | — | 13,500 | 13,500 | year |
| 4.53(1)(D) | §6652(c)(1)(D) public inspection of exemption applications / notice of status: daily (no limit) — returns required to be filed in 2027 (`eo_public_inspection_applications_daily_6652c1D`) | 25 | — | 25 | 25 | year |
| 4.53(2)(A) | §6652(c)(2)(A) org/trust return under §6034 or §6043(b): daily — returns required to be filed in 2027 (`trust_6034_daily_6652c2A`) | 10 | — | 10 | 10 | year |
| 4.53(2)(A) | §6652(c)(2)(A) org/trust: maximum — returns required to be filed in 2027 (`trust_6034_max_6652c2A`) | 6,500 | — | 6,500 | 6,500 | year |
| 4.53(2)(B) | §6652(c)(2)(B) managers: daily — returns required to be filed in 2027 (`trust_6034_managers_daily_6652c2B`) | 10 | — | 10 | 10 | year |
| 4.53(2)(B) | §6652(c)(2)(B) managers: maximum — returns required to be filed in 2027 (`trust_6034_managers_max_6652c2B`) | 6,500 | — | 6,500 | 6,500 | year |
| 4.53(2)(C)(ii) | §6652(c)(2)(C)(ii) split-interest trust gross income threshold (in excess of) — returns required to be filed in 2027 (`split_interest_trust_large_gross_income_threshold_6652c2Cii`) | 334,500 | — | 345,500 | 345,000 – 345,500 | year+october |
| 4.53(2)(C)(ii) | §6652(c)(2)(C)(ii) trust with gross income above threshold: daily — returns required to be filed in 2027 (`split_interest_trust_large_daily_6652c2Cii`) | 130 | — | 135 | 135 | year |
| 4.53(2)(C)(ii) | §6652(c)(2)(C)(ii) trust above threshold: maximum — returns required to be filed in 2027 (`split_interest_trust_large_max_6652c2Cii`) | 66,500 | — | 69,000 | 69,000 | year |
| 4.53(3)(A) | §6652(c)(3)(A) §6033(a)(2) disclosure by tax-exempt entity: daily — returns required to be filed in 2027 (`reportable_txn_disclosure_daily_6652c3A`) | 130 | — | 135 | 135 | year |
| 4.53(3)(A) | §6652(c)(3)(A) maximum — returns required to be filed in 2027 (`reportable_txn_disclosure_max_6652c3A`) | 66,500 | — | 69,000 | 69,000 | year |
| 4.53(3)(B)(ii) | §6652(c)(3)(B)(ii) failure to comply with written demand: daily — returns required to be filed in 2027 (`reportable_txn_demand_daily_6652c3Bii`) | 130 | — | 135 | 135 | year |
| 4.53(3)(B)(ii) | §6652(c)(3)(B)(ii) maximum — returns required to be filed in 2027 (`reportable_txn_demand_max_6652c3Bii`) | 13,000 | — | 13,500 | 13,500 | year |
| 4.53(2)(C)(ii) ordinary | §6652(c)(2)(C) split-interest trust (ordinary): daily — applies (1)(A) amounts (`split_interest_trust_daily_6652c2C`) | 25 | — | 25 | 25 | year |
| 4.53(2)(C)(ii) ordinary | §6652(c)(2)(C) split-interest trust (ordinary): maximum — (1)(A) $10,000 amount, no 5% limit (`split_interest_trust_max_6652c2C`) | 13,000 | — | 13,500 | 13,500 | year |
| 4.54(a) | §6695(a) preparer failure to furnish copy to taxpayer: per return/claim (per item for (e)) (`preparer_a_per_failure_6695a`) | 65 | — | 65 | 65 | year |
| 4.54(a) | §6695(a) preparer failure to furnish copy to taxpayer: calendar-year / return-period maximum (`preparer_a_max_6695a`) | 33,000 | — | 34,500 | 34,500 | year |
| 4.54(b) | §6695(b) preparer failure to sign return: per return/claim (per item for (e)) (`preparer_b_per_failure_6695b`) | 65 | — | 65 | 65 | year |
| 4.54(b) | §6695(b) preparer failure to sign return: calendar-year / return-period maximum (`preparer_b_max_6695b`) | 33,000 | — | 34,500 | 34,500 | year |
| 4.54(c) | §6695(c) preparer failure to furnish identifying number: per return/claim (per item for (e)) (`preparer_c_per_failure_6695c`) | 65 | — | 65 | 65 | year |
| 4.54(c) | §6695(c) preparer failure to furnish identifying number: calendar-year / return-period maximum (`preparer_c_max_6695c`) | 33,000 | — | 34,500 | 34,500 | year |
| 4.54(d) | §6695(d) preparer failure to retain copy or list: per return/claim (per item for (e)) (`preparer_d_per_failure_6695d`) | 65 | — | 65 | 65 | year |
| 4.54(d) | §6695(d) preparer failure to retain copy or list: calendar-year / return-period maximum (`preparer_d_max_6695d`) | 33,000 | — | 34,500 | 34,500 | year |
| 4.54(e) | §6695(e) preparer failure to file correct information returns (§6060): per return/claim (per item for (e)) (`preparer_e_per_failure_6695e`) | 65 | — | 65 | 65 | year |
| 4.54(e) | §6695(e) preparer failure to file correct information returns (§6060): calendar-year / return-period maximum (`preparer_e_max_6695e`) | 33,000 | — | 34,500 | 34,500 | year |
| 4.54(f) | §6695(f) preparer negotiation of check: per check, no limit (`preparer_f_6695f`) | 665 | — | 690 | 690 | year |
| 4.54(g) | §6695(g) preparer due diligence (HOH, CTC, AOTC, EIC): per failure, no limit (`preparer_g_6695g`) | 665 | — | 690 | 690 | year |
| 4.55 | §6698(b)(1) failure to file partnership return: amount per partner per month — returns required to be filed in 2027 (`ftf_partnership_per_partner_month_6698b1`) | 260 | — | 265 | 265 | year |
| 4.56 | §6699(b)(1) failure to file S corporation return: amount per shareholder per month — returns required to be filed in 2027 (`ftf_scorp_per_partner_month_6699b1`) | 260 | — | 265 | 265 | year |
| 4.57(a)(1) | §6721(a)(1) General rule: penalty per return/statement — return required to be filed in 2027 (`ir_general_per_item_6721a1`) | 340 | — | 360 | 360 | year |
| 4.57(a)(1) | §6721(a)(1) General rule: calendar-year maximum (gross receipts > $5M) — return required to be filed in 2027 (`ir_general_cy_max_6721a1`) | 4,191,500 | — | 4,327,500 | 4,322,500 – 4,327,500 | year+october |
| 4.57(b)(1) | §6721(b)(1) Corrected within 30 days: per return/statement — return required to be filed in 2027 (`ir_30day_per_item_6721b1`) | 60 | — | 70 | 70 | year |
| 4.57(b)(1) | §6721(b)(1) Corrected within 30 days: calendar-year maximum (gross receipts > $5M) — return required to be filed in 2027 (`ir_30day_cy_max_6721b1`) | 698,500 | — | 721,000 | 720,000 – 721,000 | year+october |
| 4.57(b)(2) | §6721(b)(2) Corrected after 30th day by August 1: per return/statement — return required to be filed in 2027 (`ir_aug1_per_item_6721b2`) | 130 | — | 140 | 140 | year |
| 4.57(b)(2) | §6721(b)(2) Corrected after 30th day by August 1: calendar-year maximum (gross receipts > $5M) — return required to be filed in 2027 (`ir_aug1_cy_max_6721b2`) | 2,095,500 | — | 2,163,500 | 2,161,000 – 2,163,500 | year+october |
| 4.57(d)(1)(A) | §6721(d)(1)(A) Small filer (gross receipts ≤ $5M): general calendar-year maximum — return required to be filed in 2027 (`ir_small_general_cy_max_6721d1A`) | 1,397,000 | — | 1,442,500 | 1,440,500 – 1,442,500 | year+october |
| 4.57(d)(1)(B) | §6721(d)(1)(B) Small filer: corrected within 30 days, calendar-year maximum — return required to be filed in 2027 (`ir_small_30day_cy_max_6721d1B`) | 244,500 | — | 252,000 | 252,000 | year |
| 4.57(d)(1)(C) | §6721(d)(1)(C) Small filer: corrected by August 1, calendar-year maximum — return required to be filed in 2027 (`ir_small_aug1_cy_max_6721d1C`) | 698,500 | — | 721,000 | 720,000 – 721,000 | year+october |
| 4.57(d)(1)(A) | §6721(d)(1)(A) Small filer: general per-item penalty (same as (a)(1)) — return required to be filed in 2027 (`ir_small_general_per_item_6721d1A`) | 340 | — | 360 | 360 | year |
| 4.57(d)(1)(B) | §6721(d)(1)(B) Small filer: 30-day per-item penalty (same as (b)(1)) — return required to be filed in 2027 (`ir_small_30day_per_item_6721d1B`) | 60 | — | 70 | 70 | year |
| 4.57(d)(1)(C) | §6721(d)(1)(C) Small filer: Aug-1 per-item penalty (same as (b)(2)) — return required to be filed in 2027 (`ir_small_aug1_per_item_6721d1C`) | 130 | — | 140 | 140 | year |
| 4.57(e)(2) | §6721(e)(2) Intentional disregard: minimum per item ('greater of $X or 10%/5% …'), rows (e)(2)(A),(B),(D) — return required to be filed in 2027 (`ir_intentional_min_6721e2`) | 690 | — | 720 | 720 | year |
| 4.57(e)(2)(C) | §6721(e)(2)(C) Intentional disregard, §6050I(a) cash return: minimum ($X or cash up to cap) — return required to be filed in 2027 (`ir_6050I_intentional_min_6721e2Ci`) | 34,930 | — | 36,060 | 36,020 – 36,060 | year+october |
| 4.57(e)(2)(C) | §6721(e)(2)(C) Intentional disregard, §6050I(a): cap on cash amount counted — return required to be filed in 2027 (`ir_6050I_intentional_cash_cap_6721e2Cii`) | 139,500 | — | 144,000 | 144,000 | year |
| 4.57(d)(2)(A) | §6721(d)(2)(A) small-filer gross receipts test (average annual gross receipts, 3 years) (`ir_small_filer_gross_receipts_test_6721d2A`) | 5,000,000 | 5,000,000 | 5,000,000 | 5,000,000 | year |
| 4.58(a)(1) | §6722(a)(1) General rule: penalty per return/statement — statement required to be furnished in 2027 (`ps_general_per_item_6722a1`) | 340 | — | 360 | 360 | year |
| 4.58(a)(1) | §6722(a)(1) General rule: calendar-year maximum (gross receipts > $5M) — statement required to be furnished in 2027 (`ps_general_cy_max_6722a1`) | 4,191,500 | — | 4,327,500 | 4,322,500 – 4,327,500 | year+october |
| 4.58(b)(1) | §6722(b)(1) Corrected within 30 days: per return/statement — statement required to be furnished in 2027 (`ps_30day_per_item_6722b1`) | 60 | — | 70 | 70 | year |
| 4.58(b)(1) | §6722(b)(1) Corrected within 30 days: calendar-year maximum (gross receipts > $5M) — statement required to be furnished in 2027 (`ps_30day_cy_max_6722b1`) | 698,500 | — | 721,000 | 720,000 – 721,000 | year+october |
| 4.58(b)(2) | §6722(b)(2) Corrected after 30th day by August 1: per return/statement — statement required to be furnished in 2027 (`ps_aug1_per_item_6722b2`) | 130 | — | 140 | 140 | year |
| 4.58(b)(2) | §6722(b)(2) Corrected after 30th day by August 1: calendar-year maximum (gross receipts > $5M) — statement required to be furnished in 2027 (`ps_aug1_cy_max_6722b2`) | 2,095,500 | — | 2,163,500 | 2,161,000 – 2,163,500 | year+october |
| 4.58(d)(1)(A) | §6722(d)(1)(A) Small filer (gross receipts ≤ $5M): general calendar-year maximum — statement required to be furnished in 2027 (`ps_small_general_cy_max_6722d1A`) | 1,397,000 | — | 1,442,500 | 1,440,500 – 1,442,500 | year+october |
| 4.58(d)(1)(B) | §6722(d)(1)(B) Small filer: corrected within 30 days, calendar-year maximum — statement required to be furnished in 2027 (`ps_small_30day_cy_max_6722d1B`) | 244,500 | — | 252,000 | 252,000 | year |
| 4.58(d)(1)(C) | §6722(d)(1)(C) Small filer: corrected by August 1, calendar-year maximum — statement required to be furnished in 2027 (`ps_small_aug1_cy_max_6722d1C`) | 698,500 | — | 721,000 | 720,000 – 721,000 | year+october |
| 4.58(d)(1)(A) | §6722(d)(1)(A) Small filer: general per-item penalty (same as (a)(1)) — statement required to be furnished in 2027 (`ps_small_general_per_item_6722d1A`) | 340 | — | 360 | 360 | year |
| 4.58(d)(1)(B) | §6722(d)(1)(B) Small filer: 30-day per-item penalty (same as (b)(1)) — statement required to be furnished in 2027 (`ps_small_30day_per_item_6722d1B`) | 60 | — | 70 | 70 | year |
| 4.58(d)(1)(C) | §6722(d)(1)(C) Small filer: Aug-1 per-item penalty (same as (b)(2)) — statement required to be furnished in 2027 (`ps_small_aug1_per_item_6722d1C`) | 130 | — | 140 | 140 | year |
| 4.58(e)(2) | §6722(e)(2) Intentional disregard: minimum per item ('greater of $X or 10%/5% …'), rows (e)(2)(A),(B) — statement required to be furnished in 2027 (`ps_intentional_min_6722e2`) | 690 | — | 720 | 720 | year |
| 4.58(d)(2)(A) | §6722(d)(2)(A) small-filer gross receipts test (average annual gross receipts, 3 years) (`ps_small_filer_gross_receipts_test_6722d2A`) | 5,000,000 | 5,000,000 | 5,000,000 | 5,000,000 | year |
| 4.59(a) | §6726(a) QOF/QROF §6039K return failure: per day — returns required to be filed in 2027 (`qof_ftf_daily_6726a`) | 510 | — | 520 | 520 | year |
| 4.59(b)(1) | §6726(b)(1) maximum per return — returns required to be filed in 2027 (`qof_ftf_max_6726b1`) | 10,000 | — | 10,000 | 10,000 | year |
| 4.59(b)(2) | §6726(b)(2) large fund gross assets threshold (in excess of, last day of taxable year) — returns required to be filed in 2027 (`qof_large_fund_gross_assets_threshold_6726b2`) | 10,230,000 | — | 10,560,000 | 10,550,000 – 10,560,000 | year+october |
| 4.59(b)(2) | §6726(b)(2) maximum per return, large fund — returns required to be filed in 2027 (`qof_large_fund_max_6726b2`) | 51,000 | — | 52,000 | 52,000 | year |
| 4.59(c)(1) | §6726(c)(1) intentional disregard: per day — returns required to be filed in 2027 (`qof_intentional_daily_6726c1`) | 2,550 | — | 2,640 | 2,630 – 2,640 | year+october |
| 4.59(c)(2) | §6726(c)(2) intentional disregard: maximum per return — returns required to be filed in 2027 (`qof_intentional_max_6726c2`) | 51,000 | — | 52,000 | 52,000 | year |
| 4.59(c)(3) | §6726(c)(3) intentional disregard: maximum per return, large fund — returns required to be filed in 2027 (`qof_intentional_large_max_6726c3`) | 255,000 | — | 264,000 | 263,000 – 264,000 | year+october |
| 4.60 | §7345(b)(1)(B) seriously delinquent tax debt threshold (greater than) (`passport_serious_delinquent_tax_debt_7345`) | 66,000 | 68,000 | 68,000 | 68,000 | firm |
| 4.61 | §7430(c)(1)(B)(iii) attorney fee award limitation per hour (fees incurred in 2026) (`attorney_fee_hourly_cap_7430`) | 260 | 270 | 270 | 270 | firm |
| 4.62 | §7702B(d)(4) per diem limitation for periodic LTC / accelerated death benefit payments (calendar year 2026) (`ltc_per_diem_limit_7702B`) | 430 | 295 | 440 | 440 | irs-rule |
| 4.63(self) | §9831(d)(2)(B)(iii) QSEHRA annual payment limit (self-only) (`qsehra_limit_self_9831`) | 6,450 | 6,700 | 6,700 | 6,700 | firm |
| 4.63(family) | §9831(d)(2)(B)(iii) QSEHRA annual payment limit (family coverage) (`qsehra_limit_family_9831`) | 13,100 | 13,550 | 13,550 | 13,500 – 13,550 | october |
| E.2010 | §2010(c)(3) basic exclusion amount (estate, gift via §2505; GST exemption §2631(c) = this amount) (`estate_basic_exclusion_2010c3`) | — | 15,480,000 | 15,480,000 | 15,460,000 – 15,480,000 | new-base+october+ambiguity |
| E.2631 | §2631(c) GST exemption = basic exclusion amount §2010(c) (`gst_exemption_2631c`) | — | 15,480,000 | 15,480,000 | 15,460,000 – 15,480,000 | new-base+october |
| E.6041 | §6041(a) information reporting threshold (also §6041A(a)(2), §3406(b)(6)) (`info_reporting_threshold_6041a`) | — | 2,100 | 2,100 | 2,100 | new-base |
| E.127 | §127(a)(2) employer educational assistance limit ($5,250) (`educational_assistance_127a2`) | — | 5,400 | 5,400 | 5,400 | new-base |
| E.199A | §199A(i)(1)(B) minimum QBI deduction ($400) (`qbi_min_deduction_199Ai`) | — | 415 | 415 | 410 – 415 | new-base+october |
| E.199A | §199A(i)(2)(A) active QBI threshold for the minimum deduction ($1,000) (`qbi_min_active_income_199Ai`) | — | 1,030 | 1,030 | 1,030 | new-base |
| E.45F | §45F(b)(1) employer child care credit limit ($500,000) (`child_care_credit_max_45F`) | — | 515943.67 | 515943.67 | 515302.79 – 515943.67 | new-base+october+ambiguity |
| E.45F | §45F(b)(1) limit for an eligible small business ($600,000) (`child_care_credit_max_small_45F`) | — | 619132.40 | 619132.40 | 618363.35 – 619132.40 | new-base+october+ambiguity |
| E.1202 | §1202(b)(4)(B) per-issuer exclusion cap ($15,000,000), stock acquired after 2025-07-04 (`qsbs_per_issuer_cap_1202b4`) | — | 15,480,000 | 15,480,000 | 15,460,000 – 15,480,000 | new-base+october+ambiguity |
| E.1202 | §1202(d)(1)(A),(B) aggregate gross assets limit ($75,000,000) (`qsbs_gross_assets_1202d1`) | — | 77,390,000 | 77,390,000 | 77,300,000 – 77,390,000 | new-base+october+ambiguity |
| E.164 | §164(b)(7)(A)(iii) applicable limitation amount (SALT), 101% of prior year (`salt_cap_164b7`) | — | 40,804 | 40,804 | 40,804 | new-base |
| E.164 | §164(b)(7)(B)(ii) SALT phase-down threshold, 101% of prior year (`salt_threshold_164b7`) | — | 510,050 | 510,050 | 510,050 | new-base |
