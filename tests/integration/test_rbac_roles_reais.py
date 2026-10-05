"""Regressão do RBAC entre o código da role no banco e as rotas (C18).

Diagnóstico: o token carregava o **UUID** da role em vez do **código**, e
mesmo com o código correto havia divergência de convenção — o banco grava
``ROLE_OUVIDOR`` e as rotas declaram ``ouvidor``. O efeito era HTTP 403 em
toda rota protegida do DOM-OUV, para qualquer usuário legítimo.

Estes testes usam token real emitido pelo DOM-IDN (`create_token_pair`), sem
`dependency_overrides`, para exercitar o caminho de produção.
"""

from __future__ import annotations

import base64
import json
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.shared.security.jwt import (
    JWTUsuarioContexto,
    _normaliza_papel,
    create_token_pair,
)

R = "/api/v1/ouv"


def _token(*roles: str) -> str:
    return create_token_pair(
        usuario_id=uuid4(), login="t", roles=list(roles), unidades_ids=[]
    ).access_token


def _claims(token: str) -> dict:
    payload = token.split(".")[1]
    payload += "=" * (-len(payload) % 4)
    return json.loads(base64.urlsafe_b64decode(payload))


def _bearer(*roles: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {_token(*roles)}"}


@pytest.fixture()
def client() -> TestClient:
    with TestClient(app, raise_server_exceptions=False) as c:
        yield c


class TestNormalizacaoDePapeis:
    @pytest.mark.parametrize(
        ("entrada", "esperado"),
        [
            ("ROLE_OUVIDOR", "OUVIDOR"),
            ("ouvidor", "OUVIDOR"),
            ("Ouvidor", "OUVIDOR"),
            ("  ROLE_ADMIN  ", "ADMIN"),
            ("", ""),
        ],
    )
    def test_reduz_a_forma_canonica(self, entrada: str, esperado: str):
        assert _normaliza_papel(entrada) == esperado

    def test_casa_codigo_do_banco_com_papel_da_rota(self):
        """A divergência de convenção não pode mais bloquear o acesso."""
        ctx = JWTUsuarioContexto(
            usuario_id=uuid4(), login="t", roles=("ROLE_OUVIDOR",), unidades_ids=()
        )
        assert ctx.possui_algum_papel("ouvidor") is True

    def test_papel_ausente_continua_negado(self):
        ctx = JWTUsuarioContexto(
            usuario_id=uuid4(),
            login="t",
            roles=("ROLE_DEMO_COMPRAS_OPERADOR",),
            unidades_ids=(),
        )
        assert ctx.possui_algum_papel("ouvidor", "corregedor") is False


class TestTokenCarregaCodigoDaRole:
    def test_token_real_tem_codigo_e_nao_uuid(self, client: TestClient):
        """C18 — o claim `roles` deve trazer o código, não o UUID da role."""
        resposta = client.post(
            "/api/v1/idn/auth/login/jwt",
            json={"login": "demo.ouvidoria.ouvidor", "senha": "Ouvidoria2026"},
        )
        if resposta.status_code != 200:
            pytest.skip("usuário demonstrativo de ouvidoria ausente no banco")

        roles = _claims(resposta.json()["access_token"])["roles"]
        assert roles, "o token precisa carregar ao menos um papel"
        for papel in roles:
            assert not _parece_uuid(papel), f"token carrega UUID, não código: {papel}"
        assert any(_normaliza_papel(p) == "OUVIDOR" for p in roles)


def _parece_uuid(valor: str) -> bool:
    """Detecta o formato de UUID (8-4-4-4-12 em hex)."""
    partes = valor.split("-")
    if len(partes) != 5:
        return False
    return all(
        p and all(c in "0123456789abcdefABCDEF" for c in p) for p in partes
    )


class TestRbacNasRotasOuv:
    @pytest.mark.parametrize(
        "papel",
        ["ROLE_OUVIDOR", "ouvidor", "ROLE_CORREGEDOR", "ROLE_AUDITOR", "ROLE_ADMIN"],
    )
    def test_papeis_de_consulta_acessam(self, client: TestClient, papel: str):
        r = client.get(f"{R}/estatisticas", headers=_bearer(papel))
        assert r.status_code == 200, r.text

    @pytest.mark.parametrize(
        "papel", ["ROLE_DEMO_COMPRAS_OPERADOR", "ROLE_DEMO_COMPRAS_GESTOR", "ROLE_X"]
    )
    def test_papeis_sem_permissao_recebem_403(self, client: TestClient, papel: str):
        """A correção não pode transformar anormalize em brecha de segurança."""
        r = client.get(f"{R}/estatisticas", headers=_bearer(papel))
        assert r.status_code == 403, r.text

    def test_sem_token_recebe_401(self, client: TestClient):
        assert client.get(f"{R}/estatisticas").status_code == 401

    def test_ouvidor_acessa_as_quatro_listas(self, client: TestClient):
        """C18 — as chamadas agrupadas do frontend OUV devem responder 200."""
        cabecalho = _bearer("ROLE_OUVIDOR")
        for url in (
            f"{R}/manifestacoes?page=1&page_size=100",
            f"{R}/denuncias?page=1&page_size=100",
            f"{R}/pedidos-lai?page=1&page_size=100",
            f"{R}/estatisticas",
        ):
            r = client.get(url, headers=cabecalho)
            assert r.status_code == 200, f"{url} -> {r.status_code} {r.text}"
