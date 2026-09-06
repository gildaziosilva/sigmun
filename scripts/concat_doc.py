import sys, io
from pathlib import Path

OUTER = Path(r'c:\ProjetosPython\sigmun-v1')
FINAL = Path(r'c:\ProjetosPython\sigmun-v1\sigmun-v1\SIGMUN-Docs\04-Modelo-de-Dados\Modelo-Conceitual.md')

parts = [OUTER / 'part1.md', OUTER / 'part2.md', OUTER / 'part3.md']

# read each part, ensure LF + trailing newline, then join
chunks = []
for p in parts:
    b = p.read_bytes()
    # normalize any CRLF -> LF
    b = b.replace(b'\r\n', b'\n')
    if not b.endswith(b'\n'):
        b += b'\n'
    # add blank-line separator between parts
    chunks.append(b)

combined = b'\n'.join(chunks)
FINAL.write_bytes(combined)

# verify
text = combined.decode('utf-8')
print('Final file bytes:', len(combined))
print('Lines:', text.count('\n'))
print('Has CR:', '\r' in text)
print('Valid UTF-8:', True)
print('--- head ---')
print(text[:120])
print('--- tail ---')
print(text[-120:])

# cleanup temp part files
for p in parts:
    p.unlink()
print('temp part files removed:', [str(p) for p in parts if p.exists()])
