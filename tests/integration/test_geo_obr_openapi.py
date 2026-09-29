"""Testes de exposicao dos dominios DOM-GEO e DOM-OBR no schema OpenAPI.

Validam que os routers dos dois dominios estao registrados na aplicacao e que
os principais caminhos publicos aparecem no contrato da API.
"""

from fastapi.testclient import TestClient

CAMINHOS_GEO = (
    "/api/v1/geo/camadas",
    "/api/v1/geo/mapas",
    "/api/v1/geo/mapas/{mapa_id}/composicao",
    "/api/v1/geo/mapas/{mapa_id}/publicar",
    "/api/v1/geo/mapas/{mapa_id}/arquivar",
    "/api/v1/geo/features",
    "/api/v1/geo/servicos",
)

CAMINHOS_OBR = (
    "/api/v1/obr/obras",
    "/api/v1/obr/obras/{obra_id}/acompanhamento",
    "/api/v1/obr/obras/{obra_id}/medicoes",
    "/api/v1/obr/obras/{obra_id}/despesas",
    "/api/v1/obr/obras/{obra_id}/etapas",
    "/api/v1/obr/obras/{obra_id}/vistorias",
    "/api/v1/obr/medicoes",
    "/api/v1/obr/despesas",
)


def test_openapi_expoe_o_dominio_geo(client: TestClient) -> None:
    paths = client.get("/openapi.json").json()["paths"]
    for caminho in CAMINHOS_GEO:
        assert caminho in paths, f"caminho {caminho} ausente no OpenAPI do DOM-GEO"


def test_openapi_expoe_o_dominio_obr(client: TestClient) -> None:
    paths = client.get("/openapi.json").json()["paths"]
    for caminho in CAMINHOS_OBR:
        assert caminho in paths, f"caminho {caminho} ausente no OpenAPI do DOM-OBR"


def test_openapi_define_tags_dos_dominios(client: TestClient) -> None:
    schema = client.get("/openapi.json").json()
    tags = {t["name"] for t in schema["tags"]}
    assert "Geoinformação Municipal" in tags
    assert "Obras e Infraestrutura" in tags


def test_operacoes_de_ciclo_de_vida_publicadas(client: TestClient) -> None:
    """RN-GEO-004/RN-GEO-006 e RN-OBR-002: transições são operações de POST."""
    paths = client.get("/openapi.json").json()["paths"]

    for caminho in (
        "/api/v1/geo/camadas/{camada_id}/ativar",
        "/api/v1/geo/camadas/{camada_id}/desativar",
        "/api/v1/geo/mapas/{mapa_id}/publicar",
        "/api/v1/geo/mapas/{mapa_id}/arquivar",
        "/api/v1/geo/servicos/{servico_id}/inativar",
    ):
        assert "post" in paths[caminho], f"{caminho} deveria expor POST"

    for caminho in (
        "/api/v1/obr/obras/{obra_id}/iniciar-execucao",
        "/api/v1/obr/obras/{obra_id}/suspender",
        "/api/v1/obr/obras/{obra_id}/concluir",
        "/api/v1/obr/obras/{obra_id}/cancelar",
        "/api/v1/obr/medicoes/{medicao_id}/aprovar",
        "/api/v1/obr/medicoes/{medicao_id}/glosar",
    ):
        assert "post" in paths[caminho], f"{caminho} deveria expor POST"
