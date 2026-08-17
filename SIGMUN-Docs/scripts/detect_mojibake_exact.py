from pathlib import Path
root = Path(__file__).resolve().parents[1]
patterns = [
    'Ã¡', 'Ã©', 'Ã­', 'Ã³', 'Ãº', 'Ã£', 'Ãµ', 'Ã§', 'Ã±',
    'Ã€', 'Ã‚', 'Ãƒ', 'Ã„', 'Ã…', 'Ã‡', 'Ãˆ', 'Ã‰', 'Ã‹', 'ÃŒ',
    'ÃŽ', 'Ã‘', 'Ã’', 'Ã“', 'Ã”', 'Ã•', 'Ã–', 'Ã™', 'Ãš', 'Ã›',
    'Ãœ', 'ÃŸ', 'Â©', 'Â®', 'Â«', 'Â»', 'â€™', 'â€œ', 'â€�', 'â€“', 'â€”', 'â€¢', 'Â'
]
found = []
for path in sorted(root.rglob('*.md')):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8', errors='ignore')
    for pat in patterns:
        if pat in text:
            found.append((path.relative_to(root), pat))
            break
print('matches', len(found))
for path, pat in found[:100]:
    print(path, pat)