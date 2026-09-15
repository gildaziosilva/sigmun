"""Testes de integração do seed de dados iniciais do DOM-GDO.

Validam a população do plano de classificação e das tabelas de
temporalidade, a integridade da hierarquia e a idempotência da
execução repetida.
"""

import pytest
from sqlalchemy import select, text

from src.core.infrastructure.database.session import SessionLocal
from src.modules.sigmun_gdo.infrastructure.database.models import (
    ClassificacaoDocumentalModel,
    TabelaTemporalidadeModel,
)
from src.modules.sigmun_gdo.infrastructure.database.seeds import (
    PLANO_CLASSIFICACAO_INICIAL,
    TABELAS_TEMPORALIDADE_INICIAIS,
    executar_seed_gdo,
)

TABELAS_GDO_SEED = (
    "gdo.documentos",
    "gdo.tabelas_temporalidades",
    "gdo.classificacoes_documentais",
    "gdo.processos_documentos",
)


@pytest.fixture(autouse=True)
def _limpar_tabelas_seed():
    """Isolamento: limpa as tabelas afetadas pelo seed antes/depois."""
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_GDO_SEED)} CASCADE"))
        session.commit()
    yield
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_GDO_SEED)} CASCADE"))
        session.commit()


def test_seed_popula_plano_classificacao_e_temporalidades():
    with SessionLocal() as session:
        resultado = executar_seed_gdo(session)

        total_classificacoes = len(session.scalars(select(ClassificacaoDocumentalModel)).all())
        total_temporalidades = len(session.scalars(select(TabelaTemporalidadeModel)).all())

    assert resultado["classificacoes_criadas"] == len(PLANO_CLASSIFICACAO_INICIAL)
    assert resultado["temporalidades_criadas"] == len(TABELAS_TEMPORALIDADE_INICIAIS)
    assert total_classificacoes == len(PLANO_CLASSIFICACAO_INICIAL)
    assert total_temporalidades == len(TABELAS_TEMPORALIDADE_INICIAIS)


def test_seed_eh_idempotente():
    """Segunda execução não deve criar registros nem alterar totais."""
    with SessionLocal() as session:
        primeira = executar_seed_gdo(session)
        segunda = executar_seed_gdo(session)

    assert primeira["classificacoes_criadas"] == len(PLANO_CLASSIFICACAO_INICIAL)
    assert segunda["classificacoes_criadas"] == 0
    assert segunda["classificacoes_existentes"] == len(PLANO_CLASSIFICACAO_INICIAL)
    assert segunda["temporalidades_criadas"] == 0
    assert segunda["temporalidades_existentes"] == len(TABELAS_TEMPORALIDADE_INICIAIS)


def test_seed_preserva_hierarquia_pai_filho():
    with SessionLocal() as session:
        executar_seed_gdo(session)
        todas = session.scalars(select(ClassificacaoDocumentalModel)).all()
        por_codigo = {m.codigo: m for m in todas}

    # Classes de nível 1 não têm pai; subclasses apontam para o pai correto
    for dados in PLANO_CLASSIFICACAO_INICIAL:
        model = por_codigo[dados["codigo"]]
        if dados["classificacao_pai"] is None:
            assert model.classificacao_pai_id is None, dados["codigo"]
        else:
            pai = por_codigo[dados["classificacao_pai"]]
            assert model.classificacao_pai_id == str(pai.id), dados["codigo"]
            assert model.nivel == dados["nivel"]
