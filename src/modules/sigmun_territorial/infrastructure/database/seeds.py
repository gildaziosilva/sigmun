"""Seeds de dados DEMO do DOM-TEL — Gestão Territorial.

Grava bairros, logradouros, plantas genéricas de valores e georreferências
usando os use cases reais do domínio (as regras de negócio são respeitadas).

IMPORTANTE:
- Os dados são DEMONISTRATIVOS e fictícios (ver `seeds_dados.py`).
- O seed é executado sob demanda (não no startup da API).
- É idempotente: reexecutar não duplica registros.
- Não realiza commit: o controle transacional pertence ao chamador.

Classificação da Informação: Pública
Responsável: Gildazio
Status da revisão: Vigente
"""

from __future__ import annotations

from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import ColumnElement

from ...application.use_cases import (
    CadastrarBairroInput,
    CadastrarBairroUseCase,
    CadastrarLogradouroInput,
    CadastrarLogradouroUseCase,
    CadastrarPlantaValoresInput,
    CadastrarPlantaValoresUseCase,
    RegistrarGeorreferenciaInput,
    RegistrarGeorreferenciaUseCase,
    RevogarPlantaValoresUseCase,
)
from ..repositories import (
    SQLAlchemyBairroRepository,
    SQLAlchemyGeorreferenciaRepository,
    SQLAlchemyLogradouroRepository,
    SQLAlchemyPlantaValoresRepository,
)
from .seeds_dados import (
    ANO_PGV,
    AUTOR_SEED,
    BAIRROS_DEMO,
    GEORREFERENCIAS_DEMO,
    LOGRADOUROS_DEMO,
    PLANTAS_DEMO,
)

__all__ = [
    "AUTOR_SEED",
    "ANO_PGV",
    "BAIRROS_DEMO",
    "LOGRADOUROS_DEMO",
    "PLANTAS_DEMO",
    "GEORREFERENCIAS_DEMO",
    "popular_seed_tel",
    "limpar_seed_tel",
]


def _criar_bairros(session: Session) -> tuple[dict[str, str], int]:
    """Cria as divisões territoriais ausentes. Retorna mapa e quantidade criada."""
    repo = SQLAlchemyBairroRepository(session)
    use_case = CadastrarBairroUseCase(repo)
    ids: dict[str, str] = {}
    criados = 0
    for item in BAIRROS_DEMO:
        existente = repo.get_by_codigo(item.codigo)
        if existente is not None:
            ids[item.codigo] = existente.id
            continue
        bairro = use_case.execute(
            CadastrarBairroInput(
                codigo=item.codigo,
                nome=item.nome,
                tipo=item.tipo,
                populacao_estimada=item.populacao_estimada,
                area_km2=item.area_km2,
                autor_id=AUTOR_SEED,
            )
        )
        ids[item.codigo] = bairro.id
        criados += 1
    return ids, criados


def _criar_logradouros(session: Session, bairros: dict[str, str]) -> tuple[dict[str, str], int]:
    """Cria os logradouros ausentes. Retorna mapa por código e quantidade criada."""
    repo = SQLAlchemyLogradouroRepository(session)
    bairros_repo = SQLAlchemyBairroRepository(session)
    use_case = CadastrarLogradouroUseCase(repo, bairros_repo)
    ids: dict[str, str] = {}
    criados = 0
    for item in LOGRADOUROS_DEMO:
        existente = repo.get_by_codigo(item.codigo)
        if existente is not None:
            ids[item.codigo] = existente.id
            continue
        logradouro = use_case.execute(
            CadastrarLogradouroInput(
                codigo=item.codigo,
                nome=item.nome,
                bairro_id=bairros[item.bairro_codigo],
                tipo=item.tipo,
                cep=item.cep,
                numero_inicial=item.numero_inicial,
                numero_final=item.numero_final,
                autor_id=AUTOR_SEED,
            )
        )
        ids[item.codigo] = logradouro.id
        criados += 1
    return ids, criados


def _criar_plantas(session: Session, bairros: dict[str, str]) -> int:
    """Cria as plantas ausentes e revoga a do exercício anterior (RN-TEL-004)."""
    repo = SQLAlchemyPlantaValoresRepository(session)
    bairros_repo = SQLAlchemyBairroRepository(session)
    use_case = CadastrarPlantaValoresUseCase(repo, bairros_repo)
    revogar = RevogarPlantaValoresUseCase(repo)
    criados = 0
    for item in PLANTAS_DEMO:
        bairro_id = bairros[item.bairro_codigo]
        # A busca considera qualquer situação: uma planta em rascunho também
        # é definitiva e não deve ser recriada a cada execução do seed.
        existente = repo.get_by_ano_bairro_ocupacao(item.ano, bairro_id, item.ocupacao)
        if existente is not None:
            # Exercício anterior fica revogado, evidenciando o ciclo de vida.
            if item.ano < ANO_PGV and existente.situacao.value == "vigente":
                revogar.execute(existente.id, "Substituída pela planta do exercício vigente")
            continue
        planta = use_case.execute(
            CadastrarPlantaValoresInput(
                ano=item.ano,
                bairro_id=bairro_id,
                ocupacao=item.ocupacao,
                valor_terreno_m2=item.valor_terreno_m2,
                valor_construcao_m2=item.valor_construcao_m2,
                aliquota_percent=item.aliquota_percent,
                legislacao=item.legislacao,
                ativar=item.ativar,
                autor_id=AUTOR_SEED,
            )
        )
        # A planta do exercício anterior já nasce revogada, cobrindo o ciclo
        # completo RASCUNHO -> VIGENTE -> REVOGADA numa única execução.
        if item.ano < ANO_PGV:
            revogar.execute(planta.id, "Substituída pela planta do exercício vigente")
        criados += 1
    return criados


def _criar_georreferencias(session: Session, bairros: dict[str, str]) -> int:
    """Registra as georreferências ainda não cadastradas para cada bairro."""
    repo = SQLAlchemyGeorreferenciaRepository(session)
    bairros_repo = SQLAlchemyBairroRepository(session)
    logradouros_repo = SQLAlchemyLogradouroRepository(session)
    use_case = RegistrarGeorreferenciaUseCase(repo, bairros_repo, logradouros_repo)
    criados = 0
    for item in GEORREFERENCIAS_DEMO:
        bairro_id = bairros[item.bairro_codigo]
        if repo.list_by_referencia(bairro_id=bairro_id):
            continue
        use_case.execute(
            RegistrarGeorreferenciaInput(
                bairro_id=bairro_id,
                geometria=item.geometria,
                latitude=item.latitude,
                longitude=item.longitude,
                vertices=[dict(v) for v in item.vertices],
                precisao_m=item.precisao_m,
                autor_id=AUTOR_SEED,
            )
        )
        criados += 1
    return criados


def popular_seed_tel(session: Session) -> dict[str, int]:
    """Popula os dados demonstrativos do DOM-TEL.

    Não realiza commit: o controle transacional pertence ao chamador. É
    idempotente: reexecutar não duplica registros.

    Retorna um resumo com as quantidades criadas nesta execução:
        bairros_criados
        logradouros_criados
        plantas_criadas
        georreferencias_criadas
    """
    bairros, bairros_criados = _criar_bairros(session)
    _, logradouros_criados = _criar_logradouros(session, bairros)
    plantas_criadas = _criar_plantas(session, bairros)
    georreferencias_criadas = _criar_georreferencias(session, bairros)

    session.flush()

    return {
        "bairros_criados": bairros_criados,
        "logradouros_criados": logradouros_criados,
        "plantas_criadas": plantas_criadas,
        "georreferencias_criadas": georreferencias_criadas,
    }


def limpar_seed_tel(session: Session) -> dict[str, int]:
    """Remove os registros criados pelo seed do DOM-TEL.

    A ordem respeita as dependências lógicas: georreferências e plantas
    primeiro, depois logradouros e bairros.

    Retorna as quantidades removidas por tabela.
    """
    from .models import (
        BairroModel,
        GeorreferenciaModel,
        LogradouroModel,
        PlantaGenericaValoresModel,
    )

    codigos_bairro = {b.codigo for b in BAIRROS_DEMO}
    codigos_logradouro = {lg.codigo for lg in LOGRADOUROS_DEMO}
    bairro_ids = [
        str(m.id)
        for m in session.query(BairroModel).filter(BairroModel.codigo.in_(codigos_bairro)).all()
    ]

    def _apagar(model: type[Any], filtro: ColumnElement[bool] | None) -> int:
        query = session.query(model)
        if filtro is not None:
            query = query.filter(filtro)
        return int(query.delete(synchronize_session=False) or 0)

    removidos: dict[str, int] = {
        "georreferencias": _apagar(
            GeorreferenciaModel,
            GeorreferenciaModel.bairro_id.in_(bairro_ids) if bairro_ids else None,
        ),
        "plantas": _apagar(
            PlantaGenericaValoresModel,
            PlantaGenericaValoresModel.bairro_id.in_(bairro_ids) if bairro_ids else None,
        ),
        "logradouros": _apagar(
            LogradouroModel,
            LogradouroModel.codigo.in_(codigos_logradouro),
        ),
        "bairros": _apagar(BairroModel, BairroModel.codigo.in_(codigos_bairro)),
    }

    session.flush()
    return removidos
