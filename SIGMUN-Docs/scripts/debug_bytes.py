from pathlib import Path
root = Path(__file__).resolve().parents[1]
for rel in [Path('000-CONSTITUICAO-DO-PROJETO-SIGMUN.md.md'), Path('99-Anexos/Estudos/Estrutura-da-Constituicao-SIGMUN.md')]:
    p = root / rel
    print('FILE', rel)
    b = p.read_bytes()
    print('len', len(b))
    print('hex', b[:80].hex())
    print('repr', repr(b[:80]))
    text = b.decode('utf-8', errors='replace')
    for i, line in enumerate(text.splitlines(), 1):
        if 'Â' in line or '�' in line or 'Ã' in line:
            print(i, repr(line))
    print()