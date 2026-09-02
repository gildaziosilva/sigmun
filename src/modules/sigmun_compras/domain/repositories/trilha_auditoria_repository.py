"""Porta (abstração) do repositório da trilha de auditoria.

Baseado em:
  - 025-Estrutura-Tecnica (seção 18 – Interfaces e Portas: ServicoDeAuditoria
    é abstração da aplicação; implementação concreta permanece na infraestrutura)
  - 017-Modelo-de-Auditoria (seções 37/39/42 – imutabilidade, separação de
    armazenamento e filtros de consulta)

A trilha é append-only: a porta não expõe atualização nem exclusão.
"""

from __future__ import annotations

import builtins
from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.registro_auditoria import (
    CategoriaEventoAuditoria,
    RegistroAuditoria,
)


class TrilhaAuditoriaRepository(ABC):
    """Abstração de persistência da trilha de auditoria."""

    @abstractmethod
    def registrar(self, registro: RegistroAuditoria) -> RegistroAuditoria:
        """Persiste (append-only) um evento de auditoria."""

    @abstractmethod
    def list(
        self,
        *,
        data_inicio: datetime | None = None,
        data_fim: datetime | None = None,
        usuario_id: UUID | None = None,
        categoria: CategoriaEventoAuditoria | None = None,
        recurso_tipo: str | None = None,
        recurso_id: UUID | None = None,
        correlation_id: UUID | None = None,
        limit: int | None = None,
        offset: int = 0,
    ) -> builtins.list[RegistroAuditoria]:
        """Consulta a trilha com filtros (017, seção 42) e paginação."""


__all__ = ["TrilhaAuditoriaRepository"]
