"""Entidade Contato do Cadastro Único Municipal.

Baseado em:
  - Modelo-Fisico.md §4.1 (Tabela: core.contatos)
  - 026-Modelo-de-Dominio-Cadastro-Unico-Municipal.md

Regras de negócio implementadas:
  - RN-CUM-006: unicidade de contato principal por tipo por pessoa
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

from src.shared.compat import UTC


class TipoContato(str, Enum):
    """Tipos de contato aceitos (constraint ``ck_contatos_tipo``)."""

    TELEFONE = "TEL"
    EMAIL = "EMAIL"
    REDES = "REDES"
    WHATSAPP = "WHATSAPP"


class Contato:
    """Contato (telefone/e-mail/redes) vinculado a uma pessoa (1:N)."""

    def __init__(
        self,
        pessoa_id: UUID,
        tipo: TipoContato,
        valor: str,
        id: UUID | None = None,
        principal: bool = False,
        created_at: datetime | None = None,
        created_by: UUID | None = None,
        updated_at: datetime | None = None,
        updated_by: UUID | None = None,
        deleted_at: datetime | None = None,
        deleted_by: UUID | None = None,
    ) -> None:
        if not valor or not valor.strip():
            raise ValueError("Valor do contato é obrigatório")
        self.id: UUID = id or uuid4()
        self.pessoa_id: UUID = pessoa_id
        self.tipo: TipoContato = tipo
        self.valor: str = valor.strip()
        self.principal: bool = principal
        self.created_at: datetime = created_at or datetime.now(UTC)
        self.created_by: UUID | None = created_by
        self.updated_at: datetime = updated_at or datetime.now(UTC)
        self.updated_by: UUID | None = updated_by
        self.deleted_at: datetime | None = deleted_at
        self.deleted_by: UUID | None = deleted_by

    def excluir(self, usuario_id: UUID | None) -> None:
        """Soft-delete do contato (RN-CUM-007)."""
        self.deleted_at = datetime.now(UTC)
        self.deleted_by = usuario_id

    def foi_excluido(self) -> bool:
        """Retorna True se o contato foi logicamente excluído."""
        return self.deleted_at is not None


__all__ = ["Contato", "TipoContato"]
