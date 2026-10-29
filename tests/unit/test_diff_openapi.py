"""Testes de regressão para scripts/diff_openapi.py."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "diff_openapi.py"


def _documento(required: list[str] | None = None) -> dict[str, Any]:
    """Cria um OpenAPI mínimo com uma propriedade opcional por padrão."""
    schema: dict[str, Any] = {
        "type": "object",
        "properties": {
            "idade": {"type": "integer"},
        },
    }

    if required is not None:
        schema["required"] = required

    return {
        "openapi": "3.0.3",
        "info": {
            "title": "API de teste",
            "version": "1.0.0",
        },
        "paths": {},
        "components": {
            "schemas": {
                "Exemplo": schema,
            },
        },
    }


def _salvar_json(path: Path, document: dict[str, Any]) -> None:
    path.write_text(
        json.dumps(document, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _executar(base: Path, head: Path) -> subprocess.CompletedProcess[str]:
    """Executa a CLI real sem alterar os snapshots do repositório."""
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--base",
            str(base),
            "--head",
            str(head),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


@pytest.fixture
def snapshots(tmp_path: Path) -> tuple[Path, Path]:
    """Prepara dois snapshots temporários equivalentes."""
    base = tmp_path / "base.json"
    head = tmp_path / "head.json"

    documento = _documento()
    _salvar_json(base, documento)
    _salvar_json(head, documento)

    return base, head


def test_head_inexistente_retorna_codigo_2_sem_traceback(
    snapshots: tuple[Path, Path],
    tmp_path: Path,
) -> None:
    base, _ = snapshots
    head_inexistente = tmp_path / "inexistente.json"

    resultado = _executar(base, head_inexistente)

    assert resultado.returncode == 2
    assert "head" in resultado.stderr.lower()
    assert "Traceback" not in resultado.stderr


def test_base_inexistente_retorna_codigo_2_sem_traceback(
    snapshots: tuple[Path, Path],
    tmp_path: Path,
) -> None:
    _, head = snapshots
    base_inexistente = tmp_path / "inexistente.json"

    resultado = _executar(base_inexistente, head)

    assert resultado.returncode == 2
    assert "base" in resultado.stderr.lower()
    assert "Traceback" not in resultado.stderr


def test_adicionar_campo_a_required_e_breaking(
    snapshots: tuple[Path, Path],
) -> None:
    base, head = snapshots

    _salvar_json(base, _documento())
    _salvar_json(head, _documento(required=["idade"]))

    resultado = _executar(base, head)

    assert resultado.returncode == 1
    assert "required adicionado" in resultado.stdout.lower()
    assert "idade" in resultado.stdout


def test_remover_campo_de_required_nao_e_breaking(
    snapshots: tuple[Path, Path],
) -> None:
    base, head = snapshots

    _salvar_json(base, _documento(required=["idade"]))
    _salvar_json(head, _documento())

    resultado = _executar(base, head)

    assert resultado.returncode == 0
    assert "required removido" in resultado.stdout.lower()
    assert "✅ sem breaking changes" in resultado.stdout.lower()


def test_snapshots_equivalentes_retorna_codigo_zero(
    snapshots: tuple[Path, Path],
) -> None:
    base, head = snapshots

    resultado = _executar(base, head)

    assert resultado.returncode == 0
    assert "Traceback" not in resultado.stderr
