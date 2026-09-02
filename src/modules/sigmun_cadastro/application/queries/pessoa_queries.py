"""Queries de aplicação do agregado Pessoa (DOM-CUM)."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from src.modules.sigmun_cadastro.domain.entities.pessoa import CategoriaPessoa, TipoPessoa


@dataclass(frozen=True)
class ConsultarPessoaQuery:
    """Consulta de uma pessoa pelo ID."""

    pessoa_id: UUID
    include_deleted: bool = False


@dataclass(frozen=True)
class ListarPessoasQuery:
    """Listagem paginada de pessoas com filtros."""

    tipo: TipoPessoa | None = None
    categoria: CategoriaPessoa | None = None
    include_deleted: bool = False
    limit: int | None = None
    offset: int = 0


__all__ = ["ConsultarPessoaQuery", "ListarPessoasQuery"]
