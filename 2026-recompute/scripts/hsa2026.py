"""Доп.: HSA/HDHP 2026 (Rev. Proc. 2025-19) по §223(g): периоды по 31 марта, округление прироста до ближайших $50."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cpi import CPI, CCPI_NOW, VINT, rnd
from hsa_control import avg
from decimal import Decimal as D
IRS = {('2250', 1997): '4400', ('4500', 1997): '8750', ('1000', 2003): '1700', ('2000', 2003): '3400', ('5000', 2003): '8500', ('10000', 2003): '17000'}
for (base, by), irs in IRS.items():
    out = []
    for vk in ('20250410', '20250911', None):
        cc = VINT[vk] if vk else CCPI_NOW
        f = avg(cc, 2025, 3) / (avg(CPI, by, 3) * avg(cc, 2016, 3) / avg(CPI, 2016, 3))
        out.append(f'{vk or "final"}: {D(base)+rnd(D(base)*(f-1), 50, "nearest")} (raw {D(base)*f:.2f})')
    print(f'base {base} y{by} IRS {irs} | ' + ' | '.join(out))
