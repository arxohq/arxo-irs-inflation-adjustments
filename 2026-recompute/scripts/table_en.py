"""English comparison table for the 2026 reconstruction. Reads results.json, writes TABLE.md."""
import json, os
from decimal import Decimal as D, ROUND_HALF_UP
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
R = json.load(open(os.path.join(ROOT, 'results.json')))
PENALTY = ('4.52', '4.53', '4.54', '4.55', '4.56', '4.57', '4.58', '4.59')
LTC = {'ltc_premium_age_40_or_less', 'ltc_premium_age_41_to_50', 'ltc_premium_age_51_to_60',
       'ltc_premium_age_61_to_70', 'ltc_premium_age_over_70', 'ltc_per_diem_limit_7702B'}
NOTE = {
 'std_deduction_hoh': ('rounding', 'statute rounds the increase (559.56 → 550); published figure is consistent with rounding the whole amount (24,184.56 → 24,150)'),
 'qualified_disability_trust_exemption': ('rounding', '§6334(d)(4)(C) rounds the increase down to $100 (1,167 → 1,100); published figure is consistent with rounding the amount; 2025: 5,150 vs 5,100'),
 'levy_exempt_dependent_amount': ('rounding', 'same rule as above: statute 5,250, published 5,300'),
 'rt_estate_10_24': ('ambiguity', 'one amount is both the end of the 10% bracket (base 2016) and the start of a bracket above 22% (base 2017); published uses 2016'),
 'rt_estate_tax_at_24': ('ambiguity', 'follows the Table 5 boundary'),
 'rt_estate_tax_at_35': ('ambiguity', 'follows the Table 5 boundary'),
 'rt_estate_tax_at_37': ('ambiguity', 'follows the Table 5 boundary'),
 'sbhic_average_wage_amount': ('no rule', 'no rounding in §45R(d)(3)(B) (34,057.75, reading the multiplier as 1 + COLA); published to the nearest $100'),
 'ag_hort_dues_limit': ('no rule', 'no rounding in §512(d)(2) (211.58); published to the dollar'),
 'low_cost_article': ('no rule', 'no rounding in §513(h)(2)(C) (13.878); published to 10 cents'),
 'insubstantial_benefit_5': ('no rule', 'Rev. Proc. 90-12 guideline; published as 1 × 13.90'),
 'insubstantial_benefit_25': ('no rule', 'published as 5 × 13.90, not indexed separately (69.39)'),
 'insubstantial_benefit_50': ('no rule', 'published as 10 × 13.90, not indexed separately (138.78)'),
 'foreign_gift_reporting_threshold_6039F': ('no rule', 'no rounding in §6039F(d) (20,573.24); published to the dollar'),
 'amt_kiddie_exemption_addon': ('applicability', 'computed correctly, but §55(d)(4)(A)(iii) makes §59(j) inapplicable'),
 'petroleum_tax_total': ('corrected', 'Oil Spill Liability Trust Fund rate expired after 2025 (§4611(f)(2)); Announcement 2026-2: $0.18'),
 'oil_spill_liability_rate': ('corrected', 'not in effect for 2026 (§4611(f)(2)); Announcement 2026-2'),
 'expatriate_avg_income_tax_threshold': ('ambiguity', '§877(a)(2) cross-reference no longer matches §1(f)(3)(B); intended base 2003 gives the published 211,000; literal reading 161,000'),
 'eo_lobbying_dues_limit_6033e3': ('inferred', 'Rev. Proc. 98-19 §5.05 names no base year; 1997 inferred from published figures'),
}

def fmt(x):
    if x is None: return '—'
    try: d = D(str(x))
    except Exception: return str(x)
    if d == d.to_integral_value(): return f'{int(d):,}'
    q = d.quantize(D('0.01'), ROUND_HALF_UP) if abs(d) >= 1 else d.quantize(D('0.0001'), ROUND_HALF_UP)
    return str(q)

def classify(o):
    if o['id'] in NOTE: return NOTE[o['id']]
    if o['id'] in LTC:
        a = o['alt'].get('medical_link_aug2016_amount_rounded', '').split(' ')[0]
        return ('basis', f"literal statutory index (mixed scales) gives {fmt(o['ours'])}; published matches a medical-component link with amount rounding ({a})")
    if o['item'].split('(')[0].strip() in PENALTY and o['class'] != 'совпало':
        p = o['alt'].get('cola_year_2026')
        return ('year', f"event-year (2027) reading, conditional on later data and an 11-month mean, gives {fmt(o['ours'])}; consistent with the 2026 adjustment{' → ' + fmt(p) if p else ''}")
    if o['class'] == 'совпало':
        fv = o['alt'].get('final_values')
        if fv and fv != o['ours'] and o['kind'] != 'derived':
            return ('match', f'matches only with C-CPI-U as available on 2025-09-11 (§1(f)(6)(A)); later revised values give {fmt(fv)}')
        return ('match', '')
    return ('?', '')

def rnd(o):
    r = o.get('rounding') or {}
    if not r or not r.get('multiple') or r.get('mode') in (None, 'none'): return '—'
    m = {'down': 'down', 'up': 'up', 'nearest': 'nearest'}.get(r['mode'], r['mode'])
    return f"{m} {r['multiple']} ({'increase' if r.get('applies_to') == 'increase' else 'amount'})"

rows = sorted(R, key=lambda o: (int(o['item'].split('(')[0].split('.')[1]), o['item'], o['id']))
from collections import Counter
c = Counter(classify(o)[0] for o in rows)
out = ['# Rev. Proc. 2025-32, section 4: reconstruction vs published figures', '',
       f'Rows: {len(rows)}. ' + ', '.join(f'{k}: {v}' for k, v in sorted(c.items())) + '.', '',
       'Classes: `match` — equal to the published figure; `rounding` — the published figure cannot result from the statute\'s increase-rounding rule; '
       '`basis` — the published figure follows an adjustment whose published basis we have not located; `year` — penalty amounts consistent with the prior year\'s adjustment; '
       '`ambiguity` — the text admits two readings; `no rule` — the statute states no rounding; `applicability` — amount for a provision that does not apply; '
       '`corrected` — corrected later by the IRS; `inferred` — convention inferred from published figures.', '',
       '| item | amount (id) | provision | base (year) → COLA year | rounding | reconstructed | published | class | note |',
       '|---|---|---|---|---|---:|---:|---|---|']
for o in rows:
    k, note = classify(o)
    base = f"{fmt(o['base'])} ({o['base_year']}) → {o['cola_year']}" if o['kind'] in ('indexed', 'not_code_indexed') and o['base'] else ('derived' if o['kind'] == 'derived' else 'statutory')
    cite = (o['cite'] or '').replace('|', '/')
    out.append(f"| {o['item']} | {o['label'] or o['id']} (`{o['id']}`) | {cite} | {base} | {rnd(o)} | {fmt(o['ours'])} | {fmt(o['irs'])} | {k} | {note} |")
open(os.path.join(ROOT, 'TABLE.md'), 'w').write('\n'.join(out) + '\n')
print(out[2])
