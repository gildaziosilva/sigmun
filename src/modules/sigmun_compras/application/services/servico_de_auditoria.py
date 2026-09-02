"""ServicoDeAuditoria – serviço de aplicação da trilha de auditoria.

Baseado em:
  - 025-Estrutura-Tecnica (seção 18): ``ServicoDeAuditoria`` é a abstração
    utilizada pela aplicação; a implementação concreta fica na infraestrutura.
  - 017-Modelo-de-Auditoria (seção 6/26): cada evento identifica origem,
    usuário, recurso, operação, data/hora e resultado.

Falhas de auditoria não devem interromper a operação de negócio: o serviço
registra o erro em log e propaga apenas para quem quiser tratar.
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any
from uuid import UUID

from src.modules.sigmun_compras.domain.entities.registro_auditoria import (
    CategoriaEventoAuditoria,
    RegistroAuditoria,
    ResultadoEventoAuditoria,
)
from src.modules.sigmun_compras.domain.repositories.trilha_auditoria_repository import (
    TrilhaAuditoriaRepository,
)

logger = logging.getLogger(__name__)


class ServicoDeAuditoria:
    """Fachada de aplicação para registro e consulta da trilha."""

    def __init__(self, repository: TrilhaAuditoriaRepository) -> None:
        self._repository = repository

    def registrar(
        self,
        *,
        categoria: CategoriaEventoAuditoria,
        tipo_evento: str,
        operacao: str,
        recurso_tipo: str,
        recurso_id: UUID | None = None,
        chave_negocio: str | None = None,
        ator_id: UUID | None = None,
        ator_perfil: str | None = None,
        origem: str = RegistroAuditoria.ORIGEM_PADRAO,
        resultado: ResultadoEventoAuditoria = ResultadoEventoAuditoria.SUCESSO,
        correlation_id: UUID | None = None,
        justificativa: str | None = None,
        detalhes: dict[str, Any] | None = None,
    ) -> RegistroAuditoria | None:
        """Registra um evento; nunca interrompe a operação de negócio."""
        try:
            registro = RegistroAuditoria(
                categoria=categoria,
                tipo_evento=tipo_evento,
                ator_id=ator_id,
                ator_perfil=ator_perfil,
                origem=origem,
                operacao=operacao,
                recurso_tipo=recurso_tipo,
                recurso_id=recurso_id,
                chave_negocio=chave_negocio,
                resultado=resultado,
                correlation_id=correlation_id,
                justificativa=justificativa,
                detalhes=detalhes,
            )
            salvo = self._repository.registrar(registro)
            logger.info("Evento de auditoria registrado: %s", salvo.tipo_evento)
            return salvo
        except Exception:  # noqa: BLE001 - auditoria não derruba a operação
            logger.exception(
                "Falha ao registrar evento de auditoria (%s/%s)",
                recurso_tipo,
                operacao,
            )
            return None

    def consultar(
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
    ) -> list[RegistroAuditoria]:
        """Consulta filtrada da trilha (017, seções 42/43)."""
        return self._repository.list(
            data_inicio=data_inicio,
            data_fim=data_fim,
            usuario_id=usuario_id,
            categoria=categoria,
            recurso_tipo=recurso_tipo,
            recurso_id=recurso_id,
            correlation_id=correlation_id,
            limit=limit,
            offset=offset,
        )


__all__ = ["ServicoDeAuditoria"]
