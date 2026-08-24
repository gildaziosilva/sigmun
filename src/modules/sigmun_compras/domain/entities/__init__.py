"""Entidades do domínio Gestão de Compras e Contratações."""

from src.modules.sigmun_compras.domain.entities.compra import (
    TRANSICOES_VALIDAS,
    Compra,
    SituacaoCompra,
)
from src.modules.sigmun_compras.domain.entities.fornecedor import Fornecedor, SituacaoFornecedor
from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra

__all__ = [
    "Compra",
    "SituacaoCompra",
    "TRANSICOES_VALIDAS",
    "Fornecedor",
    "SituacaoFornecedor",
    "ItemCompra",
]


