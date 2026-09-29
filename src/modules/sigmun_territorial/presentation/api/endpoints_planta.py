"""Endpoints do DOM-TEL — planta genérica de valores (prefixo /api/v1/tel)."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, Query, status

from ...application.interfaces import RepositorioBairro, RepositorioPlantaValores
from ...application.use_cases import (
    AtivarPlantaValoresUseCase,
    AtualizarPlantaValoresInput,
    AtualizarPlantaValoresUseCase,
    CadastrarPlantaValoresInput,
    CadastrarPlantaValoresUseCase,
    RevogarPlantaValoresUseCase,
)
from ...domain.entities import PlantaGenericaValores
from ...domain.exceptions import (
    BairroNaoEncontradoError,
    DomTelDomainError,
    PlantaValoresNaoEncontradaError,
)
from ..schemas import (
    PlantaValoresCreateRequest,
    PlantaValoresResponse,
    PlantaValoresRevogarRequest,
    PlantaValoresUpdateRequest,
)
from .deps import get_bairro_repo, get_planta_repo, obter
from .router import router


def to_planta(p: PlantaGenericaValores) -> PlantaValoresResponse:
    """Converte a entidade da planta genérica de valores na resposta da API."""
    return PlantaValoresResponse(
        id=p.id,
        ano=p.ano,
        bairro_id=p.bairro_id,
        ocupacao=p.ocupacao.value,
        valor_terreno_m2=p.valor_terreno_m2,
        valor_construcao_m2=p.valor_construcao_m2,
        aliquota_percent=p.aliquota_percent,
        situacao=p.situacao.value,
        legislacao=p.legislacao,
        created_at=p.created_at,
        updated_at=p.updated_at,
    )


@router.post("/plantas-valores", status_code=201)
def cadastrar_planta_valores(
    payload: PlantaValoresCreateRequest,
    repo: Annotated[RepositorioPlantaValores, Depends(get_planta_repo)],
    bairros: Annotated[RepositorioBairro, Depends(get_bairro_repo)],
) -> PlantaValoresResponse:
    try:
        planta = CadastrarPlantaValoresUseCase(repo, bairros).execute(
            CadastrarPlantaValoresInput(
                ano=payload.ano,
                bairro_id=payload.bairro_id,
                ocupacao=payload.ocupacao,
                valor_terreno_m2=payload.valor_terreno_m2,
                valor_construcao_m2=payload.valor_construcao_m2,
                aliquota_percent=payload.aliquota_percent,
                legislacao=payload.legislacao,
                ativar=payload.ativar,
                autor_id=payload.created_by,
            )
        )
    except BairroNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomTelDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_planta(planta)


@router.get("/plantas-valores")
def listar_plantas_valores(
    repo: Annotated[RepositorioPlantaValores, Depends(get_planta_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    bairro_id: str | None = None,
) -> list[PlantaValoresResponse]:
    return [
        to_planta(p)
        for p in repo.list_all(page=page, page_size=page_size, bairro_id=bairro_id)
    ]


@router.get("/plantas-valores/vigente")
def obter_planta_vigente(
    repo: Annotated[RepositorioPlantaValores, Depends(get_planta_repo)],
    ano: int = Query(..., ge=1900, le=2200),
    bairro_id: str = Query(..., min_length=1),
    ocupacao: str = Query("residencial", min_length=1),
) -> PlantaValoresResponse:
    planta = repo.get_vigente(ano, bairro_id, ocupacao)
    if planta is None:
        raise HTTPException(404, "Nenhuma planta genérica de valores vigente encontrada")
    return to_planta(planta)


@router.get("/plantas-valores/{planta_id}")
def obter_planta_valores(
    planta_id: str, repo: Annotated[RepositorioPlantaValores, Depends(get_planta_repo)]
) -> PlantaValoresResponse:
    planta = obter(repo, planta_id)
    if planta is None:
        raise HTTPException(404, "Planta genérica de valores não encontrada")
    return to_planta(planta)


@router.patch("/plantas-valores/{planta_id}")
def atualizar_planta_valores(
    planta_id: str,
    payload: PlantaValoresUpdateRequest,
    repo: Annotated[RepositorioPlantaValores, Depends(get_planta_repo)],
) -> PlantaValoresResponse:
    try:
        planta = AtualizarPlantaValoresUseCase(repo).execute(
            AtualizarPlantaValoresInput(
                planta_id=planta_id,
                ano=payload.ano,
                valor_terreno_m2=payload.valor_terreno_m2,
                valor_construcao_m2=payload.valor_construcao_m2,
                aliquota_percent=payload.aliquota_percent,
                legislacao=payload.legislacao,
                autor_id=payload.created_by,
            )
        )
    except PlantaValoresNaoEncontradaError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomTelDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_planta(planta)


@router.post("/plantas-valores/{planta_id}/ativar")
def ativar_planta_valores(
    planta_id: str, repo: Annotated[RepositorioPlantaValores, Depends(get_planta_repo)]
) -> PlantaValoresResponse:
    try:
        return to_planta(AtivarPlantaValoresUseCase(repo).execute(planta_id))
    except PlantaValoresNaoEncontradaError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomTelDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/plantas-valores/{planta_id}/revogar")
def revogar_planta_valores(
    planta_id: str,
    payload: PlantaValoresRevogarRequest,
    repo: Annotated[RepositorioPlantaValores, Depends(get_planta_repo)],
) -> PlantaValoresResponse:
    try:
        planta = RevogarPlantaValoresUseCase(repo).execute(planta_id, payload.motivo)
    except PlantaValoresNaoEncontradaError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomTelDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_planta(planta)

