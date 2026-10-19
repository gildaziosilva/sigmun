"""Aplica auth T-2.2 (ondas 2a/2b/2c) nos routers sem protecao.

Regra: GET/HEAD/OPTIONS -> UsuarioOpcional;
POST/PUT/PATCH/DELETE -> exigir_papeis. Idempotente.
Uso: .venv/bin/python scripts/aplicar_auth_onda2.py [--check] [--modules orc]
"""
from __future__ import annotations
import argparse
import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ALVOS: dict[str, tuple[str, list[str]]] = {
    "cadastro_imobiliario": ("cadastro", [
        "src/modules/sigmun_cadastro_imobiliario/presentation/api/endpoints_imoveis.py",
        "src/modules/sigmun_cadastro_imobiliario/presentation/api/endpoints_avaliacoes.py",
    ]),
    "rh": ("rh", [
        "src/modules/sigmun_rh/presentation/api/cargos_endpoints.py",
        "src/modules/sigmun_rh/presentation/api/folha_endpoints.py",
        "src/modules/sigmun_rh/presentation/api/ferias_freq_endpoints.py",
        "src/modules/sigmun_rh/presentation/api/lotacoes_endpoints.py",
    ]),
    "orc": ("orcamento", [
        "src/modules/sigmun_orc/presentation/api/dotacao_endpoints.py",
        "src/modules/sigmun_orc/presentation/api/planejamento_endpoints.py",
    ]),
    "tributos": ("tributos", [
        "src/modules/sigmun_tributos/presentation/api/contribuintes_imoveis_endpoints.py",
        "src/modules/sigmun_tributos/presentation/api/divida_certidao_endpoints.py",
        "src/modules/sigmun_tributos/presentation/api/lancamentos_endpoints.py",
    ]),
    "con": ("contabilidade", [
        "src/modules/sigmun_con/presentation/api/contabil_endpoints.py",
        "src/modules/sigmun_con/presentation/api/execucao_endpoints.py",
    ]),
    "patrimonio": ("patrimonio", [
        "src/modules/sigmun_patrimonio/presentation/api/endpoints.py",
    ]),
    "frotas": ("frotas", [
        "src/modules/sigmun_frotas/presentation/api/endpoints.py",
    ]),
    "met": ("metas", ["src/modules/sigmun_met/presentation/api/__init__.py"]),
    "dad": ("dados", ["src/modules/sigmun_dad/presentation/api/__init__.py"]),
    "gdo": ("gdo", ["src/modules/sigmun_gdo/presentation/api/__init__.py"]),
    "int": ("integracao", ["src/modules/sigmun_int/presentation/api/__init__.py"]),
    "geoinformacao": ("geo", [
        "src/modules/sigmun_geoinformacao/presentation/api/endpoints_camada.py",
        "src/modules/sigmun_geoinformacao/presentation/api/endpoints_servico.py",
    ]),
    "territorial": ("territorial", [
        "src/modules/sigmun_territorial/presentation/api/endpoints_geo.py",
        "src/modules/sigmun_territorial/presentation/api/endpoints_planta.py",
        "src/modules/sigmun_territorial/presentation/api/endpoints_territoriais.py",
    ]),
    "educacao": ("educacao", ["src/modules/sigmun_educacao/presentation/api/endpoints.py"]),
    "assistencia_social": ("assistencia", [
        "src/modules/sigmun_assistencia_social/presentation/api/endpoints.py",
    ]),
    "ate": ("atendimento", ["src/modules/sigmun_ate/presentation/api/__init__.py"]),
    "obras": ("obras", [
        "src/modules/sigmun_obras/presentation/api/endpoints_acompanhamento.py",
        "src/modules/sigmun_obras/presentation/api/endpoints_obra.py",
    ]),
    "dia": ("dia", ["src/modules/sigmun_dia/presentation/api/__init__.py"]),
}

AUTH_TOKENS = ("UsuarioObrigatorio", "UsuarioOpcional", "exigir_papeis",
               "require_roles_hybrid", "get_current_user", "JWTUsuarioContexto")
LEITURA = {"get", "head", "options"}
IMPORT_AUTH = (
    "from src.shared.presentation.dependencies import (\n"
    "    JWTUsuarioContexto,\n"
    "    UsuarioOpcional,\n"
    "    exigir_papeis,\n"
    ")\n"
)


def metodo_do_decorator(dec: ast.expr) -> str | None:
    func = dec.func if isinstance(dec, ast.Call) else None
    if not isinstance(func, ast.Attribute):
        return None
    if isinstance(func.value, ast.Name) and func.value.id == "router":
        if func.attr in ("get", "post", "put", "patch", "delete", "head", "options"):
            return func.attr
    return None


def tem_auth(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    src = ast.dump(fn)
    return any(t in src for t in AUTH_TOKENS)


def arg_para(metodo: str, papel: str) -> str:
    if metodo in LEITURA:
        return "usuario: UsuarioOpcional,"
    if metodo == "delete":
        return (f'usuario: Annotated[JWTUsuarioContexto, Depends('
                f'exigir_papeis("admin", "{papel}"))],')
    return (f'usuario: Annotated[JWTUsuarioContexto, Depends('
            f'exigir_papeis("gestor", "admin", "{papel}"))],')


def garante_annotated(texto: str) -> str:
    linhas = texto.splitlines(keepends=True)
    for i, ln in enumerate(linhas):
        s = ln.strip()
        if s.startswith("from typing import") and "Annotated" not in s:
            linhas[i] = ln.replace("from typing import", "from typing import Annotated,")
            linhas[i] = linhas[i].replace("Annotated, Annotated,", "Annotated,")
            break
    return "".join(linhas)


def processa(path: Path, papel: str, check: bool) -> int:
    texto = path.read_text(encoding="utf-8")
    tree = ast.parse(texto)
    alvos: list[tuple[ast.FunctionDef | ast.AsyncFunctionDef, str]] = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        mets = [m for d in node.decorator_list if (m := metodo_do_decorator(d))]
        if not mets or tem_auth(node):
            continue
        alvos.append((node, mets[0]))
    if check or not alvos:
        return len(alvos)
    novas = texto.splitlines(keepends=True)
    for fn, metodo in sorted(alvos, key=lambda t: t[0].lineno, reverse=True):
        arg = arg_para(metodo, papel)
        # Insere `usuario` como PRIMEIRO parametro: sempre valido
        # (nao-default antes de defaults e' permitido; apos `(` nao ha restricao).
        ldef = fn.lineno - 1
        linha_def = novas[ldef]
        abre = linha_def.index("(")
        pre = linha_def[: abre + 1]
        resto = linha_def[abre + 1 :]
        base = len(linha_def) - len(linha_def.lstrip())
        indent = " " * (base + 4)
        if resto.strip() == "" or resto.strip() == "\\":
            # assinatura multilinha: `def f(` sozinho na linha
            novas[ldef] = pre + f"\n{indent}{arg}\n"
        else:
            # `def f(repo, ...):` ou `def f():` — explode em multilinha
            corpo = resto.lstrip()
            if corpo.startswith("):"):
                tail = corpo[1:]  # "):..."
                novas[ldef] = f"{pre}\n{indent}{arg}\n{' ' * base}){tail}"
                if novas[ldef].endswith("\n") is False:
                    novas[ldef] += "\n"
            else:
                # tem parametros na mesma linha: quebra apos `(`
                novas[ldef] = f"{pre}\n{indent}{arg}\n{indent}{corpo}"
                if novas[ldef].endswith("\n") is False:
                    novas[ldef] += "\n"
    out = "".join(novas)
    t2 = ast.parse(out)
    tem = any(isinstance(n, ast.ImportFrom) and n.module == "src.shared.presentation.dependencies"
              for n in ast.walk(t2))
    if not tem:
        idx = 0
        for i, n in enumerate(t2.body):
            if isinstance(n, (ast.Import, ast.ImportFrom)):
                idx = i + 1
        fim = t2.body[idx - 1].end_lineno if idx else 0
        l2 = out.splitlines(keepends=True)
        l2.insert(fim, IMPORT_AUTH)
        out = "".join(l2)
    out = garante_annotated(out)
    ast.parse(out)
    path.write_text(out, encoding="utf-8")
    return len(alvos)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--modules", default="")
    args = ap.parse_args()
    filtro = {m.strip() for m in args.modules.split(",") if m.strip()}
    total = 0
    for mod, (papel, arqs) in ALVOS.items():
        if filtro and mod not in filtro:
            continue
        for rel in arqs:
            p = ROOT / rel
            if not p.exists():
                print(f"AVISO: {rel} nao existe")
                continue
            n = processa(p, papel, args.check)
            total += n
            print(f"{'[check] ' if args.check else ''}{rel}: {n} rotas")
    print(f"TOTAL: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

