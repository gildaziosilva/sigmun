"""Schemas de apresentação (Pydantic) da trilha de auditoria.

Baseado em:
  - 017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md
"""

from __future__ import annotations

from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from src.modules.sigmun_compras.domain.entities.registro_auditoria import (
    CategoriaEventoAuditoria,
    ResultadoEventoAuditoria,
)


class EventoAuditoriaResponse(BaseModel):
    """Representação de um evento da trilha nas respostas da API."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    ocorrido_em: datetime
    categoria: CategoriaEventoAuditoria
    tipo_evento: str
    ator_id: UUID | None = None
    ator_perfil: str | None = None
    origem: str
    operacao: str
    recurso_tipo: str
    recurso_id: UUID | None = None
    chave_negocio: str | None = None
    resultado: ResultadoEventoAuditoria
    correlation_id: UUID | None = None
    justificativa: str | None = None
    detalhes: dict[str, Any] | None = None


class TrilhaAuditoriaListResponse(BaseModel):
    """Envelope paginado da consulta da trilha de auditoria."""

    total: int
    page: int
    page_size: int
    items: list[EventoAuditoriaResponse]


__all__ = ["EventoAuditoriaResponse", "TrilhaAuditoriaListResponse"]
