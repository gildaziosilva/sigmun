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


class CompraEmEstadoTerminalError(ComprasDomainError):
    """Operação não permitida sobre compra em estado terminal (RN-COMPRAS-026).
    
    Estados terminais: CANCELADO, ARQUIVADO, ENCERRADO.
    """


class ItemNaoEncontradoError(ComprasDomainError):
    """Item de compra não encontrado."""


class ProcessoDocumentalNaoEncontradoError(ComprasDomainError):
    """Processo documental referenciado não encontrado (RN-COMPRAS-025)."""


class ProcessoDocumentalDuplicadoError(ComprasDomainError):
    """Já existe processo documental com o mesmo par (numero, ano)."""


class UnidadeNaoEncontradaError(ComprasDomainError):
    """Unidade administrativa referenciada não encontrada."""


class ContratoNaoEncontradoError(ComprasDomainError):
    """Contrato referenciado não encontrado."""


class ContratoDuplicadoError(ComprasDomainError):
    """Já existe contrato com o mesmo numero (RN-COMPRAS-036)."""


class ContratoEmEstadoTerminalError(ComprasDomainError):
    """Operação não permitida sobre contrato em estado terminal (RN-COMPRAS-106).
    
    Estados terminais: ENCERRADO, RESCINDIDO, EXTINTO.
    """


class OperacaoNaoPermitidaError(ComprasDomainError):
    """Operação de negócio não permitida para o estado atual da entidade."""


__all__ = [
    "ComprasDomainError",
    "FornecedorNaoEncontradoError",
    "FornecedorJaCadastradoError",
    "CompraNaoEncontradaError",
    "CompraEmEstadoTerminalError",
    "ItemNaoEncontradoError",
    "ProcessoDocumentalNaoEncontradoError",
    "ProcessoDocumentalDuplicadoError",
    "UnidadeNaoEncontradaError",
    "ContratoNaoEncontradoError",
    "ContratoDuplicadoError",
    "ContratoEmEstadoTerminalError",
    "OperacaoNaoPermitidaError",
]
