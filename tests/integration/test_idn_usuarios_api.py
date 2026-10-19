"""Testes de regressão das rotas de usuário do DOM-IDN.

Regressões cobertas:

- C14 — `GET /usuarios/{id}` chamava `BuscarUsuarioUseCase.execute()`, método
  inexistente. A rota respondia HTTP 500 para **qualquer** usuário, inclusive
  os que existiam no banco.
- C15 — os repositórios faziam `UUID(usuario_id)` sem guarda; um identificador
  malformado (`/usuarios/abc`) levantava `ValueError` e virava HTTP 500.
"""

from __future__ import annotations

from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.shared.security.jwt import (
    JWTUsuarioContexto,
    get_current_user_hybrid,
    get_current_user_hybrid_optional,
    get_current_user_jwt,
)

R = "/api/v1/idn/usuarios"


@pytest.fixture()
def client() -> TestClient:
    ctx = JWTUsuarioContexto(
        usuario_id=uuid4(),
        login="admin",
        roles=("admin",),
        unidades_ids=(),
    )
    app.dependency_overrides[get_current_user_hybrid] = lambda: ctx
    app.dependency_overrides[get_current_user_hybrid_optional] = lambda: ctx
    # T-2.3: rotas /usuarios agora exigem papel `admin` via exigir_papeis.
    app.dependency_overrides[get_current_user_jwt] = lambda: ctx
    with TestClient(app, raise_server_exceptions=False) as c:
        yield c
    app.dependency_overrides.clear()


class TestBuscarUsuario:
    def test_usuario_existente_responde_200(self, client: TestClient):
        """C14 — a rota precisa devolver os dados do usuário, não 500."""
        lista = client.get(R).json()
        assert lista["total"] > 0, "esperava ao menos um usuário no seed"

        usuario_id = lista["items"][0]["id"]
        r = client.get(f"{R}/{usuario_id}")
        assert r.status_code == 200, r.text
        assert r.json()["id"] == usuario_id
        assert r.json()["login"]

    def test_usuario_inexistente_responde_404(self, client: TestClient):
        inexistente = str(uuid4())
        r = client.get(f"{R}/{inexistente}")
        assert r.status_code == 404, r.text
        assert inexistente in r.json()["error"]["message"]

    @pytest.mark.parametrize("malformado", ["abc", "123", "not-a-uuid", "00000000-0000"])
    def test_identificador_malformado_responde_404(self, client: TestClient, malformado: str):
        """C15 — identificador inválido é "não encontrado", nunca 500."""
        r = client.get(f"{R}/{malformado}")
        assert r.status_code == 404, r.text

    def test_listagem_continua_funcional(self, client: TestClient):
        """A correção não pode quebrar a listagem."""
        r = client.get(R)
        assert r.status_code == 200, r.text
        assert "items" in r.json()


class TestCicloDeVidaUsuario:
    @pytest.mark.parametrize("acao", ["ativar", "desativar", "bloquear"])
    def test_acao_com_id_malformado_responde_404(self, client: TestClient, acao: str):
        """C15 — o mesmo vale para as rotas de ciclo de vida."""
        r = client.post(f"{R}/abc/{acao}")
        assert r.status_code == 404, r.text

    @pytest.mark.parametrize("acao", ["ativar", "desativar", "bloquear"])
    def test_acao_com_id_inexistente_responde_404(self, client: TestClient, acao: str):
        r = client.post(f"{R}/{uuid4()}/{acao}")
        assert r.status_code == 404, r.text
