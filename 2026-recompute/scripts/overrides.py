"""Ручные расчёты для сумм, не укладывающихся в общую формулу. Каждая функция возвращает
(значение, сырое, коэффициент, {альтернативы}). Источник правила — паспорт в specs/*.json."""
from decimal import Decimal as D, ROUND_HALF_UP
from cpi import cola, rnd

REG = {}
def get(i): return REG.get(i)
def reg(*ids):
    def w(fn):
        for i in ids: REG[i] = fn
        return fn
    return w

def ix(base, by, mult, mode, applies='increase', cy=2026, vintage=True):
    base = D(base); f = cola(cy, by, vintage); raw = base * f
    if applies == 'increase': return base + rnd(max(base * (f - 1), D(0)), mult, mode), raw, f
    return rnd(raw, mult, mode), raw, f

# --- §32 EITC: (b)(2)(A) база 1995, $5,000 из (b)(2)(B) база 2008; §32(j)(2)(A) — сумма до ближайших $10
EITC = {'1': ('6330', '11610', D('0.34'), D('0.1598')), '2': ('8890', '11610', D('0.40'), D('0.2106')),
        '3': ('8890', '11610', D('0.45'), D('0.2106')), '0': ('4220', '5280', D('0.0765'), D('0.0765'))}
def eitc(n):
    ei, ph, cr, po = EITC[n]
    e, _, _ = ix(ei, 1995, 10, 'nearest', 'amount')
    t, _, _ = ix(ph, 1995, 10, 'nearest', 'amount')
    f95, f08 = cola(2026, 1995), cola(2026, 2008)
    tj_text = rnd(D(ph) * f95 + D(5000) * f08, 10, 'nearest')            # чтение A: сумма, одно округление
    tj_sep = t + rnd(D(5000) * f08, 10, 'nearest')                         # чтение B: по отдельности
    mc_raw = cr * e
    mc = mc_raw.quantize(D(1), ROUND_HALF_UP)
    return dict(e=e, t=t, tj=tj_text, tj_sep=tj_sep, mc=mc, mc_raw=mc_raw, po=po)

for n in '0123':
    def mk(n):
        def max_credit(s):
            r = eitc(n); return r['mc'], r['mc_raw'], None, {'unrounded': f"{r['mc_raw']}"}
        def thr_mfj(s):
            r = eitc(n); return r['tj'], None, None, {'components_rounded_separately': r['tj_sep']}
        def comp(mfj):
            def f(s):
                r = eitc(n); th = r['tj'] if mfj else r['t']
                v_rounded_mc = th + r['mc'] / r['po']
                v_raw_mc = th + r['mc_raw'] / r['po']
                return v_rounded_mc.quantize(D(1), ROUND_HALF_UP), v_rounded_mc, None, {
                    'from_unrounded_max_credit': v_raw_mc.quantize(D(1), ROUND_HALF_UP),
                    'truncated': int(v_rounded_mc)}
            return f
        REG[f'eitc_max_credit_{n}'] = max_credit
        REG[f'eitc_phaseout_threshold_{n}_mfj'] = thr_mfj
        REG[f'eitc_phaseout_complete_{n}_other'] = comp(False)
        REG[f'eitc_phaseout_complete_{n}_mfj'] = comp(True)
    mk(n)

# --- §42(h)(3)(H) затем (I): ×1.12 без округления
@reg('lihtc_state_ceiling_per_capita')
def _lihtc_pc(s):
    v, raw, f = ix('1.75', 2001, '0.05', 'down'); return v * D('1.12'), raw, f, {'before_x1.12': v}
@reg('lihtc_state_ceiling_minimum')
def _lihtc_min(s):
    v, raw, f = ix('2000000', 2001, 5000, 'down'); return v * D('1.12'), raw, f, {'before_x1.12': v}

# --- §45R(d)(3)(B): в тексте округления нет
@reg('sbhic_average_wage_amount')
def _45r(s):
    _, raw, f = ix('25000', 2012, 1, 'none', 'amount')
    return raw, raw, f, {'nearest_100': rnd(raw, 100, 'nearest'), 'down_100': rnd(raw, 100, 'down'),
                         'down_1000_like_d3A': rnd(raw, 1000, 'down')}

# --- Notice 2020-33: перенос FSA = 20% лимита §125(i)
@reg('health_fsa_carryover_max')
def _fsa(s):
    v, raw, f = ix('2500', 2012, 50, 'down'); return v * D('0.2'), None, None, {}

# --- §55(d)(4)(A)(ii)(III)? порог трастов: 50% от $150,000, индексированных с базой 2011 до ближайших $100 (паспорт A)
@reg('amt_phaseout_estate')
def _amt_est(s):
    v, raw, f = ix('150000', 2011, 100, 'nearest', 'amount'); return v / 2, raw / 2, f, {'index_half_directly_75000': ix('75000', 2011, 100, 'nearest', 'amount')[0]}

# --- трасты: граница 10%→24% одновременно «конец 10%» (база 2016) и «начало ступени выше 22%» (база 2017)
@reg('rt_estate_10_24')
def _est1024(s):
    v17, raw17, f17 = ix('2550', 2017, 50, 'down'); v16, raw16, f16 = ix('2550', 2016, 50, 'down')
    return v17, raw17, f17, {'as_end_of_10pct_base2016': v16}

# --- §213(d)(10)(B)(ii): медицинский компонент C-CPI-U за август (Y-1) против мед. CPI-U августа 1996 × §1(f)(3)(B)
import csv, glob, os
from cpi import CPI, CCPI_NOW, VINT, MED, avg12
_SRC = os.environ.get('IRC_SRC', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data'))
def _medc():
    rows = list(csv.reader(open(glob.glob(os.path.join(_SRC, 'alfred-med', 'vintages_*.csv'))[0])))
    return {(int(r[0][:4]), int(r[0][5:7])): D(r[1]) for r in rows[1:] if r[1].strip() not in ('', '.')}
MEDC = _medc()   # винтаж 2025-09-11
def ltc_variants(base):
    b = D(base); k16 = VINT['20250911']
    lit = MEDC[(2025, 8)] / (MED[(1996, 8)] * (avg12(k16, 2016) / avg12(CPI, 2016)))          # буквально
    medn_aug = MEDC[(2025, 8)] / (MED[(1996, 8)] * (MEDC[(2016, 8)] / MED[(2016, 8)]))         # сцепка по мед. компоненту, август 2016
    cpi_only = MED[(2025, 8)] / MED[(1996, 8)]                                                  # редакция до TCJA (мед. CPI-U)
    out = {}
    for nm, f in (('literal', lit), ('medical_link_aug2016', medn_aug), ('pre_TCJA_medCPI_U', cpi_only)):
        out[nm] = (b + rnd(b * (f - 1), 10, 'nearest'), f)
    out['medical_link_aug2016_amount_rounded'] = (rnd(b * medn_aug, 10, 'nearest'), medn_aug)
    return out
for _id, _b in (('ltc_premium_age_40_or_less', '200'), ('ltc_premium_age_41_to_50', '375'), ('ltc_premium_age_51_to_60', '750'),
                ('ltc_premium_age_61_to_70', '2000'), ('ltc_premium_age_over_70', '2500')):
    def _mk(b):
        def f(s):
            o = ltc_variants(b)
            return o['literal'][0], D(b) * o['literal'][1], o['literal'][1], {k: f'{v[0]} (f={v[1]:.5f})' for k, v in o.items() if k != 'literal'}
        return f
    REG[_id] = _mk(_b)

# --- §7702B(d)(4): $175 × medical care cost adjustment §213(d)(10)(B)(ii), прирост до ближайших $10 (§7702B(d)(5))
@reg('ltc_per_diem_limit_7702B')
def _7702b(s):
    o = ltc_variants('175')
    return o['literal'][0], D(175) * o['literal'][1], o['literal'][1], {k: f'{v[0]} (f={v[1]:.5f})' for k, v in o.items() if k != 'literal'}

# --- §4611(f)(2): ставка OSLTF «shall not apply after December 31, 2025» → по тексту на 2026 год 0
@reg('oil_spill_liability_rate')
def _osltf(s): return D('0.00'), None, None, {'rev_proc_2025_32': D('0.09')}
@reg('petroleum_tax_total')
def _4611(s):
    sf, _, f = ix('0.164', 2022, '0.01', 'down', 'amount')
    return sf, None, f, {'rev_proc_2025_32_incl_osltf': sf + D('0.09'), 'announcement_2026_2': D('0.18')}
