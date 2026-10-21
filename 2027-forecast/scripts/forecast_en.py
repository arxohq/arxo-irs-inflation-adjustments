"""English view of the 2027 forecast. Reads forecast-2027.json and classes-2027.json, writes FORECAST.md.
Does not change forecast-2027.json (its SHA-256 is recorded in PIN.sha256)."""
import json, os
from decimal import Decimal as D, ROUND_HALF_UP
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
F = json.load(open(os.path.join(ROOT, 'forecast-2027.json')))
C = {x['id']: x['class'] for x in json.load(open(os.path.join(ROOT, 'classes-2027.json')))}
CODE = {'=': 'firm', 'окт': 'october', 'в': 'year', 'б': 'irs-rule', 'а': 'ambiguity', 'нов': 'new-base'}
LABEL_E = {
 'info_reporting_threshold_6041a': '§6041(a) information reporting threshold (also §6041A(a)(2), §3406(b)(6))',
 'educational_assistance_127a2': '§127(a)(2) employer educational assistance limit ($5,250)',
 'qbi_min_deduction_199Ai': '§199A(i)(1)(B) minimum QBI deduction ($400)',
 'qbi_min_active_income_199Ai': '§199A(i)(2)(A) active QBI threshold for the minimum deduction ($1,000)',
 'child_care_credit_max_45F': '§45F(b)(1) employer child care credit limit ($500,000)',
 'child_care_credit_max_small_45F': '§45F(b)(1) limit for an eligible small business ($600,000)',
 'qsbs_per_issuer_cap_1202b4': '§1202(b)(4)(B) per-issuer exclusion cap ($15,000,000), stock acquired after 2025-07-04',
 'qsbs_gross_assets_1202d1': '§1202(d)(1)(A),(B) aggregate gross assets limit ($75,000,000)',
 'salt_cap_164b7': '§164(b)(7)(A)(iii) applicable limitation amount (SALT), 101% of prior year',
 'salt_threshold_164b7': '§164(b)(7)(B)(ii) SALT phase-down threshold, 101% of prior year',
}
def fmt(x):
    if x in (None, ''): return '—'
    d = D(str(x))
    if d == d.to_integral_value(): return f'{int(d):,}'
    return str(d.quantize(D('0.01'), ROUND_HALF_UP)) if abs(d) >= 1 else str(d.normalize())
def rng(by):
    v = sorted({D(x) for x in by.values() if x not in (None, '')})
    if not v: return '—'
    return fmt(v[0]) if len(v) == 1 else f'{fmt(v[0])} – {fmt(v[-1])}'
from collections import Counter
cnt = Counter(); rows = []
for r in F:
    cls = '+'.join(CODE.get(p, p) for p in C.get(r['id'], '').split('+'))
    for p in cls.split('+'): cnt[p] += 1
    label = LABEL_E.get(r['id'], r['label'])
    rows.append(f"| {r['item']} | {label} (`{r['id']}`) | {fmt(r.get('irs_2026'))} | {fmt(r['text'])} | {fmt(r['irs_rules'])} | {rng(r['irs_by_oct'])} | {cls} |")
head = ['# 2027 inflation-adjusted amounts: forecast built from the Code before the IRS publication', '',
 f'Rows: {len(F)} (295 rows of Rev. Proc. 2025-32 section 4 plus 12 amounts first indexed under P.L. 119-21). '
 'Class occurrences (a row may carry several): ' + ', '.join(f'{k}: {v}' for k, v in sorted(cnt.items())) + '.', '',
 'Columns: **2027, text** — the statutory reading with an eleven-month mean for the September 2025–August 2026 C-CPI-U average '
 '(no all-items October 2025 value was published); **2027, IRS conventions** — the same with the conventions the 2026 figures are consistent with '
 '(amount rounding where observed, prior-year COLA for penalties, medical-component link for long-term care); **range** — the IRS-conventions value across four '
 'treatments of the missing month (eleven-month mean, geometric and linear interpolation, carry-forward of September).', '',
 'Classes: `firm` — one value under every reading and missing-month treatment; `october` — depends on the missing-month treatment; '
 '`irs-rule` — text and IRS conventions differ (as found for 2026); `year` — penalty year reading; `ambiguity` — two readings of the text; '
 '`new-base` — first indexation of a base set by P.L. 119-21.', '',
 'The SHA-256 of `forecast-2027.json` is recorded in `PIN.sha256`; this table is a view of that file.', '',
 '| item | amount (id) | 2026 published | 2027, text | 2027, IRS conventions | range across missing-month treatments | class |',
 '|---|---|---:|---:|---:|---:|---|']
open(os.path.join(ROOT, 'FORECAST.md'), 'w').write('\n'.join(head + rows) + '\n')
print(head[2][:200])
