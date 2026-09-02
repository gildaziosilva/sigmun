"""Endpoints REST para Compras (processos de compras).

Baseado em:
  - UC-COMPRAS-022 – Formalizar Contratação
  - ENT-COMPRAS-003 – Processo de Contratação
  - RN-COMPRAS-025 a 029

Rotas:
  POST   /api/v1/compras                       – registra
  GET    /api/v1/compras                       – lista com filtros
  GET    /api/v1/compras/{id}                  – consulta
  PATCH  /api/v1/compras/{id}                  – atualiza dados cadastrais
  PATCH  /api/v1/compras/{id}/situacao         – transição processual
  DELETE /api/v1/compras/{id}                  – exclui (soft-delete)

Nota: a listagem de itens da compra está em
GET /api/v1/compras/{id}/itens (router de itens).
"""

from __future__ import annotations

import logging
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_compras.application.commands.alterar_situacao_compra_command import (
    AlterarSituacaoCompraCommand,
)
from src.modules.sigmun_compras.application.commands.atualizar_compra_command import (
    AtualizarCompraCommand,
)
from src.modules.sigmun_compras.application.commands.criar_compra_command import (
    CriarCompraCommand,
)
from src.modules.sigmun_compras.application.commands.excluir_compra_command import (
    ExcluirCompraCommand,
)
from src.modules.sigmun_compras.application.commands.registrar_pendencia_compra_command import (
    RegistrarPendenciaCompraCommand,
)
from src.modules.sigmun_compras.application.queries.consultar_compra_query import (
    ConsultarCompraQuery,
)
from src.modules.sigmun_compras.application.use_cases.alterar_situacao_compra import (
    AlterarSituacaoCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_compra import (
    AtualizarCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.consultar_compra import (
    ConsultarCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.excluir_compra import (
    ExcluirCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_compras import (
    ListarComprasUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_pendencia_compra import (
    RegistrarPendenciaCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_compra import (
    RegistrarCompraUseCase,
)
from src.modules.sigmun_compras.domain.entities.compra import Compra, SituacaoCompra
from src.modules.sigmun_compras.domain.exceptions import (
    CompraNaoEncontradaError,
    FornecedorNaoEncontradoError,
    ProcessoDocumentalNaoEncontradoError,
    UnidadeNaoEncontradaError,
)
from src.modules.sigmun_compras.domain.repositories.compra_repository import (
    CompraRepository,
)
from src.modules.sigmun_compras.presentation.schemas.compra_schemas import (
    CompraCreateRequest,
    CompraListResponse,
    CompraPendenciasRequest,
    CompraResponse,
    CompraSituacaoRequest,
    CompraUpdateRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/compras", tags=["Compras - Processos"])


def get_compra_repository(
    session: Annotated[Session, Depends(get_db)],
) -> CompraRepository:
    """Fornece o repositório concreto de compras por requisição."""
    from src.modules.sigmun_compras.infrastructure.repositories import (
        SqlAlchemyCompraRepository,
    )

    return SqlAlchemyCompraRepository(session)


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
    response_model=CompraResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registra uma nova compra (processo de compras)",
    responses={
        404: {"description": "Processo documental, fornecedor ou unidade não encontrados"}
    },
)
def criar_compra(
    payload: CompraCreateRequest,
    repository: Annotated[CompraRepository, Depends(get_compra_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Compra:
    use_case = RegistrarCompraUseCase(repository)
    try:
        return use_case.execute(
            CriarCompraCommand(
                processo_documental_id=payload.processo_documental_id,
                fornecedor_id=payload.fornecedor_id,
                unidade_id=payload.unidade_id,
                numero=payload.numero,
                data=payload.data,
                valor_total=payload.valor_total,
                situacao=payload.situacao or SituacaoCompra.RASCUNHO,
                usuario_id=usuario_id,
            )
        )
    except (
        ProcessoDocumentalNaoEncontradoError,
        FornecedorNaoEncontradoError,
        UnidadeNaoEncontradaError,
    ) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get(
    "",
    response_model=CompraListResponse,
    summary="Lista compras com filtros opcionais",
)
def listar_compras(
    repository: Annotated[CompraRepository, Depends(get_compra_repository)],
    situacao: str | None = Query(None, description="Filtrar por situação processual"),
    include_inativos: bool = Query(False, description="Incluir compras excluídas"),
    page: int = Query(0, ge=0),
    page_size: int = Query(50, ge=1, le=200),
) -> CompraListResponse:
    from src.modules.sigmun_compras.application.queries.listar_compras_query import (
        ListarComprasQuery,
    )

    situacao_filtro: SituacaoCompra | None = None
    if situacao is not None:
        try:
            situacao_filtro = SituacaoCompra(situacao.upper())
        except ValueError as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Situação inválida: {situacao}. "
                f"Valores aceitos: {[s.value for s in SituacaoCompra]}",
            ) from exc

    query = ListarComprasQuery(
        situacao=situacao_filtro,
        include_inativos=include_inativos,
        page=page,
        page_size=page_size,
    )
    compras = ListarComprasUseCase(repository).execute(query)

    todos = repository.list(situacao=situacao_filtro, include_deleted=False)
    items = [CompraResponse.model_validate(c) for c in compras]
    return CompraListResponse(total=len(todos), page=page, page_size=page_size, items=items)


@router.get(
    "/{compra_id}",
    response_model=CompraResponse,
    summary="Consulta uma compra pelo ID",
    responses={404: {"description": "Compra não encontrada"}},
)
def consultar_compra(
    compra_id: UUID,
    repository: Annotated[CompraRepository, Depends(get_compra_repository)],
) -> Compra:
    use_case = ConsultarCompraUseCase(repository)
    try:
        return use_case.execute(ConsultarCompraQuery(compra_id=compra_id))
    except CompraNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.patch(
    "/{compra_id}",
    response_model=CompraResponse,
    summary="Atualiza dados cadastrais de uma compra",
    responses={
        404: {"description": "Compra não encontrada"},
        400: {"description": "Requisição inválida"},
    },
)
def atualizar_compra(
    compra_id: UUID,
    payload: CompraUpdateRequest,
    repository: Annotated[CompraRepository, Depends(get_compra_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Compra:
    use_case = AtualizarCompraUseCase(repository)
    try:
        return use_case.execute(
            AtualizarCompraCommand(
                compra_id=compra_id,
                numero=payload.numero,
                data=payload.data,
                valor_total=payload.valor_total,
                usuario_id=usuario_id,
            )
        )
    except CompraNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.patch(
    "/{compra_id}/situacao",
    response_model=CompraResponse,
    summary="Altera a situação processual da compra",
    description=(
        "Transições seguem a sequência processual (RN-COMPRAS-026). "
        "Ex.: RASCUNHO -> EM_INSTRUCAO -> EM_ANALISE -> ... -> ENCERRADO."
    ),
    responses={
        404: {"description": "Compra não encontrada"},
        400: {"description": "Transição não permitida pela sequência processual"},
    },
)
def alterar_situacao(
    compra_id: UUID,
    payload: CompraSituacaoRequest,
    repository: Annotated[CompraRepository, Depends(get_compra_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Compra:
    use_case = AlterarSituacaoCompraUseCase(repository)
    try:
        return use_case.execute(
            AlterarSituacaoCompraCommand(
                compra_id=compra_id,
                nova_situacao=payload.situacao,
                usuario_id=usuario_id,
            )
        )
    except CompraNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.patch(
    "/{compra_id}/pendencias",
    response_model=CompraResponse,
    summary="Registra ou resolve pendências impeditivas da compra",
    description=(
        "Enquanto existirem pendências impeditivas, o processo não poderá "
        "avançar para etapas incompatíveis (RN-COMPRAS-027); o cancelamento "
        "permanece permitido."
    ),
    responses={
        404: {"description": "Compra não encontrada"},
        400: {"description": "Requisição inválida"},
    },
)
def registrar_pendencias(
    compra_id: UUID,
    payload: CompraPendenciasRequest,
    repository: Annotated[CompraRepository, Depends(get_compra_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Compra:
    use_case = RegistrarPendenciaCompraUseCase(repository)
    try:
        return use_case.execute(
            RegistrarPendenciaCompraCommand(
                compra_id=compra_id,
                registrar=payload.pendencias_impeditivas,
                justificativa=payload.justificativa,
                usuario_id=usuario_id,
            )
        )
    except CompraNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.delete(
    "/{compra_id}",
    response_model=CompraResponse,
    summary="Exclui (soft-delete) uma compra",
    responses={404: {"description": "Compra não encontrada"}},
)
def excluir_compra(
    compra_id: UUID,
    repository: Annotated[CompraRepository, Depends(get_compra_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Compra:
    if usuario_id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Usuario-Id é obrigatório para exclusão.",
        )

    use_case = ExcluirCompraUseCase(repository)
    try:
        return use_case.execute(ExcluirCompraCommand(compra_id=compra_id, usuario_id=usuario_id))
    except CompraNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


__all__ = ["router", "get_compra_repository"]
