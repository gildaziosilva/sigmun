"""Varredura de rotas PUBLICAS (sem nenhuma dependencia de auth) — T-2.3.

Compara as rotas sem auth com o inventario do ADR-0010. Sai com codigo 1
se houver qualquer divergencia (ADR x codigo).

Uso: .venv/bin/python scripts/verificar_rotas_publicas.py
"""
from __future__ import annotations

import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AUTH_TOKENS = (
    "UsuarioObrigatorio",
    "UsuarioOpcional",
    "exigir_papeis",
    "require_roles_hybrid",
    "get_current_user",
    "JWTUsuarioContexto",
    "depende_",
)
METODOS = {"get", "post", "put", "patch", "delete", "head", "options"}

# Contrato do ADR-0010-endpoints-publicos.md (inventario exato).
ESPERADAS: set[str] = {
    # DOM-COM — transparencia passiva / portal fornecedor (LAI)
    "GET /api/v1/contratos",
    "GET /api/v1/contratos/{contrato_id}",
    "GET /api/v1/compras",
    "GET /api/v1/compras/{compra_id}",
    "GET /api/v1/processos-documentais",
    "GET /api/v1/processos-documentais/{processo_id}",
    "GET /api/v1/compras/{compra_id}/itens",
    "GET /api/v1/itens-compras/{item_id}",
    "GET /api/v1/fornecedores",
    "GET /api/v1/fornecedores/{fornecedor_id}",
    # DOM-CAD — estrutura organizacional (dado publico)
    "GET /api/v1/cadastro/unidades-administrativas",
    # DOM-IDN — endpoints de autenticao (por necessidade)
    "POST /api/v1/idn/auth/login",
    "POST /api/v1/idn/auth/login/jwt",
    "POST /api/v1/idn/auth/refresh",
    "POST /api/v1/idn/auth/logout",
    "POST /api/v1/idn/auth/logout/jwt",
    # Infra
    "GET /health",
    "GET /",
}

PREFIXOS: dict[str, str] = {}


def _prefixo_router(tree: ast.Module) -> str:
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(t, ast.Name) and t.id == "router" for t in node.targets):
            continue
        if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
            if node.value.func.id == "APIRouter":
                for kw in node.value.keywords:
                    if kw.arg == "prefix" and isinstance(kw.value, ast.Constant):
                        return str(kw.value.value)
    return ""


def _caminho_decorator(dec: ast.expr) -> tuple[str, str] | None:
    alvo = dec.func if isinstance(dec, ast.Call) else dec
    if not (isinstance(alvo, ast.Attribute) and alvo.attr in METODOS):
        return None
    caminho = ""
    if isinstance(dec, ast.Call) and dec.args and isinstance(dec.args[0], ast.Constant):
        caminho = str(dec.args[0].value)
    return alvo.attr.upper(), caminho


def varre() -> set[str]:
    acha: set[str] = set()
    alvos = sorted(ROOT.glob("src/modules/*/presentation/**/*.py")) + [ROOT / "src/main.py"]
    for path in alvos:
        if not path.exists():
            continue
        texto = path.read_text(encoding="utf-8")
        tree = ast.parse(texto)
        prefixo = _prefixo_router(tree) if path.name != "main.py" else ""
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            tem_auth = any(t in ast.dump(node) for t in AUTH_TOKENS)
            if tem_auth:
                continue
            for dec in node.decorator_list:
                mc = _caminho_decorator(dec)
                if mc:
                    metodo, caminho = mc
                    full = (prefixo + caminho) or "/"
                    if not full.startswith("/"):
                        full = "/" + full
                    acha.add(f"{metodo} {full}")
    return acha


def main() -> int:
    atuais = varre()
    faltando = ESPERADAS - atuais  # no ADR mas sumiram do codigo
    a_mais = atuais - ESPERADAS  # rotas novas sem decisao no ADR
    if faltando:
        print("DIVERGENCIA — no ADR mas sem correspondencia no codigo:")
        for x in sorted(faltando):
            print(f"  - {x}")
    if a_mais:
        print("DIVERGENCIA — rotas publicas SEM decisao registrada no ADR-0010:")
        for x in sorted(a_mais):
            print(f"  + {x}")
    if faltando or a_mais:
        print(f"esperado={len(ESPERADAS)} atual={len(atuais)}")
        return 1
    print(f"OK — {len(atuais)} rotas publicas batem exatamente com o ADR-0010.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
