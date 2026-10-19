"""Testes unitários dos repositórios SQLAlchemy de Diárias (DOM-DIA).

Cobertura alvo: >= 80% para sqlalchemy_diaria_repository.py (atual: 24.6%)
                   sqlalchemy_prestacao_repository.py (atual: 28.3%)
"""
from datetime import date, datetime
from uuid import uuid4

import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import SessionLocal
from src.modules.sigmun_dia.domain.entities import (
    CategoriaDiaria,
    Diaria,
    PrestacaoContas,
    StatusDiaria,
)
from src.modules.sigmun_dia.infrastructure.database.models import (
    DiariaModel,
    PrestacaoContasModel,
)
from src.modules.sigmun_dia.infrastructure.repositories import (
    SQLAlchemyDiariaRepository,
    SQLAlchemyPrestacaoContasRepository,
)


@pytest.fixture
def db_session():
    """Sessao de banco real para testes (commit ao final)."""
    db = SessionLocal()
    try:
        db.execute(text("TRUNCATE TABLE dia.diarias, dia.prestacoes_contas CASCADE"))
        db.commit()
        yield db
    finally:
        db.execute(text("TRUNCATE TABLE dia.diarias, dia.prestacoes_contas CASCADE"))
        db.commit()
        db.close()


@pytest.fixture
def repo_diaria(db_session: Session):
    return SQLAlchemyDiariaRepository(db_session)


@pytest.fixture
def repo_prestacao(db_session: Session):
    return SQLAlchemyPrestacaoContasRepository(db_session)


def _make_diaria(
    **kwargs,
) -> Diaria:
    defaults = {
        "id": str(uuid4()),
        "viagem_id": "viagem-1",
        "servidor_id": "servidor-1",
        "dota_id": "dota-1",
        "categoria": CategoriaDiaria.EVENTO,
        "descricao": "Diaria de teste",
        "data_inicio": date(2024, 1, 15),
        "data_fim": date(2024, 1, 20),
        "valor_diaria": 150.0,
        "valor_total": 300.0,
        "status": StatusDiaria.SOLICITADA,
        "data_solicitacao": datetime(2024, 1, 10),
    }
    defaults.update(kwargs)
    return Diaria(**defaults)


def _make_prestacao(
    **kwargs,
) -> PrestacaoContas:
    defaults = {
        "id": str(uuid4()),
        "diaria_id": "diaria-1",
        "servidor_id": "servidor-1",
        "dota_id": "dota-1",
        "status": "aberta",
        "data_emissao": date(2024, 1, 10),
        "data_vencimento": date(2024, 2, 10),
        "documento_id": "doc-1",
        "valor_previsto": 300.0,
        "valor_apresentado": 300.0,
        "valor_glosado": 0.0,
        "valor_liquido": 300.0,
    }
    defaults.update(kwargs)
    return PrestacaoContas(**defaults)


class TestSQLAlchemyDiariaRepository:
    """Testes para SQLAlchemyDiariaRepository."""

    def test_save_cria_nova_diaria(self, repo_diaria):
        diaria = _make_diaria()
        salva = repo_diaria.save(diaria)
        assert salva.id == diaria.id
        assert salva.viagem_id == diaria.viagem_id

    def test_save_atualiza_diaria_existente(self, repo_diaria):
        diaria = _make_diaria(status=StatusDiaria.SOLICITADA)
        repo_diaria.save(diaria)

        diaria.status = StatusDiaria.AUTORIZADA
        diaria.valor_total = 500.0
        atualizada = repo_diaria.save(diaria)

        assert atualizada.status == StatusDiaria.AUTORIZADA
        assert atualizada.valor_total == 500.0

        from src.modules.sigmun_dia.infrastructure.database.models import DiariaModel
        from uuid import UUID, uuid4
        modelo = repo_diaria._session.get(DiariaModel, UUID(diaria.id))
        assert modelo is not None
        assert modelo.status == StatusDiaria.AUTORIZADA.value
        assert float(modelo.valor_total) == 500.0

    def test_get_by_id_existente(self, repo_diaria):
        diaria = _make_diaria()
        repo_diaria.save(diaria)

        encontrada = repo_diaria.get_by_id(diaria.id)
        assert encontrada is not None
        assert encontrada.id == diaria.id
        assert encontrada.viagem_id == diaria.viagem_id

    def test_get_by_id_inexistente(self, repo_diaria):
        from uuid import uuid4
        encontrada = repo_diaria.get_by_id(str(uuid4()))
        assert encontrada is None

    def test_get_by_id_deletado_nao_retorna(self, repo_diaria):
        diaria = _make_diaria()
        repo_diaria.save(diaria)
        repo_diaria.delete(diaria.id)

        encontrada = repo_diaria.get_by_id(diaria.id)
        assert encontrada is None

    def test_get_by_viagem(self, repo_diaria):
        viagem_id = "viagem-456"
        d1 = _make_diaria(viagem_id=viagem_id)
        d2 = _make_diaria(viagem_id=viagem_id)
        d3 = _make_diaria(viagem_id="outra-viagem")

        repo_diaria.save(d1)
        repo_diaria.save(d2)
        repo_diaria.save(d3)

        resultado = repo_diaria.get_by_viagem(viagem_id)
        assert len(resultado) == 2
        assert all(d.viagem_id == viagem_id for d in resultado)

    def test_find_by_servidor(self, repo_diaria):
        servidor_id = "servidor-789"
        d1 = _make_diaria(servidor_id=servidor_id)
        d2 = _make_diaria(servidor_id=servidor_id)
        d3 = _make_diaria(servidor_id="outro-servidor")

        repo_diaria.save(d1)
        repo_diaria.save(d2)
        repo_diaria.save(d3)

        resultado = repo_diaria.find_by_servidor(servidor_id)
        assert len(resultado) == 2
        assert all(d.servidor_id == servidor_id for d in resultado)

    def test_find_by_dota(self, repo_diaria):
        dota_id = "dota-999"
        d1 = _make_diaria(dota_id=dota_id)
        d2 = _make_diaria(dota_id=dota_id)

        repo_diaria.save(d1)
        repo_diaria.save(d2)

        resultado = repo_diaria.find_by_dota(dota_id)
        assert len(resultado) == 2
        assert all(d.dota_id == dota_id for d in resultado)

    def test_find_by_status(self, repo_diaria):
        from src.modules.sigmun_dia.domain.entities import StatusDiaria
        d1 = _make_diaria(status=StatusDiaria.SOLICITADA)
        d2 = _make_diaria(status=StatusDiaria.SOLICITADA)
        d3 = _make_diaria(status=StatusDiaria.AUTORIZADA)

        repo_diaria.save(d1)
        repo_diaria.save(d2)
        repo_diaria.save(d3)

        resultado = repo_diaria.find_by_status(StatusDiaria.SOLICITADA.value)
        assert len(resultado) == 2
        assert all(d.status == StatusDiaria.SOLICITADA for d in resultado)

    def test_find_ativas(self, repo_diaria):
        from src.modules.sigmun_dia.domain.entities import StatusDiaria
        d1 = _make_diaria(status=StatusDiaria.SOLICITADA)
        d2 = _make_diaria(status=StatusDiaria.AUTORIZADA)
        d3 = _make_diaria(status=StatusDiaria.CANCELADA)

        repo_diaria.save(d1)
        repo_diaria.save(d2)
        repo_diaria.save(d3)

        repo_diaria.delete(d3.id)

        ativas = repo_diaria.find_ativas()
        assert len(ativas) == 2
        assert all(d.is_active for d in ativas)

    def test_delete_marca_como_deletado(self, repo_diaria):
        from src.modules.sigmun_dia.infrastructure.database.models import DiariaModel
        from uuid import UUID, uuid4

        diaria = _make_diaria()
        repo_diaria.save(diaria)

        repo_diaria.delete(diaria.id)

        modelo = repo_diaria._session.get(DiariaModel, UUID(diaria.id))
        assert modelo is not None
        assert modelo.is_deleted is True

    def test_delete_inexistente_nao_erro(self, repo_diaria):
        from uuid import uuid4
        repo_diaria.delete(str(uuid4()))



class TestSQLAlchemyPrestacaoContasRepository:
    """Testes para SQLAlchemyPrestacaoContasRepository."""

    def test_save_cria_nova_prestacao(self, repo_prestacao):
        prestacao = _make_prestacao()
        salva = repo_prestacao.save(prestacao)
        assert salva.id == prestacao.id
        assert salva.diaria_id == prestacao.diaria_id

    def test_save_atualiza_prestacao_existente(self, repo_prestacao):
        prestacao = _make_prestacao(status="aberta")
        repo_prestacao.save(prestacao)

        prestacao.status = "aprovada"
        prestacao.valor_glosado = 50.0
        prestacao.valor_liquido = 250.0
        atualizada = repo_prestacao.save(prestacao)

        assert atualizada.status == "aprovada"
        assert atualizada.valor_glosado == 50.0

    def test_get_by_id_existente(self, repo_prestacao):
        prestacao = _make_prestacao()
        repo_prestacao.save(prestacao)

        encontrada = repo_prestacao.get_by_id(prestacao.id)
        assert encontrada is not None
        assert encontrada.id == prestacao.id

    def test_get_by_id_inexistente(self, repo_prestacao):
        from uuid import uuid4
        encontrada = repo_prestacao.get_by_id(str(uuid4()))
        assert encontrada is None

    def test_get_by_diaria(self, repo_prestacao):
        diaria_id = "diaria-xyz"
        p1 = _make_prestacao(diaria_id=diaria_id)
        p2 = _make_prestacao(diaria_id="outra-diaria")

        repo_prestacao.save(p1)
        repo_prestacao.save(p2)

        encontrada = repo_prestacao.get_by_diaria(diaria_id)
        assert encontrada is not None
        assert encontrada.id == p1.id

    def test_get_by_diaria_inexistente(self, repo_prestacao):
        encontrada = repo_prestacao.get_by_diaria("diaria-inexistente")
        assert encontrada is None

    def test_find_authors(self, repo_prestacao):
        p1 = _make_prestacao(status="aberta")
        p2 = _make_prestacao(status="aberta")
        p3 = _make_prestacao(status="aprovada")

        repo_prestacao.save(p1)
        repo_prestacao.save(p2)
        repo_prestacao.save(p3)

        abertas = repo_prestacao.find_authors()
        assert len(abertas) == 2
        assert all(p.status == "aberta" for p in abertas)

    def test_delete_marca_como_deletado(self, repo_prestacao):
        from src.modules.sigmun_dia.infrastructure.database.models import PrestacaoContasModel
        from uuid import UUID, uuid4

        prestacao = _make_prestacao()
        repo_prestacao.save(prestacao)

        repo_prestacao.delete(prestacao.id)

        modelo = repo_prestacao._session.get(PrestacaoContasModel, UUID(prestacao.id))
        assert modelo is not None
        assert modelo.is_deleted is True

    def test_delete_inexistente_nao_erro(self, repo_prestacao):
        from uuid import uuid4
        repo_prestacao.delete(str(uuid4()))



class TestConversaoEntidadeModelo:
    """Testes de conversao entre entidade e modelo (caminho _to_entity)."""

    def test_diaria_to_entity_todos_campos(self, repo_diaria, db_session):
        diaria = _make_diaria(
            id="00000000-0000-0000-0000-000000000001",
            motivo_cancelamento="motivo teste",
            motivo_glosa="glosa teste",
            valor_glosado=50.0,
            documento_prestacao_id="doc-123",
        )
        repo_diaria.save(diaria)

        recuperada = repo_diaria.get_by_id("00000000-0000-0000-0000-000000000001")
        assert recuperada is not None
        assert recuperada.id == "00000000-0000-0000-0000-000000000001"
        assert recuperada.motivo_cancelamento == "motivo teste"
        assert recuperada.motivo_glosa == "glosa teste"
        assert recuperada.valor_glosado == 50.0
        assert recuperada.documento_prestacao_id == "doc-123"

    def test_prestacao_to_entity_todos_campos(self, repo_prestacao, db_session):
        prestacao = _make_prestacao(
            id="00000000-0000-0000-0000-000000000002",
            motivo_glosa="glosa",
            valor_glosado=75.0,
        )
        repo_prestacao.save(prestacao)

        recuperada = repo_prestacao.get_by_id("00000000-0000-0000-0000-000000000002")
        assert recuperada is not None
        assert recuperada.motivo_glosa == "glosa"
        assert recuperada.valor_glosado == 75.0


class TestCasosDeBorda:
    """Testes de casos de borda e validacoes."""

    def test_save_diaria_com_datas_none(self, repo_diaria):
        diaria = _make_diaria(
            data_autorizacao=None,
            data_calculo=None,
            data_concessao=None,
        )
        salva = repo_diaria.save(diaria)
        assert salva.data_autorizacao is None

    def test_save_diaria_valores_zero(self, repo_diaria):
        diaria = _make_diaria(valor_diaria=0.0, valor_total=0.0)
        salva = repo_diaria.save(diaria)
        assert salva.valor_diaria == 0.0
        assert salva.valor_total == 0.0

    def test_prestacao_valores_glosa(self, repo_prestacao):
        prestacao = _make_prestacao(
            valor_apresentado=1000.0,
            valor_glosado=200.0,
            valor_liquido=800.0,
        )
        salva = repo_prestacao.save(prestacao)
        assert salva.valor_glosado == 200.0
        assert salva.valor_liquido == 800.0


