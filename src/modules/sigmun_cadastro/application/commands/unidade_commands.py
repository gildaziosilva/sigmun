"""Commands de aplicação de Unidades Administrativas (DOM-CUM)."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CriarUnidadeCommand:
    """Registro de nova unidade administrativa (RN-CUM-008/009)."""

    nome: str
    usuario_id: UUID | None = None
    unidade_pai_id: UUID | None = None
    sigla: str | None = None
    codigo_ibge: str | None = None
    codigo_siafi: str | None = None


@dataclass(frozen=True)
class AtualizarUnidadeCommand:
    """Atualização de unidade administrativa (PATCH parcial)."""

    unidade_id: UUID
    usuario_id: UUID | None = None
    nome: str | None = None
    sigla: str | None = None
    codigo_ibge: str | None = None
    codigo_siafi: str | None = None
    unidade_pai_id: UUID | None = None


@dataclass(frozen=True)
class ExcluirUnidadeCommand:
    """Exclusão lógica de unidade administrativa (RN-CUM-007)."""

    unidade_id: UUID
    usuario_id: UUID


__all__ = ["CriarUnidadeCommand", "AtualizarUnidadeCommand", "ExcluirUnidadeCommand"]
