"""Итоговая таблица: сумма → статья → база → округление → наше → IRS → класс. Читает results.json."""
import json, os, sys
from decimal import Decimal as D, ROUND_HALF_UP
HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.environ.get('IRC_WORK', os.path.join(HERE, '..'))
R = json.load(open(os.path.join(WORK, 'results.json')))

PENALTY_ITEMS = ('4.52', '4.53', '4.54', '4.55', '4.56', '4.57', '4.58', '4.59')
NOTE = {
 'std_deduction_hoh': ('б', 'IRS округлил до $50 всю сумму (24 184.56 → 24 150); §63(c)(7)(B)(ii) округляет прирост (559.56 → 550)'),
 'qualified_disability_trust_exemption': ('б', 'IRS округлил сумму (5 317 → 5 300); §6334(d)(4)(C), на который ссылается §642(b)(2)(C)(iii)(II), округляет прирост до $100 вниз (1 167 → 1 100); в 2025: текст 5 150, IRS 5 100'),
 'levy_exempt_dependent_amount': ('б', 'то же правило §6334(d)(4)(C): текст 5 250, IRS 5 300'),
 'rt_estate_10_24': ('а', 'текст двусмыслен: граница — «конец 10%» (база 2016 после §70101(b)) и «начало ступени выше 22%» (база 2017); IRS выбрал 2016 → 3 300'),
 'rt_estate_tax_at_24': ('а', 'следствие границы 10→24 для трастов'),
 'rt_estate_tax_at_35': ('а', 'следствие границы 10→24 для трастов'),
 'rt_estate_tax_at_37': ('а', 'следствие границы 10→24 для трастов'),
 'sbhic_average_wage_amount': ('б', 'в §45R(d)(3)(B) и 26 CFR 1.45R-3 округления нет (34 057.75); IRS дал ближайшие $100'),
 'ag_hort_dues_limit': ('б', 'округления в §512(d)(2) нет (211.58); IRS — до доллара'),
 'low_cost_article': ('б', 'округления в §513(h)(2)(C) нет (13.878); IRS — до 10 центов'),
 'insubstantial_benefit_5': ('б', 'Rev. Proc. 90-12/92-102: правила округления нет; IRS = 1×/5×/10× от 13.90'),
 'insubstantial_benefit_25': ('б', 'то же: 5 × 13.90 = 69.50, а не самостоятельная индексация (69.39)'),
 'insubstantial_benefit_50': ('б', 'то же: 10 × 13.90 = 139'),
 'foreign_gift_reporting_threshold_6039F': ('б', 'округления в §6039F(d) нет (20 573.24); IRS — до доллара'),
 'amt_kiddie_exemption_addon': ('б', 'сумма посчитана верно, но §59(j) не применяется: §55(d)(4)(A)(iii) (P.L. 116-94, с 2018), постоянный после §70107(a)'),
 'petroleum_tax_total': ('в', 'ставка OSLTF $0.09 истекла 31.12.2025 (§4611(f)(2)); по тексту 2026 = $0.18; IRS исправил Announcement 2026-2'),
 'oil_spill_liability_rate': ('в', 'по тексту на 2026 не действует (§4611(f)(2)); Announcement 2026-2'),
 'expatriate_avg_income_tax_threshold': ('а', 'отсылка §877(a)(2) («2003» вместо «1992» в §1(f)(3)(B)) не согласована с TCJA; по смыслу база 2003 → 211 000 (= IRS); буквально подстановка пустая → 161 000'),
 'eo_lobbying_dues_limit_6033e3': ('а', 'Rev. Proc. 98-19 §5.05 не называет базовый год; 1997 восстановлен подбором (147 в 2026 и 110 в 2014)'),
}
LTC = {'ltc_premium_age_40_or_less', 'ltc_premium_age_41_to_50', 'ltc_premium_age_51_to_60', 'ltc_premium_age_61_to_70', 'ltc_premium_age_over_70', 'ltc_per_diem_limit_7702B'}

def fmt(x):
    if x is None: return '—'
    try:
        d = D(str(x))
    except Exception:
        return str(x)
    if d == d.to_integral_value(): return f'{int(d):,}'.replace(',', ' ')
    q = d.quantize(D('0.01'), ROUND_HALF_UP) if abs(d) >= 1 else d.quantize(D('0.0001'), ROUND_HALF_UP)
    return str(q).rstrip('0').rstrip('.') if '.' in str(q) else str(q)

def classify(o):
    if o['id'] in NOTE: return NOTE[o['id']]
    if o['id'] in LTC:
        a = o['alt'].get('medical_link_aug2016_amount_rounded', '')
        return ('б', f"буквально (мед. C-CPI-U ÷ мед. CPI-U × общий коэффициент §1(f)(3)(B)) → {fmt(o['ours'])}; IRS = сцепка по мед. компоненту на авг. 2016 и округление суммы → {a.split(' ')[0]}")
    if o['item'].split('(')[0].strip() in PENALTY_ITEMS and o['class'] != 'совпало':
        p = o['alt'].get('cola_year_2026')
        return ('в', f"текст: COLA за год подачи 2027 (C-CPI-U сен.2025–авг.2026, без окт.2025) → {fmt(o['ours'])}; IRS взял COLA 2026 → {fmt(p) if p else 'IRS'}")
    if o['class'] == 'совпало':
        fv = o['alt'].get('final_values')
        if fv and fv != o['ours'] and o['kind'] != 'derived':
            return ('=', f'совпадает только на значениях C-CPI-U от 11.09.2025 (§1(f)(6)(A)); на нынешних → {fmt(fv)}')
        return ('=', '')
    return ('?', o['class'])

def rounding(o):
    r = o.get('rounding') or {}
    if not r or not r.get('multiple') or r.get('mode') in (None, 'none'): return '—'
    m = {'down': '↓', 'up': '↑', 'nearest': '≈'}.get(r['mode'], r['mode'])
    return f"{m}{r['multiple']} {'прирост' if r.get('applies_to') == 'increase' else 'сумма'}"

def main():
    rows = sorted(R, key=lambda o: (int(o['item'].split('(')[0].split('.')[1]), o['item'], o['id']))
    out = ['| п. | сумма (id) | статья | база → год COLA | округление | по тексту | IRS | класс | примечание |',
           '|---|---|---|---|---|---:|---:|:-:|---|']
    from collections import Counter
    c = Counter()
    for o in rows:
        k, note = classify(o); c[k] += 1
        base = f"{fmt(o['base'])} ({o['base_year']}) → {o['cola_year']}" if o['kind'] in ('indexed', 'not_code_indexed') and o['base'] else ('производная' if o['kind'] == 'derived' else 'статутная')
        cite = (o['cite'] or '').replace('|', '/')[:70]
        out.append(f"| {o['item']} | {o['label'] or o['id']} | {cite} | {base} | {rounding(o)} | {fmt(o['ours'])} | {fmt(o['irs'])} | {k} | {note} |")
    head = [f'Всего сумм: {len(rows)}. ' + ', '.join(f'{k}: {v}' for k, v in sorted(c.items())), '',
            'Классы: `=` совпало; `а` наше чтение (текст неоднозначен или требует реконструкции); `б` IRS против текста; `в` даты или последующая поправка.', '']
    open(os.path.join(WORK, 'TABLE.ru.md'), 'w').write('\n'.join(head + out) + '\n')
    print(head[0])

if __name__ == '__main__':
    main()
