"""Contrato do repositório de Unidades Administrativas (DOM-CUM).

Padrão validado no DOM-COMPRAS-001.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from src.modules.sigmun_cadastro.domain.entities.unidade_administrativa import (
    UnidadeAdministrativa,
)


class UnidadeAdministrativaRepository(ABC):
    """Contrato de persistência de unidades administrativas."""

    @abstractmethod
    def save(self, unidade: UnidadeAdministrativa) -> UnidadeAdministrativa:
        """Cria ou atualiza a unidade."""

    @abstractmethod
    def get_by_id(
        self, unidade_id: UUID, *, include_deleted: bool = False
    ) -> UnidadeAdministrativa | None:
        """Retorna a unidade pelo ID."""

    @abstractmethod
    def list(
        self,
        *,
        include_deleted: bool = False,
        limit: int | None = None,
        offset: int = 0,
    ) -> list[UnidadeAdministrativa]:
        """Lista unidades com paginação."""

    @abstractmethod
    def delete(self, unidade_id: UUID, usuario_id: UUID) -> None:
        """Soft-delete da unidade (RN-CUM-007)."""

    @abstractmethod
    def exists_sigla(self, sigla: str, *, exclude_id: UUID | None = None) -> bool:
        """Verifica unicidade de sigla (RN-CUM-009)."""

    @abstractmethod
    def get_ancestral_ids(self, unidade_id: UUID, *, max_depth: int = 32) -> list[UUID]:
        """Retorna a cadeia de ancestrais (para validar RN-CUM-008)."""

    @abstractmethod
    def exists_codigo_ibge(self, codigo_ibge: str, *, exclude_id: UUID | None = None) -> bool:
        """Verifica unicidade do código IBGE (RN-CUM-009)."""

    @abstractmethod
    def exists_codigo_siafi(self, codigo_siafi: str, *, exclude_id: UUID | None = None) -> bool:
        """Verifica unicidade do código SIAFI (RN-CUM-009)."""

    @abstractmethod
    def tem_filhas_ativas(self, unidade_id: UUID) -> bool:
        """Retorna True se existem unidades filhas não excluídas."""


__all__ = ["UnidadeAdministrativaRepository"]
