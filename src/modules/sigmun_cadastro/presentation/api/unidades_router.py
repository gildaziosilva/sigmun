"""Endpoints REST de Unidades Administrativas (DOM-CUM).

Baseado em:
  - 004-Mapa-de-Servicos-Cadastro-Unico-Municipal.md
  - RN-CUM-007 (exclusão lógica), RN-CUM-008 (hierarquia sem ciclos)
  - RN-CUM-009 (unicidade de sigla/códigos IBGE/SIAFI)

Nota: autorização e auditoria estruturadas seguem o padrão do
DOM-COMPRAS-001 (header X-Usuario-Id provisório até o DOM-IDN).
"""

from __future__ import annotations

import logging
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_cadastro.application.commands.unidade_commands import (
    AtualizarUnidadeCommand,
    CriarUnidadeCommand,
    ExcluirUnidadeCommand,
)
from src.modules.sigmun_cadastro.application.queries.unidade_queries import (
    ConsultarUnidadeQuery,
    ListarUnidadesQuery,
)
from src.modules.sigmun_cadastro.application.use_cases.atualizar_unidade import (
    AtualizarUnidadeUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.consultar_unidade import (
    ConsultarUnidadeUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.excluir_unidade import (
    ExcluirUnidadeUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.listar_unidades import (
    ListarUnidadesUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.registrar_unidade import (
    RegistrarUnidadeUseCase,
)
from src.modules.sigmun_cadastro.domain.entities.unidade_administrativa import (
    UnidadeAdministrativa,
)
from src.modules.sigmun_cadastro.domain.exceptions import (
    CadastroDomainError,
    CicloHierarquiaError,
    UnidadeJaExistenteError,
    UnidadeNaoEncontradaError,
)
from src.modules.sigmun_cadastro.domain.repositories.unidade_administrativa_repository import (
    UnidadeAdministrativaRepository,
)
from src.modules.sigmun_cadastro.infrastructure.repositories import (
    SqlAlchemyUnidadeAdministrativaRepository,
)
from src.modules.sigmun_cadastro.presentation.schemas.unidade_schemas import (
    UnidadeCreateRequest,
    UnidadeListResponse,
    UnidadeResponse,
    UnidadeUpdateRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/cadastro/unidades-administrativas",
    tags=["Cadastro - Unidades Administrativas"],
)


# -- Providers (composition root do módulo) ------------------------------------


def get_unidade_repository(
    session: Annotated[Session, Depends(get_db)],
) -> UnidadeAdministrativaRepository:
    """Fornece o repositório concreto por requisição."""
    return SqlAlchemyUnidadeAdministrativaRepository(session)


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


# -- Endpoints ------------------------------------------------------------------


@router.post(
    "",
    response_model=UnidadeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registra uma nova unidade administrativa",
    responses={
        400: {"description": "Requisição inválida"},
        409: {"description": "Sigla/código duplicado ou ciclo hierárquico"},
    },
)
def registrar_unidade(
    payload: UnidadeCreateRequest,
    repository: Annotated[
        UnidadeAdministrativaRepository, Depends(get_unidade_repository)
    ],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> UnidadeAdministrativa:
    """Registra uma unidade administrativa (RN-CUM-008/009)."""
    command = CriarUnidadeCommand(
        nome=payload.nome,
        usuario_id=usuario_id,
        unidade_pai_id=payload.unidade_pai_id,
        sigla=payload.sigla,
        codigo_ibge=payload.codigo_ibge,
        codigo_siafi=payload.codigo_siafi,
    )
    try:
        return RegistrarUnidadeUseCase(repository).execute(command)
    except UnidadeJaExistenteError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=str(exc)
        ) from exc
    except (CicloHierarquiaError, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)
        ) from exc


@router.get(
    "",
    response_model=UnidadeListResponse,
    summary="Lista unidades administrativas com paginação",
)
def listar_unidades(
    repository: Annotated[
        UnidadeAdministrativaRepository, Depends(get_unidade_repository)
    ],
    include_deleted: bool = Query(False, description="Incluir unidades excluídas"),
    page: int = Query(0, ge=0, description="Página (base zero)"),
    page_size: int = Query(50, ge=1, le=200, description="Tamanho da página"),
) -> UnidadeListResponse:
    """Lista paginada de unidades administrativas."""
    offset = page * page_size
    query = ListarUnidadesQuery(
        include_deleted=include_deleted, limit=page_size, offset=offset
    )
    unidades = ListarUnidadesUseCase(repository).execute(query)
    total = len(repository.list(include_deleted=include_deleted))
    items = [UnidadeResponse.model_validate(u) for u in unidades]
    return UnidadeListResponse(total=total, page=page, page_size=page_size, items=items)
