from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
corrupt_patterns = [
    'Ã¡', 'Ã©', 'Ã­', 'Ã³', 'Ãº', 'Ã£', 'Ãµ', 'Ã§', 'Ã±',
    'Ã', 'â€™', 'â€œ', 'â€�', 'â€“', 'â€”', 'Â', '�', '\?\?'
]

results = {}
for path in sorted(root.rglob('*.md')):
    if '.git' in path.parts:
        continue
    try:
        text = path.read_text(encoding='utf-8', errors='ignore')
    except UnicodeDecodeError:
        continue
    for pat in corrupt_patterns:
        if re.search(re.escape(pat), text):
            results.setdefault(pat, []).append(str(path.relative_to(root)))

for pat, paths in sorted(results.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"{pat}: {len(paths)}")
    for p in paths[:20]:
        print(f"  {p}")
    print()