"""Паспорта 2027 года из паспортов 2026 (specs/A–D.json разведки 21.10.2026). Новые базы OBBBA — в specs/E.json
(пишется руками, этот скрипт его не трогает). Правила переноса:
- год COLA 2026 → 2027 (суммы на налоговый/календарный год 2027);
- штрафы пп. 4.52–4.59 («returns required to be filed in 2028»): по тексту COLA за 2028 год подачи,
  по практике IRS — COLA за 2027 (как IRS сделал в Rev. Proc. 2025-32);
- §55(d)(4)(B): $1,000,000 индексируется с 2027 года с базой 2025 (P.L. 119-21 §70107(b));
- число IRS 2026 и наше 2026 сохраняются как irs_value_2026 / ours_2026; irs_value пуст до выхода Rev. Proc."""
import json, os, copy
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '..', '2026-recompute')
OUT = os.path.join(HERE, '..', 'specs')

def main():
    ours26 = {r['id']: r for r in json.load(open(os.path.join(SRC, 'results.json')))}
    n = 0
    for g in 'ABCD':
        out = []
        for s in json.load(open(os.path.join(SRC, 'specs', f'{g}.json'))):
            t = copy.deepcopy(s)
            t['irs_value_2026'] = s['irs_value']; t['irs_value'] = None
            t['ours_2026'] = ours26.get(s['id'], {}).get('ours')
            cy, cp = s.get('cola_year'), s.get('cola_year_irs_practice')
            if cp:                                   # штрафы: год подачи 2028
                t['cola_year'], t['cola_year_irs_practice'] = int(cy) + 1, int(cp) + 1
                t['passport_2027'] = 'returns required to be filed in 2028: текст — COLA 2028 (C-CPI-U сен.2026–авг.2027 ещё не существует), практика IRS — COLA 2027'
            elif cy is not None and int(cy) == 2026:
                t['cola_year'] = 2027
            if s['id'] == 'amt_phaseout_mfj':
                t['kind'] = 'indexed'; t['cola_year'] = 2027; t['base_year'] = '2025'
                t['passport_2027'] = ('§55(d)(4)(B) после P.L. 119-21 §70107(b): «after 2018 (2026, in the case of the $1,000,000 amount '
                                      'in subparagraph (A)(ii)(I))» и подстановка «calendar year 2025» — первый индексируемый год 2027; '
                                      'округление как у сумм §55(d)(4) (ближайшие $100 суммы).')
            out.append(t); n += 1
        json.dump(out, open(os.path.join(OUT, f'{g}.json'), 'w'), ensure_ascii=False, indent=1)
    print('паспортов перенесено:', n)

if __name__ == '__main__':
    main()
