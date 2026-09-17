"""Regressão da identidade corporativa de Compras (ADR-0006)."""

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "SIGMUN-Docs"


def test_openapi_identifica_compras_com_codigo_corporativo(app_instance):
    """A identidade exposta não deve ser derivada da pasta do piloto."""
    description = app_instance.openapi()["info"]["description"]
    assert "(DOM-COM)" in description
    assert "DOM-COMPRAS-001" not in description


def test_documentacao_corporativa_usa_identidade_canonica():
    """Referências correntes devem identificar Compras como DOM-COM."""
    paths = (
        DOCS / "01-Arquitetura-Corporativa"
        / "030-Roadmap-de-Implementacao-dos-Dominios.md",
        DOCS / "02-Modelo-de-Negocio"
        / "Mapa-de-Dominios.md",
        DOCS / "DOM-COMPRAS-001"
        / "000-Dominio-Gestao-de-Compras-e-Contratacoes.md",
        DOCS / "DOM-COMPRAS-001"
        / "001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md",
        DOCS / "DOM-COMPRAS-001"
        / "002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md",
        DOCS / "DOM-COMPRAS-001"
        / "003-Mapa-de-Processos-Gestao-de-Compras-e-Contratacoes.md",
        DOCS / "DOM-COMPRAS-001"
        / "004-Mapa-de-Servicos-Gestao-de-Compras-e-Contratacoes.md",
        DOCS / "DOM-COMPRAS-001"
        / "012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md",
    )

    for path in paths:
        text = path.read_text(encoding="utf-8")
        assert "DOM-COM" in text, str(path)


def test_scripts_preservam_localizacao_fisica_das_evidencias():
    """Inspeciona caminhos sem importar scripts de deploy ou monitoramento."""
    for name in ("deploy_controlled_env.py", "operations_monitor.py"):
        tree = ast.parse(
            (ROOT / "scripts" / name).read_text(encoding="utf-8")
        )
        assignments = [
            node
            for node in tree.body
            if isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name)
                and target.id == "EVIDENCE_DIR"
                for target in node.targets
            )
        ]
        assert len(assignments) == 1

        values = [
            node.value
            for node in ast.walk(assignments[0].value)
            if isinstance(node, ast.Constant)
        ]

        assert "DOM-COMPRAS-001" in values
        assert "DOM-COM" not in values

    assert (DOCS / "DOM-COMPRAS-001/evidencias").is_dir()


def test_referencias_correntes_do_codigo_nao_usam_identidade_historica():
    """Código-fonte corrente não deve usar a identidade histórica."""
    for path in (ROOT / "src").rglob("*.py"):
        assert "DOM-COMPRAS" not in path.read_text(encoding="utf-8"), str(path)
