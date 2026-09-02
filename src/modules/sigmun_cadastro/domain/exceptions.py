"""Exceções de domínio do Cadastro Único Municipal (DOM-CUM)."""

from __future__ import annotations


class CadastroDomainError(Exception):
    """Erro base do domínio de Cadastro Único Municipal."""


class PessoaNaoEncontradoError(CadastroDomainError):
    """Pessoa não encontrada."""


class PessoaExcluidaError(CadastroDomainError):
    """Operação sobre pessoa logicamente excluída (RN-CUM-007)."""


class DocumentoDuplicadoError(CadastroDomainError):
    """Documento (CPF/CNPJ/...) já registrado para outra pessoa (RN-CUM-004)."""


class DocumentoInvalidoError(CadastroDomainError):
    """Documento com número inválido (dígitos verificadores, RN-CUM-002/003)."""


class EnderecoNaoEncontradoError(CadastroDomainError):
    """Endereço não encontrado para a pessoa."""


class UnidadeNaoEncontradaError(CadastroDomainError):
    """Unidade administrativa não encontrada."""


class UnidadeJaExistenteError(CadastroDomainError):
    """Unidade administrativa com sigla/código já registrado (RN-CUM-009)."""


class UnidadeComFilhasAtivasError(CadastroDomainError):
    """Exclusão de unidade que possui unidades filhas ativas (RN-CUM-007)."""


class CicloHierarquiaError(CadastroDomainError):
    """Hierarquia de unidades administrativas com ciclo (RN-CUM-008)."""


__all__ = [
    "CadastroDomainError",
    "PessoaNaoEncontradoError",
    "PessoaExcluidaError",
    "DocumentoDuplicadoError",
    "DocumentoInvalidoError",
    "EnderecoNaoEncontradoError",
    "UnidadeNaoEncontradaError",
    "UnidadeJaExistenteError",
    "UnidadeComFilhasAtivasError",
    "CicloHierarquiaError",
]
