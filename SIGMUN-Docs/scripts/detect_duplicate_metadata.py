from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]

def count_stanzas(text):
    blocks = [block.strip() for block in text.split('---') if block.strip()]
    return len(blocks), blocks

for path in sorted(root.rglob('*.md')):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8', errors='ignore')
    blocks = [b.strip() for b in text.split('---')]
    # metadata blocks often include Projeto and Status and Documentos
    metadata_blocks = [b for b in blocks if 'Projeto:' in b and 'Status:' in b]
    if len(metadata_blocks) > 1:
        print(path.relative_to(root), 'metadata blocks', len(metadata_blocks))
        for i, b in enumerate(metadata_blocks, 1):
            print('--- block', i)
            print(b[:240].replace('\n', ' '))
        print()