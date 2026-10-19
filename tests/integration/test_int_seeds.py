"""Testes de integração dos seeds do DOM-INT — Integração e Interoperabilidade.

Validam a populacao dos conectores oficiais (GOV.BR, e-Social, SIAFIC, PNCP),
a idempotência da execucao repetida e a limpeza.
"""
import pytest
from sqlalchemy import select, text

from src.core.infrastructure.database.session import SessionLocal
from src.modules.sigmun_int.infrastructure.database.models import ConectorModel
from src.modules.sigmun_int.infrastructure.database.seeds import (
    popular_seed_int,
)

TABELAS_INT_SEED = (
    "integracao.conectores",
)


@pytest.fixture(autouse=True)
def _limpar_tabelas_seed():
    """Isolamento: limpa as tabelas afetadas pelo seed antes/depois."""
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_INT_SEED)} CASCADE"))
        session.commit()
    yield
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_INT_SEED)} CASCADE"))
        session.commit()


def test_seed_popula_conectores():
    """Seed popula os conectores oficiais."""
    with SessionLocal() as session:
        resultado = popular_seed_int(session)
        session.commit()

        total = len(session.scalars(select(ConectorModel)).all())

    assert resultado["conectores_criados"] >= 4  # GOV.BR, e-Social, SIAFIC, PNCP
    assert total == resultado["conectores_criados"]


def test_seed_eh_idempotente():
    """Segunda execucao nao deve criar registros duplicados."""
    with SessionLocal() as session:
        primeira = popular_seed_int(session)
        session.commit()

    with SessionLocal() as session:
        total_antes = len(session.scalars(select(ConectorModel)).all())
        segunda = popular_seed_int(session)
        session.commit()

    assert segunda["conectores_criados"] == 0
    assert segunda["conectores_existentes"] == total_antes


def test_seed_conectores_oficiais():
    """Verifica se os conectores oficiais foram criados."""
    from src.modules.sigmun_int.application.use_cases.conector_use_cases import CONECTORES_OFICIAIS

    with SessionLocal() as session:
        popular_seed_int(session)
        session.commit()

        conectores = session.scalars(select(ConectorModel)).all()
        codigos = {c.codigo for c in conectores}

    for conector in CONECTORES_OFICIAIS:
        assert conector["codigo"] in codigos