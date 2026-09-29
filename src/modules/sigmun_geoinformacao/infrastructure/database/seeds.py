"""Seeds de dados DEMO do DOM-GEO — Geoinformação Municipal.

Grava camadas, mapas SIG, composições, elementos geoespaciais e serviços
usando os use cases reais do domínio (as regras de negócio são respeitadas).

IMPORTANTE:
- Os dados são DEMONSTRATIVOS e fictícios (ver `seeds_dados.py`).
- O seed é executado sob demanda (não no startup da API).
- É idempotente: reexecutar não duplica registros.
- Não realiza commit: o controle transacional pertence ao chamador.

Classificação da Informação: Pública
Responsável: Equipe SIGMUN
Status da revisão: Vigente
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from ...application.use_cases import (
    CadastrarCamadaInput,
    CadastrarCamadaUseCase,
    CadastrarMapaInput,
    CadastrarMapaUseCase,
    CadastrarServicoInput,
    CadastrarServicoUseCase,
    ComporCamadaInput,
    ComporCamadaUseCase,
    PublicarMapaUseCase,
    RegistrarFeatureInput,
    RegistrarFeatureUseCase,
)
from ..repositories import (
    SQLAlchemyCamadaMapaRepository,
    SQLAlchemyFeatureGeoRepository,
    SQLAlchemyMapaCamadaRepository,
    SQLAlchemyMapaSigRepository,
    SQLAlchemyServicoGeoRepository,
)
from .seeds_dados import (
    AUTOR_SEED,
    CAMADAS_DEMO,
    FEATURES_DEMO,
    MAPAS_DEMO,
    SERVICOS_DEMO,
)

__all__ = [
    "AUTOR_SEED",
    "CAMADAS_DEMO",
    "MAPAS_DEMO",
    "FEATURES_DEMO",
    "SERVICOS_DEMO",
    "popular_seed_geo",
    "limpar_seed_geo",
]


def _criar_camadas(session: Session) -> tuple[dict[str, str], int]:
    """Cria as camadas ausentes. Retorna mapa por código e quantidade criada."""
    repo = SQLAlchemyCamadaMapaRepository(session)
    use_case = CadastrarCamadaUseCase(repo)
    ids: dict[str, str] = {}
    criados = 0
    for item in CAMADAS_DEMO:
        existente = repo.get_by_codigo(item.codigo)
        if existente is not None:
            ids[item.codigo] = existente.id
            continue
        camada = use_case.execute(
            CadastrarCamadaInput(
                codigo=item.codigo,
                nome=item.nome,
                descricao=item.descricao,
                tipo=item.tipo,
                formato=item.formato,
                fonte=item.fonte,
                url_servico=item.url_servico,
                ativar=item.ativar,
                autor_id=AUTOR_SEED,
            )
        )
        ids[item.codigo] = camada.id
        criados += 1
    return ids, criados


def _criar_mapas(
    session: Session, camadas: dict[str, str]
) -> tuple[dict[str, str], int, int]:
    """Cria os mapas e suas composições. Retorna ids, criados e publicados."""
    repo = SQLAlchemyMapaSigRepository(session)
    vinculos = SQLAlchemyMapaCamadaRepository(session)
    repo_camadas = SQLAlchemyCamadaMapaRepository(session)
    use_case = CadastrarMapaUseCase(repo)
    compor = ComporCamadaUseCase(vinculos, repo, repo_camadas)
    publicar = PublicarMapaUseCase(repo, vinculos, repo_camadas)

    ids: dict[str, str] = {}
    criados = 0
    publicados = 0
    for item in MAPAS_DEMO:
        existente = repo.get_by_codigo(item.codigo)
        if existente is None:
            mapa = use_case.execute(
                CadastrarMapaInput(
                    codigo=item.codigo,
                    nome=item.nome,
                    descricao=item.descricao,
                    tipo=item.tipo,
                    escala_denominador=item.escala,
                    lat_min=-13.25,
                    lon_min=-39.55,
                    lat_max=-13.05,
                    lon_max=-39.40,
                    autor_id=AUTOR_SEED,
                )
            )
            mapa_id = mapa.id
            criados += 1
        else:
            mapa_id = existente.id

        for ordem, codigo_camada in enumerate(item.camadas):
            camada_id = camadas.get(codigo_camada)
            if camada_id is None or vinculos.get_by_mapa_camada(mapa_id, camada_id):
                continue
            compor.execute(
                ComporCamadaInput(
                    mapa_id=mapa_id,
                    camada_id=camada_id,
                    ordem=ordem,
                    autor_id=AUTOR_SEED,
                )
            )

        if item.publicar and repo.get_by_id(mapa_id) is not None:
            from ...domain.entities import SituacaoMapaSig

            alvo = repo.get_by_id(mapa_id)
            if alvo is not None and alvo.situacao is SituacaoMapaSig.RASCUNHO:
                publicar.execute(mapa_id, AUTOR_SEED)
                publicados += 1

        ids[item.codigo] = mapa_id
    return ids, criados, publicados


def _criar_features(session: Session, camadas: dict[str, str]) -> int:
    """Cria os elementos geoespaciais ainda não cadastrados."""
    repo = SQLAlchemyFeatureGeoRepository(session)
    repo_camadas = SQLAlchemyCamadaMapaRepository(session)
    use_case = RegistrarFeatureUseCase(repo, repo_camadas)
    criados = 0
    for item in FEATURES_DEMO:
        camada_id = camadas.get(item.camada_codigo)
        if camada_id is None or repo.get_by_codigo_camada(item.codigo, camada_id):
            continue
        use_case.execute(
            RegistrarFeatureInput(
                codigo=item.codigo,
                nome=item.nome,
                descricao=item.descricao,
                camada_id=camada_id,
                geometria=item.geometria,
                latitude=item.latitude,
                longitude=item.longitude,
                vertices=[{"latitude": item.latitude, "longitude": item.longitude}],
                autor_id=AUTOR_SEED,
            )
        )
        criados += 1
    return criados


def _criar_servicos(session: Session) -> int:
    """Cria os serviços geoespaciais ainda não cadastrados."""
    repo = SQLAlchemyServicoGeoRepository(session)
    use_case = CadastrarServicoUseCase(repo)
    criados = 0
    for item in SERVICOS_DEMO:
        if repo.get_by_codigo(item.codigo) is not None:
            continue
        use_case.execute(
            CadastrarServicoInput(
                codigo=item.codigo,
                nome=item.nome,
                descricao=item.descricao,
                tipo=item.tipo,
                url=item.url,
                camada=item.camada,
                autor_id=AUTOR_SEED,
            )
        )
        criados += 1
    return criados


def popular_seed_geo(session: Session) -> dict[str, int]:
    """Popula os dados demonstrativos do DOM-GEO.

    Não realiza commit: o controle transacional pertence ao chamador. É
    idempotente: reexecutar não duplica registros.

    Retorna um resumo com as quantidades criadas nesta execução.
    """
    camadas, camadas_criadas = _criar_camadas(session)
    _, mapas_criados, mapas_publicados = _criar_mapas(session, camadas)
    features_criados = _criar_features(session, camadas)
    servicos_criados = _criar_servicos(session)

    session.flush()

    return {
        "camadas_criadas": camadas_criadas,
        "mapas_criados": mapas_criados,
        "mapas_publicados": mapas_publicados,
        "features_criados": features_criados,
        "servicos_criados": servicos_criados,
    }


def limpar_seed_geo(session: Session) -> dict[str, int]:
    """Remove os registros criados pelo seed do DOM-GEO.

    A ordem respeita as dependências lógicas: elementos geoespaciais e serviços
    primeiro, depois as composições, os mapas e por fim as camadas.

    Retorna as quantidades removidas por tabela.
    """
    from .models import (
        CamadaMapaModel,
        FeatureGeoModel,
        MapaCamadaModel,
        MapaSigModel,
        ServicoGeoModel,
    )

    codigos_camada = {c.codigo for c in CAMADAS_DEMO}
    codigos_mapa = {m.codigo for m in MAPAS_DEMO}
    camada_ids = [
        str(m.id)
        for m in session.query(CamadaMapaModel)
        .filter(CamadaMapaModel.codigo.in_(codigos_camada))
        .all()
    ]
    mapa_ids = [
        str(m.id)
        for m in session.query(MapaSigModel)
        .filter(MapaSigModel.codigo.in_(codigos_mapa))
        .all()
    ]

    removidos = {
        "features": int(
            session.query(FeatureGeoModel)
            .filter(FeatureGeoModel.camada_id.in_(camada_ids))
            .delete(synchronize_session=False)
            or 0
        )
        if camada_ids
        else 0,
        "servicos": int(
            session.query(ServicoGeoModel)
            .filter(ServicoGeoModel.codigo.in_({s.codigo for s in SERVICOS_DEMO}))
            .delete(synchronize_session=False)
            or 0
        ),
        "composicoes": int(
            session.query(MapaCamadaModel)
            .filter(MapaCamadaModel.mapa_id.in_(mapa_ids))
            .delete(synchronize_session=False)
            or 0
        )
        if mapa_ids
        else 0,
        "mapas": int(
            session.query(MapaSigModel)
            .filter(MapaSigModel.codigo.in_(codigos_mapa))
            .delete(synchronize_session=False)
            or 0
        ),
        "camadas": int(
            session.query(CamadaMapaModel)
            .filter(CamadaMapaModel.codigo.in_(codigos_camada))
            .delete(synchronize_session=False)
            or 0
        ),
    }

    session.flush()
    return removidos
