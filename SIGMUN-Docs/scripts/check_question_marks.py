from pathlib import Path
root = Path(__file__).resolve().parents[1]
for path in sorted(root.rglob('*.md')):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8', errors='ignore')
    matches = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if '?' in line or '�' in line:
            matches.append((lineno, line))
    if matches:
        print(path.relative_to(root))
        for lineno, line in matches:
            print(f'{lineno}: {line}')
        print()