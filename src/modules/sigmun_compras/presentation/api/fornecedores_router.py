"""Endpoints REST para Gestão de Fornecedores.

Baseado em:
  - UC-COMPRAS-019/020/021 – Cadastrar / Consultar / Inativar Fornecedor
  - SRV-COMPRAS-007 – Gestão de Fornecedores
  - RN-COMPRAS-030 a 033

Nota: autorização e auditoria estruturada serão aplicadas nas etapas 11 e 12
da sequência do ROADMAP (Onda 1).
"""

from __future__ import annotations

import logging
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_compras.application.commands.atualizar_fornecedor_command import (
    AtualizarFornecedorCommand,
)
from src.modules.sigmun_compras.application.commands.criar_fornecedor_command import (
    CriarFornecedorCommand,
)
from src.modules.sigmun_compras.application.commands.inativar_fornecedor_command import (
    InativarFornecedorCommand,
)
from src.modules.sigmun_compras.application.queries.consultar_fornecedor_query import (
    ConsultarFornecedorQuery,
)
from src.modules.sigmun_compras.application.queries.listar_fornecedores_query import (
    ListarFornecedoresQuery,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_fornecedor import (
    AtualizarFornecedorUseCase,
    FornecedorNaoEncontradoError,
)
from src.modules.sigmun_compras.application.use_cases.consultar_fornecedor import (
    ConsultarFornecedorUseCase,
)
from src.modules.sigmun_compras.application.use_cases.inativar_fornecedor import (
    InativarFornecedorUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_fornecedores import (
    ListarFornecedoresUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_fornecedor import (
    FornecedorJaCadastradoError,
    RegistrarFornecedorUseCase,
)
from src.modules.sigmun_compras.domain.entities.fornecedor import (
    Fornecedor,
    SituacaoFornecedor,
)
from src.modules.sigmun_compras.domain.repositories.fornecedor_repository import (
    FornecedorRepository,
)
from src.modules.sigmun_compras.infrastructure.repositories import (
    SqlAlchemyFornecedorRepository,
)
from src.modules.sigmun_compras.presentation.schemas.fornecedor_schemas import (
    FornecedorCreateRequest,
    FornecedorListResponse,
    FornecedorResponse,
    FornecedorUpdateRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/fornecedores", tags=["Compras - Fornecedores"])


# -- Providers (composition root do módulo) ----------------------------------


def get_fornecedor_repository(
    session: Annotated[Session, Depends(get_db)],
) -> FornecedorRepository:
    """Fornece o repositório concreto por requisição."""
    return SqlAlchemyFornecedorRepository(session)


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
    response_model=FornecedorResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastra um novo fornecedor",
    responses={409: {"description": "Fornecedor já cadastrado (RN-COMPRAS-031)"}},
)
def criar_fornecedor(
    payload: FornecedorCreateRequest,
    repository: Annotated[FornecedorRepository, Depends(get_fornecedor_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Fornecedor:
    """Cadastra um fornecedor (UC-COMPRAS-019)."""
    use_case = RegistrarFornecedorUseCase(repository)
    try:
        return use_case.execute(
            CriarFornecedorCommand(
                pessoa_juridica_id=payload.pessoa_juridica_id,
                situacao_cadastro=payload.situacao_cadastro,
                usuario_id=usuario_id,
            )
        )
    except FornecedorJaCadastradoError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc
    except IntegrityError as exc:
        # Corrida entre exists_pessoa_juridica e o INSERT: a constraint UNIQUE
        # do banco garante a unicidade cadastral (RN-COMPRAS-031).
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Fornecedor já cadastrado para esta pessoa jurídica "
            "(RN-COMPRAS-031) ou violação de integridade referencial.",
        ) from exc
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc


@router.get(
    "",
    response_model=FornecedorListResponse,
    summary="Lista fornecedores com filtros opcionais",
)
def listar_fornecedores(
    repository: Annotated[FornecedorRepository, Depends(get_fornecedor_repository)],
    situacao: str | None = Query(None, description="Filtrar por situação cadastral"),
    include_inativos: bool = Query(True, description="Incluir fornecedores não excluídos"),
    page: int = Query(0, ge=0, description="Página (base zero)"),
    page_size: int = Query(50, ge=1, le=200, description="Tamanho da página"),
) -> FornecedorListResponse:
    """Lista paginada de fornecedores (SRV-COMPRAS-007)."""
    situacao_filtro: SituacaoFornecedor | None = None
    if situacao is not None:
        try:
            situacao_filtro = SituacaoFornecedor(situacao.upper())
        except ValueError as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Situação inválida: {situacao}. "
                f"Valores aceitos: {[s.value for s in SituacaoFornecedor]}",
            ) from exc

    query = ListarFornecedoresQuery(
        situacao=situacao_filtro,
        include_inativos=include_inativos,
        page=page,
        page_size=page_size,
    )
    fornecedores = ListarFornecedoresUseCase(repository).execute(query)
    total = len(repository.list(situacao=situacao_filtro, include_deleted=False))
    items = [FornecedorResponse.model_validate(f) for f in fornecedores]
    return FornecedorListResponse(total=total, page=page, page_size=page_size, items=items)


@router.get(
    "/{fornecedor_id}",
    response_model=FornecedorResponse,
    summary="Consulta um fornecedor pelo ID",
    responses={404: {"description": "Fornecedor não encontrado"}},
)
def consultar_fornecedor(
    fornecedor_id: UUID,
    repository: Annotated[FornecedorRepository, Depends(get_fornecedor_repository)],
) -> Fornecedor:
    """Consulta dados cadastrais de um fornecedor (UC-COMPRAS-020)."""
    use_case = ConsultarFornecedorUseCase(repository)
    try:
        return use_case.execute(ConsultarFornecedorQuery(fornecedor_id=fornecedor_id))
    except FornecedorNaoEncontradoError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.patch(
    "/{fornecedor_id}",
    response_model=FornecedorResponse,
    summary="Atualiza os dados cadastrais de um fornecedor",
    responses={
        404: {"description": "Fornecedor não encontrado"},
        400: {"description": "Requisição inválida"},
    },
)
def atualizar_fornecedor(
    fornecedor_id: UUID,
    payload: FornecedorUpdateRequest,
    repository: Annotated[FornecedorRepository, Depends(get_fornecedor_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Fornecedor:
    """Atualiza situação cadastral e/ou macro categoria (RN-COMPRAS-033)."""
    if payload.situacao_cadastro is None and payload.macro_categoria is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Informe ao menos um campo para atualização.",
        )

    use_case = AtualizarFornecedorUseCase(repository)
    try:
        atual = use_case.execute(
            AtualizarFornecedorCommand(
                fornecedor_id=fornecedor_id,
                situacao_cadastro=payload.situacao_cadastro,
                usuario_id=usuario_id,
            )
        )
    except FornecedorNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    if payload.macro_categoria is not None:
        atual.macro_categoria = payload.macro_categoria
        repository.update(atual)

    return atual


@router.delete(
    "/{fornecedor_id}",
    response_model=FornecedorResponse,
    summary="Inativa (soft-delete) um fornecedor",
    responses={404: {"description": "Fornecedor não encontrado"}},
)
def inativar_fornecedor(
    fornecedor_id: UUID,
    repository: Annotated[FornecedorRepository, Depends(get_fornecedor_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Fornecedor:
    """Inativa um fornecedor preservando histórico (UC-COMPRAS-021)."""
    if usuario_id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Usuario-Id é obrigatório para inativação.",
        )

    use_case = InativarFornecedorUseCase(repository)
    try:
        return use_case.execute(
            InativarFornecedorCommand(fornecedor_id=fornecedor_id, usuario_id=usuario_id)
        )
    except FornecedorNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


__all__ = ["router", "get_fornecedor_repository"]
