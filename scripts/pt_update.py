import sys, io
from pathlib import Path

PT = Path(r'c:\ProjetosPython\sigmun-v1\sigmun-v1\SIGMUN-Docs\Plano-de-Trabalho.md')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

raw = PT.read_bytes()
# 1) normalize line endings to LF (consistente com o restante do repo)
text = raw.replace(b'\r\n', b'\n').replace(b'\r', b'\n').decode('utf-8')

repls = [
    ('| Modelo de Dados (Corporativo) | ⚪ Não iniciado |',
     '| Modelo de Dados (Corporativo) | 🟡 Em andamento (Conceitual iniciado) |'),
    ('| Modelo de Dados (Corporativo) | ⚪ | 0% |',
     '| Modelo de Dados (Corporativo) | 🟡 | 25% |'),
    ('Status: ⚪ Não iniciada (nível corporativo)',
     'Status: 🟡 Iniciada (nível corporativo; Modelo Conceitual concluído)'),
    ('- [ ] Modelo Conceitual (corporativo — placeholder; referência disponível no domínio-piloto Compras)',
     '- [x] Modelo Conceitual (corporativo — `04-Modelo-de-Dados/Modelo-Conceitual.md`)'),
    ('| 1.2 | | |',
     '| 1.2 | 2026-08-19 | Iniciada a Fase 5 — Modelo de Dados (Modelo Conceitual Corporativo) |'),
]

for old, new in repls:
    n = text.count(old)
    if n != 1:
        print(f'!! ATENCAO: encontrado {n} ocorrencias de: {old!r}')
    else:
        text = text.replace(old, new, 1)
        print(f'ok: {old[:55]!r}...')

PT.write_bytes(text.encode('utf-8'))
assert b'\r' not in PT.read_bytes(), 'PT ainda tem CR'
print('PT escrito em UTF-8/LF. Bytes:', len(PT.read_bytes()))
