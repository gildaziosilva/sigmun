"""Dependências e mapeadores compartilhados pelos endpoints do DOM-TEL."""

from __future__ import annotations

from typing import Annotated, Any, Protocol

from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db

from ...application.interfaces import (
    RepositorioBairro,
    RepositorioGeorreferencia,
    RepositorioLogradouro,
    RepositorioPlantaValores,
)
from ...domain.entities import Bairro, Logradouro
from ...infrastructure.repositories import (
    SQLAlchemyBairroRepository,
    SQLAlchemyGeorreferenciaRepository,
    SQLAlchemyLogradouroRepository,
    SQLAlchemyPlantaValoresRepository,
)
from ..schemas import BairroResponse, LogradouroResponse


class RepoComId(Protocol):
    """Port mínimo com busca por identificador."""

    def get_by_id(self, entidade_id: str) -> Any:
        """Busca a entidade pelo identificador."""
        ...


def get_bairro_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioBairro:
    """Fornece o port de bairros."""
    return SQLAlchemyBairroRepository(session)


def get_logradouro_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioLogradouro:
    """Fornece o port de logradouros."""
    return SQLAlchemyLogradouroRepository(session)


def get_planta_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioPlantaValores:
    """Fornece o port de plantas genéricas de valores."""
    return SQLAlchemyPlantaValoresRepository(session)


def get_georreferencia_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioGeorreferencia:
    """Fornece o port de georreferências."""
    return SQLAlchemyGeorreferenciaRepository(session)


def obter(repo: RepoComId, entidade_id: str) -> Any:
    """Busca por id tolerando UUID malformado (evita 500 em input inválido)."""
    try:
        return repo.get_by_id(entidade_id)
    except (ValueError, AttributeError):
        return None


def to_bairro(b: Bairro) -> BairroResponse:
    """Converte a entidade de bairro na resposta da API."""
    return BairroResponse(
        id=b.id,
        codigo=b.codigo,
        nome=b.nome,
        tipo=b.tipo.value,
        populacao_estimada=b.populacao_estimada,
        area_km2=b.area_km2,
        situacao=b.situacao.value,
        created_at=b.created_at,
        updated_at=b.updated_at,
    )


def to_logradouro(lg: Logradouro) -> LogradouroResponse:
    """Converte a entidade de logradouro na resposta da API."""
    return LogradouroResponse(
        id=lg.id,
        codigo=lg.codigo,
        nome=lg.nome,
        tipo=lg.tipo.value,
        bairro_id=lg.bairro_id,
        cep=lg.cep,
        numero_inicial=lg.numero_inicial,
        numero_final=lg.numero_final,
        situacao=lg.situacao.value,
        created_at=lg.created_at,
        updated_at=lg.updated_at,
    )


__all__ = [
    "get_bairro_repo",
    "get_logradouro_repo",
    "get_planta_repo",
    "get_georreferencia_repo",
    "obter",
    "to_bairro",
    "to_logradouro",
]
