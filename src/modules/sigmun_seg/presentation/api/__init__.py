"""API Router for DOM-SEG (Segurança da Informação).

Endpoints REST para:
- Controles de Segurança
- Políticas de Segurança
- Incidentes de Segurança
- Chaves Criptográficas
- Credenciais

Cada endpoint constrói o caso de uso com repositório SQLAlchemy injetado por
dependência (session via get_db), seguindo o padrão Clean Architecture.
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_seg.application.interfaces import (
    ChaveCriptograficaRepositoryInterface,
    ControleSegurancaRepositoryInterface,
    CredencialRepositoryInterface,
    IncidenteSegurancaRepositoryInterface,
    PoliticaSegurancaRepositoryInterface,
)
from src.modules.sigmun_seg.application.use_cases.chave_use_cases import (
    BuscarChaveUseCase,
    CriarChaveUseCase,
    DeletarChaveUseCase,
    ExpirarChaveUseCase,
    RevogarChaveUseCase,
)
from src.modules.sigmun_seg.application.use_cases.controle_use_cases import (
    AtualizarControleSegurancaUseCase,
    BuscarControleSegurancaUseCase,
    CriarControleSegurancaUseCase,
    DeletarControleSegurancaUseCase,
    ImplementarControleSegurancaUseCase,
    ParcialmenteImplementadoUseCase,
)
from src.modules.sigmun_seg.application.use_cases.credencial_use_cases import (
    BuscarCredencialUseCase,
    CriarCredencialUseCase,
    RevogarCredencialUseCase,
    SuspenderCredencialUseCase,
)
from src.modules.sigmun_seg.application.use_cases.incidente_use_cases import (
    BuscarIncidenteSegurancaUseCase,
    DeletarIncidenteSegurancaUseCase,
    EncerrarIncidenteSegurancaUseCase,
    EscalarIncidenteSegurancaUseCase,
    MitigarIncidenteSegurancaUseCase,
    RegistrarIncidenteSegurancaUseCase,
    ResolverIncidenteSegurancaUseCase,
)
from src.modules.sigmun_seg.application.use_cases.politica_use_cases import (
    AprovarPoliticaSegurancaUseCase,
    AtualizarPoliticaSegurancaUseCase,
    BuscarPoliticaSegurancaUseCase,
    CriarPoliticaSegurancaUseCase,
    DeletarPoliticaSegurancaUseCase,
)
from src.modules.sigmun_seg.domain.exceptions import (
    ChaveJaRevogadaError,
    ChaveNaoEncontradaError,
    ControleJaExisteError,
    ControleNaoEncontradoError,
    CredencialJaRevogadaError,
    CredencialNaoEncontradaError,
    IncidenteJaResolvidoError,
    IncidenteNaoEncontradoError,
    NivelRiscoInvalidoError,
    PoliticaJaExisteError,
    PoliticaNaoEncontradaError,
)
from src.modules.sigmun_seg.infrastructure.repositories import (
    SqlAlchemyChaveCriptograficaRepository,
    SqlAlchemyControleSegurancaRepository,
    SqlAlchemyCredencialRepository,
    SqlAlchemyIncidenteSegurancaRepository,
    SqlAlchemyPoliticaSegurancaRepository,
)
from src.modules.sigmun_seg.presentation.schemas.chave_schemas import (
    ChavePayload,
    ChaveResponse,
)
from src.modules.sigmun_seg.presentation.schemas.controle_schemas import (
    ControlePayload,
    ControleResponse,
)
from src.modules.sigmun_seg.presentation.schemas.credencial_schemas import (
    CredencialPayload,
    CredencialResponse,
)
from src.modules.sigmun_seg.presentation.schemas.incidente_schemas import (
    IncidentePayload,
    IncidenteResponse,
)
from src.modules.sigmun_seg.presentation.schemas.politica_schemas import (
    PoliticaPayload,
    PoliticaResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/seg", tags=["Segurança da Informação"])


# -- Providers de repositório (composition root) -----------------------------


def get_controle_repo(
    session: Annotated[Session, Depends(get_db)],
) -> ControleSegurancaRepositoryInterface:
    return SqlAlchemyControleSegurancaRepository(session)


def get_politica_repo(
    session: Annotated[Session, Depends(get_db)],
) -> PoliticaSegurancaRepositoryInterface:
    return SqlAlchemyPoliticaSegurancaRepository(session)


def get_incidente_repo(
    session: Annotated[Session, Depends(get_db)],
) -> IncidenteSegurancaRepositoryInterface:
    return SqlAlchemyIncidenteSegurancaRepository(session)


def get_chave_repo(
    session: Annotated[Session, Depends(get_db)],
) -> ChaveCriptograficaRepositoryInterface:
    return SqlAlchemyChaveCriptograficaRepository(session)


def get_credencial_repo(
    session: Annotated[Session, Depends(get_db)],
) -> CredencialRepositoryInterface:
    return SqlAlchemyCredencialRepository(session)


def _usuario_id_header(
    x_usuario_id: Annotated[
        str | None,
        Header(
            alias="X-Usuario-Id",
            description="Identificador do usuário autenticado (provisório).",
        ),
    ] = None,
) -> str | None:
    return x_usuario_id


def obj_to_dict(instance: object) -> dict:
    """Converte entidade (dataclass) em dict serializável (Enums e datetime)."""
    out = {}
    for k, v in vars(instance).items():
        if isinstance(v, datetime):
            out[k] = v.isoformat()
        elif hasattr(v, "value"):  # Enum
            out[k] = v.value
        else:
            out[k] = v
    return out


# ============================ CONTROLES DE SEGURANÇA ============================


@router.get(
    "/controles",
    response_model=list[ControleResponse],
    summary="Lista controles de segurança",
)
def listar_controles(
    repo: Annotated[ControleSegurancaRepositoryInterface, Depends(get_controle_repo)],
    page: int = Query(default=0, ge=0),
    page_size: int = Query(default=50, ge=1, le=200),
    status: str | None = Query(default=None),
    tipo: str | None = Query(default=None),
    categoria: str | None = Query(default=None),
) -> list[ControleResponse]:
    items, _ = BuscarControleSegurancaUseCase(repo).list_all(
        page, page_size, status, tipo, categoria
    )
    return [ControleResponse(**obj_to_dict(c)) for c in items]


@router.post(
    "/controles",
    response_model=ControleResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registra um controle de segurança",
)
def criar_controle(
    repo: Annotated[ControleSegurancaRepositoryInterface, Depends(get_controle_repo)],
    payload: ControlePayload,
) -> ControleResponse:
    try:
        controle = CriarControleSegurancaUseCase(repo).execute(
            codigo=payload.codigo,
            nome=payload.nome,
            descricao=payload.descricao,
            tipo=payload.tipo,
            categoria=payload.categoria,
            nivel_risco=payload.nivel_risco,
        )
    except ControleJaExisteError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    except (NivelRiscoInvalidoError, ValueError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return ControleResponse(**obj_to_dict(controle))


@router.get(
    "/controles/{controle_id}",
    response_model=ControleResponse,
    summary="Busca um controle de segurança por ID",
)
def obter_controle(
    repo: Annotated[ControleSegurancaRepositoryInterface, Depends(get_controle_repo)],
    controle_id: UUID,
) -> ControleResponse:
    try:
        controle = BuscarControleSegurancaUseCase(repo).get_by_id(str(controle_id))
    except ControleNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return ControleResponse(**obj_to_dict(controle))


@router.put(
    "/controles/{controle_id}",
    response_model=ControleResponse,
    summary="Atualiza um controle de segurança",
)
def atualizar_controle(
    repo: Annotated[ControleSegurancaRepositoryInterface, Depends(get_controle_repo)],
    controle_id: UUID,
    payload: ControlePayload,
) -> ControleResponse:
    try:
        controle = AtualizarControleSegurancaUseCase(repo).execute(
            str(controle_id),
            nome=payload.nome,
            descricao=payload.descricao,
            categoria=payload.categoria,
            nivel_risco=payload.nivel_risco,
        )
    except ControleNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except (NivelRiscoInvalidoError, ValueError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return ControleResponse(**obj_to_dict(controle))


@router.post(
    "/controles/{controle_id}/implementar",
    response_model=ControleResponse,
    summary="Marca um controle como implementado",
)
def implementar_controle(
    repo: Annotated[ControleSegurancaRepositoryInterface, Depends(get_controle_repo)],
    controle_id: UUID,
) -> ControleResponse:
    try:
        controle = ImplementarControleSegurancaUseCase(repo).execute(str(controle_id))
    except ControleNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return ControleResponse(**obj_to_dict(controle))


@router.post(
    "/controles/{controle_id}/parcial",
    response_model=ControleResponse,
    summary="Marca um controle como parcialmente implementado",
)
def parcial_controle(
    repo: Annotated[ControleSegurancaRepositoryInterface, Depends(get_controle_repo)],
    controle_id: UUID,
) -> ControleResponse:
    try:
        controle = ParcialmenteImplementadoUseCase(repo).execute(str(controle_id))
    except ControleNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return ControleResponse(**obj_to_dict(controle))


@router.delete(
    "/controles/{controle_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Remove (exclusão lógica) um controle de segurança",
)
def deletar_controle(
    repo: Annotated[ControleSegurancaRepositoryInterface, Depends(get_controle_repo)],
    controle_id: UUID,
) -> None:
    try:
        DeletarControleSegurancaUseCase(repo).execute(str(controle_id))
    except ControleNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


# ============================ POLÍTICAS DE SEGURANÇA ============================


@router.get(
    "/politicas",
    response_model=list[PoliticaResponse],
    summary="Lista políticas de segurança",
)
def listar_politicas(
    repo: Annotated[PoliticaSegurancaRepositoryInterface, Depends(get_politica_repo)],
    page: int = Query(default=0, ge=0),
    page_size: int = Query(default=50, ge=1, le=200),
    ativa: bool | None = Query(default=None),
) -> list[PoliticaResponse]:
    items, _ = BuscarPoliticaSegurancaUseCase(repo).list_all(page, page_size, ativa)
    return [PoliticaResponse(**obj_to_dict(p)) for p in items]


@router.post(
    "/politicas",
    response_model=PoliticaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registra uma política de segurança",
)
def criar_politica(
    repo: Annotated[PoliticaSegurancaRepositoryInterface, Depends(get_politica_repo)],
    payload: PoliticaPayload,
) -> PoliticaResponse:
    try:
        politica = CriarPoliticaSegurancaUseCase(repo).execute(
            codigo=payload.codigo,
            titulo=payload.titulo,
            conteudo=payload.conteudo,
            versao=payload.versao,
        )
    except PoliticaJaExisteError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return PoliticaResponse(**obj_to_dict(politica))


@router.get(
    "/politicas/{politica_id}",
    response_model=PoliticaResponse,
    summary="Busca uma política de segurança por ID",
)
def obter_politica(
    repo: Annotated[PoliticaSegurancaRepositoryInterface, Depends(get_politica_repo)],
    politica_id: UUID,
) -> PoliticaResponse:
    try:
        politica = BuscarPoliticaSegurancaUseCase(repo).get_by_id(str(politica_id))
    except PoliticaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return PoliticaResponse(**obj_to_dict(politica))


@router.put(
    "/politicas/{politica_id}",
    response_model=PoliticaResponse,
    summary="Atualiza uma política de segurança",
)
def atualizar_politica(
    repo: Annotated[PoliticaSegurancaRepositoryInterface, Depends(get_politica_repo)],
    politica_id: UUID,
    payload: PoliticaPayload,
) -> PoliticaResponse:
    try:
        politica = AtualizarPoliticaSegurancaUseCase(repo).execute(
            str(politica_id), titulo=payload.titulo, conteudo=payload.conteudo
        )
    except PoliticaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return PoliticaResponse(**obj_to_dict(politica))


@router.post(
    "/politicas/{politica_id}/aprovar",
    response_model=PoliticaResponse,
    summary="Aprova uma política de segurança",
)
def aprovar_politica(
    repo: Annotated[PoliticaSegurancaRepositoryInterface, Depends(get_politica_repo)],
    politica_id: UUID,
    usuario_id: str = Depends(_usuario_id_header),
) -> PoliticaResponse:
    try:
        politica = AprovarPoliticaSegurancaUseCase(repo).execute(
            str(politica_id), aprovador_id=usuario_id or "sistema"
        )
    except PoliticaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return PoliticaResponse(**obj_to_dict(politica))


@router.delete(
    "/politicas/{politica_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Remove (exclusão lógica) uma política de segurança",
)
def deletar_politica(
    repo: Annotated[PoliticaSegurancaRepositoryInterface, Depends(get_politica_repo)],
    politica_id: UUID,
) -> None:
    try:
        DeletarPoliticaSegurancaUseCase(repo).execute(str(politica_id))
    except PoliticaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


# ============================ INCIDENTES DE SEGURANÇA ============================


@router.get(
    "/incidentes",
    response_model=list[IncidenteResponse],
    summary="Lista incidentes de segurança",
)
def listar_incidentes(
    repo: Annotated[IncidenteSegurancaRepositoryInterface, Depends(get_incidente_repo)],
    page: int = Query(default=0, ge=0),
    page_size: int = Query(default=50, ge=1, le=200),
    severidade: str | None = Query(default=None),
    status: str | None = Query(default=None),
) -> list[IncidenteResponse]:
    items, _ = BuscarIncidenteSegurancaUseCase(repo).list_all(page, page_size, severidade, status)
    return [IncidenteResponse(**obj_to_dict(i)) for i in items]


@router.post(
    "/incidentes",
    response_model=IncidenteResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registra um incidente de segurança",
)
def registrar_incidente(
    repo: Annotated[IncidenteSegurancaRepositoryInterface, Depends(get_incidente_repo)],
    payload: IncidentePayload,
    usuario_id: str = Depends(_usuario_id_header),
) -> IncidenteResponse:
    try:
        incidente = RegistrarIncidenteSegurancaUseCase(repo).execute(
            titulo=payload.titulo,
            descricao=payload.descricao,
            severidade=payload.severidade,
            impacto=payload.impacto,
            categoria=payload.categoria,
            relator_id=usuario_id or payload.relator_id,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return IncidenteResponse(**obj_to_dict(incidente))


@router.get(
    "/incidentes/{incidente_id}",
    response_model=IncidenteResponse,
    summary="Busca um incidente de segurança por ID",
)
def obter_incidente(
    repo: Annotated[IncidenteSegurancaRepositoryInterface, Depends(get_incidente_repo)],
    incidente_id: UUID,
) -> IncidenteResponse:
    try:
        incidente = BuscarIncidenteSegurancaUseCase(repo).get_by_id(str(incidente_id))
    except IncidenteNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return IncidenteResponse(**obj_to_dict(incidente))


@router.post(
    "/incidentes/{incidente_id}/escalar",
    response_model=IncidenteResponse,
    summary="Escala um incidente para um responsável",
)
def escalar_incidente(
    repo: Annotated[IncidenteSegurancaRepositoryInterface, Depends(get_incidente_repo)],
    incidente_id: UUID,
    atribuido_a: str = Query(..., description="Responsável pelo incidente"),
) -> IncidenteResponse:
    try:
        incidente = EscalarIncidenteSegurancaUseCase(repo).execute(str(incidente_id), atribuido_a)
    except IncidenteNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return IncidenteResponse(**obj_to_dict(incidente))


@router.post(
    "/incidentes/{incidente_id}/mitigar",
    response_model=IncidenteResponse,
    summary="Inicia mitigação de um incidente",
)
def mitigar_incidente(
    repo: Annotated[IncidenteSegurancaRepositoryInterface, Depends(get_incidente_repo)],
    incidente_id: UUID,
) -> IncidenteResponse:
    try:
        incidente = MitigarIncidenteSegurancaUseCase(repo).execute(str(incidente_id))
    except IncidenteNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return IncidenteResponse(**obj_to_dict(incidente))


@router.post(
    "/incidentes/{incidente_id}/resolver",
    response_model=IncidenteResponse,
    summary="Resolve um incidente",
)
def resolver_incidente(
    repo: Annotated[IncidenteSegurancaRepositoryInterface, Depends(get_incidente_repo)],
    incidente_id: UUID,
) -> IncidenteResponse:
    try:
        incidente = ResolverIncidenteSegurancaUseCase(repo).execute(str(incidente_id))
    except IncidenteNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except IncidenteJaResolvidoError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    return IncidenteResponse(**obj_to_dict(incidente))


@router.post(
    "/incidentes/{incidente_id}/encerrar",
    response_model=IncidenteResponse,
    summary="Encerra um incidente resolvido",
)
def encerrar_incidente(
    repo: Annotated[IncidenteSegurancaRepositoryInterface, Depends(get_incidente_repo)],
    incidente_id: UUID,
) -> IncidenteResponse:
    try:
        incidente = EncerrarIncidenteSegurancaUseCase(repo).execute(str(incidente_id))
    except IncidenteNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return IncidenteResponse(**obj_to_dict(incidente))


@router.delete(
    "/incidentes/{incidente_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Remove (exclusão lógica) um incidente",
)
def deletar_incidente(
    repo: Annotated[IncidenteSegurancaRepositoryInterface, Depends(get_incidente_repo)],
    incidente_id: UUID,
) -> None:
    try:
        DeletarIncidenteSegurancaUseCase(repo).execute(str(incidente_id))
    except IncidenteNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


# ============================ CHAVES CRIPTOGRÁFICAS ============================


@router.get(
    "/chaves",
    response_model=list[ChaveResponse],
    summary="Lista chaves criptográficas",
)
def listar_chaves(
    repo: Annotated[ChaveCriptograficaRepositoryInterface, Depends(get_chave_repo)],
    page: int = Query(default=0, ge=0),
    page_size: int = Query(default=50, ge=1, le=200),
    status: str | None = Query(default=None),
) -> list[ChaveResponse]:
    items, _ = BuscarChaveUseCase(repo).list_all(page, page_size, status)
    return [ChaveResponse(**obj_to_dict(c)) for c in items]


@router.post(
    "/chaves",
    response_model=ChaveResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registra uma chave criptográfica",
)
def criar_chave(
    repo: Annotated[ChaveCriptograficaRepositoryInterface, Depends(get_chave_repo)],
    payload: ChavePayload,
) -> ChaveResponse:
    try:
        chave = CriarChaveUseCase(repo).execute(
            nome=payload.nome,
            algoritmo=payload.algoritmo,
            tipo=payload.tipo,
            tamanho_bits=payload.tamanho_bits,
            responsavel_id=payload.responsavel_id,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return ChaveResponse(**obj_to_dict(chave))


@router.get(
    "/chaves/{chave_id}",
    response_model=ChaveResponse,
    summary="Busca uma chave criptográfica por ID",
)
def obter_chave(
    repo: Annotated[ChaveCriptograficaRepositoryInterface, Depends(get_chave_repo)],
    chave_id: UUID,
) -> ChaveResponse:
    try:
        chave = BuscarChaveUseCase(repo).get_by_id(str(chave_id))
    except ChaveNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return ChaveResponse(**obj_to_dict(chave))


@router.post(
    "/chaves/{chave_id}/revogar",
    response_model=ChaveResponse,
    summary="Revoga uma chave criptográfica",
)
def revogar_chave(
    repo: Annotated[ChaveCriptograficaRepositoryInterface, Depends(get_chave_repo)],
    chave_id: UUID,
) -> ChaveResponse:
    try:
        chave = RevogarChaveUseCase(repo).execute(str(chave_id))
    except ChaveNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ChaveJaRevogadaError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    return ChaveResponse(**obj_to_dict(chave))


@router.post(
    "/chaves/{chave_id}/expirar",
    response_model=ChaveResponse,
    summary="Marca uma chave criptográfica como expirada",
)
def expirar_chave(
    repo: Annotated[ChaveCriptograficaRepositoryInterface, Depends(get_chave_repo)],
    chave_id: UUID,
) -> ChaveResponse:
    try:
        chave = ExpirarChaveUseCase(repo).execute(str(chave_id))
    except ChaveNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return ChaveResponse(**obj_to_dict(chave))


@router.delete(
    "/chaves/{chave_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Remove (exclusão lógica) uma chave criptográfica",
)
def deletar_chave(
    repo: Annotated[ChaveCriptograficaRepositoryInterface, Depends(get_chave_repo)],
    chave_id: UUID,
) -> None:
    try:
        DeletarChaveUseCase(repo).execute(str(chave_id))
    except ChaveNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


# ============================ CREDENCIAIS ============================


@router.get(
    "/credenciais",
    response_model=list[CredencialResponse],
    summary="Lista credenciais",
)
def listar_credenciais(
    repo: Annotated[CredencialRepositoryInterface, Depends(get_credencial_repo)],
    page: int = Query(default=0, ge=0),
    page_size: int = Query(default=50, ge=1, le=200),
    status: str | None = Query(default=None),
    tipo: str | None = Query(default=None),
) -> list[CredencialResponse]:
    items, _ = BuscarCredencialUseCase(repo).list_all(page, page_size, status, tipo)
    return [CredencialResponse(**obj_to_dict(c)) for c in items]


@router.post(
    "/credenciais",
    response_model=CredencialResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registra uma credencial de acesso",
)
def criar_credencial(
    repo: Annotated[CredencialRepositoryInterface, Depends(get_credencial_repo)],
    payload: CredencialPayload,
) -> CredencialResponse:
    try:
        credencial = CriarCredencialUseCase(repo).execute(
            usuario_id=payload.usuario_id,
            identificador=payload.identificador,
            tipo=payload.tipo,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return CredencialResponse(**obj_to_dict(credencial))


@router.get(
    "/credenciais/{credencial_id}",
    response_model=CredencialResponse,
    summary="Busca uma credencial por ID",
)
def obter_credencial(
    repo: Annotated[CredencialRepositoryInterface, Depends(get_credencial_repo)],
    credencial_id: UUID,
) -> CredencialResponse:
    try:
        credencial = BuscarCredencialUseCase(repo).get_by_id(str(credencial_id))
    except CredencialNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return CredencialResponse(**obj_to_dict(credencial))


@router.post(
    "/credenciais/{credencial_id}/suspender",
    response_model=CredencialResponse,
    summary="Suspende uma credencial",
)
def suspender_credencial(
    repo: Annotated[CredencialRepositoryInterface, Depends(get_credencial_repo)],
    credencial_id: UUID,
) -> CredencialResponse:
    try:
        credencial = SuspenderCredencialUseCase(repo).execute(str(credencial_id))
    except CredencialNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return CredencialResponse(**obj_to_dict(credencial))


@router.post(
    "/credenciais/{credencial_id}/revogar",
    response_model=CredencialResponse,
    summary="Revoga uma credencial",
)
def revogar_credencial(
    repo: Annotated[CredencialRepositoryInterface, Depends(get_credencial_repo)],
    credencial_id: UUID,
) -> CredencialResponse:
    try:
        credencial = RevogarCredencialUseCase(repo).execute(str(credencial_id))
    except CredencialNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except CredencialJaRevogadaError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    return CredencialResponse(**obj_to_dict(credencial))


__all__ = [
    "router",
    "get_controle_repo",
    "get_politica_repo",
    "get_incidente_repo",
    "get_chave_repo",
    "get_credencial_repo",
    "obj_to_dict",
]
