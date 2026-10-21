"""Натурный опыт: как IRS обошёлся без октября 2025. HSA/HDHP 2027 (Rev. Proc. 2026-24) по §223(g):
COLA §1(f)(3) с периодами по 31 марта, база 1997 (лимиты взносов) и 2003 (HDHP), прирост до ближайших $50.
Окно Apr 2025 – Mar 2026 содержит октябрь 2025. Винтаж — 2026-04-10 (выход мартовского значения), как в
контроле 2026 года (там 6 из 6 совпали на винтаже 2025-04-10)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D
from cpi27 import VINT, CPI, avg12, rnd, OCT_MODES

IRS = {('2250', 1997): '4500', ('4500', 1997): '9000', ('1000', 2003): '1750', ('2000', 2003): '3500',
       ('5000', 2003): '8700', ('10000', 2003): '17400'}
LABEL = {('2250', 1997): 'взнос self-only §223(b)(2)(A)', ('4500', 1997): 'взнос family §223(b)(2)(B)',
         ('1000', 2003): 'HDHP франшиза self-only', ('2000', 2003): 'HDHP франшиза family',
         ('5000', 2003): 'HDHP предел расходов self-only', ('10000', 2003): 'HDHP предел расходов family'}

def factor(cc, by, mode):
    return avg12(cc, 2026, mode, 3) / (avg12(CPI, by, 'm11', 3) * avg12(cc, 2016, 'm11', 3) / avg12(CPI, 2016, 'm11', 3))

def main():
    hits = {(vk, m): 0 for vk in ('20260410', '20260911') for m in OCT_MODES}
    lines = []
    for (base, by), irs in IRS.items():
        cells = []
        for vk in ('20260410', '20260911'):
            for m in OCT_MODES:
                f = factor(VINT[vk], by, m)
                v = D(base) + rnd(D(base) * (f - 1), 50, 'nearest')
                if v == D(irs): hits[(vk, m)] += 1
                cells.append(f'{vk}/{m}: {v} ({D(base) * f:.2f})')
        lines.append(f'{LABEL[(base, by)]}: база {base} ({by}), IRS {irs} | ' + ' | '.join(cells))
    lines.append('совпадений с Rev. Proc. 2026-24 из 6: ' + ', '.join(f'{vk}/{m}={n}' for (vk, m), n in hits.items()))
    # DPCSA §223(c)(1)(E)(ii)(II): $150, база 2025 (§223(g)(1)(B)(iii)), периоды по 31 марта, прирост до $50
    for m in OCT_MODES:
        f = avg12(VINT['20260410'], 2026, m, 3) / avg12(VINT['20260410'], 2025, 'm11', 3)
        lines.append(f'DPCSA $150 (база 2025), {m}: f={f:.6f} → {150 + rnd(150 * (f - 1), 50, "nearest")} (IRS 150)')
    return lines

if __name__ == '__main__':
    print('\n'.join(main()))
