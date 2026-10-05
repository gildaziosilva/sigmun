"""Testes de exposição do schema OpenAPI (item 10 do roadmap)."""

import ast
import pathlib

import pytest
from fastapi.testclient import TestClient


def test_openapi_schema_exposto(client: TestClient):
    response = client.get("/openapi.json")

    assert response.status_code == 200
    schema = response.json()
    assert schema["openapi"].startswith("3.")
    assert schema["info"]["title"] == "SIGMUN API"
    assert schema["info"]["version"] == "0.1.0"
    assert schema["info"]["contact"]["email"] == "ti@camacan.ba.gov.br"


def test_dependencias_de_fastapi_existem_no_modulo() -> None:
    """Nenhuma `Depends(x)` pode referenciar identificador inexistente.

    Com `from __future__ import annotations`, a anotação vira string e o
    FastAPI a resolve em tempo de geração do schema. Se `x` não existir no
    módulo, a resolução falha com `PydanticUserError: ... is not fully
    defined` — e isso derruba o **OpenAPI inteiro**, expondo todos os domínios
    a uma falha de módulo alheio.
    """
    raiz = pathlib.Path(__file__).resolve().parents[2] / "src"
    indefinidas: list[str] = []

    for arquivo in raiz.rglob("*.py"):
        try:
            arvore = ast.parse(arquivo.read_text(encoding="utf-8"))
        except SyntaxError:  # pragma: no cover
            continue

        definidos: set[str] = set()
        for no in ast.walk(arvore):
            if isinstance(no, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                definidos.add(no.name)
            elif isinstance(no, ast.Assign):
                definidos.update(t.id for t in no.targets if isinstance(t, ast.Name))
            elif isinstance(no, (ast.Import, ast.ImportFrom)):
                definidos.update(
                    (a.asname or a.name).split(".")[0] for a in no.names
                )

        for no in ast.walk(arvore):
            if isinstance(no, ast.Call) and getattr(no.func, "id", None) == "Depends":
                for arg in no.args:
                    if isinstance(arg, ast.Name) and arg.id not in definidos:
                        indefinidas.append(f"{arquivo.name}:{no.lineno} Depends({arg.id})")

    assert not indefinidas, "dependências inexistentes: " + ", ".join(indefinidas)


@pytest.mark.parametrize(
    "dominio",
    ["/api/v1/ate/atendimentos", "/api/v1/cadastro/pessoas", "/api/v1/ouv/manifestacoes"],
)
def test_openapi_expoe_dominio_independente_dos_outros(
    client: TestClient, dominio: str
) -> None:
    """Um defeito em qualquer módulo não pode esconder os demais domínios."""
    schema = client.get("/openapi.json").json()
    assert dominio in schema["paths"], f"{dominio} ausente no OpenAPI"


def test_openapi_contem_endpoints_do_dominio_compras(client: TestClient) -> None:
    schema = client.get("/openapi.json").json()
    paths = schema["paths"]

    for path in (
        "/api/v1/fornecedores",
        "/api/v1/compras",
        "/api/v1/processos-documentais",
        "/api/v1/contratos",
        "/api/v1/contratos/formalizar",
    ):
        assert path in paths, f"caminho {path} ausente no OpenAPI"


def test_openapi_define_tags_do_dominio(client: TestClient) -> None:
    schema = client.get("/openapi.json").json()
    tags = {t["name"] for t in schema["tags"]}

    assert "Compras - Fornecedores" in tags
    assert "Compras - Itens" in tags
    assert "Compras - Processos" in tags
    assert "Compras - Contratos" in tags
    assert "Compras - Processos Documentais" in tags


def test_docs_redoc_disponiveis(client: TestClient) -> None:
    assert client.get("/docs").status_code == 200
    assert client.get("/redoc").status_code == 200
