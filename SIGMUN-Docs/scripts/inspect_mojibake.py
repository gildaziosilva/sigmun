from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
paths = [
    root / '00-Governanca' / '000-CONSTITUICAO-DO-PROJETO-SIGMUN.md.md',
    root / '00-Governanca' / '000A–Padrao-Corporativo-de-Documentacao-do-SIGMUN.md',
    root / '000-CONSTITUICAO-DO-PROJETO-SIGMUN.md.md',
    root / '96-Sustentabilidade' / '001-Plano-de-Captacao-de-Recursos.md',
    root / '96-Sustentabilidade' / '002-Programa-Nacional-de-Colaboradores.md.md',
    root / '96-Sustentabilidade' / '005-Modelo-de-Certificacao-e-Servicos.md.md',
    root / '97-Estudos-e-Pesquisas' / '001-Estudo-Nacional-da-Transformacao-Digital-dos-Municipios-Brasileiros.md',
    root / '97-Estudos-e-Pesquisas' / '007-Framework-Nacional-de-Avaliacao-da-Maturidade-Digital-Municipal.md',
    root / '97-Estudos-e-Pesquisas' / '012-Modelo-de-Diagnostico-e-Plano-de-Evolucao.md',
    root / '97-Estudos-e-Pesquisas' / '013-Modelo-de-Certificacao-da-Maturidade-Digital-Municipal.md',
    root / '99-Anexos' / 'Estudos' / 'Estrutura-da-Constituicao-SIGMUN.md'
]
for path in paths:
    if not path.exists():
        print(f'MISSING {path}')
        continue
    b = path.read_bytes()
    print('FILE', path.relative_to(root))
    print('BYTES', b[:80])
    try:
        t = b.decode('utf-8')
        print('DECODED OK')
    except UnicodeDecodeError as e:
        print('UTF8 FAIL', e)
        t = b.decode('utf-8', errors='replace')
    for i, line in enumerate(t.splitlines(), 1):
        if 'Ã' in line or 'Â' in line or '�' in line or '??' in line:
            print(f' {i}: {repr(line)}')
    print()