"""Контроль метода: HSA §223(b)(2)(B) family limit 2018 — Rev. Proc. 2017-37 ($6,900) против 2018-18 ($6,850)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cpi import CPI, CCPI_NOW, VINT, rnd
from decimal import Decimal as D

def avg(series, year, end_month):
    ms = [((year - 1) if m > end_month else year, m) for m in list(range(end_month + 1, 13)) + list(range(1, end_month + 1))]
    return sum(series[k] for k in ms) / D(12)

def show(label, base, f, mult=50):
    inc = D(base) * (f - 1)
    print(f'{label:<64} COLA={f:.6f} raw={D(base)*f:.2f} -> {D(base)+rnd(inc, mult, "nearest")}')

for base, nm in (('4500', 'family'), ('2250', 'self-only')):
    print(f'== {nm} base ${base}')
    # до TCJA: §1(f)(3) CPI(2017)/CPI(1997), годы — 12 мес. по 31 марта (§223(g)(1) посл. предл.)
    show('2017-37: CPI-U, Mar-31 periods', base, avg(CPI, 2017, 3) / avg(CPI, 1997, 3))
    for vk, vlab in (('20170914', 'vintage 2017-09-14'), ('20180313', 'vintage 2018-03-13'), (None, 'current final')):
        cc = VINT[vk] if vk else CCPI_NOW
        f = avg(cc, 2017, 3) / (avg(CPI, 1997, 3) * avg(cc, 2016, 3) / avg(CPI, 2016, 3))
        show(f'2018-18: C-CPI-U, all Mar-31, {vlab}', base, f)
        f2 = avg(cc, 2017, 3) / (avg(CPI, 1997, 3) * avg(cc, 2016, 8) / avg(CPI, 2016, 8))
        show(f'2018-18: C-CPI-U, Mar-31 num/base, 2016 ratio Aug-31, {vlab}', base, f2)
