"""Atualiza o inventario documental do item 13 do Plano de Trabalho."""

import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT / "SIGMUN-Docs"
PLAN_FILE = DOCS_ROOT / "Plano-de-Trabalho.md"


def first_value(text: str, pattern: str, default: str) -> str:
    match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip() if match else default


def document_number(name: str) -> str:
    match = re.match(r"^(\d{3,})[-_]", name)
    return match.group(1) if match else "—"


def document_status(text: str) -> str:
    status = first_value(text, r"\*\*Status:\*\*\s*(.+)", "A validar")
    normalized = status.casefold()
    if "vigente" in normalized or "conclu" in normalized:
        return "✅"
    if "elabora" in normalized or "não iniciado" in normalized or "nao iniciado" in normalized:
        return "⚪"
    return "🟡"


def document_version(text: str) -> str:
    return first_value(text, r"\*\*Vers[^:]*:\*\*\s*([^\r\n]+)", "A informar")


def dependencies(text: str) -> str:
    marker = re.search(r"Documento\(s\) Relacionado\(s\):\s*(.*?)(?:\r?\n\s*---|\r?\n\s*#)", text, re.IGNORECASE | re.DOTALL)
    if not marker:
        return "Não declaradas"

    entries = re.findall(r"^\s*[-*]\s+(.+?)\s*$", marker.group(1), re.MULTILINE)
    if not entries:
        return "Não declaradas"
    visible = entries[:3]
    suffix = f" (+{len(entries) - 3})" if len(entries) > 3 else ""
    return "; ".join(visible) + suffix


def display_name(path: Path) -> str:
    name = path.stem.replace("|", "\\|")
    return name.replace("\r", " ").replace("\n", " ")


def display_directory(path: Path) -> str:
    relative_parent = path.parent.relative_to(DOCS_ROOT).as_posix()
    return relative_parent if relative_parent != "." else "Raiz"


def build_table() -> str:
    rows = [
        "| Nº | Documento | Diretório | Status | Versão | Dependências |",
        "|----|-----------|-----------|--------|---------|--------------|",
    ]
    files = sorted(DOCS_ROOT.rglob("*.md"), key=lambda path: path.relative_to(DOCS_ROOT).as_posix().casefold())
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        rows.append(
            f"| {document_number(path.name)} | {display_name(path)} | {display_directory(path)} | "
            f"{document_status(text)} | {document_version(text)} | {dependencies(text)} |"
        )
    return "\n".join(rows)


def update_plan() -> int:
    content = PLAN_FILE.read_text(encoding="utf-8")
    start_marker = "# 13. Controle Detalhado dos Documentos"
    end_marker = "# 14. Controle de Entregáveis"
    start = content.index(start_marker)
    end = content.index(end_marker, start)
    replacement = (
        f"{start_marker}\n\n"
        "Esta seção registra todos os documentos Markdown existentes em `SIGMUN-Docs`, "
        "com status e versão extraídos dos metadados disponíveis.\n\n"
        f"{build_table()}\n\n"
        "> **Observação:** documentos sem metadado explícito são marcados como `A validar` "
        "ou `Não declaradas`; a tabela deve ser regenerada após a criação ou revisão de documentos.\n\n"
        "---\n\n"
    )
    PLAN_FILE.write_text(content[:start] + replacement + content[end:], encoding="utf-8", newline="\n")
    return len(list(DOCS_ROOT.rglob("*.md")))


if __name__ == "__main__":
    print(f"Documentos refletidos: {update_plan()}")