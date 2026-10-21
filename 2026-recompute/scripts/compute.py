"""Пересчёт сумм Rev. Proc. 2025-32 по паспортам specs/*.json. Decimal; float запрещён."""
import sys, json, glob, os, re
sys.path.insert(0, os.path.dirname(__file__))
from decimal import Decimal as D, ROUND_FLOOR
from cpi import cola, rnd, avg12, CPI, MED, CCPI_NOW
import overrides

WORK = os.environ.get('IRC_WORK', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

def load():
    specs = []
    for f in sorted(glob.glob(os.path.join(WORK, 'specs', '*.json'))):
        for s in json.load(open(f)):
            s['_group'] = os.path.basename(f)[:-5]
            specs.append(s)
    return specs

def num(x):
    if x is None: return None
    x = str(x).replace('$', '').replace(',', '').strip()
    try: return D(x)
    except Exception: return None

def calc_indexed(s, vintage=True, flip=False, cola_year=None):
    base = num(s['base_amount'])
    cy = int(cola_year or s['cola_year'])
    by = int(str(s['base_year'])[:4])
    r = s.get('rounding') or {}
    mult, mode = r.get('multiple') or '1', r.get('mode') or 'none'
    applies = r.get('applies_to') or 'increase'
    if flip: applies = 'amount' if applies == 'increase' else 'increase'
    if cy > 2026 and vintage: vintage = False      # будущих винтажей нет: берём текущие значения BLS
    f = cola(cy, by, vintage)
    raw = base * f
    inc = max(base * (f - 1), D(0))
    if mode == 'none': return raw, raw, f
    if applies == 'increase':
        return base + rnd(inc, mult, mode), raw, f
    return rnd(raw, mult, mode), raw, f

def main():
    specs = load()
    vals, rows = {}, []
    pending = []
    for s in specs:
        ov = overrides.get(s['id'])
        if ov:
            v, raw, f, alt = ov(s)
            vals[s['id']] = v; rows.append((s, v, raw, f, alt)); continue
        if s['kind'] in ('indexed', 'not_code_indexed') and num(s.get('base_amount')) is not None and s.get('cola_year') and s.get('base_year'):
            v, raw, f = calc_indexed(s)
            vf, _, _ = calc_indexed(s, vintage=False)
            vx, _, _ = calc_indexed(s, flip=True)
            alt = {'final_values': vf, 'flip_rounding': vx}
            if s.get('cola_year_irs_practice'):
                vp, _, fp = calc_indexed(s, cola_year=s['cola_year_irs_practice'])
                alt['cola_year_' + str(s['cola_year_irs_practice'])] = vp
                alt['cola_year_' + str(s['cola_year_irs_practice']) + '_flip'] = calc_indexed(s, flip=True, cola_year=s['cola_year_irs_practice'])[0]
            vals[s['id']] = v
            rows.append((s, v, raw, f, alt))
        elif s['kind'] == 'fixed_statutory':
            v = num(s.get('base_amount')) or num(s['irs_value'])
            vals[s['id']] = v; rows.append((s, v, None, None, {}))
        else:
            pending.append(s)
    # derived: несколько проходов
    for _ in range(5):
        left = []
        for s in pending:
            fml = s.get('derived_formula')
            if not fml: left.append(s); continue
            expr = fml.split('=')[-1] if '=' in fml else fml
            expr = re.sub(r'(?<![\w.])(\d+(?:\.\d+)?)', lambda m: f"D('{m.group(1)}')", expr)
            try:
                v = eval(re.sub(r'([A-Za-z_][A-Za-z0-9_]*)', lambda m: f'vals["{m.group(1)}"]' if m.group(1) in vals else m.group(1), expr), {'D': D, 'vals': vals, 'min': min, 'max': max, 'rnd': rnd})
                vals[s['id']] = D(v); rows.append((s, D(v), None, None, {}))
            except Exception:
                left.append(s)
        pending = left
    for s in pending:
        rows.append((s, None, None, None, {}))
    return rows

def classify(s, v, alt):
    irs = num(s['irs_value'])
    if v is None: return 'не посчитано'
    if irs is None: return 'нет числа IRS'
    if v == irs: return 'совпало'
    hit = [k for k, x in alt.items() if num(x) == irs]
    return 'РАСХОЖДЕНИЕ' + (' [IRS = ' + ', '.join(hit) + ']' if hit else '')

if __name__ == '__main__':
    rows = main()
    out = []
    for s, v, raw, f, alt in rows:
        cl = classify(s, v, alt)
        out.append({'item': s['item'], 'id': s['id'], 'label': s.get('label'), 'kind': s['kind'],
                    'cite': s.get('index_cite') or s.get('base_amount_cite'), 'base': s.get('base_amount'),
                    'cola_year': s.get('cola_year'), 'base_year': s.get('base_year'), 'rounding': s.get('rounding'),
                    'ours': str(v) if v is not None else None, 'raw': f'{raw:.4f}' if raw is not None else None,
                    'factor': f'{f:.8f}' if f is not None else None,
                    'irs': s['irs_value'], 'class': cl, 'alt': {k: str(x) for k, x in alt.items()},
                    'doubts': s.get('doubts', ''), 'special': s.get('special', '')})
    json.dump(out, open(os.path.join(WORK, 'results.json'), 'w'), ensure_ascii=False, indent=1)
    from collections import Counter
    print(Counter(o['class'] for o in out))
    for o in out:
        if o['class'] != 'совпало':
            print(f"{o['item']:<8} {o['id']:<40} ours={o['ours']} irs={o['irs']} raw={o['raw']} {o['alt']} [{o['class']}]")
