"""Testes de integração dos seeds DEMO do DOM-GEO — Geoinformação Municipal.

Validam a populacao de camadas, mapas, features e serviços,
além da idempotência da execucao repetida e da limpeza.
"""
import pytest
from sqlalchemy import select, text

from src.core.infrastructure.database.session import SessionLocal
from src.modules.sigmun_geoinformacao.infrastructure.database.models import (
    CamadaMapaModel,
    FeatureGeoModel,
    MapaSigModel,
    MapaCamadaModel,
    ServicoGeoModel,
)
from src.modules.sigmun_geoinformacao.infrastructure.database.seeds import (
    CAMADAS_DEMO,
    MAPAS_DEMO,
    FEATURES_DEMO,
    SERVICOS_DEMO,
    popular_seed_geo,
    limpar_seed_geo,
)

TABELAS_GEO_SEED = (
    "geo.features_geo",
    "geo.servicos_geo",
    "geo.mapas_camadas",
    "geo.mapas_sig",
    "geo.camadas_mapa",
)


@pytest.fixture(autouse=True)
def _limpar_tabelas_seed():
    """Isolamento: limpa as tabelas afetadas pelo seed antes/depois."""
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_GEO_SEED)} CASCADE"))
        session.commit()
    yield
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_GEO_SEED)} CASCADE"))
        session.commit()


def test_seed_popula_todas_as_entidades():
    """Seed popula camadas, mapas, features e serviços."""
    with SessionLocal() as session:
        resultado = popular_seed_geo(session)
        session.commit()

        total_camadas = len(session.scalars(select(CamadaMapaModel)).all())
        total_mapas = len(session.scalars(select(MapaSigModel)).all())
        total_features = len(session.scalars(select(FeatureGeoModel)).all())
        total_servicos = len(session.scalars(select(ServicoGeoModel)).all())

    assert resultado["camadas_criadas"] == len(CAMADAS_DEMO)
    assert resultado["mapas_criados"] == len(MAPAS_DEMO)
    assert resultado["features_criados"] == len(FEATURES_DEMO)
    assert resultado["servicos_criados"] == len(SERVICOS_DEMO)

    assert total_camadas == len(CAMADAS_DEMO)
    assert total_mapas == len(MAPAS_DEMO)
    assert total_features == len(FEATURES_DEMO)
    assert total_servicos == len(SERVICOS_DEMO)


def test_seed_eh_idempotente():
    """Segunda execucao nao deve criar registros duplicados."""
    with SessionLocal() as session:
        primeira = popular_seed_geo(session)
        session.commit()

    with SessionLocal() as session:
        segunda = popular_seed_geo(session)
        session.commit()

    assert segunda["camadas_criadas"] == 0
    assert segunda["mapas_criados"] == 0
    assert segunda["features_criados"] == 0
    assert segunda["servicos_criados"] == 0


def test_seed_popula_camadas_com_dados_corretos():
    """Camadas sao criadas com os dados esperados."""
    with SessionLocal() as session:
        popular_seed_geo(session)
        session.commit()

        camadas = session.scalars(select(CamadaMapaModel)).all()

    assert len(camadas) == len(CAMADAS_DEMO)
    for camada in camadas:
        demo = next(c for c in CAMADAS_DEMO if c.codigo == camada.codigo)
        assert camada.nome == demo.nome
        assert camada.descricao == demo.descricao
        assert camada.tipo == demo.tipo
        assert camada.formato == demo.formato