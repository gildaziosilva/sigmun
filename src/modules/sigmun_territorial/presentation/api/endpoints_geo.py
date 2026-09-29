"""Endpoints do DOM-TEL — georreferenciamento territorial (prefixo /api/v1/tel)."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, Query, status

from ...application.interfaces import (
    RepositorioBairro,
    RepositorioGeorreferencia,
    RepositorioLogradouro,
)
from ...application.use_cases import (
    ExcluirGeorreferenciaUseCase,
    RegistrarGeorreferenciaInput,
    RegistrarGeorreferenciaUseCase,
)
from ...domain.entities import Georreferencia
from ...domain.exceptions import (
    BairroNaoEncontradoError,
    DomTelDomainError,
    GeorreferenciaNaoEncontradaError,
    LogradouroNaoEncontradoError,
)
from ..schemas import (
    GeorreferenciaCreateRequest,
    GeorreferenciaResponse,
    VerticeGeometria,
)
from .deps import (
    get_bairro_repo,
    get_georreferencia_repo,
    get_logradouro_repo,
    obter,
)
from .router import router


def to_georreferencia(g: Georreferencia) -> GeorreferenciaResponse:
    """Converte a entidade de georreferência na resposta da API."""
    return GeorreferenciaResponse(
        id=g.id,
        bairro_id=g.bairro_id,
        logradouro_id=g.logradouro_id,
        geometria=g.geometria.value,
        latitude=g.latitude,
        longitude=g.longitude,
        altitude_m=g.altitude_m,
        vertices=[VerticeGeometria(**v) for v in g.vertices],
        datum=g.datum.value,
        precisao_m=g.precisao_m,
        data_levantamento=g.data_levantamento,
        created_at=g.created_at,
    )


@router.post("/georreferencias", status_code=201)
def registrar_georreferencia(
    payload: GeorreferenciaCreateRequest,
    repo: Annotated[RepositorioGeorreferencia, Depends(get_georreferencia_repo)],
    bairros: Annotated[RepositorioBairro, Depends(get_bairro_repo)],
    logradouros: Annotated[RepositorioLogradouro, Depends(get_logradouro_repo)],
) -> GeorreferenciaResponse:
    try:
        georreferencia = RegistrarGeorreferenciaUseCase(repo, bairros, logradouros).execute(
            RegistrarGeorreferenciaInput(
                bairro_id=payload.bairro_id,
                logradouro_id=payload.logradouro_id,
                geometria=payload.geometria,
                latitude=payload.latitude,
                longitude=payload.longitude,
                altitude_m=payload.altitude_m,
                vertices=[v.model_dump() for v in payload.vertices],
                datum=payload.datum,
                precisao_m=payload.precisao_m,
                data_levantamento=payload.data_levantamento,
                autor_id=payload.created_by,
            )
        )
    except (BairroNaoEncontradoError, LogradouroNaoEncontradoError) as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomTelDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_georreferencia(georreferencia)


@router.get("/georreferencias")
def listar_georreferencias(
    repo: Annotated[RepositorioGeorreferencia, Depends(get_georreferencia_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> list[GeorreferenciaResponse]:
    return [to_georreferencia(g) for g in repo.list_all(page=page, page_size=page_size)]


@router.get("/georreferencias/referencia")
def listar_georreferencias_por_referencia(
    repo: Annotated[RepositorioGeorreferencia, Depends(get_georreferencia_repo)],
    bairro_id: str | None = None,
    logradouro_id: str | None = None,
) -> list[GeorreferenciaResponse]:
    if not bairro_id and not logradouro_id:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            "Informe bairro_id ou logradouro_id para filtrar as georreferências",
        )
    return [
        to_georreferencia(g)
        for g in repo.list_by_referencia(bairro_id=bairro_id, logradouro_id=logradouro_id)
    ]


@router.get("/georreferencias/{georreferencia_id}")
def obter_georreferencia(
    georreferencia_id: str,
    repo: Annotated[RepositorioGeorreferencia, Depends(get_georreferencia_repo)],
) -> GeorreferenciaResponse:
    georreferencia = obter(repo, georreferencia_id)
    if georreferencia is None:
        raise HTTPException(404, "Georreferência não encontrada")
    return to_georreferencia(georreferencia)


@router.delete("/georreferencias/{georreferencia_id}")
def excluir_georreferencia(
    georreferencia_id: str,
    repo: Annotated[RepositorioGeorreferencia, Depends(get_georreferencia_repo)],
) -> GeorreferenciaResponse:
    try:
        georreferencia = ExcluirGeorreferenciaUseCase(repo).execute(georreferencia_id)
    except GeorreferenciaNaoEncontradaError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomTelDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_georreferencia(georreferencia)
