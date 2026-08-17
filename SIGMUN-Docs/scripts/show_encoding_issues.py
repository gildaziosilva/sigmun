from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
patterns = ['Ã', 'Â', '�']
for path in sorted(root.rglob('*.md')):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8', errors='ignore')
    found = False
    for i, line in enumerate(text.splitlines(), start=1):
        if any(pat in line for pat in patterns):
            if not found:
                print(path.relative_to(root))
                found = True
            print(f'{i}: {line}')
    if found:
        print()