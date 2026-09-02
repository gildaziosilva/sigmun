"""Endpoints REST para Processos Documentais.

Baseado em:
  - UC-COMPRAS-013/014 – Abrir e Instruir Processo de Contratação
  - RN-COMPRAS-004 – Integridade do Histórico
  - RN-COMPRAS-025 – Processo Único

Nota: a listagem das compras vinculadas está em GET /api/v1/compras.
"""

from __future__ import annotations

import logging
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_compras.application.commands.atualizar_processo_documental_command import (
    AtualizarProcessoDocumentalCommand,
)
from src.modules.sigmun_compras.application.commands.criar_processo_documental_command import (
    CriarProcessoDocumentalCommand,
)
from src.modules.sigmun_compras.application.commands.excluir_processo_documental_command import (
    ExcluirProcessoDocumentalCommand,
)
from src.modules.sigmun_compras.application.queries.consultar_processo_documental_query import (
    ConsultarProcessoDocumentalQuery,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_processo_documental import (
    AtualizarProcessoDocumentalUseCase,
)
from src.modules.sigmun_compras.application.use_cases.consultar_processo_documental import (
    ConsultarProcessoDocumentalUseCase,
)
from src.modules.sigmun_compras.application.use_cases.excluir_processo_documental import (
    ExcluirProcessoDocumentalUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_processo_documental import (
    RegistrarProcessoDocumentalUseCase,
)
from src.modules.sigmun_compras.domain.entities.processo_documental import (
    ProcessoDocumental,
)
from src.modules.sigmun_compras.domain.exceptions import (
    ProcessoDocumentalDuplicadoError,
    ProcessoDocumentalNaoEncontradoError,
    UnidadeNaoEncontradaError,
)
from src.modules.sigmun_compras.domain.repositories.processo_documental_repository import (
    ProcessoDocumentalRepository,
)
from src.modules.sigmun_compras.presentation.schemas.processo_documental_schemas import (
    ProcessoDocumentalCreateRequest,
    ProcessoDocumentalListResponse,
    ProcessoDocumentalResponse,
    ProcessoDocumentalUpdateRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/processos-documentais", tags=["Compras - Processos Documentais"]
)


def get_processo_documental_repository(
    session: Annotated[Session, Depends(get_db)],
) -> ProcessoDocumentalRepository:
    """Fornece o repositório concreto por requisição."""
    from src.modules.sigmun_compras.infrastructure.repositories import (
        SqlAlchemyProcessoDocumentalRepository,
    )

    return SqlAlchemyProcessoDocumentalRepository(session)


def _usuario_id_header(
    x_usuario_id: Annotated[
        UUID | None,
        Header(
            alias="X-Usuario-Id",
            description="Identificador do usuário autenticado (provisório até DOM-IDN).",
        ),
    ] = None,
) -> UUID | None:
    return x_usuario_id


# -- Endpoints ----------------------------------------------------------------


@router.post(
    "",
    response_model=ProcessoDocumentalResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Abre um novo processo documental",
    responses={
        404: {"description": "Unidade administrativa não encontrada"},
        409: {"description": "Já existe processo com o mesmo numero/ano"},
    },
)
def criar_processo(
    payload: ProcessoDocumentalCreateRequest,
    repository: Annotated[
        ProcessoDocumentalRepository, Depends(get_processo_documental_repository)
    ],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> ProcessoDocumental:
    use_case = RegistrarProcessoDocumentalUseCase(repository)
    try:
        return use_case.execute(
            CriarProcessoDocumentalCommand(
                unidade_id=payload.unidade_id,
                numero=payload.numero,
                ano=payload.ano,
                assunto=payload.assunto,
                descricao=payload.descricao,
                usuario_id=usuario_id,
            )
        )
    except UnidadeNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ProcessoDocumentalDuplicadoError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get(
    "",
    response_model=ProcessoDocumentalListResponse,
    summary="Lista processos documentais com filtros opcionais",
)
def listar_processos(
    repository: Annotated[
        ProcessoDocumentalRepository, Depends(get_processo_documental_repository)
    ],
    unidade_id: Annotated[UUID | None, Query(description="Filtrar por unidade")] = None,
    ano: Annotated[
        int | None, Query(ge=1900, le=2100, description="Filtrar por ano")
    ] = None,
    include_inativos: Annotated[bool, Query(description="Incluir excluídos")] = False,
    page: Annotated[int, Query(ge=0)] = 0,
    page_size: Annotated[int, Query(ge=1, le=200)] = 50,
) -> ProcessoDocumentalListResponse:
    from src.modules.sigmun_compras.application.queries.listar_processos_documentais_query import (
        ListarProcessosDocumentaisQuery,
    )
    from src.modules.sigmun_compras.application.use_cases.listar_processos_documentais import (
        ListarProcessosDocumentaisUseCase,
    )

    query = ListarProcessosDocumentaisQuery(
        unidade_id=unidade_id,
        ano=ano,
        include_inativos=include_inativos,
        page=page,
        page_size=page_size,
    )
    processos = ListarProcessosDocumentaisUseCase(repository).execute(query)

    todos = repository.list(
        unidade_id=unidade_id, ano=ano, include_deleted=False
    )
    items = [ProcessoDocumentalResponse.model_validate(p) for p in processos]
    return ProcessoDocumentalListResponse(
        total=len(todos), page=page, page_size=page_size, items=items
    )


@router.get(
    "/{processo_id}",
    response_model=ProcessoDocumentalResponse,
    summary="Consulta um processo documental pelo ID",
    responses={404: {"description": "Processo não encontrado"}},
)
def consultar_processo(
    processo_id: UUID,
    repository: Annotated[
        ProcessoDocumentalRepository, Depends(get_processo_documental_repository)
    ],
) -> ProcessoDocumental:
    use_case = ConsultarProcessoDocumentalUseCase(repository)
    try:
        return use_case.execute(ConsultarProcessoDocumentalQuery(processo_id=processo_id))
    except ProcessoDocumentalNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.patch(
    "/{processo_id}",
    response_model=ProcessoDocumentalResponse,
    summary="Atualiza um processo documental",
    responses={
        404: {"description": "Processo não encontrado"},
        400: {"description": "Requisição inválida"},
        409: {"description": "Já existe processo com o mesmo numero/ano"},
    },
)
def atualizar_processo(
    processo_id: UUID,
    payload: ProcessoDocumentalUpdateRequest,
    repository: Annotated[
        ProcessoDocumentalRepository, Depends(get_processo_documental_repository)
    ],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> ProcessoDocumental:
    use_case = AtualizarProcessoDocumentalUseCase(repository)
    try:
        return use_case.execute(
            AtualizarProcessoDocumentalCommand(
                processo_id=processo_id,
                numero=payload.numero,
                ano=payload.ano,
                assunto=payload.assunto,
                descricao=payload.descricao,
                usuario_id=usuario_id,
            )
        )
    except ProcessoDocumentalNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ProcessoDocumentalDuplicadoError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.delete(
    "/{processo_id}",
    response_model=ProcessoDocumentalResponse,
    summary="Exclui (soft-delete) um processo documental",
    responses={404: {"description": "Processo não encontrado"}},
)
def excluir_processo(
    processo_id: UUID,
    repository: Annotated[
        ProcessoDocumentalRepository, Depends(get_processo_documental_repository)
    ],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> ProcessoDocumental:
    if usuario_id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Usuario-Id é obrigatório para exclusão.",
        )

    use_case = ExcluirProcessoDocumentalUseCase(repository)
    try:
        return use_case.execute(
            ExcluirProcessoDocumentalCommand(processo_id=processo_id, usuario_id=usuario_id)
        )
    except ProcessoDocumentalNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


__all__ = ["router", "get_processo_documental_repository"]
