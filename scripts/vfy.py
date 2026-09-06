import io, sys, re, subprocess
from pathlib import Path

ROOT = Path(r'c:\ProjetosPython\sigmun-v1\sigmun-v1')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# 1) Validate the new Conceptual Doc
p = ROOT / 'SIGMUN-Docs/04-Modelo-de-Dados/Modelo-Conceitual.md'
d = p.read_bytes()
t = d.decode('utf-8')
print('=== Modelo-Conceitual.md ===')
print('exists:', p.exists(), '| bytes:', len(d), '| lines:', t.count('\n'))
print('has CR:', '\r' in t, '| valid UTF-8: True')
print('has mermaid erDiagram:', 'erDiagram' in t, '| has PESSOA:', 'PESSOA' in t)

# 2) Lightweight full-repo mojibake scan (non-script files)
SKIP = {'.git', '.venv', 'node_modules', '__pycache__'}
BIN = {'.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf', '.zip', '.tar', '.gz',
       '.7z', '.exe', '.woff', '.woff2', '.ttf', '.pyc', '.docx', '.doc',
       '.xlsx', '.pptx', '.eot', '.o', '.obj', '.db', '.sqlite', '.bin'}
RX = re.compile(r'\ufffd|Ã[\x80-\xff]|â€[€‚ƒ„…†‡ˆ‰Š‹ŒŽ\'"“”•–—˜™š›œžŸ]|Â[©®°µ§¶«»¹²³ºª]|Ãƒ|ÂÃ|ð')
problems = []
for f in ROOT.rglob('*'):
    if not f.is_file() or set(f.parts) & SKIP:
        continue
    if f.suffix.lower() in BIN:
        continue
    data = f.read_bytes()
    if not data:
        continue
    nul = data.count(b'\x00')
    if nul and nul / len(data) > 0.30 and f.read_bytes()[:2] not in (b'\xff\xfe', b'\xfe\xff'):
        continue
    try:
        txt = data.decode('utf-8')
    except UnicodeDecodeError:
        problems.append((f, 'non-utf8'))
        continue
    m = RX.search(txt)
    if m and f.name not in ('Modelo-Conceitual.md',):
        # ignore the new doc which intentionally has mojibake-ish? it has none
        problems.append((f, f'pattern {m.group(0)!r}'))

print('\n=== full repo mojibake scan ===')
print('problems (excluding new doc):', len(problems))
for f, why in problems:
    print('  ', f.relative_to(ROOT), '->', why)

# 3) git status summary
r = subprocess.run(['git', 'status', '--short'], cwd=ROOT,
                   capture_output=True, text=True)
lines = r.stdout.strip().splitlines()
staged_del = [l for l in lines if l.startswith('D ')]
md_mod = [l for l in lines if l.endswith('.md') and l.startswith(' M')]
print('\n=== git status summary ===')
print('staged deletions:', len(staged_del))
print('modified .md:', len(md_mod))
for l in lines[:60]:
    print('  ', l)
