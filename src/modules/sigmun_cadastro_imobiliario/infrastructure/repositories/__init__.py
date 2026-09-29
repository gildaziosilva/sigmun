"""Repositórios SQLAlchemy do DOM-IMO — Cadastro Imobiliário."""

from .avaliacao import (
    SQLAlchemyAvaliacaoRepository,
    SQLAlchemyCaracteristicaRepository,
    SQLAlchemyGeometriaRepository,
)
from .imovel import SQLAlchemyImovelRepository
from .proprietario import SQLAlchemyProprietarioRepository

__all__ = [
    "SQLAlchemyImovelRepository",
    "SQLAlchemyProprietarioRepository",
    "SQLAlchemyAvaliacaoRepository",
    "SQLAlchemyCaracteristicaRepository",
    "SQLAlchemyGeometriaRepository",
]
