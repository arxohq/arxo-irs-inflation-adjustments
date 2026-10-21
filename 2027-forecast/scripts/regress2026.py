"""Регрессия: тот же compute27.py на паспортах и винтаже 2026 года обязан повторить разведку 21.10.2026.
Ожидается: чтение «текст» = прежнее «наше» во всех вычислимых суммах; чтение «правила IRS» = Rev. Proc. 2025-32
во всех суммах, кроме §4611 (IRS исправил Announcement 2026-2)."""
import json, os, subprocess, sys, tempfile
from decimal import Decimal as D
HERE = os.path.dirname(os.path.abspath(__file__))
OLD = os.path.join(HERE, '..', '..', '2026-recompute')

def n(x):
    try: return D(str(x).replace(',', ''))
    except Exception: return None

def main():
    out = os.path.join(tempfile.mkdtemp(), 'regress2026.json')
    env = dict(os.environ, IRC_CY='2026', IRC_SPECS=os.path.join(OLD, 'specs'), IRC_OUT=out)
    subprocess.run([sys.executable, '-I', os.path.join(HERE, 'compute27.py')], env=env, check=True, capture_output=True)
    new = {r['id']: r for r in json.load(open(out))}
    old = {r['id']: r for r in json.load(open(os.path.join(OLD, 'results.json')))}
    q = lambda x: n(x).quantize(D('0.000001'))   # прогноз хранит несокращённые суммы до 6 знаков
    t_bad = [i for i, o in old.items() if new[i]['text'] is not None and q(new[i]['text']) != q(o['ours'])]
    i_ok = [i for i, o in old.items() if new[i]['irs_rules'] is not None and n(new[i]['irs_rules']) == n(o['irs'])]
    i_bad = [(i, new[i]['irs_rules'], old[i]['irs']) for i in old if i not in i_ok]
    print(f'текст ≠ разведка 2026: {len(t_bad)} {t_bad}')
    print(f'правила IRS = Rev. Proc. 2025-32: {len(i_ok)} из {len(old)}; остальные: {i_bad}')

if __name__ == '__main__':
    main()
