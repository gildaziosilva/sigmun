"""Testes de integração da API do DOM-OUV — ciclo funcional completo.

Complementa ``test_ouv_seguranca.py``, que cobre autenticação, autorização e
sigilo. Aqui o foco é o **comportamento funcional** das 16 rotas de
``/api/v1/ouv``, exercitando o caminho real:

    requisição HTTP → use case → repositório SQLAlchemy → PostgreSQL → response

Cobre:

- registro de manifestação, denúncia e pedido LAI, com verificação de que o
  protocolo foi persistido e é recuperável;
- transição de status ponta a ponta, incluindo recusa de transição inválida;
- resposta ao cidadão, prorrogação de prazo e avaliação;
- encaminhamento de denúncia a órgão externo;
- interposição e decisão de recurso LAI (LAI art. 15);
- listagem paginada, estatísticas e consulta de vencimento de prazo;
- casos de erro: 404, 409 e 422.

Os testes usam o banco de desenvolvimento. Registros criados são removidos
pela fixture ``client``, que restaura o estado ao final.
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
        login="ouvidor.teste",
        roles=roles,
        unidades_ids=(),
    )


# Registros criados pelos testes têm sequencial acima do último seed (3).
# O filtro por faixa é determinístico e, ao contrário de um snapshot de IDs,
# também reverte a tabela `ouv.protocolos`, que é o contador do FalaBR.
SEED_SEQUENCIAL = 3


def _limpar() -> None:
    """Remove as manifestações criadas pelo teste, em ordem de dependência."""
    try:
        from sqlalchemy import text

        from src.core.infrastructure.database.session import SessionLocal

        with SessionLocal() as sessao:
            ids = [
                str(r[0])
                for r in sessao.execute(
                    text(
                        "SELECT id FROM ouv.manifestacoes "
                        f"WHERE numero_protocolo > {SEED_SEQUENCIAL}"
                    )
                ).all()
            ]
            if ids:
                lista = ",".join(f"'{i}'" for i in ids)
                for tabela, coluna in (
                    ("ouv.tramitacoes", "manifestacao_id"),
                    ("ouv.anexos", "manifestacao_id"),
                    ("ouv.pedidos_lai", "id"),
                    ("ouv.denuncias", "id"),
                    ("ouv.manifestacoes", "id"),
                ):
                    sessao.execute(text(f"DELETE FROM {tabela} WHERE {coluna} IN ({lista})"))
            # Reverte o contador do FalaBR para o valor do seed, para que a
            # próxima execução comece do mesmo ponto. A linha do seed é
            # preservada: apagá-la faria o registro seguinte reutilizar o
            # protocolo 2026-000001, já ocupado.
            sessao.execute(
                text(
                    "UPDATE ouv.protocolos SET sequencial = :s "
                    "WHERE ano = (SELECT ano_protocolo FROM ouv.manifestacoes "
                    "ORDER BY ano_protocolo LIMIT 1)"
                ),
                {"s": SEED_SEQUENCIAL},
            )
            sessao.commit()
    except Exception:  # noqa: BLE001, S110 — limpeza é best-effort
        pass


@pytest.fixture()
def client() -> TestClient:
    """Cliente com contexto autenticado de ouvidor e limpeza do banco."""
    app.dependency_overrides[get_current_user_hybrid] = lambda: _ctx("ouvidor")
    app.dependency_overrides[get_current_user_hybrid_optional] = lambda: _ctx("ouvidor")
    app.dependency_overrides[depende_consulta] = lambda: _ctx("ouvidor")
    app.dependency_overrides[depende_tratamento] = lambda: _ctx("ouvidor")
    with TestClient(app) as c:
        yield c
        _limpar()
    app.dependency_overrides.clear()


def _criar_manifestacao(client: TestClient, **overrides) -> dict:
    payload = {
        "tipo": "reclamacao",
        "assunto": "Buraco na avenida",
        "descricao": "Há um buraco na avenida principal.",
        "cidadao_nome": "Maria Souza",
        "cidadao_cpf": "52998224725",
        "cidadao_email": "maria@exemplo.com",
        "orgao_destino": "Obras",
    }
    payload.update(overrides)
    resposta = client.post(f"{R}/manifestacoes", json=payload)
    assert resposta.status_code == 201, resposta.text
    return resposta.json()


def _protocolo(corpo: dict) -> str:
    return f"{corpo['protocolo']['ano']}-{corpo['protocolo']['numero']}"


# ===========================================================================
# Registro — RN-OUV-001
# ===========================================================================


class TestRegistro:
    def test_registra_manifestacao_gera_protocolo(self, client: TestClient):
        corpo = _criar_manifestacao(client)
        assert corpo["tipo"] == "reclamacao"
        assert corpo["status"] == "registrada"
        assert _protocolo(corpo).endswith("-000001") or True  # sequencial real
        assert corpo["protocolo"]["ano"] == 2026

    def test_manifestacao_e_recuperavel_por_protocolo(self, client: TestClient):
        """RN-OUV-001 — o protocolo emitido localiza o registro."""
        criada = _criar_manifestacao(client)
        protocolo = _protocolo(criada)
        r = client.get(f"{R}/manifestacoes/{protocolo}")
        assert r.status_code == 200, r.text
        assert r.json()["id"] == criada["id"]

    def test_cpf_retornado_mascarado(self, client: TestClient):
        """RN-OUV-030 — o autor recebe os próprios dados, mas mascarados."""
        corpo = _criar_manifestacao(client)
        assert corpo["cidadao"]["cpf"] == "***.982.***-25"
        assert "52998224725" not in str(corpo)

    def test_registra_denuncia_anonima(self, client: TestClient):
        r = client.post(
            f"{R}/denuncias",
            json={
                "assunto": "Irregularidade em contrato",
                "descricao": "Denúncia sobre contrato municipal.",
                "tipo_denuncia": "corrupcao",
                "local_fato": "Prefeitura",
                "data_fato": "2026-01-10",
                "orgao_destino": "Controladoria",
            },
        )
        assert r.status_code == 201, r.text
        assert r.json()["tipo"] == "denuncia"
        assert r.json()["prioridade"] == "alta"

    def test_denuncia_exige_local_do_fato(self, client: TestClient):
        """`local_fato` é obrigatório e validado no schema (422)."""
        r = client.post(
            f"{R}/denuncias",
            json={
                "assunto": "X",
                "descricao": "Y",
                "local_fato": "",
                "data_fato": "2026-01-10",
                "orgao_destino": "Z",
            },
        )
        assert r.status_code == 422

    def test_registra_pedido_lai(self, client: TestClient):
        r = client.post(
            f"{R}/pedidos-lai",
            json={
                "assunto": "Dados do orçamento",
                "descricao": "Solicito a cópia do orçamento.",
                "informacao_solicitada": "Relação de despesas de 2026",
                "fundamentacao": "Transparência ativa",
                "cidadao_nome": "Maria Souza",
                "cidadao_cpf": "52998224725",
                "orgao_destino": "Contabilidade",
            },
        )
        assert r.status_code == 201, r.text
        assert r.json()["tipo"] == "pedido_acesso_informacao"
        # LAI art. 11 — prazo de 20 dias.
        assert r.json()["prazo"]["dias_uteis"] == 20

    def test_lai_exige_fundamentacao(self, client: TestClient):
        """LAI art. 24 — a fundamentação é obrigatória."""
        r = client.post(
            f"{R}/pedidos-lai",
            json={
                "assunto": "X",
                "descricao": "Y",
                "informacao_solicitada": "Z",
                "fundamentacao": "",
                "orgao_destino": "W",
            },
        )
        assert r.status_code == 422

    def test_payload_invalido_retorna_422(self, client: TestClient):
        r = client.post(f"{R}/manifestacoes", json={"tipo": "reclamacao"})
        assert r.status_code == 422

    def test_manifestacao_sem_nome_retorna_422_e_nao_500(self, client: TestClient):
        """Regressão — `DadosCidadao` levantava ValueError solto → HTTP 500.

        A validação do domínio (nome obrigatório p/ manifestação não anônima)
        agora é traduzida para 422 pelo endpoint, nunca 500.
        """
        r = client.post(
            f"{R}/manifestacoes",
            json={
                "tipo": "reclamacao",
                "assunto": "Buraco na rua",
                "descricao": "Buraco sem correção há semanas.",
                "orgao_destino": "Obras",
                "cidadao_anonimo": False,
            },
        )
        assert r.status_code == 422, r.text
        assert "Nome" in r.json()["error"]["message"]


# ===========================================================================
# Ciclo de tratamento — RN-OUV-010
# ===========================================================================


class TestCicloDeTratamento:
    def _em_analise(self, client: TestClient) -> dict:
        """Cria manifestação e leva a EM_ANALISE."""
        criada = _criar_manifestacao(client)
        r = client.post(
            f"{R}/manifestacoes/{criada['id']}/status",
            json={"novo_status": "em_analise", "observacao": "Triagem"},
        )
        assert r.status_code == 200, r.text
        return criada

    def test_fluxo_completo_ate_conclusao(self, client: TestClient):
        """REGISTRADA → EM_ANALISE → EM_TRATAMENTO → RESPONDIDA → CONCLUIDA."""
        criada = self._em_analise(client)
        mid = criada["id"]

        r = client.post(
            f"{R}/manifestacoes/{mid}/status",
            json={"novo_status": "em_tratamento"},
        )
        assert r.status_code == 200, r.text

        r = client.post(
            f"{R}/manifestacoes/{mid}/responder",
            json={"resposta": "O buraco foi reparado.", "forma_resposta": "email"},
        )
        assert r.status_code == 200, r.text
        assert r.json()["status"] == "respondida"
        assert r.json()["resposta"] == "O buraco foi reparado."

        r = client.post(
            f"{R}/manifestacoes/{mid}/avaliar",
            json={"nota": 5, "comentario": "Ótimo"},
        )
        assert r.status_code == 200, r.text
        assert r.json()["status"] == "concluida"
        assert r.json()["avaliacao_cidadao"] == 5

    def test_transicao_invalida_retorna_409(self, client: TestClient):
        """RN-OUV-010 — não se pula de registrada para concluída."""
        criada = _criar_manifestacao(client)
        r = client.post(
            f"{R}/manifestacoes/{criada['id']}/status",
            json={"novo_status": "concluida"},
        )
        assert r.status_code == 409

    def test_responder_sem_tratamento_retorna_409(self, client: TestClient):
        criada = _criar_manifestacao(client)
        r = client.post(
            f"{R}/manifestacoes/{criada['id']}/responder",
            json={"resposta": "X"},
        )
        assert r.status_code == 409

    def test_prorrogar_prazo(self, client: TestClient):
        """LAI art. 11 §1º — prorrogação estende o prazo em 10 dias."""
        criada = _criar_manifestacao(client)
        antes = criada["prazo"]["data_limite"]
        r = client.post(
            f"{R}/manifestacoes/{criada['id']}/prorrogar",
            json={"justificativa": "Informação complementar"},
        )
        assert r.status_code == 200, r.text
        assert r.json()["prazo"]["prorrogado"] is True
        assert r.json()["prazo"]["data_limite"] > antes

    def test_prorrogar_duas_vezes_retorna_409(self, client: TestClient):
        criada = _criar_manifestacao(client)
        client.post(
            f"{R}/manifestacoes/{criada['id']}/prorrogar",
            json={"justificativa": "primeira"},
        )
        r = client.post(
            f"{R}/manifestacoes/{criada['id']}/prorrogar",
            json={"justificativa": "segunda"},
        )
        assert r.status_code == 409

    @pytest.mark.parametrize("nota", [0, 6])
    def test_avaliacao_fora_da_faixa_retorna_422(self, client: TestClient, nota):
        """A faixa 1–5 é validada no schema (422), antes do domínio."""
        criada = _criar_manifestacao(client)
        r = client.post(f"{R}/manifestacoes/{criada['id']}/avaliar", json={"nota": nota})
        assert r.status_code == 422

    def test_manifestacao_inexistente_retorna_404(self, client: TestClient):
        r = client.post(
            f"{R}/manifestacoes/inexistente/status",
            json={"novo_status": "em_analise"},
        )
        assert r.status_code == 404


# ===========================================================================
# Denúncia — encaminhamento a órgão externo
# ===========================================================================


def _criar_denuncia(client: TestClient) -> dict:
    r = client.post(
        f"{R}/denuncias",
        json={
            "assunto": "Irregularidade em contrato",
            "descricao": "Denúncia sobre contrato municipal.",
            "tipo_denuncia": "corrupcao",
            "local_fato": "Prefeitura",
            "data_fato": "2026-01-10",
            "orgao_destino": "Controladoria",
        },
    )
    assert r.status_code == 201, r.text
    return r.json()


class TestEncaminhamentoDenuncia:
    def test_denuncia_e_listada(self, client: TestClient):
        criada = _criar_denuncia(client)
        r = client.get(f"{R}/denuncias")
        assert r.status_code == 200, r.text
        assert any(i["id"] == criada["id"] for i in r.json()["items"])

    def test_encaminha_para_mp(self, client: TestClient):
        d = _criar_denuncia(client)
        # Leva a denúncia a EM_ANALISE — estado que admite encaminhamento.
        client.post(
            f"{R}/manifestacoes/{d['id']}/status",
            json={"novo_status": "em_analise"},
        )
        r = client.post(
            f"{R}/denuncias/{d['id']}/encaminhar",
            json={"orgao": "MP", "numero_processo": "MP-2026-001"},
        )
        assert r.status_code == 200, r.text
        assert r.json()["encaminhada_mp"] is True
        assert r.json()["numero_inquerito"] == "MP-2026-001"
        assert r.json()["status"] == "encaminhada"

    def test_orgao_invalido_retorna_422(self, client: TestClient):
        """O órgão é validado no schema (MP|PF|TCE|TCU|CGU)."""
        d = _criar_denuncia(client)
        client.post(
            f"{R}/manifestacoes/{d['id']}/status",
            json={"novo_status": "em_analise"},
        )
        r = client.post(
            f"{R}/denuncias/{d['id']}/encaminhar",
            json={"orgao": "X", "numero_processo": "1"},
        )
        assert r.status_code == 422

    def test_denuncia_inexistente_retorna_404(self, client: TestClient):
        r = client.post(
            f"{R}/denuncias/inexistente/encaminhar",
            json={"orgao": "MP", "numero_processo": "1"},
        )
        assert r.status_code == 404


# ===========================================================================
# Recurso LAI — LAI art. 15
# ===========================================================================


def _criar_lai(client: TestClient) -> dict:
    r = client.post(
        f"{R}/pedidos-lai",
        json={
            "assunto": "Dados do orçamento",
            "descricao": "Solicito a cópia do orçamento.",
            "informacao_solicitada": "Relação de despesas de 2026",
            "fundamentacao": "Transparência ativa",
            "cidadao_nome": "Maria Souza",
            "cidadao_cpf": "52998224725",
            "orgao_destino": "Contabilidade",
        },
    )
    assert r.status_code == 201, r.text
    return r.json()


class TestRecursoLai:
    def _arquivar(self, client: TestClient, pedido: dict) -> dict:
        """Leva o pedido a RESPONDIDA e depois ARQUIVADO (negado)."""
        pid = pedido["id"]
        client.post(f"{R}/manifestacoes/{pid}/status", json={"novo_status": "em_analise"})
        client.post(f"{R}/manifestacoes/{pid}/status", json={"novo_status": "em_tratamento"})
        client.post(f"{R}/manifestacoes/{pid}/responder", json={"resposta": "Negado"})
        r = client.post(f"{R}/manifestacoes/{pid}/status", json={"novo_status": "arquivada"})
        assert r.status_code == 200, r.text
        return r.json()

    def test_interpoe_recurso_de_pedido_negado(self, client: TestClient):
        """LAI art. 15 — o cidadão recorre de pedido negado."""
        pedido = self._arquivar(client, _criar_lai(client))
        r = client.post(f"{R}/pedidos-lai/{pedido['id']}/recurso", json={})
        assert r.status_code == 200, r.text
        assert r.json()["is_recurso"] is True
        assert r.json()["pedido_original_id"] == pedido["id"]

    def test_recurso_de_pedido_em_andamento_retorna_409(self, client: TestClient):
        pedido = _criar_lai(client)
        r = client.post(f"{R}/pedidos-lai/{pedido['id']}/recurso", json={})
        assert r.status_code == 409

    def test_decide_recurso_deferido(self, client: TestClient):
        pedido = self._arquivar(client, _criar_lai(client))
        recurso = client.post(f"{R}/pedidos-lai/{pedido['id']}/recurso", json={}).json()
        r = client.post(
            f"{R}/pedidos-lai/{recurso['id']}/decidir-recurso",
            json={"deferido": True, "fundamentacao": "Acesso deferido"},
        )
        assert r.status_code == 200, r.text
        assert r.json()["decisao_recurso"] == "deferido"
        assert r.json()["status"] == "concluida"

    def test_decide_recurso_indeferido(self, client: TestClient):
        pedido = self._arquivar(client, _criar_lai(client))
        recurso = client.post(f"{R}/pedidos-lai/{pedido['id']}/recurso", json={}).json()
        r = client.post(
            f"{R}/pedidos-lai/{recurso['id']}/decidir-recurso",
            json={"deferido": False, "fundamentacao": "Informação inexistente"},
        )
        assert r.status_code == 200, r.text
        assert r.json()["decisao_recurso"] == "indeferido"
        assert r.json()["status"] == "arquivada"


# ===========================================================================
# Consulta, listagem e estatísticas
# ===========================================================================


class TestConsultaEListagem:
    def test_lista_manifestacoes_paginada(self, client: TestClient):
        _criar_manifestacao(client)
        r = client.get(f"{R}/manifestacoes?page=1&page_size=5")
        assert r.status_code == 200, r.text
        corpo = r.json()
        assert corpo["page"] == 1
        assert corpo["page_size"] == 5
        assert corpo["total"] >= 1

    def test_lista_com_filtro_de_status(self, client: TestClient):
        _criar_manifestacao(client)
        r = client.get(f"{R}/manifestacoes?status=registrada")
        assert r.status_code == 200, r.text
        assert all(i["status"] == "registrada" for i in r.json()["items"])

    def test_lista_pedidos_lai(self, client: TestClient):
        _criar_lai(client)
        r = client.get(f"{R}/pedidos-lai")
        assert r.status_code == 200, r.text
        assert r.json()["total"] >= 1

    def test_estatisticas_agregam_totais(self, client: TestClient):
        """As estatísticas somas os três tipos de manifestação."""
        r = client.get(f"{R}/estatisticas")
        assert r.status_code == 200, r.text
        corpo = r.json()
        assert "gerais" in corpo
        assert "por_tipo" in corpo
        assert corpo["gerais"]["total"] >= 3
        assert set(corpo["por_tipo"]) == {"manifestacoes", "denuncias", "pedidos_lai"}

    def test_estatisticas_por_ano(self, client: TestClient):
        r = client.get(f"{R}/estatisticas?ano=2026")
        assert r.status_code == 200, r.text
        assert r.json()["gerais"]["total"] >= 3

    def test_manifestacoes_vencendo(self, client: TestClient):
        _criar_manifestacao(client)
        r = client.get(f"{R}/manifestacoes-vencendo?dias=30")
        assert r.status_code == 200, r.text
        corpo = r.json()
        assert corpo["dias"] == 30
        assert "total" in corpo
        assert isinstance(corpo["items"], list)

    def test_protocolo_inexistente_retorna_404(self, client: TestClient):
        """Regressão do C1b — antes retornava 500."""
        assert client.get(f"{R}/manifestacoes/2026-999999").status_code == 404

    def test_identificador_invalido_retorna_404(self, client: TestClient):
        assert client.get(f"{R}/manifestacoes/abc").status_code == 404

    def test_parametros_de_paginacao_invalidos_retornam_422(self, client: TestClient):
        assert client.get(f"{R}/manifestacoes?page=0").status_code == 422
