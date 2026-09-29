"""Testes de integração dos seeds DEMO do DOM-TEL (Gestão Territorial).

Validam a populacao de bairros, logradouros, plantas genericas de valores e
georreferencias, alem da idempotencia da execucao repetida e da limpeza.
"""

import pytest
from sqlalchemy import select, text

from src.core.infrastructure.database.session import SessionLocal
from src.modules.sigmun_territorial.infrastructure.database.models import (
    BairroModel,
    GeorreferenciaModel,
    LogradouroModel,
    PlantaGenericaValoresModel,
)
from src.modules.sigmun_territorial.infrastructure.database.seeds import (
    BAIRROS_DEMO,
    GEORREFERENCIAS_DEMO,
    LOGRADOUROS_DEMO,
    PLANTAS_DEMO,
    limpar_seed_tel,
    popular_seed_tel,
)

TABELAS_TEL_SEED = (
    "tel.georreferencias",
    "tel.planta_generica_valores",
    "tel.logradouros",
    "tel.bairros",
)


@pytest.fixture(autouse=True)
def _limpar_tabelas_seed():
    """Isolamento: limpa as tabelas afetadas pelo seed antes/depois."""
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_TEL_SEED)} CASCADE"))
        session.commit()
    yield
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_TEL_SEED)} CASCADE"))
        session.commit()


def test_seed_popula_todas_as_tabelas():
    with SessionLocal() as session:
        resultado = popular_seed_tel(session)
        session.commit()

        total_bairros = len(session.scalars(select(BairroModel)).all())
        total_logradouros = len(session.scalars(select(LogradouroModel)).all())
        total_plantas = len(session.scalars(select(PlantaGenericaValoresModel)).all())
        total_geo = len(session.scalars(select(GeorreferenciaModel)).all())

    assert resultado["bairros_criados"] == len(BAIRROS_DEMO)
    assert resultado["logradouros_criados"] == len(LOGRADOUROS_DEMO)
    assert resultado["georreferencias_criadas"] == len(GEORREFERENCIAS_DEMO)
    assert total_bairros == len(BAIRROS_DEMO)
    assert total_logradouros == len(LOGRADOUROS_DEMO)
    assert total_geo == len(GEORREFERENCIAS_DEMO)
    # Uma planta por item do seed, alem das possiveis revogacoes.
    assert total_plantas >= len(PLANTAS_DEMO)


def test_seed_eh_idempotente():
    """Segunda execucao nao deve criar registros."""
    with SessionLocal() as session:
        popular_seed_tel(session)
        session.commit()

        segunda = popular_seed_tel(session)
        session.commit()

    assert segunda["bairros_criados"] == 0
    assert segunda["logradouros_criados"] == 0
    assert segunda["plantas_criadas"] == 0
    assert segunda["georreferencias_criadas"] == 0


def test_seed_cobre_todos_os_status_da_planta():
    """O seed gera rascunho, vigente e revogada (RN-TEL-004)."""
    with SessionLocal() as session:
        popular_seed_tel(session)
        session.commit()

        situacoes = {
            p.situacao for p in session.scalars(select(PlantaGenericaValoresModel)).all()
        }

    assert {"rascunho", "vigente", "revogada"} <= situacoes


def test_seed_respeita_regras_de_negocio():
    """Logradouros vinculados a bairros existentes e geometrias consistentes."""
    with SessionLocal() as session:
        popular_seed_tel(session)
        session.commit()

        bairros = session.scalars(select(BairroModel)).all()
        logradouros = session.scalars(select(LogradouroModel)).all()
        georreferencias = session.scalars(select(GeorreferenciaModel)).all()
        bairros_ids = {str(b.id) for b in bairros}

    assert len({b.codigo for b in bairros}) == len(bairros)
    assert len({lg.codigo for lg in logradouros}) == len(logradouros)
    # Todo logradouro referencia um bairro cadastrado (RN-TEL-002).
    assert all(lg.bairro_id in bairros_ids for lg in logradouros)
    # Toda georreferencia esta vinculada a um bairro, nunca a ambos (RN-TEL-005).
    assert all(
        bool(g.bairro_id) != bool(g.logradouro_id) for g in georreferencias
    )


def test_limpar_seed_remove_os_dados():
    with SessionLocal() as session:
        popular_seed_tel(session)
        session.commit()

        removidos = limpar_seed_tel(session)
        session.commit()

        assert session.scalars(select(BairroModel)).all() == []
        assert session.scalars(select(LogradouroModel)).all() == []
        assert session.scalars(select(PlantaGenericaValoresModel)).all() == []
        assert session.scalars(select(GeorreferenciaModel)).all() == []

    assert removidos["bairros"] == len(BAIRROS_DEMO)
    assert removidos["logradouros"] == len(LOGRADOUROS_DEMO)
    assert removidos["georreferencias"] == len(GEORREFERENCIAS_DEMO)
