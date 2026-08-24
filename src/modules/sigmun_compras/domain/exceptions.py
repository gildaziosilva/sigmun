"""Exceções de domínio do módulo Gestão de Compras e Contratações.

Centralizadas em um único módulo para que camadas superiores
(apresentação, testes) capturem uma mesma classe independentemente
do caso de uso que a lançou.
"""

from __future__ import annotations


class ComprasDomainError(Exception):
    """Base das exceções de negócio do domínio Compras."""


class FornecedorNaoEncontradoError(ComprasDomainError):
    """Fornecedor não encontrado."""


class FornecedorJaCadastradoError(ComprasDomainError):
    """Fornecedor já cadastrado para a mesma pessoa jurídica (RN-COMPRAS-031)."""


class CompraNaoEncontradaError(ComprasDomainError):
    """Compra referenciada não encontrada."""


class ItemNaoEncontradoError(ComprasDomainError):
    """Item de compra não encontrado."""


__all__ = [
    "ComprasDomainError",
    "FornecedorNaoEncontradoError",
    "FornecedorJaCadastradoError",
    "CompraNaoEncontradaError",
    "ItemNaoEncontradoError",
]
