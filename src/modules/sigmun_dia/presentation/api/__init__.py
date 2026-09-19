"""Endpoints REST de Gestão de Diárias, Viagens e Deslocamentos (DOM-DIA)."""

from __future__ import annotations

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_dia.application.interfaces import (
    RepositorioDiaria,
    RepositorioPrestacaoContas,
    RepositorioViagem,
)
from src.modules.sigmun_dia.application.use_cases import (
    AprovacaoPrestacaoInputDTO,
    AprovarPrestacaoUseCase,
    AutorizarDiariaUseCase,
    CalcularDiariaUseCase,
    ConfirmarConcessaoUseCase,
    ConcederDiariaUseCase,
    CriarDiariaUseCase,
    CriarPrestacaoContasInputDTO,
    CriarPrestacaoContasUseCase,
    CriarViagemUseCase,
    GlosagemPrestacaoInputDTO,
    GlosarPrestacaoUseCase,
    IniciarPrestacaoUseCase,
    PagarDiariaUseCase,
    RestituicaPrestacaoInputDTO,
    RestituirPrestacaoUseCase,
    ReverterParaPagamentoUseCase,
    SolicitacaoDiariaInput,
    SolicitarDiariaUseCase,
    SolicitarViagemInput,
    TramitarViagemUseCase,
    VisitarViagemUseCase,
)
from src.modules.sigmun_dia.infrastructure.repositories import (
    SQLAlchemyDiariaRepository,
    SQLAlchemyPrestacaoContasRepository,
    SQLAlchemyViagemRepository,
)
from src.modules.sigmun_dia.presentation.schemas import (
    DiariaCreateRequest,
    DiariaResponse,
    PrestacaoContasCreateRequest,
    PrestacaoContasResponse,
    ViagemCreateRequest,
    ViagemResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/dia", tags=["Gestão de Diárias, Viagens e Deslocamentos"])


# =============================================================================
# Dependency Injection
# =============================================================================


def get_viagem_repository(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioViagem:
    return SQLAlchemyViagemRepository(session)


def get_diaria_repository(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioDiaria:
    return SQLAlchemyDiariaRepository(session)


def get_prestacao_repository(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioPrestacaoContas:
    return SQLAlchemyPrestacaoContasRepository(session)


# =============================================================================
# Endpoints de Viagem
# =============================================================================


@router.post(
    "/viagens",
    response_model=ViagemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Solicita uma nova viagem oficial",
    responses={409: {"model": None}},
)
def solicitar_viagem(
    payload: ViagemCreateRequest,
    repo: Annotated[RepositorioViagem, Depends(get_viagem_repository)],
) -> ViagemResponse:
    """Solicita uma nova viagem oficial."""
    try:
        use_case = CriarViagemUseCase(repo)
        dto = SolicitarViagemInput(
            servidor_id=payload.servidor_id,
            dota_id=payload.dota_id,
            motivo=payload.motivo,
            cargo_ocupado=payload.cargo_ocupado,
            unidade_origem_id=payload.unidade_origem_id,
            unidade_destino_id=payload.unidade_destino_id,
            data_inicio=payload.data_inicio,
            data_fim=payload.data_fim,
            destino=payload.destino,
            is_antecipacao=payload.is_antecipacao,
            autor_id="",
        )
        viagem = use_case.execute(dto)
        return _viagem_to_response(viagem)
    except Exception as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.post(
    "/viagens/{viagem_id}/tramitar",
    response_model=ViagemResponse,
    summary="Tramita uma viagem entre unidades",
)
def tramitar_viagem(
    viagem_id: str,
    payload: ViagemCreateRequest,
    repo: Annotated[RepositorioViagem, Depends(get_viagem_repository)],
) -> ViagemResponse:
    """Tramita uma viagem entre unidades."""
    try:
        use_case = TramitarViagemUseCase(repo)
        dto = SolicitarViagemInput(
            viagem_id=viagem_id,
            unidade_origem_id=payload.unidade_origem_id,
            unidade_destino_id=payload.unidade_destino_id,
            autor_id="",
        )
        viagem = use_case.execute(dto)
        return _viagem_to_response(viagem)
    except Exception as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.post(
    "/viagens/{viagem_id}/visitar",
    response_model=ViagemResponse,
    summary="Visita uma viagem (registra chegada)",
)
def visitar_viagem(
    viagem_id: str,
    payload: ViagemCreateRequest,
    repo: Annotated[RepositorioViagem, Depends(get_viagem_repository)],
) -> ViagemResponse:
    """Visita uma viagem (registra chegada)."""
    try:
        use_case = VisitarViagemUseCase(repo)
        dto = SolicitarViagemInput(
            viagem_id=viagem_id,
            data_visita=payload.data_inicio,
            visitante_id=payload.servidor_id,
            observacoes=payload.motivo,
            autor_id="",
        )
        viagem = use_case.execute(dto)
        return _viagem_to_response(viagem)
    except Exception as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get(
    "/viagens/{viagem_id}",
    response_model=ViagemResponse,
    summary="Busca uma viagem por ID",
    responses={404: {"model": None}},
)
def buscar_viagem(
    viagem_id: str,
    repo: Annotated[RepositorioViagem, Depends(get_viagem_repository)],
) -> ViagemResponse:
    """Busca uma viagem por ID."""
    viagem = repo.get_by_id(viagem_id)
    if not viagem:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Viagem não encontrada")
    return _viagem_to_response(viagem)


@router.get(
    "/viagens/servidor/{servidor_id}",
    response_model=list[ViagemResponse],
    summary="Lista viagens de um servidor",
)
def viagens_do_servidor(
    servidor_id: str,
    repo: Annotated[RepositorioViagem, Depends(get_viagem_repository)],
) -> list[ViagemResponse]:
    """Lista viagens de um servidor."""
    viagens = repo.find_by_servidor(servidor_id)
    return [_viagem_to_response(v) for v in viagens]


# =============================================================================
# Endpoints de Diária
# =============================================================================


@router.post(
    "/diarias",
    response_model=DiariaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Solicita uma nova diária",
    responses={409: {"model": None}},
)
def solicitar_diaria(
    payload: DiariaCreateRequest,
    repo_diaria: Annotated[RepositorioDiaria, Depends(get_diaria_repository)],
    repo_viagem: Annotated[RepositorioViagem, Depends(get_viagem_repository)],
) -> DiariaResponse:
    """Solicita uma nova diária."""
    try:
        use_case = CriarDiariaUseCase(repo_diaria, repo_viagem)
        dto = SolicitacaoDiariaInput(
            servidor_id=payload.servidor_id,
            dota_id=payload.dota_id,
            viagem_id=payload.viagem_id,
            categoria=payload.categoria,
            descricao=payload.descricao,
            data_inicio=payload.data_inicio,
            data_fim=payload.data_fim,
            valor_diaria=payload.valor_diaria,
            autor_id="",
        )
        diaria = use_case.execute(dto)
        return _diaria_to_response(diaria)
    except Exception as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.post(
    "/diarias/{diaria_id}/autorizar",
    response_model=DiariaResponse,
    summary="Autoriza uma diária (RN-DIA-004)",
)
def autorizar_diaria(
    diaria_id: str,
    repo: Annotated[RepositorioDiaria, Depends(get_diaria_repository)],
) -> DiariaResponse:
    """Autoriza uma diária (RN-DIA-004)."""
    try:
        use_case = AutorizarDiariaUseCase(repo)
        diaria = use_case.execute(diaria_id, "")
        return _diaria_to_response(diaria)
    except Exception as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.post(
    "/diarias/{diaria_id}/calcular",
    response_model=DiariaResponse,
    summary="Calcula o valor da diária (RN-DIA-005)",
)
def calcular_diaria(
    diaria_id: str,
    repo: Annotated[RepositorioDiaria, Depends(get_diaria_repository)],
) -> DiariaResponse:
    """Calcula o valor da diária (RN-DIA-005)."""
    try:
        use_case = CalcularDiariaUseCase(repo)
        diaria = use_case.execute(diaria_id)
        return _diaria_to_response(diaria)
    except Exception as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.post(
    "/diarias/{diaria_id}/conceder",
    response_model=DiariaResponse,
    summary="Confirma concessão da diária (RN-DIA-006)",
)
def conceder_diaria(
    diaria_id: str,
    payload: DiariaCreateRequest,
    repo: Annotated[RepositorioDiaria, Depends(get_diaria_repository)],
) -> DiariaResponse:
    """Confirma concessão da diária (RN-DIA-006)."""
    try:
        use_case = ConfirmarConcessaoUseCase(repo)
        diaria = use_case.execute(diaria_id, payload.data_inicio, payload.data_fim)
        return _diaria_to_response(diaria)
    except Exception as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.post(
    "/diarias/{diaria_id}/iniciar-prestacao",
    response_model=DiariaResponse,
    summary="Inicia a prestação de contas (RN-DIA-007)",
)
def iniciar_prestacao(
    diaria_id: str,
    repo: Annotated[RepositorioDiaria, Depends(get_diaria_repository)],
) -> DiariaResponse:
    """Inicia a prestação de contas (RN-DIA-007)."""
    try:
        use_case = IniciarPrestacaoUseCase(repo)
        diaria = use_case.execute(diaria_id)
        return _diaria_to_response(diaria)
    except Exception as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.post(
    "/diarias/{diaria_id}/pagar",
    response_model=DiariaResponse,
    summary="Registra pagamento da diária (RN-DIA-008)",
)
def pagar_diaria(
    diaria_id: str,
    repo: Annotated[RepositorioDiaria, Depends(get_diaria_repository)],
) -> DiariaResponse:
    """Registra pagamento da diária (RN-DIA-008)."""
    try:
        use_case = ReverterParaPagamentoUseCase(repo)
        diaria = use_case.execute(diaria_id)
        return _diaria_to_response(diaria)
    except Exception as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get(
    "/diarias/{diaria_id}",
    response_model=DiariaResponse,
    summary="Busca uma diária por ID",
    responses={404: {"model": None}},
)
def buscar_diaria(
    diaria_id: str,
    repo: Annotated[RepositorioDiaria, Depends(get_diaria_repository)],
) -> DiariaResponse:
    """Busca uma diária por ID."""
    diaria = repo.get_by_id(diaria_id)
    if not diaria:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Diária não encontrada")
    return _diaria_to_response(diaria)


@router.get(
    "/diarias/servidor/{servidor_id}",
    response_model=list[DiariaResponse],
    summary="Lista diárias de um servidor",
)
def diarias_do_servidor(
    servidor_id: str,
    repo: Annotated[RepositorioDiaria, Depends(get_diaria_repository)],
) -> list[DiariaResponse]:
    """Lista diárias de um servidor."""
    diarias = repo.find_by_servidor(servidor_id)
    return [_diaria_to_response(d) for d in diarias]


@router.get(
    "/diarias/status/{status}",
    response_model=list[DiariaResponse],
    summary="Lista diárias por status",
)
def diarias_por_status(
    status: str,
    repo: Annotated[RepositorioDiaria, Depends(get_diaria_repository)],
) -> list[DiariaResponse]:
    """Lista diárias por status."""
    diarias = repo.find_by_status(status)
    return [_diaria_to_response(d) for d in diarias]


# =============================================================================
# Endpoints de Prestação de Contas
# =============================================================================


@router.post(
    "/prestacoes",
    response_model=PrestacaoContasResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Abre uma prestação de contas",
)
def abrir_prestacao(
    payload: PrestacaoContasCreateRequest,
    repo_prestacao: Annotated[RepositorioPrestacaoContas, Depends(get_prestacao_repository)],
    repo_diaria: Annotated[RepositorioDiaria, Depends(get_diaria_repository)],
) -> PrestacaoContasResponse:
    """Abre uma prestação de contas."""
    try:
        use_case = CriarPrestacaoContasUseCase(repo_prestacao, repo_diaria)
        dto = CriarPrestacaoContasInputDTO(
            diaria_id=payload.diaria_id,
            servidor_id=payload.servidor_id,
            dota_id=payload.dota_id,
            documento_id=payload.documento_id,
            valor_previsto=payload.valor_previsto,
            valor_apresentado=payload.valor_apresentado,
            data_vencimento=payload.data_vencimento,
            autor_id="",
        )
        prestacao = use_case.execute(dto)
        return _prestacao_to_response(prestacao)
    except Exception as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.post(
    "/prestacoes/{prestacao_id}/aprovar",
    response_model=PrestacaoContasResponse,
    summary="Aprova uma prestação de contas (RN-DIA-011)",
)
def aprovar_prestacao(
    prestacao_id: str,
    repo_prestacao: Annotated[RepositorioPrestacaoContas, Depends(get_prestacao_repository)],
    repo_diaria: Annotated[RepositorioDiaria, Depends(get_diaria_repository)],
) -> PrestacaoContasResponse:
    """Aprova uma prestação de contas (RN-DIA-011)."""
    try:
        use_case = AprovarPrestacaoUseCase(repo_diaria, repo_prestacao)
        # Buscar a diaria_id a partir da prestacao_id
        prestacao = repo_prestacao.get_by_id(prestacao_id)
        if not prestacao:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Prestação não encontrada")
        dto = AprovacaoPrestacaoInputDTO(
            diaria_id=prestacao.diaria_id,
            autor_id="",
        )
        prestacao = use_case.execute(dto)
        return _prestacao_to_response(prestacao)
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.post(
    "/prestacoes/{prestacao_id}/glosar",
    response_model=PrestacaoContasResponse,
    summary="Glosa uma prestação de contas (RN-DIA-012)",
)
def glosar_prestacao(
    prestacao_id: str,
    motivo: str,
    valor_glosado: float,
    repo_prestacao: Annotated[RepositorioPrestacaoContas, Depends(get_prestacao_repository)],
    repo_diaria: Annotated[RepositorioDiaria, Depends(get_diaria_repository)],
) -> PrestacaoContasResponse:
    """Glosa uma prestação de contas (RN-DIA-012)."""
    try:
        use_case = GlosarPrestacaoUseCase(repo_diaria, repo_prestacao)
        # Buscar a diaria_id a partir da prestacao_id
        prestacao = repo_prestacao.get_by_id(prestacao_id)
        if not prestacao:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Prestação não encontrada")
        dto = GlosagemPrestacaoInputDTO(
            diaria_id=prestacao.diaria_id,
            motivo=motivo,
            valor_glosado=valor_glosado,
            autor_id="",
        )
        prestacao = use_case.execute(dto)
        return _prestacao_to_response(prestacao)
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get(
    "/prestacoes/{prestacao_id}",
    response_model=PrestacaoContasResponse,
    summary="Busca uma prestação por ID",
    responses={404: {"model": None}},
)
def buscar_prestacao(
    prestacao_id: str,
    repo: Annotated[RepositorioPrestacaoContas, Depends(get_prestacao_repository)],
) -> PrestacaoContasResponse:
    """Busca uma prestação por ID."""
    prestacao = repo.get_by_id(prestacao_id)
    if not prestacao:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Prestação não encontrada")
    return _prestacao_to_response(prestacao)



@router.post(
    "/prestacoes/{prestacao_id}/restituir",
    response_model=PrestacaoContasResponse,
    summary="Restitui valor glosado de uma prestação (RN-DIA-013)",
)
def restituir_prestacao(
    prestacao_id: str,
    repo_prestacao: Annotated[RepositorioPrestacaoContas, Depends(get_prestacao_repository)],
    repo_diaria: Annotated[RepositorioDiaria, Depends(get_diaria_repository)],
) -> PrestacaoContasResponse:
    """Restitui o valor glosado de uma prestação de contas (RN-DIA-013)."""
    try:
        use_case = RestituirPrestacaoUseCase(repo_diaria, repo_prestacao)
        # Buscar a diaria_id a partir da prestacao_id
        prestacao = repo_prestacao.get_by_id(prestacao_id)
        if not prestacao:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Prestação não encontrada")
        dto = RestituicaPrestacaoInputDTO(
            diaria_id=prestacao.diaria_id,
            autor_id="",
        )
        prestacao = use_case.execute(dto)
        return _prestacao_to_response(prestacao)
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get(
    "/prestacoes/abertas",
    response_model=list[PrestacaoContasResponse],
    summary="Lista prestações abertas",
)
def prestacoes_abertas(
    repo: Annotated[RepositorioPrestacaoContas, Depends(get_prestacao_repository)],
) -> list[PrestacaoContasResponse]:
    """Lista prestações abertas."""
    prestacoes = repo.find_authors()
    return [_prestacao_to_response(p) for p in prestacoes]


# =============================================================================
# Helper functions
# =============================================================================


def _viagem_to_response(viagem) -> ViagemResponse:
    """Converte Viagem para ViagemResponse."""
    return ViagemResponse(
        id=viagem.id,
        servidor_id=viagem.servidor_id,
        dota_id=viagem.dota_id,
        motivo=viagem.motivo,
        cargo_ocupado=viagem.cargo_ocupado,
        unidade_origem_id=viagem.unidade_origem_id,
        unidade_destino_id=viagem.unidade_destino_id,
        data_inicio=viagem.data_inicio,
        data_fim=viagem.data_fim,
        destino=viagem.destino,
        is_antecipacao=viagem.is_antecipacao,
        created_at=viagem.created_at,
        updated_at=viagem.updated_at,
        created_by=viagem.created_by,
        is_deleted=viagem.is_deleted,
    )


def _diaria_to_response(diaria) -> DiariaResponse:
    """Converte Diaria para DiariaResponse."""
    return DiariaResponse(
        id=diaria.id,
        viagem_id=diaria.viagem_id,
        servidor_id=diaria.servidor_id,
        dota_id=diaria.dota_id,
        categoria=diaria.categoria.value,
        descricao=diaria.descricao,
        data_inicio=diaria.data_inicio,
        data_fim=diaria.data_fim,
        valor_diaria=diaria.valor_diaria,
        valor_total=diaria.valor_total,
        status=diaria.status.value,
        data_solicitacao=diaria.data_solicitacao,
        data_autorizacao=diaria.data_autorizacao,
        data_calculo=diaria.data_calculo,
        data_concessao=diaria.data_concessao,
        data_inicio_prestacao=diaria.data_inicio_prestacao,
        data_fim_prestacao=diaria.data_fim_prestacao,
        data_pagamento=diaria.data_pagamento,
        data_aprovacao=diaria.data_aprovacao,
        data_glosa=diaria.data_glosa,
        data_restituicao=diaria.data_restituicao,
        data_cancelamento=diaria.data_cancelamento,
        motivo_cancelamento=diaria.motivo_cancelamento,
        motivo_glosa=diaria.motivo_glosa,
        valor_glosado=diaria.valor_glosado,
        documento_prestacao_id=diaria.documento_prestacao_id,
        created_at=diaria.created_at,
        updated_at=diaria.updated_at,
        created_by=diaria.created_by,
        updated_by=diaria.updated_by,
        is_deleted=diaria.is_deleted,
    )


def _prestacao_to_response(prestacao) -> PrestacaoContasResponse:
    """Converte PrestacaoContas para PrestacaoContasResponse."""
    return PrestacaoContasResponse(
        id=prestacao.id,
        diaria_id=prestacao.diaria_id,
        servidor_id=prestacao.servidor_id,
        dota_id=prestacao.dota_id,
        data_emissao=prestacao.data_emissao,
        data_vencimento=prestacao.data_vencimento,
        documento_id=prestacao.documento_id,
        valor_previsto=prestacao.valor_previsto,
        valor_apresentado=prestacao.valor_apresentado,
        valor_glosado=prestacao.valor_glosado,
        valor_liquido=prestacao.valor_liquido,
        status=prestacao.status,
        motivo_glosa=prestacao.motivo_glosa,
        created_at=prestacao.created_at,
        updated_at=prestacao.updated_at,
        created_by=prestacao.created_by,
        is_deleted=prestacao.is_deleted,
    )
