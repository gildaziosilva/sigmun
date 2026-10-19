"""RBAC por domínio — TODO2 T-2.4.

Para cada um dos 24 módulos com rotas, percorre o trio papel x operação:

- (a) sem token -> 401;
- (b) papel errado -> 403;
- (c) papel correto -> acesso autorizado (nunca 401/403).

Nota sobre (c): a rota representativa é chamada com corpo vazio. Quando a
autorização passa, o handler responde 2xx (quando o corpo é aceito), 404 (id
inexistente) ou 422 (corpo inválido) — todos códigos **pós-autorização**. O
que este teste garante é que o papel correto nunca é bloqueado (401/403) e
que a resposta é um sucesso da camada HTTP (< 500). O detalhe "2xx com payload
válido" é coberto pelos testes funcionais de cada módulo.

Exceções registradas em SIGMUN-Docs/00-Governanca/ADR/ADR-0010 (rotas
públicas) e ADR-0008 (denúncia anônima por LAI) ficam fora desta varredura:
a rota representativa de cada módulo é sempre uma rota de escrita com papel.
"""

from __future__ import annotations

from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.shared.security.jwt import JWTUsuarioContexto, get_current_user_jwt

UUID_ZERO = "00000000-0000-0000-0000-000000000000"

# (modulo, metodo, caminho, papel_correto) — um caso por módulo com rotas.
CASOS: list[tuple[str, str, str, str]] = [
    ("seg", "POST", "/api/v1/seg/chaves", "admin"),
    ("cadastro", "POST", "/api/v1/cadastro/pessoas", "admin"),
    ("cadastro_imobiliario", "POST", "/api/v1/imo/avaliacoes", "admin"),
    ("rh", "POST", "/api/v1/pes/cargos", "admin"),
    ("saude", "POST", "/api/v1/sau/agendamentos", "admin"),
    ("orc", "POST", "/api/v1/orc/dotacoes", "admin"),
    ("tributos", "POST", "/api/v1/tri/contribuintes", "admin"),
    ("con", "POST", "/api/v1/con/contas", "admin"),
    ("patrimonio", "POST", "/api/v1/pat/bens", "admin"),
    ("frotas", "POST", "/api/v1/fro/veiculos", "admin"),
    ("met", "POST", "/api/v1/met/classificacoes", "admin"),
    ("dad", "POST", "/api/v1/dad/ativos", "admin"),
    ("gdo", "POST", "/api/v1/gdo/documentos", "admin"),
    ("int", "POST", "/api/v1/int/apis", "admin"),
    ("geoinformacao", "POST", "/api/v1/geo/camadas", "admin"),
    ("territorial", "POST", "/api/v1/tel/bairros", "admin"),
    ("educacao", "POST", "/api/v1/edu/alunos", "admin"),
    ("assistencia_social", "POST", "/api/v1/ass/atendimentos", "admin"),
    ("ate", "POST", "/api/v1/ate/atendimentos/iniciar", "admin"),
    ("obras", "POST", "/api/v1/obr/despesas", "admin"),
    ("dia", "POST", "/api/v1/dia/diarias", "admin"),
    ("idn", "POST", "/api/v1/idn/usuarios", "admin"),
    ("compras", "POST", "/api/v1/compras", "admin"),
    # DOM-OUV: depende_tratamento aceita apenas ouvidor/corregedor (ADR-0008).
    (
        "ouvidoria",
        "POST",
        "/api/v1/ouv/manifestacoes/{manifestacao_id}/responder",
        "ouvidor",
    ),
]

PAPEL_ERRADO = "estagiario_sem_papel"


def _ctx(*roles: str) -> JWTUsuarioContexto:
    return JWTUsuarioContexto(
        usuario_id=uuid4(),
        login="teste.rbac",
        roles=roles,
        unidades_ids=(),
    )


def _rota_real(caminho: str) -> str:
    """Substitui parâmetros de caminho por um UUID neutro."""
    while "{" in caminho:
        inicio = caminho.index("{")
        fim = caminho.index("}") + 1
        caminho = caminho[:inicio] + UUID_ZERO + caminho[fim:]
    return caminho


@pytest.fixture()
def client() -> TestClient:
    app.dependency_overrides.clear()
    with TestClient(app, raise_server_exceptions=False) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.mark.parametrize(
    ("modulo", "metodo", "caminho", "papel_correto"),
    CASOS,
    ids=[caso[0] for caso in CASOS],
)
def test_rbac_sem_token_retorna_401(
    client: TestClient, modulo: str, metodo: str, caminho: str, papel_correto: str
):
    """(a) requisição sem token é rejeitada com 401."""
    del modulo, papel_correto
    rota = _rota_real(caminho)
    resposta = client.request(metodo, rota, json={})
    assert resposta.status_code == 401, f"{metodo} {rota}: {resposta.status_code}"


@pytest.mark.parametrize(
    ("modulo", "metodo", "caminho", "papel_correto"),
    CASOS,
    ids=[caso[0] for caso in CASOS],
)
def test_rbac_papel_errado_retorna_403(
    client: TestClient, modulo: str, metodo: str, caminho: str, papel_correto: str
):
    """(b) autenticado com papel errado recebe 403."""
    del papel_correto
    rota = _rota_real(caminho)
    app.dependency_overrides[get_current_user_jwt] = lambda: _ctx(PAPEL_ERRADO)
    resposta = client.request(metodo, rota, json={})
    assert resposta.status_code == 403, f"{metodo} {rota}: {resposta.status_code}"


@pytest.mark.parametrize(
    ("modulo", "metodo", "caminho", "papel_correto"),
    CASOS,
    ids=[caso[0] for caso in CASOS],
)
def test_rbac_papel_correto_e_autorizado(
    client: TestClient, modulo: str, metodo: str, caminho: str, papel_correto: str
):
    """(c) papel correto passa pela autorização (nunca 401/403; < 500)."""
    del modulo
    rota = _rota_real(caminho)
    app.dependency_overrides[get_current_user_jwt] = lambda: _ctx(papel_correto)
    resposta = client.request(metodo, rota, json={})
    assert resposta.status_code not in (401, 403), (
        f"{metodo} {rota} com papel '{papel_correto}': {resposta.status_code}"
    )
    assert resposta.status_code < 500, (
        f"{metodo} {rota} com papel '{papel_correto}' gerou 500: {resposta.text}"
    )
