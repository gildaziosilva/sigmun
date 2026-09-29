"""Repositórios SQLAlchemy do DOM-TEL — Gestão Territorial."""

from .bairro import SQLAlchemyBairroRepository
from .georreferencia import SQLAlchemyGeorreferenciaRepository
from .logradouro import SQLAlchemyLogradouroRepository
from .planta import SQLAlchemyPlantaValoresRepository

__all__ = [
    "SQLAlchemyBairroRepository",
    "SQLAlchemyLogradouroRepository",
    "SQLAlchemyPlantaValoresRepository",
    "SQLAlchemyGeorreferenciaRepository",
]
