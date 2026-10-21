"""Ряды CPI-U и C-CPI-U и COLA по IRC §1(f)(3)-(6). Decimal, без float."""
import csv, json, glob, os
from decimal import Decimal as D, getcontext
getcontext().prec = 50
SRC = os.environ.get('IRC_SRC', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data'))

def _bls():
    cpi, ccpi = {}, {}
    for f in sorted(glob.glob(os.path.join(SRC, 'bls', 'bls-*.json'))):
        d = json.load(open(f))
        for s in d['Results']['series']:
            tgt = cpi if s['seriesID'] == 'CUUR0000SA0' else ccpi
            for r in s['data']:
                if r['period'].startswith('M') and r['period'] != 'M13' and r['value'] not in ('-', ''):
                    tgt[(int(r['year']), int(r['period'][1:]))] = D(r['value'])
    return cpi, ccpi

def _alfred():
    f = glob.glob(os.path.join(SRC, 'alfred', 'vintages_*.csv'))[0]
    rows = list(csv.reader(open(f)))
    hdr = rows[0]; out = {h.split('_')[-1]: {} for h in hdr[1:]}
    for r in rows[1:]:
        y, m = int(r[0][:4]), int(r[0][5:7])
        for h, v in zip(hdr[1:], r[1:]):
            if v.strip() not in ('', '.'):
                out[h.split('_')[-1]][(y, m)] = D(v)
    return out

CPI, CCPI_NOW = _bls()

def _med():
    out = {}
    for f in sorted(glob.glob(os.path.join(SRC, 'bls', 'med-*.json'))):
        for s in json.load(open(f))['Results']['series']:
            for r in s['data']:
                if r['period'].startswith('M') and r['period'] != 'M13' and r['value'] not in ('-', ''):
                    out[(int(r['year']), int(r['period'][1:]))] = D(r['value'])
    return out
MED = _med()
VINT = _alfred()   # {'20170914': {...}, '20250911': {...}}

MISSING = set()

def avg12(series, year):
    """Среднее за 12 месяцев, заканчивающихся 31 августа year (§1(f)(4), (6)(B))."""
    ms = [(year - 1, m) for m in range(9, 13)] + [(year, m) for m in range(1, 9)]
    vals = [series[k] for k in ms if k in series]
    if len(vals) < 12:
        MISSING.add((year, 12 - len(vals)))      # окт. 2025: BLS не публиковал (приостановка работы правительства)
        if len(vals) < 11: raise KeyError((year, ms))
    return sum(vals) / D(len(vals))

def ccpi_series(cola_year, vintage=True):
    """§1(f)(6)(A): значения на дату первой публикации августа (cola_year-1)."""
    if not vintage:
        return CCPI_NOW
    key = {2018: '20170914', 2025: '20240911', 2026: '20250911'}.get(cola_year)
    if not key:
        # Винтажа нет: для 2027 и далее — нынешние значения BLS (21.10.2026). Это допущение, а не §1(f)(6)(A);
        # compute.py вызывает с vintage=False явно, поэтому сюда попадает только незаявленный год.
        raise KeyError(f'нет винтажа C-CPI-U для COLA {cola_year}: передайте vintage=False явно')
    return VINT[key]

def cola(cola_year, base_year=2016, vintage=True, method='ccpi'):
    """Коэффициент 1+COLA за календарный год cola_year по §1(f)(3).
    method='cpi' — до-TCJA (§1(f)(3) ред. до P.L. 115-97): CPI(Y-1)/CPI(base)."""
    if method == 'cpi':
        return avg12(CPI, cola_year - 1) / avg12(CPI, base_year)
    cc = ccpi_series(cola_year, vintage)
    num = avg12(cc, cola_year - 1)
    if base_year >= 2016:
        den = avg12(cc, base_year)                 # §1(f)(3)(C) / (A)(ii) при base=2016 совпадает
        if base_year == 2016:
            den = avg12(CPI, 2016) * (avg12(cc, 2016) / avg12(CPI, 2016))
    else:
        den = avg12(CPI, base_year) * (avg12(cc, 2016) / avg12(CPI, 2016))
    return num / den

def rnd(x, mult, mode):
    from decimal import ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_UP
    m = D(mult)
    q = x / m
    if mode == 'down': q = q.to_integral_value(ROUND_FLOOR)
    elif mode == 'up': q = q.to_integral_value(ROUND_CEILING)
    elif mode == 'nearest': q = q.to_integral_value(ROUND_HALF_UP)
    elif mode == 'none': return x
    return q * m

def indexed(base, cola_year, base_year, mult, mode, applies_to='increase', vintage=True, method='ccpi'):
    base = D(base)
    f = cola(cola_year, int(base_year), vintage, method)
    inc = base * (f - 1)
    if inc < 0: inc = D(0)   # «increased by» — COLA «percentage (if any)»
    if applies_to == 'increase':
        return base + rnd(inc, mult, mode), base * f
    return rnd(base * f, mult, mode), base * f
