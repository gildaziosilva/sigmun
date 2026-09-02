"""Contrato do repositório de Pessoas (DOM-CUM).

O domínio define a interface; a infraestrutura (SQLAlchemy) implementa.
Padrão validado no DOM-COMPRAS-001 (FornecedorRepository).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from src.modules.sigmun_cadastro.domain.entities.pessoa import (
    CategoriaPessoa,
    Pessoa,
    TipoPessoa,
)
from src.modules.sigmun_cadastro.domain.entities.documento import TipoDocumento


class PessoaRepository(ABC):
    """Contrato de persistência do agregado Pessoa."""

    @abstractmethod
    def save(self, pessoa: Pessoa) -> Pessoa:
        """Cria ou atualiza o agregado (raiz + extensão + filhos)."""

    @abstractmethod
    def get_by_id(
        self, pessoa_id: UUID, *, include_deleted: bool = False
    ) -> Pessoa | None:
        """Retorna o agregado hidratado (endereços, documentos, contatos)."""

    @abstractmethod
    def list(
        self,
        *,
        tipo: TipoPessoa | None = None,
        categoria: CategoriaPessoa | None = None,
        include_deleted: bool = False,
        limit: int | None = None,
        offset: int = 0,
    ) -> list[Pessoa]:
        """Lista pessoas com filtros e paginação (hidratadas)."""

    @abstractmethod
    def delete(self, pessoa_id: UUID, usuario_id: UUID) -> None:
        """Soft-delete da pessoa (RN-CUM-007)."""

    @abstractmethod
    def exists_documento(self, tipo: TipoDocumento, numero: str) -> bool:
        """Verifica se o documento já está registrado (RN-CUM-004)."""


__all__ = ["PessoaRepository"]
