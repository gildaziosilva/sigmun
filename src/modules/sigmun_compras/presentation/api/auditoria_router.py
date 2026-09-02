"""Endpoints REST da Trilha de Auditoria.

Baseado em:
  - 017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md
    (seção 40 – controle de acesso restrito por perfil;
     seção 41 – o acesso à auditoria também deve ser auditado;
     seção 42 – filtros de consulta)

Rotas:
  GET /api/v1/auditoria – consulta filtrada e paginada da trilha
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_compras.application.queries.consultar_trilha_auditoria_query import (
    ConsultarTrilhaAuditoriaQuery,
)
from src.modules.sigmun_compras.application.services.servico_de_auditoria import (
    ServicoDeAuditoria,
)
from src.modules.sigmun_compras.application.use_cases.consultar_trilha_auditoria import (
    ConsultarTrilhaAuditoriaUseCase,
)
from src.modules.sigmun_compras.domain.entities.registro_auditoria import (
    CategoriaEventoAuditoria,
)
from src.modules.sigmun_compras.domain.repositories.trilha_auditoria_repository import (
    TrilhaAuditoriaRepository,
)
from src.modules.sigmun_compras.presentation.schemas.auditoria_schemas import (
    EventoAuditoriaResponse,
    TrilhaAuditoriaListResponse,
)
from src.shared.security import UsuarioContexto, exigir_papeis

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/auditoria", tags=["Compras - Auditoria"])

# 017-Modelo-de-Auditoria, seção 40: perfis com acesso à trilha.
_exigir_leitor_auditoria = exigir_papeis(
    "auditor",
    "controladoria",
    "administrador_seguranca",
)


def get_trilha_auditoria_repository(
    session: Annotated[Session, Depends(get_db)],
) -> TrilhaAuditoriaRepository:
    """Fornece o repositório concreto da trilha por requisição."""
    from src.modules.sigmun_compras.infrastructure.repositories import (
        SqlAlchemyTrilhaAuditoriaRepository,
    )

    return SqlAlchemyTrilhaAuditoriaRepository(session)


@router.get(
    "",
    response_model=TrilhaAuditoriaListResponse,
    summary="Consulta a trilha de auditoria com filtros",
    description=(
        "Acesso restrito aos perfis auditor, controladoria e "
        "administrador_seguranca (017, seção 40). O próprio acesso é "
        "registrado na trilha como evento de ACESSO (017, seção 41)."
    ),
    responses={
        status.HTTP_401_UNAUTHORIZED: {"description": "Autenticação obrigatória"},
        status.HTTP_403_FORBIDDEN: {"description": "Perfil sem acesso à auditoria"},
    },
)
def consultar_auditoria(
    leitor: Annotated[UsuarioContexto, Depends(_exigir_leitor_auditoria)],
    repository: Annotated[TrilhaAuditoriaRepository, Depends(get_trilha_auditoria_repository)],
    data_inicio: Annotated[datetime | None, Query(description="Início do período")] = None,
    data_fim: Annotated[datetime | None, Query(description="Fim do período")] = None,
    usuario_id: Annotated[UUID | None, Query(description="Filtrar por usuário")] = None,
    categoria: Annotated[
        str | None,
        Query(description="Categoria do evento (ver valores de CategoriaEventoAuditoria)"),
    ] = None,
    recurso_tipo: Annotated[str | None, Query(description="Tipo do recurso")] = None,
    recurso_id: Annotated[UUID | None, Query(description="Id do recurso")] = None,
    correlation_id: Annotated[UUID | None, Query(description="Correlation id")] = None,
    page: Annotated[int, Query(ge=0)] = 0,
    page_size: Annotated[int, Query(ge=1, le=200)] = 50,
) -> TrilhaAuditoriaListResponse:
    categoria_filtro: CategoriaEventoAuditoria | None = None
    if categoria is not None:
        try:
            categoria_filtro = CategoriaEventoAuditoria(categoria.upper())
        except ValueError:
            logger.warning("Categoria de auditoria inválida: %s", categoria)
            return TrilhaAuditoriaListResponse(total=0, page=page, page_size=page_size, items=[])

    servico = ServicoDeAuditoria(repository)
    eventos = ConsultarTrilhaAuditoriaUseCase(repository).execute(
        ConsultarTrilhaAuditoriaQuery(
            data_inicio=data_inicio,
            data_fim=data_fim,
            usuario_id=usuario_id,
            categoria=categoria_filtro,
            recurso_tipo=recurso_tipo,
            recurso_id=recurso_id,
            correlation_id=correlation_id,
            page=page,
            page_size=page_size,
        )
    )
    total = repository.count(
        data_inicio=data_inicio,
        data_fim=data_fim,
        usuario_id=usuario_id,
        categoria=categoria_filtro,
        recurso_tipo=recurso_tipo,
        recurso_id=recurso_id,
        correlation_id=correlation_id,
    )

    # 017-Modelo-de-Auditoria, seção 41: auditar o acesso à auditoria.
    servico.registrar(
        categoria=CategoriaEventoAuditoria.ACESSO,
        tipo_evento="TrilhaConsultada",
        operacao="consultarAuditoria",
        recurso_tipo="TrilhaAuditoria",
        ator_id=leitor.usuario_id,
        ator_perfil=",".join(leitor.papeis) or None,
        detalhes={
            "filtros": {
                "categoria": categoria_filtro.value if categoria_filtro else None,
                "usuario_id": str(usuario_id) if usuario_id else None,
                "recurso_tipo": recurso_tipo,
                "recurso_id": str(recurso_id) if recurso_id else None,
                "correlation_id": str(correlation_id) if correlation_id else None,
            },
            "resultados_retornados": len(eventos),
        },
    )

    items = [EventoAuditoriaResponse.model_validate(e) for e in eventos]
    return TrilhaAuditoriaListResponse(total=total, page=page, page_size=page_size, items=items)


__all__ = ["router", "get_trilha_auditoria_repository"]
