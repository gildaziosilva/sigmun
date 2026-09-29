"""Dependências e mapeadores compartilhados pelos endpoints do DOM-IMO."""

from __future__ import annotations

from typing import Annotated, Any, Protocol

from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db

from ...application.interfaces import (
    RepositorioAvaliacao,
    RepositorioCaracteristica,
    RepositorioGeometria,
    RepositorioImovel,
    RepositorioProprietario,
)
from ...domain.entities import (
    AvaliacaoImovel,
    CaracteristicaImovel,
    GeometriaImovel,
    Imovel,
    ProprietarioImovel,
)
from ...infrastructure.repositories import (
    SQLAlchemyAvaliacaoRepository,
    SQLAlchemyCaracteristicaRepository,
    SQLAlchemyGeometriaRepository,
    SQLAlchemyImovelRepository,
    SQLAlchemyProprietarioRepository,
)
from ..schemas import (
    AvaliacaoResponse,
    CaracteristicaResponse,
    GeometriaResponse,
    ImovelResponse,
    ProprietarioResponse,
    VerticeGeometria,
)


class RepoComId(Protocol):
    """Port mínimo com busca por identificador."""

    def get_by_id(self, entidade_id: str) -> Any:
        """Busca a entidade pelo identificador."""
        ...


def get_imovel_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioImovel:
    """Fornece o port de imóveis."""
    return SQLAlchemyImovelRepository(session)


def get_proprietario_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioProprietario:
    """Fornece o port de vínculos de propriedade."""
    return SQLAlchemyProprietarioRepository(session)


def get_avaliacao_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioAvaliacao:
    """Fornece o port de avaliações."""
    return SQLAlchemyAvaliacaoRepository(session)


def get_caracteristica_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioCaracteristica:
    """Fornece o port de características construtivas."""
    return SQLAlchemyCaracteristicaRepository(session)


def get_geometria_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioGeometria:
    """Fornece o port de geometrias dos lotes."""
    return SQLAlchemyGeometriaRepository(session)


def obter(repo: RepoComId, entidade_id: str) -> Any:
    """Busca por id tolerando UUID malformado (evita 500 em input inválido)."""
    try:
        return repo.get_by_id(entidade_id)
    except (ValueError, AttributeError):
        return None


def to_imovel(i: Imovel) -> ImovelResponse:
    """Converte a entidade de imóvel na resposta da API."""
    return ImovelResponse(
        id=i.id,
        inscricao_imobiliaria=i.inscricao_imobiliaria,
        logradouro_id=i.logradouro_id,
        bairro_id=i.bairro_id,
        numero=i.numero,
        complemento=i.complemento,
        tipo=i.tipo.value,
        situacao=i.situacao.value,
        tipo_propriedade=i.tipo_propriedade.value,
        area_terreno_m2=i.area_terreno_m2,
        area_construida_m2=i.area_construida_m2,
        ano_construcao=i.ano_construcao,
        created_at=i.created_at,
        updated_at=i.updated_at,
    )


def to_proprietario(p: ProprietarioImovel) -> ProprietarioResponse:
    """Converte a entidade de vínculo de propriedade na resposta da API."""
    return ProprietarioResponse(
        id=p.id,
        imovel_id=p.imovel_id,
        pessoa_id=p.pessoa_id,
        nome=p.nome,
        cpf=p.cpf,
        vinculo=p.vinculo.value,
        principal=p.principal,
        created_at=p.created_at,
        updated_at=p.updated_at,
    )


def to_avaliacao(a: AvaliacaoImovel) -> AvaliacaoResponse:
    """Converte a entidade de avaliação na resposta da API."""
    return AvaliacaoResponse(
        id=a.id,
        imovel_id=a.imovel_id,
        ano=a.ano,
        valor_terreno_m2_unitario=a.valor_terreno_m2_unitario,
        valor_construcao_m2_unitario=a.valor_construcao_m2_unitario,
        aliquota_percent=a.aliquota_percent,
        area_terreno_m2=a.area_terreno_m2,
        area_construida_m2=a.area_construida_m2,
        valor_terreno=a.valor_terreno,
        valor_construcao=a.valor_construcao,
        valor_venal=a.valor_venal,
        valor_lancamento=a.valor_lancamento,
        situacao=a.situacao.value,
        data_avaliacao=a.data_avaliacao,
        created_at=a.created_at,
        updated_at=a.updated_at,
    )


def to_caracteristica(c: CaracteristicaImovel) -> CaracteristicaResponse:
    """Converte a entidade de característica construtiva na resposta da API."""
    return CaracteristicaResponse(
        id=c.id,
        imovel_id=c.imovel_id,
        obra=c.obra.value,
        numero_pavimentos=c.numero_pavimentos,
        ano_renovacao=c.ano_renovacao,
        observacao=c.observacao,
        created_at=c.created_at,
        updated_at=c.updated_at,
    )


def to_geometria(g: GeometriaImovel) -> GeometriaResponse:
    """Converte a entidade de geometria do lote na resposta da API."""
    return GeometriaResponse(
        id=g.id,
        imovel_id=g.imovel_id,
        geometria=g.geometria,
        latitude=g.latitude,
        longitude=g.longitude,
        vertices=[VerticeGeometria(**v) for v in g.vertices],
        datum=g.datum,
        precisao_m=g.precisao_m,
        data_levantamento=g.data_levantamento,
        created_at=g.created_at,
    )


__all__ = [
    "get_imovel_repo",
    "get_proprietario_repo",
    "get_avaliacao_repo",
    "get_caracteristica_repo",
    "get_geometria_repo",
    "obter",
    "to_imovel",
    "to_proprietario",
    "to_avaliacao",
    "to_caracteristica",
    "to_geometria",
]
