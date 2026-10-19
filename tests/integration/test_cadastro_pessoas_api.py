"""Testes de regressão das rotas de pessoas do DOM-CUM.

Regressão coberta:

- C17 — `SqlAlchemyPessoaRepository` não implementava o método abstrato
  `listar_desatualizadas` (declarado em ``PessoaRepository``). Como a classe
  permanecia abstrata, **toda** rota que dependesse dela — inclusive
  ``GET /api/v1/cadastro/pessoas`` — respondia HTTP 500.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.shared.security.jwt import (
    JWTUsuarioContexto,
    get_current_user_hybrid,
    get_current_user_hybrid_optional,
)

R = "/api/v1/cadastro/pessoas"


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
    with TestClient(app, raise_server_exceptions=False) as c:
        yield c
    app.dependency_overrides.clear()


class TestListarPessoas:
    def test_listagem_responde_200(self, client: TestClient):
        """C17 — a rota deve responder, não estourar na injeção do repositório."""
        r = client.get(f"{R}?page=1&page_size=50")
        assert r.status_code == 200, r.text
        corpo = r.json()
        assert "total" in corpo
        assert "items" in corpo

    def test_listagem_respeita_page_size(self, client: TestClient):
        r = client.get(f"{R}?page=1&page_size=1")
        assert r.status_code == 200, r.text
        corpo = r.json()
        assert len(corpo["items"]) <= 1

    def test_listagem_pagina_2_nao_reparte_a_1(self, client: TestClient):
        """A paginação é base-1: a página 2 não pode repetir a página 1."""
        p1 = client.get(f"{R}?page=1&page_size=1").json()["items"]
        p2 = client.get(f"{R}?page=2&page_size=1").json()["items"]
        if p1 and p2:
            assert p1[0]["id"] != p2[0]["id"]

    def test_consulta_por_id_responde_200(self, client: TestClient):
        """Consultar pessoa do seed também depende do repositório."""
        itens = client.get(f"{R}?page=1&page_size=1").json()["items"]
        if not itens:
            pytest.skip("sem pessoas no seed")
        r = client.get(f"{R}/{itens[0]['id']}")
        assert r.status_code == 200, r.text

    @pytest.mark.parametrize("query", ["page=0", "page_size=0", "page_size=500"])
    def test_parametros_invalidos_respondem_422(self, client: TestClient, query: str):
        r = client.get(f"{R}?{query}")
        assert r.status_code == 422, r.text


class TestListarDesatualizadas:
    """Contrato do método que faltava (ADR-0007)."""

    @pytest.fixture()
    def repo(self):
        from src.core.infrastructure.database.session import SessionLocal
        from src.modules.sigmun_cadastro.infrastructure.repositories import (
            SqlAlchemyPessoaRepository,
        )

        with SessionLocal() as sessao:
            yield SqlAlchemyPessoaRepository(sessao)

    def test_repositorio_e_instanciavel(self, repo):
        """A classe não pode manter métodos abstratos por implementar."""
        assert type(repo).__abstractmethods__ == frozenset()

    def test_retorna_lista_de_uuid(self, repo):
        resultado = repo.listar_desatualizadas(datetime.now(timezone.utc) - timedelta(days=365))
        assert isinstance(resultado, list)
        assert all(isinstance(p, UUID) for p in resultado)

    def test_respeita_limite(self, repo):
        resultado = repo.listar_desatualizadas(
            datetime.now(timezone.utc) - timedelta(days=365), limite=1
        )
        assert len(resultado) <= 1

    def test_corte_no_futuro_traz_todas_as_vivas(self, repo):
        """Semântica de `updated_at < corte`: um corte futuro marca todas.

        A pessoa só é considerada desatualizada se `updated_at` for **anterior**
        ao corte, então um corte no futuro inclui todo mundo vivo.
        """
        assert repo.listar_desatualizadas(datetime.now(timezone.utc) + timedelta(days=1)) != []

    def test_corte_anterior_ao_cadastro_nao_traz_nada(self, repo):
        """Nada é anterior a uma data que precede o próprio cadastro."""
        assert repo.listar_desatualizadas(datetime(2000, 1, 1, tzinfo=timezone.utc)) == []

    def test_use_case_revisao_consome_o_metodo(self, repo):
        """O use case de revisão (ADR-0007) funciona com o repositório real."""
        from src.modules.sigmun_cadastro.application.use_cases.revisar_cadastral import (
            RevisarCadastralUseCase,
        )

        relatorio = RevisarCadastralUseCase(repo).execute(limite_meses=12)
        assert "total" in relatorio
        assert relatorio["total"] == len(relatorio["pessoas_desatualizadas"])
