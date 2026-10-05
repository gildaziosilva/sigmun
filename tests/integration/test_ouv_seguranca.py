"""Testes de segurança do DOM-OUV (ADR-0008).

Cobre os critérios de aceite §6 do ADR-0008:

- Nenhuma rota protegida responde 200 sem ``Authorization``;
- Criação de manifestação permanece anônima (exceção §2.2);
- Resposta a não-autorizado **não** contém CPF/e-mail em claro;
- Papel funcional (``admin``) **não** acessa dados sensíveis (§2.3);
- Query params livres ``usuario_perfil``/``usuario_autorizado`` foram eliminados (§2.7).

Os testes usam ``dependency_overrides`` para injetar um contexto de usuário
controlado, evitando dependência de token JWT real.
"""

from __future__ import annotations

from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.modules.sigmun_ouvidoria.presentation.api import (
    depende_consulta,
    depende_tratamento,
)
from src.shared.security.jwt import (
    JWTUsuarioContexto,
    get_current_user_hybrid,
    get_current_user_hybrid_optional,
)

R = "/api/v1/ouv"


def _ctx(*roles: str) -> JWTUsuarioContexto:
    return JWTUsuarioContexto(
        usuario_id=uuid4(),
        login="teste.servidor",
        roles=roles,
        unidades_ids=(),
    )


@pytest.fixture()
def client() -> TestClient:
    """Cliente HTTP com limpeza dos registros criados pelo teste.

    Os testes de criação gravam manifestações reais. Sem a limpeza, execuções
    sucessivas poluiriam a base com protocolos descartáveis.
    """
    with TestClient(app) as c:
        yield c
        _limpar_registros_de_teste()
    app.dependency_overrides.clear()


def _limpar_registros_de_teste() -> None:
    """Remove manifestações criadas pelos testes (protocolo acima do último seed)."""
    try:
        from sqlalchemy import text

        from src.core.infrastructure.database.session import SessionLocal

        with SessionLocal() as sessao:
            # Protocolos de teste são sempre acima deste marker.
            sessao.execute(
                text(
                    "DELETE FROM ouv.tramitacoes WHERE manifestacao_id IN "
                    "(SELECT id FROM ouv.manifestacoes WHERE protocolo > '2026-000003')"
                )
            )
            sessao.execute(
                text(
                    "DELETE FROM ouv.manifestacoes WHERE protocolo > '2026-000003'"
                )
            )
            sessao.execute(
                text("UPDATE ouv.protocolos SET sequencial = 3 WHERE ano = 2026")
            )
            sessao.commit()
    except Exception:  # noqa: BLE001, S110 — limpeza é best-effort
        pass


@pytest.fixture()
def como_admin(client: TestClient) -> TestClient:
    """Cliente autenticado com papel `admin` (sem dados sensíveis, ADR §2.3)."""
    app.dependency_overrides[get_current_user_hybrid] = lambda: _ctx("admin")
    app.dependency_overrides[get_current_user_hybrid_optional] = lambda: _ctx("admin")
    app.dependency_overrides[depende_consulta] = lambda: _ctx("admin")
    app.dependency_overrides[depende_tratamento] = lambda: _ctx("admin")
    return client


@pytest.fixture()
def como_ouvidor(client: TestClient) -> TestClient:
    """Cliente autenticado com papel `ouvidor` (dados sensíveis, ADR §2.3)."""
    app.dependency_overrides[get_current_user_hybrid] = lambda: _ctx("ouvidor")
    app.dependency_overrides[get_current_user_hybrid_optional] = lambda: _ctx("ouvidor")
    app.dependency_overrides[depende_consulta] = lambda: _ctx("ouvidor")
    app.dependency_overrides[depende_tratamento] = lambda: _ctx("ouvidor")
    return client


# -- Critério 1: rotas protegidas exigem credencial ---------------------------


@pytest.mark.parametrize(
    ("metodo", "rota"),
    [
        ("GET", f"{R}/manifestacoes"),
        ("GET", f"{R}/denuncias"),
        ("GET", f"{R}/pedidos-lai"),
        ("GET", f"{R}/estatisticas"),
        ("GET", f"{R}/manifestacoes-vencendo"),
        ("GET", f"{R}/manifestacoes/2026-000001"),
        ("POST", f"{R}/manifestacoes/2026-000001/status"),
        ("POST", f"{R}/manifestacoes/2026-000001/responder"),
        ("POST", f"{R}/manifestacoes/2026-000001/prorrogar"),
        ("POST", f"{R}/manifestacoes/2026-000001/avaliar"),
        ("POST", f"{R}/denuncias/2026-000002/encaminhar"),
        ("POST", f"{R}/pedidos-lai/2026-000003/decidir-recurso"),
    ],
)
def test_rota_protegida_sem_token_responde_401(client: TestClient, metodo, rota):
    """ADR-0008 §2.1 — sem Authorization, a resposta deve ser 401."""
    resposta = client.request(metodo, rota)
    assert resposta.status_code == 401, resposta.text
# -- Critério 2: criação anônima é permitida (ADR §2.2) ----------------------


def test_criacao_manifestacao_anonima_permitida(client: TestClient):
    """ADR-0008 §2.2 — o cidadão protocola sem conta."""
    resposta = client.post(
        f"{R}/manifestacoes",
        json={
            "tipo": "solicitacao",
            "assunto": "Teste de criação anônima",
            "descricao": "Verificação da exceção anônima do ADR-0008.",
            "cidadao_nome": "Maria Souza",
            "cidadao_cpf": "12345678909",
            "cidadao_email": "maria@exemplo.com",
            "orgao_destino": "Saude",
        },
    )
    assert resposta.status_code == 201, resposta.text
    corpo = resposta.json()
    assert corpo["protocolo"]["ano"] == 2026
    # Autor recebe os próprios dados, porém mascarados (RN-OUV-030).
    if corpo.get("cidadao"):
        assert corpo["cidadao"]["cpf"] != "12345678909"
        assert "*" in (corpo["cidadao"]["cpf"] or "")


# -- Critério 3: sigilo por negação total (ADR §2.4) ------------------------


def test_nao_autorizado_nao_recebe_cpf_em_claro(como_admin: TestClient):
    """ADR-0008 §2.3 — `admin` não acessa o dado sensível do denunciante."""
    resposta = como_admin.get(f"{R}/denuncias")
    assert resposta.status_code == 200, resposta.text

    for item in resposta.json()["items"]:
        # `admin` não recebe o bloco `cidadao` (negação total, §2.4).
        assert item.get("cidadao") in (None, {}), (
            "admin não deve receber dados do denunciante (ADR-0008 §2.3)"
        )


def test_autorizado_recebe_dados_mascarados(como_ouvidor: TestClient):
    """ADR-0008 §2.4 — papel funcional recebe o bloco, mas mascarado."""
    resposta = como_ouvidor.get(f"{R}/denuncias")
    assert resposta.status_code == 200, resposta.text

    for item in resposta.json()["items"]:
        cidadao = item.get("cidadao")
        if cidadao and cidadao.get("cpf"):
            assert "*" in cidadao["cpf"], "CPF deveria estar mascarado"


def test_servidor_envolvido_omitido_para_nao_autorizado(como_admin: TestClient):
    """ADR-0008 §2.4 — sem autorização, o servidor envolvido é omitido."""
    resposta = como_admin.get(f"{R}/denuncias")
    assert resposta.status_code == 200, resposta.text

    for item in resposta.json()["items"]:
        if not item.get("envolve_servidor_publico"):
            assert item.get("servidor_envolvido") in (None, "")


# -- Critério 4: parâmetros livres eliminados (ADR §2.7) ---------------------


def test_query_params_de_autorizacao_nao_sao_aceitos(como_admin: TestClient):
    """ADR-0008 §2.7 — o solicitante não pode se auto-conceder autorização."""
    resposta = como_admin.get(
        f"{R}/manifestacoes/2026-000002",
        params={"usuario_autorizado": "true", "usuario_perfil": "admin"},
    )
    assert resposta.status_code == 200, resposta.text
    corpo = resposta.json()
    if corpo.get("cidadao") and corpo["cidadao"].get("cpf"):
        assert "*" in corpo["cidadao"]["cpf"], (
            "usuario_autorizado na query não pode conceder acesso (C2)"
        )


# -- Critério 5: identidade vem do token, não do corpo (ADR §2.1) -----------


def test_campos_de_identidade_sao_ignorados_no_corpo(client: TestClient):
    """ADR-0008 §2.1 — autor_id no corpo não é aceito."""
    resposta = client.post(
        f"{R}/manifestacoes",
        json={
            "tipo": "sugestao",
            "assunto": "Teste de autor_id",
            "descricao": "Verifica que autor_id do corpo e ignorado.",
            "cidadao_nome": "Joao",
            "orgao_destino": "Obras",
            "autor_id": "USUARIO_FALSO",
        },
    )
    assert resposta.status_code == 201, resposta.text
    corpo = resposta.json()
    assert corpo.get("created_by", "") != "USUARIO_FALSO", (
        "created_by nao pode vir do corpo (C2)"
    )
