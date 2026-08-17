from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
patterns = [
    'Ã¡', 'Ã©', 'Ã­', 'Ã³', 'Ãº', 'Ã£', 'Ãµ', 'Ã§', 'Ã±',
    'Ã‰', 'Ã ', 'Ãª', 'Ãª', 'Ã‚', 'Ã´', 'Ãª', 'Ãª',
    'â€™', 'â€œ', 'â€�', 'â€“', 'â€”', 'â€', 'Â', '??', '�'
]

for path in sorted(root.rglob('*.md')):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8', errors='ignore')
    matches = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for pat in patterns:
            if pat in line:
                matches.append((lineno, pat, line))
                break
    if matches:
        print(path.relative_to(root))
        for lineno, pat, line in matches[:10]:
            print(f'{lineno}: {pat!r} -> {line}')
        if len(matches) > 10:
            print(f'  ... and {len(matches)-10} more')
        print()