"""Inventario de endpoints x auth nos modulos onda 2a/2b."""
import re
import pathlib

mods = ['orc', 'tributos', 'con', 'patrimonio', 'frotas', 'met', 'dad',
        'cadastro_imobiliario', 'rh']
# decorador pode ocupar varias linhas; casa @X.METODO( ... ) seguido de def
pat = re.compile(
    r'@(\w+)\.(get|post|put|patch|delete)\((.*?)\)\s*\n\s*def\s+(\w+)\((.*?)\)\s*(?:->.*?)?:',
    re.DOTALL,
)
auth_pat = re.compile(r'UsuarioObrigatorio|UsuarioOpcional|exigir_papeis|JWTUsuarioContexto')

for m in mods:
    print(f"===== sigmun_{m} =====")
    base = pathlib.Path(f"src/modules/sigmun_{m}/presentation")
    for f in sorted(base.rglob("*.py")):
        text = f.read_text(encoding='utf-8')
        for mm in pat.finditer(text):
            router_var, method, deco_args, func, sig = mm.groups()
            has_auth = bool(auth_pat.search(sig))
            path = (deco_args.split(',')[0].strip() or '?')[:55]
            print(f"  {f.relative_to(base)} :: {method.upper():6} {path:55} {func} auth={'SIM' if has_auth else 'NAO'}")
    print()
