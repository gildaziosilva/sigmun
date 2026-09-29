"""Endpoints do DOM-IMO — avaliações, características e geometria do lote."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, Query, status

from ...application.interfaces import (
    RepositorioAvaliacao,
    RepositorioCaracteristica,
    RepositorioGeometria,
    RepositorioImovel,
)
from ...application.use_cases import (
    AvaliarImovelInput,
    AvaliarImovelUseCase,
    CancelarAvaliacaoUseCase,
    ConcluirAvaliacaoUseCase,
    RegistrarCaracteristicaInput,
    RegistrarCaracteristicaUseCase,
    RegistrarGeometriaInput,
    RegistrarGeometriaUseCase,
)
from ...domain.exceptions import (
    AvaliacaoNaoEncontradaError,
    DomImoDomainError,
    ImovelNaoEncontradoError,
)
from ..schemas import (
    AvaliacaoCancelarRequest,
    AvaliacaoCreateRequest,
    AvaliacaoResponse,
    CaracteristicaCreateRequest,
    CaracteristicaResponse,
    GeometriaCreateRequest,
    GeometriaResponse,
)
from .deps import (
    get_avaliacao_repo,
    get_caracteristica_repo,
    get_geometria_repo,
    get_imovel_repo,
    obter,
    to_avaliacao,
    to_caracteristica,
    to_geometria,
)
from .router import router


@router.post("/avaliacoes", status_code=201)
def avaliar_imovel(
    payload: AvaliacaoCreateRequest,
    repo: Annotated[RepositorioAvaliacao, Depends(get_avaliacao_repo)],
    imoveis: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
) -> AvaliacaoResponse:
    try:
        avaliacao = AvaliarImovelUseCase(repo, imoveis).execute(
            AvaliarImovelInput(
                imovel_id=payload.imovel_id,
                ano=payload.ano,
                valor_terreno_m2_unitario=payload.valor_terreno_m2_unitario,
                valor_construcao_m2_unitario=payload.valor_construcao_m2_unitario,
                aliquota_percent=payload.aliquota_percent,
                data_avaliacao=payload.data_avaliacao,
                concluir=payload.concluir,
                autor_id=payload.created_by,
            )
        )
    except ImovelNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomImoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_avaliacao(avaliacao)


@router.get("/avaliacoes")
def listar_avaliacoes(
    repo: Annotated[RepositorioAvaliacao, Depends(get_avaliacao_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> list[AvaliacaoResponse]:
    return [to_avaliacao(a) for a in repo.list_all(page=page, page_size=page_size)]


@router.get("/avaliacoes/imovel/{imovel_id}")
def listar_avaliacoes_do_imovel(
    imovel_id: str,
    imoveis: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
    repo: Annotated[RepositorioAvaliacao, Depends(get_avaliacao_repo)],
) -> list[AvaliacaoResponse]:
    if obter(imoveis, imovel_id) is None:
        raise HTTPException(404, "Imóvel não encontrado")
    return [to_avaliacao(a) for a in repo.list_by_imovel(imovel_id)]


@router.get("/avaliacoes/{avaliacao_id}")
def obter_avaliacao(
    avaliacao_id: str, repo: Annotated[RepositorioAvaliacao, Depends(get_avaliacao_repo)]
) -> AvaliacaoResponse:
    avaliacao = obter(repo, avaliacao_id)
    if avaliacao is None:
        raise HTTPException(404, "Avaliação não encontrada")
    return to_avaliacao(avaliacao)


@router.post("/avaliacoes/{avaliacao_id}/concluir")
def concluir_avaliacao(
    avaliacao_id: str, repo: Annotated[RepositorioAvaliacao, Depends(get_avaliacao_repo)]
) -> AvaliacaoResponse:
    try:
        return to_avaliacao(ConcluirAvaliacaoUseCase(repo).execute(avaliacao_id))
    except AvaliacaoNaoEncontradaError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomImoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/avaliacoes/{avaliacao_id}/cancelar")
def cancelar_avaliacao(
    avaliacao_id: str,
    payload: AvaliacaoCancelarRequest,
    repo: Annotated[RepositorioAvaliacao, Depends(get_avaliacao_repo)],
) -> AvaliacaoResponse:
    try:
        return to_avaliacao(CancelarAvaliacaoUseCase(repo).execute(avaliacao_id, payload.motivo))
    except AvaliacaoNaoEncontradaError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomImoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/caracteristicas", status_code=201)
def registrar_caracteristica(
    payload: CaracteristicaCreateRequest,
    repo: Annotated[RepositorioCaracteristica, Depends(get_caracteristica_repo)],
    imoveis: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
) -> CaracteristicaResponse:
    try:
        caracteristica = RegistrarCaracteristicaUseCase(repo, imoveis).execute(
            RegistrarCaracteristicaInput(
                imovel_id=payload.imovel_id,
                obra=payload.obra,
                numero_pavimentos=payload.numero_pavimentos,
                ano_renovacao=payload.ano_renovacao,
                observacao=payload.observacao,
                autor_id=payload.created_by,
            )
        )
    except ImovelNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomImoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_caracteristica(caracteristica)


@router.get("/caracteristicas/imovel/{imovel_id}")
def obter_caracteristica_do_imovel(
    imovel_id: str,
    imoveis: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
    repo: Annotated[RepositorioCaracteristica, Depends(get_caracteristica_repo)],
) -> CaracteristicaResponse:
    if obter(imoveis, imovel_id) is None:
        raise HTTPException(404, "Imóvel não encontrado")
    caracteristica = repo.get_by_imovel(imovel_id)
    if caracteristica is None:
        raise HTTPException(404, "Característica construtiva não encontrada")
    return to_caracteristica(caracteristica)


@router.get("/caracteristicas")
def listar_caracteristicas(
    repo: Annotated[RepositorioCaracteristica, Depends(get_caracteristica_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> list[CaracteristicaResponse]:
    return [to_caracteristica(c) for c in repo.list_all(page=page, page_size=page_size)]


@router.post("/geometrias", status_code=201)
def registrar_geometria(
    payload: GeometriaCreateRequest,
    repo: Annotated[RepositorioGeometria, Depends(get_geometria_repo)],
    imoveis: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
) -> GeometriaResponse:
    try:
        geometria = RegistrarGeometriaUseCase(repo, imoveis).execute(
            RegistrarGeometriaInput(
                imovel_id=payload.imovel_id,
                geometria=payload.geometria,
                latitude=payload.latitude,
                longitude=payload.longitude,
                vertices=[v.model_dump() for v in payload.vertices],
                datum=payload.datum,
                precisao_m=payload.precisao_m,
                data_levantamento=payload.data_levantamento,
                autor_id=payload.created_by,
            )
        )
    except ImovelNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomImoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_geometria(geometria)


@router.get("/geometrias")
def listar_geometrias(
    repo: Annotated[RepositorioGeometria, Depends(get_geometria_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> list[GeometriaResponse]:
    return [to_geometria(g) for g in repo.list_all(page=page, page_size=page_size)]


@router.get("/geometrias/imovel/{imovel_id}")
def obter_geometria_do_imovel(
    imovel_id: str,
    imoveis: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
    repo: Annotated[RepositorioGeometria, Depends(get_geometria_repo)],
) -> GeometriaResponse:
    if obter(imoveis, imovel_id) is None:
        raise HTTPException(404, "Imóvel não encontrado")
    geometria = repo.get_by_imovel(imovel_id)
    if geometria is None:
        raise HTTPException(404, "Geometria do lote não encontrada")
    return to_geometria(geometria)

