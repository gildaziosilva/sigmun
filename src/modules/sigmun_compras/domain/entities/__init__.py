"""Entidades do domínio Gestão de Compras e Contratações."""

from src.modules.sigmun_compras.domain.entities.fornecedor import Fornecedor, SituacaoFornecedor
from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra

__all__ = ["Fornecedor", "SituacaoFornecedor", "ItemCompra"]


