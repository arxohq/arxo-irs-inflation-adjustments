"""Таблица прогноза 2027: сумма → статья → база → округление → по тексту → по правилам IRS → класс-кандидат и причина.
Читает forecast-2027.json, пишет FORECAST.ru.md."""
import json, os
from decimal import Decimal as D, ROUND_HALF_UP
HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, '..')
R = json.load(open(os.path.join(WORK, 'forecast-2027.json')))
PENALTY_ITEMS = ('4.52', '4.53', '4.54', '4.55', '4.56', '4.57', '4.58', '4.59')

# Причины расхождения-кандидата. Классы — как в сверке 2026: а — наше чтение; б — IRS против текста; в — даты/поправка.
B_RULE = {
 'std_deduction_hoh': '§63(c)(7)(B)(ii) округляет прирост до $50 вниз; IRS в 2026 округлил всю сумму (24 150)',
 'qualified_disability_trust_exemption': '§6334(d)(4)(C) через §642(b)(2)(C)(iii)(II) округляет прирост до $100 вниз; IRS в 2025 и 2026 округлял сумму',
 'levy_exempt_dependent_amount': '§6334(d)(4)(C) округляет прирост до $100 вниз; IRS в 2025 и 2026 округлял сумму',
 'sbhic_average_wage_amount': 'в §45R(d)(3)(B) округления нет; IRS в 2026 дал ближайшие $100',
 'ag_hort_dues_limit': 'в §512(d)(2) округления нет; IRS — до доллара',
 'low_cost_article': 'в §513(h)(2)(C) округления нет; IRS — до 10 центов',
 'insubstantial_benefit_5': 'следует за low-cost article',
 'insubstantial_benefit_25': 'Rev. Proc. 90-12/92-102: IRS публикует 5× low-cost article, а не индексацию $25',
 'insubstantial_benefit_50': 'Rev. Proc. 90-12/92-102: IRS публикует 10× low-cost article, а не индексацию $50',
 'foreign_gift_reporting_threshold_6039F': 'в §6039F(d) округления нет; IRS — до доллара',
 'amt_kiddie_exemption_addon': 'сумма построена верно, но §59(j) не применяется (§55(d)(4)(A)(iii)); IRS публикует её ежегодно',
}
A_RULE = {
 'rt_estate_10_24': 'граница трастов 10%→24%: «конец 10%» (база 2016) или «начало ступени выше 22%» (база 2017, §70101(b)); IRS в 2026 взял 2016',
 'rt_estate_tax_at_24': 'следствие границы 10→24 для трастов', 'rt_estate_tax_at_35': 'следствие границы 10→24 для трастов',
 'rt_estate_tax_at_37': 'следствие границы 10→24 для трастов',
 'expatriate_avg_income_tax_threshold': '§877(a)(2): подстановка «2003» вместо «1992» после TCJA пуста; по смыслу база 2003 (= IRS 2026)',
 'eo_lobbying_dues_limit_6033e3': 'Rev. Proc. 98-19 §5.05 не называет базовый год; 1997 восстановлен подбором',
}
LTC = {'ltc_premium_age_40_or_less', 'ltc_premium_age_41_to_50', 'ltc_premium_age_51_to_60', 'ltc_premium_age_61_to_70',
       'ltc_premium_age_over_70', 'ltc_per_diem_limit_7702B'}
NEW = {
 'estate_basic_exclusion_2010c3': 'новая база OBBBA (2025), первый индексируемый год; округляется сумма до $10,000',
 'gst_exemption_2631c': 'равен basic exclusion amount',
 'info_reporting_threshold_6041a': 'новая база OBBBA (2025), прирост до $100; год — календарный год платежей',
 'educational_assistance_127a2': 'новая база OBBBA (2025), прирост до $50',
 'qbi_min_deduction_199Ai': 'новая база OBBBA (2025), прирост до $5', 'qbi_min_active_income_199Ai': 'новая база OBBBA (2025), прирост до $5',
 'child_care_credit_max_45F': 'новая база OBBBA (2025); в §45F(b)(2) правила округления НЕТ — IRS, вероятно, округлит (как §45R)',
 'child_care_credit_max_small_45F': 'новая база OBBBA (2025); в §45F(b)(2) правила округления НЕТ — IRS, вероятно, округлит (как §45R)',
 'qsbs_per_issuer_cap_1202b4': 'новая база OBBBA (2025), прирост до $10,000',
 'qsbs_gross_assets_1202d1': 'новая база OBBBA (2025), прирост до $10,000; нумерация вставки «(b)(4)» конфликтует с уже существующим (b)(4)',
 'salt_cap_164b7': 'статутный рост 101% (не C-CPI-U), округления нет', 'salt_threshold_164b7': 'статутный рост 101% (не C-CPI-U), округления нет',
 'amt_phaseout_mfj': 'первый индексируемый год порога $1,000,000 (база 2025, §70107(b))',
 'amt_phaseout_single': 'следует за порогом MFJ (50%)', 'amt_phaseout_mfs': 'следует за порогом MFJ (50%)',
}

def fmt(x):
    if x is None: return '—'
    try: d = D(str(x).replace(',', ''))
    except Exception: return str(x)
    if d == d.to_integral_value(): return f'{int(d):,}'.replace(',', ' ')
    q = d.quantize(D('0.01'), ROUND_HALF_UP) if abs(d) >= 1 else d.quantize(D('0.0001'), ROUND_HALF_UP)
    s = str(q); return s.rstrip('0').rstrip('.') if '.' in s else s

def octs(o, key):
    v = o[key]; return len({x for x in v.values()}) > 1

def classify(o):
    """→ (класс, прогноз-кандидат IRS, причина). Классы прогноза: '=' твёрдый; 'окт' зависит от октября 2025;
    'а', 'б', 'в' — кандидаты в расхождение по причинам 2026 года; 'нов' — первая индексация OBBBA."""
    i = o['id']; item = o['item'].split('(')[0].strip()
    reasons, cls = [], []
    if item in PENALTY_ITEMS:
        cls.append('в'); reasons.append('штраф за декларации 2028 года: по тексту COLA 2028 (C-CPI-U сен.2026–авг.2027) — не вычислим до сентября 2027; прогноз — практика IRS, COLA 2027')
    if i in B_RULE: cls.append('б'); reasons.append(B_RULE[i])
    if i in LTC: cls.append('б'); reasons.append('§213(d)(10)(B)(ii): буквально смешанный знаменатель (мед. CPI-U × общий §1(f)(3)(B)); IRS сцепляет по мед. компоненту на авг. 2016 и округляет сумму до $10')
    if i in A_RULE: cls.append('а'); reasons.append(A_RULE[i])
    if i in NEW: cls.append('нов'); reasons.append(NEW[i])
    if i in ('petroleum_tax_total', 'oil_spill_liability_rate'):
        cls.append('в'); reasons.append('ставка OSLTF истекла 31.12.2025 (§4611(f)(2), Announcement 2026-2): ждём только Superfund')
    if octs(o, 'irs_by_oct') or (o['text'] is not None and octs(o, 'text_by_oct')):
        cls.append('окт')
        ib = o['irs_by_oct']
        reasons.append(f"октябрь 2025: 11 мес. → {fmt(ib['m11'])}; интерполяция → {fmt(ib['geo'])}" + (f"; перенос сентября → {fmt(ib['cf'])}" if ib['cf'] != ib['geo'] else ''))
    alt = o.get('alt') or {}
    if 'irs_alt_150pct_single' in alt:
        reasons.append(f"второе объяснение числа IRS 2026 (24 150 = 1,5 × 16 100): 1,5 × single → {fmt(alt['irs_alt_150pct_single']['m11'])}")
    if 'base2025_from_vintage_20250911' in alt:
        b = alt['base2025_from_vintage_20250911']
        if b['m11'] != (o['text'] or o['irs_rules']):
            cls.append('а'); reasons.append(f"§1(f)(6)(A): база 2025 берётся из винтажа 2026-09-11; если IRS возьмёт среднее 2025 года из выпуска 11.09.2025 → {fmt(b['m11'])}")
    if not cls: cls.append('=')
    return '+'.join(cls), '; '.join(reasons)

def rounding(o):
    r = o.get('rounding') or {}
    if not r or not r.get('multiple') or r.get('mode') in (None, 'none'): return '—'
    m = {'down': '↓', 'up': '↑', 'nearest': '≈'}.get(r['mode'], r['mode'])
    return f"{m}{r['multiple']} {'прирост' if r.get('applies_to') == 'increase' else 'сумма'}"

def sortkey(o):
    it = o['item'].split('(')[0].strip()
    if it.startswith('E.'): return (99, o['item'], o['id'])
    return (int(it.split('.')[1]), o['item'], o['id'])

def main():
    rows = sorted(R, key=sortkey)
    from collections import Counter
    c, firm = Counter(), 0
    out = ['| п. | сумма (id) | статья | база → год COLA (текст / IRS) | округление | 2026 IRS | 2027 по тексту | 2027 по правилам IRS | класс | причина |',
           '|---|---|---|---|---|---:|---:|---:|:-:|---|']
    for o in rows:
        k, why = classify(o); o['class'] = k; o['why'] = why
        for part in k.split('+'): c[part] += 1
        if k == '=': firm += 1
        if o['kind'] in ('indexed', 'not_code_indexed') and o['base']:
            cy = f"{o['cola_year_text']}" + (f" / {o['cola_year_irs']}" if str(o['cola_year_irs']) != str(o['cola_year_text']) else '')
            base = f"{fmt(o['base'])} ({o['base_year']}) → {cy}"
        else:
            base = {'derived': 'производная', 'fixed_statutory': 'статутная', 'statutory_formula': 'статутная формула'}.get(o['kind'], o['kind'])
        cite = (o['cite'] or '').replace('|', '/')[:70]
        out.append(f"| {o['item']} | {o['label'] or o['id']} (`{o['id']}`) | {cite} | {base} | {rounding(o)} | {fmt(o['irs_2026'])} | "
                   f"{fmt(o['text']) if o['text'] is not None else 'не вычислим'} | {fmt(o['irs_rules'])} | {k} | {why} |")
    head = [f'Всего сумм: {len(rows)} (295 пунктов Rev. Proc. 2025-32 + {len(rows) - 295} новых баз OBBBA). Твёрдых (класс `=`): {firm}.',
            'Вхождения классов (сумма может нести несколько): ' + ', '.join(f'`{k}`: {v}' for k, v in sorted(c.items())) + '.', '',
            'Классы: `=` твёрдый прогноз — текст и правила IRS дают одно число при любом учёте октября 2025; '
            '`окт` — число зависит от того, как усреднить год без октября 2025 (в колонках — вариант «среднее 11 месяцев», '
            'альтернатива — в причине); `а` наше чтение; `б` правило IRS против буквы статьи (выявлено в 2026); '
            '`в` год индекса (штрафы); `нов` — первая индексация базы OBBBA.', '']
    open(os.path.join(WORK, 'FORECAST.ru.md'), 'w').write('# Прогноз индексируемых сумм IRC на 2027 год\n\n' + '\n'.join(head + out) + '\n')
    json.dump([{k: o[k] for k in ('item', 'id', 'class', 'why')} for o in rows], open(os.path.join(WORK, 'classes-2027.json'), 'w'), ensure_ascii=False, indent=1)
    print(head[0]); print(head[1])

if __name__ == '__main__':
    main()
