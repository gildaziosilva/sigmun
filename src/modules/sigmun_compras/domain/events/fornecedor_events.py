"""Eventos de domínio para Fornecedor.

Baseado em:
  - 007-Regras-de-Negocio (RN-COMPRAS-030 a 033)
  - 017-Modelo-de-Auditoria
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class FornecedorCriadoEvent:
    """Evento disparado quando um fornecedor é registrado."""

    fornecedor_id: UUID
    pessoa_juridica_id: UUID
    situacao_cadastro: str
    created_at: datetime


@dataclass(frozen=True)
class FornecedorAtualizadoEvent:
    """Evento disparado quando dados de um fornecedor são atualizados."""

    fornecedor_id: UUID
    pessoa_juridica_id: UUID | None
    situacao_cadastro: str
    updated_at: datetime


@dataclass(frozen=True)
class FornecedorInativadoEvent:
    """Evento disparado quando um fornecedor é inativado."""

    fornecedor_id: UUID
    pessoa_juridica_id: UUID
    updated_at: datetime
