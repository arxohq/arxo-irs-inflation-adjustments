"""Прогноз индексируемых сумм 2027 года из текста IRC до выхода Rev. Proc. Decimal; float запрещён.

Восемь прогонов: чтение {text, irs} × режим октября 2025 {m11, geo, lin, cf}.
- text — буква статьи (паспорт specs/*.json);
- irs  — правила IRS, выявленные сверкой 2026 года (записка 21.10.2026): округление суммы вместо прироста
  (HoH, §6334/§642, LTC), сцепка LTC по медицинскому компоненту, округления без текста (§45R, §512(d),
  §513(h), §6039F, Rev. Proc. 90-12), год COLA штрафов = год подачи − 1, граница трастов 10→24 с базой 2016.
Главный прогноз — text/m11 и irs/m11 (m11 — метод BLS для средних при пропуске октября)."""
import os, sys, json, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, ROUND_HALF_UP
from cpi27 import cola, rnd, indexed, avg12, CPI, MED, VINT, VMED, VKEY, OCT_MODES

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, '..')
CY = int(os.environ.get('IRC_CY', '2027'))          # 2026 — регрессия против разведки 21.10.2026
SPECS = os.environ.get('IRC_SPECS', os.path.join(WORK, 'specs'))
OUTF = os.environ.get('IRC_OUT', os.path.join(WORK, 'forecast-2027.json'))
PENALTY_ITEMS = ('4.52', '4.53', '4.54', '4.55', '4.56', '4.57', '4.58', '4.59')

def load():
    specs = []
    for f in sorted(glob.glob(os.path.join(SPECS, '*.json'))):
        for s in json.load(open(f)):
            s['_group'] = os.path.basename(f)[:-5]; specs.append(s)
    return specs

def num(x):
    if x is None: return None
    try: return D(str(x).replace('$', '').replace(',', '').strip())
    except Exception: return None

# ---------- переопределения: fn(s, reading, oct) -> (значение, сырое, коэффициент, правило) ----------
OV = {}
def ov(*ids):
    def w(fn):
        for i in ids: OV[i] = fn
        return fn
    return w

def ix(base, by, mult, mode, applies, oc, cy=CY):
    return indexed(base, cy, by, mult, mode, applies, oc)

# §32 EITC: суммы (b)(2)(A) база 1995 до ближайших $10 суммы; $5,000 MFJ база 2008; макс. кредит до доллара (эмпирика 2026)
EITC = {'1': ('6330', '11610', D('0.34'), D('0.1598')), '2': ('8890', '11610', D('0.40'), D('0.2106')),
        '3': ('8890', '11610', D('0.45'), D('0.2106')), '0': ('4220', '5280', D('0.0765'), D('0.0765'))}
def eitc(n, oc):
    ei, ph, cr, po = EITC[n]
    e = ix(ei, 1995, 10, 'nearest', 'amount', oc)[0]
    t = ix(ph, 1995, 10, 'nearest', 'amount', oc)[0]
    tj = rnd(D(ph) * cola(CY, 1995, oc) + D(5000) * cola(CY, 2008, oc), 10, 'nearest')
    mc = (cr * e).quantize(D(1), ROUND_HALF_UP)
    return dict(e=e, t=t, tj=tj, mc=mc, po=po)
for _n in '0123':
    def _mk(n):
        OV[f'eitc_max_credit_{n}'] = lambda s, r, oc: (eitc(n, oc)['mc'], None, None, 'кредит до доллара (эмпирика 2026)')
        OV[f'eitc_phaseout_threshold_{n}_mfj'] = lambda s, r, oc: (eitc(n, oc)['tj'], None, None, 'сумма двух компонент, одно округление')
        def comp(mfj):
            def f(s, r, oc):
                x = eitc(n, oc); th = x['tj'] if mfj else x['t']
                return (th + x['mc'] / x['po']).quantize(D(1), ROUND_HALF_UP), None, None, 'от округлённого кредита до доллара'
            return f
        OV[f'eitc_phaseout_complete_{n}_other'] = comp(False)
        OV[f'eitc_phaseout_complete_{n}_mfj'] = comp(True)
    _mk(_n)

@ov('lihtc_state_ceiling_per_capita')
def _(s, r, oc):
    v, raw, f = ix('1.75', 2001, '0.05', 'down', 'increase', oc); return v * D('1.12'), raw, f, '§42(h)(3)(H), затем ×1.12 (I)'
@ov('lihtc_state_ceiling_minimum')
def _(s, r, oc):
    v, raw, f = ix('2000000', 2001, 5000, 'down', 'increase', oc); return v * D('1.12'), raw, f, '§42(h)(3)(H), затем ×1.12 (I)'

@ov('sbhic_average_wage_amount')
def _(s, r, oc):
    _, raw, f = ix('25000', 2012, 1, 'none', 'amount', oc)
    if r == 'irs': return rnd(raw, 100, 'nearest'), raw, f, 'IRS: до ближайших $100 (в тексте округления нет)'
    return raw, raw, f, 'без округления (§45R(d)(3)(B))'

@ov('health_fsa_carryover_max')
def _(s, r, oc):
    v = ix('2500', 2012, 50, 'down', 'increase', oc)[0]; return v * D('0.2'), None, None, 'Notice 2020-33: 20% лимита §125(i)'

@ov('amt_phaseout_estate')
def _(s, r, oc):
    v, raw, f = ix('150000', 2011, 100, 'nearest', 'amount', oc); return v / 2, raw / 2, f, '50% от $150,000 база 2011'

@ov('rt_estate_10_24')
def _(s, r, oc):
    if r == 'irs':
        v, raw, f = ix('2550', 2016, 50, 'down', 'increase', oc); return v, raw, f, 'IRS: как конец 10% (база 2016)'
    v, raw, f = ix('2550', 2017, 50, 'down', 'increase', oc); return v, raw, f, 'начало ступени выше 22% (база 2017, §70101(b))'

# §213(d)(10)(B)(ii) и §7702B(d)(4): медицинский C-CPI-U за август 2026 (винтаж 2026-09-11)
def ltc(base, r):
    b = D(base); med_cc = VMED[VKEY[CY]]; cc = VINT[VKEY[CY]]
    if r == 'irs':
        f = med_cc[(CY - 1, 8)] / (MED[(1996, 8)] * (med_cc[(2016, 8)] / MED[(2016, 8)]))
        return rnd(b * f, 10, 'nearest'), b * f, f, 'IRS: сцепка по мед. компоненту на авг. 2016, округление суммы до $10'
    f = med_cc[(CY - 1, 8)] / (MED[(1996, 8)] * (avg12(cc, 2016) / avg12(CPI, 2016)))
    return b + rnd(b * (f - 1), 10, 'nearest'), b * f, f, 'буквально: мед. C-CPI-U ÷ (мед. CPI-U авг.1996 × общий §1(f)(3)(B)), прирост до $10'
for _id, _b in (('ltc_premium_age_40_or_less', '200'), ('ltc_premium_age_41_to_50', '375'), ('ltc_premium_age_51_to_60', '750'),
                ('ltc_premium_age_61_to_70', '2000'), ('ltc_premium_age_over_70', '2500'), ('ltc_per_diem_limit_7702B', '175')):
    OV[_id] = (lambda b: (lambda s, r, oc: ltc(b, r)))(_b)

@ov('oil_spill_liability_rate')
def _(s, r, oc): return D('0.00'), None, None, '§4611(f)(2): не применяется после 31.12.2025 (Announcement 2026-2)'
@ov('petroleum_tax_total')
def _(s, r, oc):
    v, raw, f = ix('0.164', 2022, '0.01', 'down', 'amount', oc); return v, raw, f, 'только Superfund §4611(c)(2)(B)'

# Правила IRS, отличные от буквы
def irs_amount_round(mult, mode, note):
    def f(s, r, oc):
        base = num(s['base_amount']); by = int(str(s['base_year'])[:4]); rd = s['rounding']
        v, raw, fc = ix(base, by, rd.get('multiple'), rd.get('mode'), rd.get('applies_to') or 'increase', oc)
        if r == 'irs': return rnd(raw, mult, mode), raw, fc, note
        return v, raw, fc, 'по тексту'
    return f
OV['std_deduction_hoh'] = irs_amount_round(50, 'down', 'IRS: вся сумма вниз до $50 (2026: 24 150)')
OV['levy_exempt_dependent_amount'] = irs_amount_round(100, 'down', 'IRS: вся сумма вниз до $100 (2025, 2026)')
OV['qualified_disability_trust_exemption'] = irs_amount_round(100, 'down', 'IRS: вся сумма вниз до $100 (2025, 2026)')
OV['ag_hort_dues_limit'] = irs_amount_round(1, 'nearest', 'IRS: до доллара (в тексте нет)')
OV['low_cost_article'] = irs_amount_round('0.10', 'nearest', 'IRS: до 10 центов (в тексте нет)')
OV['foreign_gift_reporting_threshold_6039F'] = irs_amount_round(1, 'nearest', 'IRS: до доллара (в тексте нет)')
def _ib(k):
    def f(s, r, oc):
        base = num(s['base_amount']); _, raw, fc = ix(base, 1987, None, 'none', 'amount', oc)
        if r == 'irs':
            la = rnd(D(5) * fc, '0.10', 'nearest'); return la * k, raw, fc, f'IRS: {k}× low-cost article'
        return raw, raw, fc, 'Rev. Proc. 90-12/92-102 без правила округления'
    return f
OV['insubstantial_benefit_25'] = _ib(5)
OV['insubstantial_benefit_50'] = _ib(10)

# ---------- прогон ----------
def run(specs, reading, oc):
    vals, info, pending = {}, {}, []
    for s in specs:
        i = s['id']
        if i in OV:
            v, raw, f, note = OV[i](s, reading, oc); vals[i] = v; info[i] = (raw, f, note); continue
        k = s['kind']
        if k in ('indexed', 'not_code_indexed') and num(s.get('base_amount')) is not None and s.get('cola_year') and s.get('base_year'):
            cy = int(s['cola_year'])
            if reading == 'irs' and s.get('cola_year_irs_practice'): cy = int(s['cola_year_irs_practice'])
            if cy > CY:
                vals[i] = None; info[i] = (None, None, f'COLA {cy}: C-CPI-U сен.{cy - 2}–авг.{cy - 1} не опубликован'); continue
            rd = s.get('rounding') or {}
            v, raw, f = ix(num(s['base_amount']), int(str(s['base_year'])[:4]), rd.get('multiple'), rd.get('mode') or 'none',
                           rd.get('applies_to') or 'increase', oc, cy)
            vals[i] = v; info[i] = (raw, f, f'COLA {cy}'); continue
        if k == 'fixed_statutory':
            vals[i] = num(s.get('base_amount')); info[i] = (None, None, 'статутная'); continue
        pending.append(s)
    for _ in range(6):
        left = []
        for s in pending:
            fml = s.get('derived_formula')
            if not fml: left.append(s); continue
            expr = fml.split('=')[-1] if '=' in fml else fml
            expr = expr.replace('%', '*D("0.01")')
            names = re.findall(r'[A-Za-z_][A-Za-z0-9_]*', expr)
            refs = [n for n in names if n not in ('D', 'min', 'max', 'rnd')]
            if any(n not in vals for n in refs): left.append(s); continue
            if any(vals[n] is None for n in refs):
                vals[s['id']] = None; info[s['id']] = (None, None, 'производная от невычислимой'); continue
            e = re.sub(r'(?<![\w.])(\d+(?:\.\d+)?)', lambda m: f"D('{m.group(1)}')", expr)
            e = re.sub(r'[A-Za-z_][A-Za-z0-9_]*', lambda m: f'vals["{m.group(0)}"]' if m.group(0) in vals else m.group(0), e)
            vals[s['id']] = D(eval(e, {'D': D, 'vals': vals, 'min': min, 'max': max, 'rnd': rnd}))
            info[s['id']] = (None, None, 'производная')
        pending = left
    for s in pending:
        vals[s['id']] = None; info[s['id']] = (None, None, 'не посчитано')
    return vals, info

def fmtd(x):
    if x is None: return None
    x = D(x)
    if x == x.to_integral_value(): return str(x.quantize(D(1)))
    return format(x.quantize(D('0.000001'), ROUND_HALF_UP).normalize(), 'f')   # несокращённые суммы — до 6 знаков

def main():
    specs = load()
    runs = {(r, oc): run(specs, r, oc) for r in ('text', 'irs') for oc in OCT_MODES}
    out = []
    for s in specs:
        i = s['id']
        tv = {oc: runs[('text', oc)][0][i] for oc in OCT_MODES}
        iv = {oc: runs[('irs', oc)][0][i] for oc in OCT_MODES}
        raw, f, note_t = runs[('text', 'm11')][1][i]
        alt = {}
        if i == 'std_deduction_hoh':      # IRS 2026 = 24 150 = 1,5 × 16 100: второе объяснение числа IRS
            alt['irs_alt_150pct_single'] = {oc: fmtd(D('1.5') * runs[('irs', oc)][0]['std_deduction_single']) for oc in OCT_MODES}
        rd = s.get('rounding') or {}
        if s['kind'] == 'indexed' and str(s.get('base_year'))[:4] == '2025' and s.get('base_amount'):
            alt['base2025_from_vintage_20250911'] = {oc: fmtd(indexed(num(s['base_amount']), CY, 2025, rd.get('multiple'), rd.get('mode') or 'none',
                                                                     rd.get('applies_to') or 'increase', oc, '20250911')[0]) for oc in OCT_MODES}
        _, _, note_i = runs[('irs', 'm11')][1][i]
        out.append({
            'item': s['item'], 'id': i, 'group': s['_group'], 'label': s.get('label'), 'kind': s['kind'],
            'cite': s.get('index_cite') or s.get('base_amount_cite'), 'base': s.get('base_amount'), 'base_year': s.get('base_year'),
            'cola_year_text': s.get('cola_year'), 'cola_year_irs': s.get('cola_year_irs_practice') or s.get('cola_year'),
            'rounding': s.get('rounding'),
            'text': fmtd(tv['m11']), 'irs_rules': fmtd(iv['m11']),
            'text_by_oct': {oc: fmtd(v) for oc, v in tv.items()}, 'irs_by_oct': {oc: fmtd(v) for oc, v in iv.items()},
            'raw_m11': f'{raw:.4f}' if raw is not None else None, 'factor_m11': f'{f:.8f}' if f is not None else None,
            'note_text': note_t, 'note_irs': note_i, 'alt': alt,
            'irs_2026': s.get('irs_value_2026'), 'ours_2026': s.get('ours_2026'),
        })
    json.dump(out, open(OUTF, 'w'), ensure_ascii=False, indent=1)
    print('сумм:', len(out))

if __name__ == '__main__':
    main()
