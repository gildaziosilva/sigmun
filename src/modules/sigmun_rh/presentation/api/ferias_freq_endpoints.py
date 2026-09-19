"""Endpoints de ferias/frequencia (DOM-PES)."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from pydantic import BaseModel, Field

from src.modules.sigmun_rh.application.interfaces import (
    RepositorioFerias,
    RepositorioFrequencia,
    RepositorioServidor,
)
from src.modules.sigmun_rh.application.use_cases_ferias import (
    AprovarFeriasUseCase,
    ConcluirFeriasUseCase,
    IniciarGozoFeriasUseCase,
    PlanejarFeriasInput,
    PlanejarFeriasUseCase,
)
from src.modules.sigmun_rh.application.use_cases_frequencia import (
    JustificarFaltaInput,
    JustificarFaltaUseCase,
    RegistrarFrequenciaInput,
    RegistrarFrequenciaUseCase,
)
from src.modules.sigmun_rh.domain.exceptions import DomPesDomainError
from src.modules.sigmun_rh.presentation.schemas.pes_operacionais_schemas import (
    FeriasCreateRequest,
    FeriasResponse,
    FrequenciaCreateRequest,
    FrequenciaResponse,
)

from .operacional import get_ferias_repo, get_freq_repo, get_serv_repo

router = APIRouter(prefix="/api/v1/pes", tags=["Gestao de Pessoas"])


def _ferias_to_response(ferias) -> FeriasResponse:
    return FeriasResponse(
        id=ferias.id, servidor_id=ferias.servidor_id,
        data_inicio_gozo=ferias.data_inicio_gozo,
        data_fim_gozo=ferias.data_fim_gozo, dias=ferias.dias,
        parcela=ferias.parcela, status=ferias.status.value,
        created_at=ferias.created_at,
    )


def _freq_to_response(freq) -> FrequenciaResponse:
    return FrequenciaResponse(
        id=freq.id, servidor_id=freq.servidor_id, data=freq.data,
        tipo=freq.tipo.value, minutos_atraso=freq.minutos_atraso,
        desconto_folha=freq.desconto_folha, created_at=freq.created_at,
    )


@router.post("/ferias", status_code=201)
def planejar_ferias(
    payload: FeriasCreateRequest,
    repo: Annotated[RepositorioFerias, Depends(get_ferias_repo)],
    servidores: Annotated[RepositorioServidor, Depends(get_serv_repo)],
):
    """Planeja ferias."""
    try:
        ferias = PlanejarFeriasUseCase(repo, servidores).execute(
            PlanejarFeriasInput(
                servidor_id=payload.servidor_id,
                periodo_aquisitivo_inicio=payload.periodo_aquisitivo_inicio,
                periodo_aquisitivo_fim=payload.periodo_aquisitivo_fim,
                data_inicio_gozo=payload.data_inicio_gozo,
                data_fim_gozo=payload.data_fim_gozo,
                dias=payload.dias, parcela=payload.parcela,
                autor_id=payload.created_by,
            )
        )
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _ferias_to_response(ferias)


@router.post("/ferias/{ferias_id}/aprovar")
def aprovar_ferias(
    ferias_id: str, repo: Annotated[RepositorioFerias, Depends(get_ferias_repo)]
):
    """Aprova ferias."""
    try:
        ferias = AprovarFeriasUseCase(repo).execute(ferias_id)
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _ferias_to_response(ferias)


@router.post("/ferias/{ferias_id}/concluir")
def concluir_ferias(
    ferias_id: str, repo: Annotated[RepositorioFerias, Depends(get_ferias_repo)]
):
    """Conclui ferias em gozo."""
    try:
        ferias = ConcluirFeriasUseCase(repo).execute(ferias_id)
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _ferias_to_response(ferias)


@router.post("/frequencias", status_code=201)
def registrar_frequencia(
    payload: FrequenciaCreateRequest,
    repo: Annotated[RepositorioFrequencia, Depends(get_freq_repo)],
    servidores: Annotated[RepositorioServidor, Depends(get_serv_repo)],
):
    """Registra frequencia."""
    try:
        freq = RegistrarFrequenciaUseCase(repo, servidores).execute(
            RegistrarFrequenciaInput(
                servidor_id=payload.servidor_id, data=payload.data,
                tipo=payload.tipo, hora_entrada=payload.hora_entrada,
                hora_saida=payload.hora_saida,
                minutos_atraso=payload.minutos_atraso,
                autor_id=payload.created_by,
            )
        )
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _freq_to_response(freq)

class JustificativaRequest(BaseModel):
    """Payload de justificativa de falta."""

    justificativa: str = Field(..., min_length=3)


@router.post("/ferias/{ferias_id}/iniciar-gozo")
def iniciar_gozo(
    ferias_id: str, repo: Annotated[RepositorioFerias, Depends(get_ferias_repo)]
):
    """Inicia gozo de ferias aprovadas."""
    try:
        ferias = IniciarGozoFeriasUseCase(repo).execute(ferias_id)
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _ferias_to_response(ferias)


@router.post("/frequencias/{frequencia_id}/justificar")
def justificar_falta(
    frequencia_id: str,
    payload: JustificativaRequest,
    repo: Annotated[RepositorioFrequencia, Depends(get_freq_repo)],
):
    """Justifica falta registrada."""
    try:
        freq = JustificarFaltaUseCase(repo).execute(
            JustificarFaltaInput(
                frequencia_id=frequencia_id,
                justificativa=payload.justificativa,
            )
        )
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _freq_to_response(freq)


__all__ = ["router"]

__all__ = ["router"]
