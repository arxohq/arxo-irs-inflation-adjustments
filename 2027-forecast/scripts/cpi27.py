"""Ряды и COLA по IRC §1(f)(3)-(6) для 2027 года. Decimal, без float.

C-CPI-U — винтаж ALFRED 2026-09-11 (день выхода августа 2026, §1(f)(6)(A)); CPI-U и медицинский
CPI-U не пересматриваются и берутся из рядов BLS разведки 2026 года (соседний каталог evidence).
Октябрь 2025 BLS не публиковал: среднее за 12 месяцев по 31 августа 2026 считается в одном из
режимов OCT (см. avg12)."""
import csv, glob, json, os
from decimal import Decimal as D, getcontext, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_UP
getcontext().prec = 50
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')
DATA26 = os.path.join(HERE, '..', '..', '2026-recompute', 'data')

def _bls(prefix, sid):
    out = {}
    for f in sorted(glob.glob(os.path.join(DATA26, 'bls', prefix + '-*.json'))):
        for s in json.load(open(f))['Results']['series']:
            if s['seriesID'] != sid: continue
            for r in s['data']:
                if r['period'].startswith('M') and r['period'] != 'M13' and r['value'] not in ('-', ''):
                    out[(int(r['year']), int(r['period'][1:]))] = D(r['value'])
    return out

def _alfred(path):
    rows = list(csv.reader(open(path)))
    out = {h.split('_')[-1]: {} for h in rows[0][1:]}
    for r in rows[1:]:
        y, m = int(r[0][:4]), int(r[0][5:7])
        for h, v in zip(rows[0][1:], r[1:]):
            if v.strip() not in ('', '.'):
                out[h.split('_')[-1]][(y, m)] = D(v)
    return out

CPI = _bls('bls', 'CUUR0000SA0')          # CPI-U, все позиции (окт. 2025 нет)
MED = _bls('med', 'CUUR0000SAM')          # CPI-U, медицинский компонент
VINT = _alfred(os.path.join(DATA, 'alfred', 'SUUR0000SA0_vintages_2025-09-11_to_2026-10-14.csv'))
VMED = _alfred(os.path.join(DATA, 'alfred-med', 'SUUR0000SAM_vintages_2025-09-11_to_2026-10-14.csv'))
VKEY = {2026: '20250911', 2027: '20260911'}   # §1(f)(6)(A): на дату первой публикации августа (Y-1)
OCT_MODES = ('m11', 'geo', 'lin', 'cf')
OCT_LABEL = {'m11': 'среднее 11 опубликованных (метод BLS для годовых средних, FAQ Q10)',
             'geo': 'октябрь = √(сен×ноя) (приближение BLS в сезонной корректировке, FAQ Q12)',
             'lin': 'октябрь = (сен+ноя)/2 (линейная интерполяция)',
             'cf': 'октябрь = сентябрь (перенос вперёд, как BLS импутировал цены)'}

def months(year, end_month=8):
    return [((year - 1) if m > end_month else year, m) for m in list(range(end_month + 1, 13)) + list(range(1, end_month + 1))]

def avg12(series, year, oct_mode='m11', end_month=8):
    ms = months(year, end_month)
    vals = {k: series[k] for k in ms if k in series}
    miss = [k for k in ms if k not in series]
    if not miss:
        return sum(vals.values()) / D(12)
    if miss != [(2025, 10)]:
        raise KeyError(f'нет значений {miss} для года {year}')
    s, n = series[(2025, 9)], series[(2025, 11)]
    if oct_mode == 'm11':
        return sum(vals.values()) / D(11)
    fill = {'geo': (s * n).sqrt(), 'lin': (s + n) / 2, 'cf': s}[oct_mode]
    return (sum(vals.values()) + fill) / D(12)

def cola(cola_year, base_year, oct_mode='m11', base_vintage=None):
    """1 + COLA за календарный год cola_year по §1(f)(3) (ред. после P.L. 115-97).
    base_vintage — не по тексту: среднее базового года (≥ 2016) из другого винтажа (проверка «замороженной базы»)."""
    cc = VINT[VKEY[cola_year]]
    num = avg12(cc, cola_year - 1, oct_mode)
    if base_year >= 2016:
        den = avg12(VINT[base_vintage] if base_vintage else cc, base_year)
    else:
        den = avg12(CPI, base_year) * (avg12(cc, 2016) / avg12(CPI, 2016))
    return num / den

def rnd(x, mult, mode):
    if mode in (None, 'none') or not mult: return x
    m = D(str(mult)); q = x / m
    if mode == 'down': q = q.to_integral_value(ROUND_FLOOR)
    elif mode == 'up': q = q.to_integral_value(ROUND_CEILING)
    elif mode == 'nearest': q = q.to_integral_value(ROUND_HALF_UP)
    else: raise ValueError(mode)
    return q * m

def indexed(base, cola_year, base_year, mult, mode, applies='increase', oct_mode='m11', base_vintage=None):
    """Возвращает (итог, сырое base×f, f). «increased by» — COLA «percentage (if any)», прирост ≥ 0."""
    base = D(str(base)); f = cola(cola_year, int(base_year), oct_mode, base_vintage); raw = base * f
    if applies == 'increase':
        return base + rnd(max(base * (f - 1), D(0)), mult, mode), raw, f
    return rnd(raw, mult, mode), raw, f
