"""Testes de integração dos seeds DEMO do DOM-IMO (Cadastro Imobiliário).

Validam a populacao de imoveis, proprietarios, avaliacoes, caracteristicas e
geometrias, alem da idempotencia da execucao repetida e da limpeza.
"""

import pytest
from sqlalchemy import select, text

from src.core.infrastructure.database.session import SessionLocal
from src.modules.sigmun_cadastro_imobiliario.infrastructure.database.models import (
    AvaliacaoImovelModel,
    CaracteristicaImovelModel,
    GeometriaImovelModel,
    ImovelModel,
    ProprietarioImovelModel,
)
from src.modules.sigmun_cadastro_imobiliario.infrastructure.database.seeds import (
    AVALIACOES_DEMO,
    CARACTERISTICAS_DEMO,
    GEOMETRIAS_DEMO,
    IMOVEIS_DEMO,
    PROPRIETARIOS_DEMO,
    limpar_seed_imo,
    popular_seed_imo,
)
from src.modules.sigmun_territorial.infrastructure.database.seeds import popular_seed_tel

TABELAS_IMO_SEED = (
    "imo.geometrias_imoveis",
    "imo.caracteristicas_imoveis",
    "imo.avaliacoes_imoveis",
    "imo.proprietarios_imoveis",
    "imo.imoveis",
)
TABELAS_TEL_SEED = (
    "tel.georreferencias",
    "tel.planta_generica_valores",
    "tel.logradouros",
    "tel.bairros",
)


@pytest.fixture(autouse=True)
def _popular_tel_e_limpar():
    """O seed do DOM-IMO depende do territorio; popula e limpa ao final."""
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_IMO_SEED)} CASCADE"))
        session.commit()
        popular_seed_tel(session)
        session.commit()
    yield
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_IMO_SEED)} CASCADE"))
        session.commit()


def test_seed_popula_todas_as_tabelas():
    with SessionLocal() as session:
        resultado = popular_seed_imo(session)
        session.commit()

        total_imoveis = len(session.scalars(select(ImovelModel)).all())
        total_prop = len(session.scalars(select(ProprietarioImovelModel)).all())
        total_car = len(session.scalars(select(CaracteristicaImovelModel)).all())
        total_geo = len(session.scalars(select(GeometriaImovelModel)).all())
        total_aval = len(session.scalars(select(AvaliacaoImovelModel)).all())

    assert resultado["imoveis_criados"] == len(IMOVEIS_DEMO)
    assert resultado["proprietarios_criados"] == len(PROPRIETARIOS_DEMO)
    assert resultado["caracteristicas_criadas"] == len(CARACTERISTICAS_DEMO)
    assert resultado["geometrias_criadas"] == len(GEOMETRIAS_DEMO)
    assert resultado["avaliacoes_criadas"] == len(AVALIACOES_DEMO)

    assert total_imoveis == len(IMOVEIS_DEMO)
    assert total_prop == len(PROPRIETARIOS_DEMO)
    assert total_car == len(CARACTERISTICAS_DEMO)
    assert total_geo == len(GEOMETRIAS_DEMO)
    assert total_aval == len(AVALIACOES_DEMO)


def test_seed_eh_idempotente():
    """Segunda execucao nao deve criar registros."""
    with SessionLocal() as session:
        popular_seed_imo(session)
        session.commit()

        segunda = popular_seed_imo(session)
        session.commit()

    for chave in (
        "imoveis_criados",
        "proprietarios_criados",
        "caracteristicas_criadas",
        "geometrias_criadas",
        "avaliacoes_criadas",
    ):
        assert segunda[chave] == 0


def test_seed_respeita_regras_de_negocio():
    """Inscrição única, um titular principal por imóvel e referências válidas."""
    with SessionLocal() as session:
        popular_seed_imo(session)
        session.commit()

        imoveis = session.scalars(select(ImovelModel)).all()
        proprietarios = session.scalars(select(ProprietarioImovelModel)).all()
        imoveis_ids = {str(i.id) for i in imoveis}

    # RN-IMO-001: inscrições únicas.
    assert len({i.inscricao_imobiliaria for i in imoveis}) == len(imoveis)
    # RN-IMO-002: todo imóvel referencia logradouro e bairro.
    assert all(i.logradouro_id and i.bairro_id for i in imoveis)
    # RN-IMO-006: todo vínculo pertence a um imóvel populado.
    assert all(p.imovel_id in imoveis_ids for p in proprietarios)
    # RN-IMO-006: no máximo um titular principal por imóvel.
    principais = [
        p.imovel_id for p in proprietarios if p.principal and p.vinculo == "titular"
    ]
    assert len(principais) == len(set(principais))


def test_seed_cobre_status_das_avaliacoes():
    """O seed gera avaliações concluídas e canceladas (RN-IMO-005)."""
    with SessionLocal() as session:
        popular_seed_imo(session)
        session.commit()

        situacoes = {
            a.situacao for a in session.scalars(select(AvaliacaoImovelModel)).all()
        }

    assert {"concluida", "cancelada"} <= situacoes


def test_limpar_seed_remove_os_dados():
    with SessionLocal() as session:
        popular_seed_imo(session)
        session.commit()

        removidos = limpar_seed_imo(session)
        session.commit()

        assert session.scalars(select(ImovelModel)).all() == []
        assert session.scalars(select(ProprietarioImovelModel)).all() == []
        assert session.scalars(select(AvaliacaoImovelModel)).all() == []
        assert session.scalars(select(CaracteristicaImovelModel)).all() == []
        assert session.scalars(select(GeometriaImovelModel)).all() == []

    assert removidos["imoveis"] == len(IMOVEIS_DEMO)
    assert removidos["proprietarios"] == len(PROPRIETARIOS_DEMO)
    assert removidos["avaliacoes"] == len(AVALIACOES_DEMO)
