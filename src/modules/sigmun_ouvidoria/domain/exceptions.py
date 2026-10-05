"""Exceções do domínio DOM-OUV (Ouvidoria FalaBR / e-OUV municipal)."""

from __future__ import annotations


class DomOuvDomainError(Exception):
    """Erro base do domínio DOM-OUV."""


class ManifestacaoNaoEncontradaError(DomOuvDomainError):
    """Manifestação não encontrada."""


class DenunciaNaoEncontradaError(DomOuvDomainError):
    """Denúncia não encontrada."""


class PedidoLaiNaoEncontradoError(DomOuvDomainError):
    """Pedido de acesso à informação (LAI) não encontrado."""


class ProtocoloJaExistenteError(DomOuvDomainError):
    """Protocolo já cadastrado (único por ano)."""


class RegraNegocioError(DomOuvDomainError):
    """Violação de regra de negócio do domínio."""


class EstadoInvalidoError(DomOuvDomainError):
    """Transição de estado inválida."""


class PrazoVencidoError(DomOuvDomainError):
    """Prazo de resposta vencido."""


class AcessoNegadoError(DomOuvDomainError):
    """Acesso negado - sigilo ou restrição legal."""


__all__ = [
    "DomOuvDomainError",
    "ManifestacaoNaoEncontradaError",
    "DenunciaNaoEncontradaError",
    "PedidoLaiNaoEncontradoError",
    "ProtocoloJaExistenteError",
    "RegraNegocioError",
    "EstadoInvalidoError",
    "PrazoVencidoError",
    "AcessoNegadoError",
]
