"""Сверка прогноза с Rev. Proc. на 2027 год — запускать ПОСЛЕ публикации IRS.

Вход: irs-2027.json — {id: "число из Rev. Proc."} (заполняется вручную по PDF; sha256 PDF — в SOURCES.sha256).
Перед сверкой проверить: sha256 forecast-2027.json равен закреплённому в PIN.sha256 (прогноз не правили задним числом).
Классы — те же, что в сверке 2026 года: = совпало с текстом; а — наше чтение; б — IRS против текста; в — даты/поправка;
дополнительно помечается, какой учёт октября 2025 воспроизводит число IRS."""
import json, os, hashlib, sys
from decimal import Decimal as D
HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, '..')

def n(x):
    try: return D(str(x).replace(',', '').replace('$', ''))
    except Exception: return None

def main():
    pin = open(os.path.join(WORK, 'PIN.sha256')).read().split()[0]
    got = hashlib.sha256(open(os.path.join(WORK, 'forecast-2027.json'), 'rb').read()).hexdigest()
    if pin != got: sys.exit(f'forecast-2027.json изменён после закрепления: {got} ≠ {pin}')
    F = {r['id']: r for r in json.load(open(os.path.join(WORK, 'forecast-2027.json')))}
    C = {r['id']: r for r in json.load(open(os.path.join(WORK, 'classes-2027.json')))}
    I = json.load(open(os.path.join(WORK, 'irs-2027.json')))
    rows, cnt = [], {}
    for i, irs in I.items():
        f = F.get(i)
        if f is None: rows.append(f'| {i} | — | — | {irs} | нет в прогнозе | |'); continue
        v = n(irs); hits = []
        if f['text'] is not None and n(f['text']) == v: hits.append('текст/11 мес.')
        for oc, x in f['text_by_oct'].items():
            if oc != 'm11' and x is not None and n(x) == v: hits.append(f'текст/{oc}')
        for oc, x in f['irs_by_oct'].items():
            if x is not None and n(x) == v: hits.append(f'правила IRS/{oc}')
        for name, byoc in (f.get('alt') or {}).items():
            for oc, x in byoc.items():
                if x is not None and n(x) == v: hits.append(f'{name}/{oc}')
        if f['text'] is not None and n(f['text']) == v: k = '='
        elif any(h.startswith('текст/') for h in hits): k = '= (окт: ' + ', '.join(h for h in hits if h.startswith('текст/')) + ')'
        elif hits: k = '+'.join(x for x in C[i]['class'].split('+') if x not in ('окт', '=')) or 'б'
        else: k = '? новое расхождение'
        cnt[k] = cnt.get(k, 0) + 1
        rows.append(f"| {f['item']} | {i} | {f['text'] or 'не вычислим'} | {irs} | {k} | {', '.join(hits)} |")
    head = ['# Сверка прогноза 2027 с Rev. Proc.', '', f'Закреплённый прогноз: sha256 {pin}.', '',
            'Итог: ' + ', '.join(f'{k}: {v}' for k, v in sorted(cnt.items())), '',
            '| п. | id | по тексту (11 мес.) | IRS | класс | какие варианты дают число IRS |', '|---|---|---:|---:|---|---|']
    open(os.path.join(WORK, 'COMPARE.ru.md'), 'w').write('\n'.join(head + rows) + '\n')
    print(head[4])

if __name__ == '__main__':
    main()
