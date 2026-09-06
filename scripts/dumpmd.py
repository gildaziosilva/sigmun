import sys, io
from pathlib import Path
p = Path(r'c:\ProjetosPython\sigmun-v1\sigmun-v1\SIGMUN-Docs\04-Modelo-de-Dados\Modelo-Conceitual.md')
d = p.read_bytes()
print('LEN', len(d))
print(repr(d))
