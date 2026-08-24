"""Endpoints REST para Itens de Compra (produtos e serviços).

Baseado em:
  - ENT-COMPRAS-004 – Item da Contratação
  - RN-COMPRAS-011/012

Rotas aninhadas à compra (criar/listar) e diretas por item
(consultar/atualizar/remover).
"""

from __future__ import annotations

import logging
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_compras.application.commands.atualizar_item_compra_command import (
    AtualizarItemCompraCommand,
)
from src.modules.sigmun_compras.application.commands.criar_item_compra_command import (
    CriarItemCompraCommand,
)
from src.modules.sigmun_compras.application.commands.remover_item_compra_command import (
    RemoverItemCompraCommand,
)
from src.modules.sigmun_compras.application.queries.consultar_item_compra_query import (
    ConsultarItemCompraQuery,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_item_compra import (
    AtualizarItemCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.consultar_item_compra import (
    ConsultarItemCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_itens_compra import (
    ListarItensCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_item_compra import (
    RegistrarItemCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.remover_item_compra import (
    RemoverItemCompraUseCase,
)
from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra
from src.modules.sigmun_compras.domain.exceptions import (
    CompraNaoEncontradaError,
    ItemNaoEncontradoError,
)
from src.modules.sigmun_compras.domain.repositories.item_compra_repository import (
    ItemCompraRepository,
)
from src.modules.sigmun_compras.infrastructure.repositories import (
    SqlAlchemyItemCompraRepository,
)
from src.modules.sigmun_compras.presentation.schemas.item_compra_schemas import (
    ItemCompraCreateRequest,
    ItemCompraListResponse,
    ItemCompraResponse,
    ItemCompraUpdateRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1", tags=["Compras - Itens"])


def get_item_compra_repository(
    session: Annotated[Session, Depends(get_db)],
) -> ItemCompraRepository:
    """Fornece o repositório concreto de itens por requisição."""
    return SqlAlchemyItemCompraRepository(session)


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


# -- Endpoints aninhados à compra ----------------------------------------------


@router.post(
    "/compras/{compra_id}/itens",
    response_model=ItemCompraResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Inclui um item (produto ou serviço) em uma compra",
    responses={404: {"description": "Compra não encontrada"}},
)
def criar_item(
    compra_id: UUID,
    payload: ItemCompraCreateRequest,
    repository: Annotated[ItemCompraRepository, Depends(get_item_compra_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> ItemCompra:
    use_case = RegistrarItemCompraUseCase(repository)
    try:
        return use_case.execute(
            CriarItemCompraCommand(
                compra_id=compra_id,
                descricao=payload.descricao,
                quantidade=payload.quantidade,
                valor_unitario=payload.valor_unitario,
                usuario_id=usuario_id,
            )
        )
    except CompraNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except IntegrityError as exc:
        # Corrida entre exists_compra e o INSERT: a FK garante a integridade.
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Compra não encontrada"
        ) from exc


@router.get(
    "/compras/{compra_id}/itens",
    response_model=ItemCompraListResponse,
    summary="Lista os itens de uma compra",
    responses={404: {"description": "Compra não encontrada"}},
)
def listar_itens(
    compra_id: UUID,
    repository: Annotated[ItemCompraRepository, Depends(get_item_compra_repository)],
    page: int = Query(0, ge=0),
    page_size: int = Query(50, ge=1, le=200),
) -> ItemCompraListResponse:
    from src.modules.sigmun_compras.application.queries.listar_itens_compra_query import (
        ListarItensCompraQuery,
    )

    query = ListarItensCompraQuery(compra_id=compra_id, page=page, page_size=page_size)
    try:
        itens = ListarItensCompraUseCase(repository).execute(query)
    except CompraNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc

    todos = repository.list_by_compra(compra_id=compra_id, include_deleted=False)
    items = [ItemCompraResponse.model_validate(i) for i in itens]
    return ItemCompraListResponse(total=len(todos), page=page, page_size=page_size, items=items)


@router.get(
    "/itens-compras/{item_id}",
    response_model=ItemCompraResponse,
    summary="Consulta um item de compra pelo ID",
    responses={404: {"description": "Item não encontrado"}},
)
def consultar_item(
    item_id: UUID,
    repository: Annotated[ItemCompraRepository, Depends(get_item_compra_repository)],
) -> ItemCompra:
    use_case = ConsultarItemCompraUseCase(repository)
    try:
        return use_case.execute(ConsultarItemCompraQuery(item_id=item_id))
    except ItemNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.patch(
    "/itens-compras/{item_id}",
    response_model=ItemCompraResponse,
    summary="Atualiza um item de compra",
    responses={
        404: {"description": "Item não encontrado"},
        400: {"description": "Requisição inválida"},
    },
)
def atualizar_item(
    item_id: UUID,
    payload: ItemCompraUpdateRequest,
    repository: Annotated[ItemCompraRepository, Depends(get_item_compra_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> ItemCompra:
    use_case = AtualizarItemCompraUseCase(repository)
    try:
        return use_case.execute(
            AtualizarItemCompraCommand(
                item_id=item_id,
                descricao=payload.descricao,
                quantidade=payload.quantidade,
                valor_unitario=payload.valor_unitario,
                usuario_id=usuario_id,
            )
        )
    except ItemNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.delete(
    "/itens-compras/{item_id}",
    response_model=ItemCompraResponse,
    summary="Remove (soft-delete) um item de compra",
    responses={404: {"description": "Item não encontrado"}},
)
def remover_item(
    item_id: UUID,
    repository: Annotated[ItemCompraRepository, Depends(get_item_compra_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> ItemCompra:
    if usuario_id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Usuario-Id é obrigatório para remoção.",
        )

    use_case = RemoverItemCompraUseCase(repository)
    try:
        return use_case.execute(RemoverItemCompraCommand(item_id=item_id, usuario_id=usuario_id))
    except ItemNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


__all__ = ["router", "get_item_compra_repository"]
