"""Endpoints do DOM-GEO — elementos geoespaciais e serviços (prefixo /api/v1/geo)."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, Query, status

from ...application.interfaces import (
    RepositorioCamadaMapa,
    RepositorioFeatureGeo,
    RepositorioServicoGeo,
)
from ...application.use_cases import (
    AtualizarServicoInput,
    AtualizarServicoUseCase,
    CadastrarServicoInput,
    CadastrarServicoUseCase,
    ExcluirFeatureUseCase,
    ExcluirServicoUseCase,
    InativarServicoUseCase,
    RegistrarFeatureInput,
    RegistrarFeatureUseCase,
)
from ...domain.exceptions import DomGeoDomainError
from ..schemas import (
    FeatureCreateRequest,
    FeatureResponse,
    ServicoCreateRequest,
    ServicoResponse,
    ServicoUpdateRequest,
)
from .deps import (
    get_camada_repo,
    get_feature_repo,
    get_servico_repo,
    obter,
    to_feature,
    to_servico,
)
from .router import router


@router.post("/features", status_code=201)
def registrar_feature(
    payload: FeatureCreateRequest,
    repo: Annotated[RepositorioFeatureGeo, Depends(get_feature_repo)],
    camadas: Annotated[RepositorioCamadaMapa, Depends(get_camada_repo)],
) -> FeatureResponse:
    try:
        feature = RegistrarFeatureUseCase(repo, camadas).execute(
            RegistrarFeatureInput(
                codigo=payload.codigo,
                nome=payload.nome,
                descricao=payload.descricao,
                camada_id=payload.camada_id,
                geometria=payload.geometria,
                latitude=payload.latitude,
                longitude=payload.longitude,
                vertices=[v.model_dump() for v in payload.vertices],
                datum=payload.datum,
                atributos=payload.atributos,
                autor_id=payload.created_by,
            )
        )
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_feature(feature)


@router.get("/features")
def listar_features(
    repo: Annotated[RepositorioFeatureGeo, Depends(get_feature_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> list[FeatureResponse]:
    return [to_feature(f) for f in repo.list_all(page=page, page_size=page_size)]


@router.get("/features/camada/{camada_id}")
def listar_features_por_camada(
    camada_id: str,
    repo: Annotated[RepositorioFeatureGeo, Depends(get_feature_repo)],
) -> list[FeatureResponse]:
    """Lista os elementos geoespaciais de uma camada (RN-GEO-008)."""
    return [to_feature(f) for f in repo.list_by_camada(camada_id)]


@router.get("/features/{feature_id}")
def obter_feature(
    feature_id: str,
    repo: Annotated[RepositorioFeatureGeo, Depends(get_feature_repo)],
) -> FeatureResponse:
    feature = obter(repo, feature_id)
    if feature is None:
        raise HTTPException(404, "Elemento geoespacial não encontrado")
    return to_feature(feature)


@router.delete("/features/{feature_id}")
def excluir_feature(
    feature_id: str,
    repo: Annotated[RepositorioFeatureGeo, Depends(get_feature_repo)],
) -> FeatureResponse:
    try:
        return to_feature(ExcluirFeatureUseCase(repo).execute(feature_id))
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/servicos", status_code=201)
def cadastrar_servico(
    payload: ServicoCreateRequest,
    repo: Annotated[RepositorioServicoGeo, Depends(get_servico_repo)],
) -> ServicoResponse:
    try:
        servico = CadastrarServicoUseCase(repo).execute(
            CadastrarServicoInput(
                codigo=payload.codigo,
                nome=payload.nome,
                descricao=payload.descricao,
                tipo=payload.tipo,
                url=payload.url,
                camada=payload.camada,
                datum=payload.datum,
                srid=payload.srid,
                zoom_minimo=payload.zoom_minimo,
                zoom_maximo=payload.zoom_maximo,
                publico=payload.publico,
                autor_id=payload.created_by,
            )
        )
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_servico(servico)


@router.get("/servicos")
def listar_servicos(
    repo: Annotated[RepositorioServicoGeo, Depends(get_servico_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    tipo: str | None = None,
) -> list[ServicoResponse]:
    return [to_servico(s) for s in repo.list_all(page=page, page_size=page_size, tipo=tipo)]


@router.get("/servicos/{servico_id}")
def obter_servico(
    servico_id: str,
    repo: Annotated[RepositorioServicoGeo, Depends(get_servico_repo)],
) -> ServicoResponse:
    servico = obter(repo, servico_id)
    if servico is None:
        raise HTTPException(404, "Serviço geoespacial não encontrado")
    return to_servico(servico)


@router.patch("/servicos/{servico_id}")
def atualizar_servico(
    servico_id: str,
    payload: ServicoUpdateRequest,
    repo: Annotated[RepositorioServicoGeo, Depends(get_servico_repo)],
) -> ServicoResponse:
    try:
        servico = AtualizarServicoUseCase(repo).execute(
            AtualizarServicoInput(
                servico_id=servico_id,
                codigo=payload.codigo,
                nome=payload.nome,
                descricao=payload.descricao,
                tipo=payload.tipo,
                url=payload.url,
                camada=payload.camada,
                datum=payload.datum,
                srid=payload.srid,
                zoom_minimo=payload.zoom_minimo,
                zoom_maximo=payload.zoom_maximo,
                publico=payload.publico,
                autor_id=payload.created_by,
            )
        )
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_servico(servico)


@router.post("/servicos/{servico_id}/inativar")
def inativar_servico(
    servico_id: str,
    repo: Annotated[RepositorioServicoGeo, Depends(get_servico_repo)],
    created_by: str = "",
) -> ServicoResponse:
    try:
        return to_servico(InativarServicoUseCase(repo).execute(servico_id, created_by))
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.delete("/servicos/{servico_id}")
def excluir_servico(
    servico_id: str,
    repo: Annotated[RepositorioServicoGeo, Depends(get_servico_repo)],
) -> ServicoResponse:
    try:
        return to_servico(ExcluirServicoUseCase(repo).execute(servico_id))
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
