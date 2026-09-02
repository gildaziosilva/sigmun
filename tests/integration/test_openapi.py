"""Testes de exposição do schema OpenAPI (item 10 do roadmap)."""

from fastapi.testclient import TestClient


def test_openapi_schema_exposto(client: TestClient):
    response = client.get("/openapi.json")

    assert response.status_code == 200
    schema = response.json()
    assert schema["openapi"].startswith("3.")
    assert schema["info"]["title"] == "SIGMUN API"
    assert schema["info"]["version"] == "0.1.0"
    assert schema["info"]["contact"]["email"] == "ti@camacan.ba.gov.br"


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
