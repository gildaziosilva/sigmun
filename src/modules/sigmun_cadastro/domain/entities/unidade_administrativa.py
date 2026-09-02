"""Entidade Unidade Administrativa do Cadastro Único Municipal.

Baseado em:
  - Modelo-Fisico.md §4.1 (Tabela: core.unidades_administrativas)
  - 026-Modelo-de-Dominio-Cadastro-Unico-Municipal.md

Regras de negócio implementadas:
  - RN-CUM-008: hierarquia sem ciclos (unidade não pode ser ancestral
    de si mesma)
  - RN-CUM-009: sigla, código IBGE e código SIAFI únicos
  - RN-CUM-007: exclusão lógica preservando histórico
"""

from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from src.shared.compat import UTC


class UnidadeAdministrativa:
    """Unidade organizacional do município, hierárquica (auto-referência)."""

    def __init__(
        self,
        nome: str,
        id: UUID | None = None,
        unidade_pai_id: UUID | None = None,
        codigo_ibge: str | None = None,
        codigo_siafi: str | None = None,
        sigla: str | None = None,
        created_at: datetime | None = None,
        created_by: UUID | None = None,
        updated_at: datetime | None = None,
        updated_by: UUID | None = None,
        deleted_at: datetime | None = None,
        deleted_by: UUID | None = None,
    ) -> None:
        if not nome or not nome.strip():
            raise ValueError("Nome da unidade administrativa é obrigatório")
        self.id: UUID = id or uuid4()
        self.nome: str = nome.strip()
        self.unidade_pai_id: UUID | None = unidade_pai_id
        self.codigo_ibge: str | None = codigo_ibge
        self.codigo_siafi: str | None = codigo_siafi
        self.sigla: str | None = sigla
        self.created_at: datetime = created_at or datetime.now(UTC)
        self.created_by: UUID | None = created_by
        self.updated_at: datetime = updated_at or datetime.now(UTC)
        self.updated_by: UUID | None = updated_by
        self.deleted_at: datetime | None = deleted_at
        self.deleted_by: UUID | None = deleted_by

    # -- Comportamentos de domínio -------------------------------------------

    def atualizar(
        self,
        nome: str | None = None,
        sigla: str | None = None,
        codigo_ibge: str | None = None,
        codigo_siafi: str | None = None,
        unidade_pai_id: UUID | None = None,
        usuario_id: UUID | None = None,
    ) -> None:
        """Atualiza os dados da unidade (RN-CUM-007: não operar excluída)."""
        if self.foi_excluido():
            raise ValueError(
                "Unidade administrativa excluída não pode ser atualizada (RN-CUM-007)"
            )
        if self.unidade_pai_id == self.id or unidade_pai_id == self.id:
            raise ValueError("Unidade não pode ser pai de si mesma (RN-CUM-008)")
        if nome is not None:
            if not nome.strip():
                raise ValueError("Nome da unidade administrativa é obrigatório")
            self.nome = nome.strip()
        if sigla is not None:
            self.sigla = sigla
        if codigo_ibge is not None:
            self.codigo_ibge = codigo_ibge
        if codigo_siafi is not None:
            self.codigo_siafi = codigo_siafi
        if unidade_pai_id is not None:
            self.unidade_pai_id = unidade_pai_id
        self.updated_at = datetime.now(UTC)
        if usuario_id:
            self.updated_by = usuario_id

    def excluir(self, usuario_id: UUID) -> None:
        """Soft-delete da unidade (RN-CUM-007)."""
        if self.foi_excluido():
            return
        self.deleted_at = datetime.now(UTC)
        self.deleted_by = usuario_id

    def foi_excluido(self) -> bool:
        """Retorna True se a unidade foi logicamente excluída."""
        return self.deleted_at is not None


__all__ = ["UnidadeAdministrativa"]
