"""Endpoints do DOM-GEO — camadas de mapa e mapas SIG (prefixo /api/v1/geo)."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, Query, status

from ...application.interfaces import (
    RepositorioCamadaMapa,
    RepositorioMapaCamada,
    RepositorioMapaSig,
)
from ...application.use_cases import (
    ArquivarMapaUseCase,
    AtivarCamadaUseCase,
    AtualizarCamadaInput,
    AtualizarCamadaUseCase,
    AtualizarMapaInput,
    AtualizarMapaUseCase,
    CadastrarCamadaInput,
    CadastrarCamadaUseCase,
    CadastrarMapaInput,
    CadastrarMapaUseCase,
    ComporCamadaInput,
    ComporCamadaUseCase,
    DesativarCamadaUseCase,
    ExcluirCamadaUseCase,
    ExcluirMapaUseCase,
    PublicarMapaUseCase,
    RemoverComposicaoUseCase,
)
from ...domain.exceptions import DomGeoDomainError
from ..schemas import (
    CamadaCreateRequest,
    CamadaResponse,
    CamadaUpdateRequest,
    MapaCamadaResponse,
    MapaComposicaoRequest,
    MapaCreateRequest,
    MapaResponse,
    MapaUpdateRequest,
)
from .deps import (
    get_camada_repo,
    get_mapa_repo,
    get_vinculo_repo,
    obter,
    to_camada,
    to_mapa,
    to_vinculo,
)
from .router import router


@router.post("/camadas", status_code=201)
def cadastrar_camada(
    payload: CamadaCreateRequest,
    repo: Annotated[RepositorioCamadaMapa, Depends(get_camada_repo)],
) -> CamadaResponse:
    try:
        camada = CadastrarCamadaUseCase(repo).execute(
            CadastrarCamadaInput(
                codigo=payload.codigo,
                nome=payload.nome,
                descricao=payload.descricao,
                tipo=payload.tipo,
                formato=payload.formato,
                fonte=payload.fonte,
                data_atualizacao=payload.data_atualizacao,
                datum=payload.datum,
                srid=payload.srid,
                url_servico=payload.url_servico,
                zoom_minimo=payload.zoom_minimo,
                zoom_maximo=payload.zoom_maximo,
                ativar=payload.ativar,
                autor_id=payload.created_by,
            )
        )
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_camada(camada)


@router.get("/camadas")
def listar_camadas(
    repo: Annotated[RepositorioCamadaMapa, Depends(get_camada_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    tipo: str | None = None,
) -> list[CamadaResponse]:
    return [to_camada(c) for c in repo.list_all(page=page, page_size=page_size, tipo=tipo)]


@router.get("/camadas/{camada_id}")
def obter_camada(
    camada_id: str,
    repo: Annotated[RepositorioCamadaMapa, Depends(get_camada_repo)],
) -> CamadaResponse:
    camada = obter(repo, camada_id)
    if camada is None:
        raise HTTPException(404, "Camada de mapa não encontrada")
    return to_camada(camada)


@router.patch("/camadas/{camada_id}")
def atualizar_camada(
    camada_id: str,
    payload: CamadaUpdateRequest,
    repo: Annotated[RepositorioCamadaMapa, Depends(get_camada_repo)],
) -> CamadaResponse:
    try:
        camada = AtualizarCamadaUseCase(repo).execute(
            AtualizarCamadaInput(
                camada_id=camada_id,
                codigo=payload.codigo,
                nome=payload.nome,
                descricao=payload.descricao,
                tipo=payload.tipo,
                formato=payload.formato,
                fonte=payload.fonte,
                data_atualizacao=payload.data_atualizacao,
                datum=payload.datum,
                srid=payload.srid,
                url_servico=payload.url_servico,
                zoom_minimo=payload.zoom_minimo,
                zoom_maximo=payload.zoom_maximo,
                visivel=payload.visivel,
                autor_id=payload.created_by,
            )
        )
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_camada(camada)


@router.post("/camadas/{camada_id}/ativar")
def ativar_camada(
    camada_id: str,
    repo: Annotated[RepositorioCamadaMapa, Depends(get_camada_repo)],
    created_by: str = "",
) -> CamadaResponse:
    try:
        return to_camada(AtivarCamadaUseCase(repo).execute(camada_id, created_by))
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/camadas/{camada_id}/desativar")
def desativar_camada(
    camada_id: str,
    repo: Annotated[RepositorioCamadaMapa, Depends(get_camada_repo)],
    created_by: str = "",
) -> CamadaResponse:
    try:
        return to_camada(DesativarCamadaUseCase(repo).execute(camada_id, created_by))
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.delete("/camadas/{camada_id}")
def excluir_camada(
    camada_id: str,
    repo: Annotated[RepositorioCamadaMapa, Depends(get_camada_repo)],
    vinculos: Annotated[RepositorioMapaCamada, Depends(get_vinculo_repo)],
    mapas: Annotated[RepositorioMapaSig, Depends(get_mapa_repo)],
) -> CamadaResponse:
    try:
        return to_camada(ExcluirCamadaUseCase(repo, vinculos, mapas).execute(camada_id))
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/mapas", status_code=201)
def cadastrar_mapa(
    payload: MapaCreateRequest,
    repo: Annotated[RepositorioMapaSig, Depends(get_mapa_repo)],
) -> MapaResponse:
    try:
        mapa = CadastrarMapaUseCase(repo).execute(
            CadastrarMapaInput(
                codigo=payload.codigo,
                nome=payload.nome,
                descricao=payload.descricao,
                tipo=payload.tipo,
                datum=payload.datum,
                srid=payload.srid,
                escala_denominador=payload.escala_denominador,
                zoom_inicial=payload.zoom_inicial,
                zoom_minimo=payload.zoom_minimo,
                zoom_maximo=payload.zoom_maximo,
                lat_min=payload.lat_min,
                lon_min=payload.lon_min,
                lat_max=payload.lat_max,
                lon_max=payload.lon_max,
                autor_id=payload.created_by,
            )
        )
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_mapa(mapa)


@router.get("/mapas")
def listar_mapas(
    repo: Annotated[RepositorioMapaSig, Depends(get_mapa_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    situacao: str | None = None,
) -> list[MapaResponse]:
    return [to_mapa(m) for m in repo.list_all(page=page, page_size=page_size, situacao=situacao)]


@router.get("/mapas/{mapa_id}")
def obter_mapa(
    mapa_id: str,
    repo: Annotated[RepositorioMapaSig, Depends(get_mapa_repo)],
) -> MapaResponse:
    mapa = obter(repo, mapa_id)
    if mapa is None:
        raise HTTPException(404, "Mapa SIG não encontrado")
    return to_mapa(mapa)


@router.patch("/mapas/{mapa_id}")
def atualizar_mapa(
    mapa_id: str,
    payload: MapaUpdateRequest,
    repo: Annotated[RepositorioMapaSig, Depends(get_mapa_repo)],
) -> MapaResponse:
    try:
        mapa = AtualizarMapaUseCase(repo).execute(
            AtualizarMapaInput(
                mapa_id=mapa_id,
                codigo=payload.codigo,
                nome=payload.nome,
                descricao=payload.descricao,
                tipo=payload.tipo,
                datum=payload.datum,
                srid=payload.srid,
                escala_denominador=payload.escala_denominador,
                zoom_inicial=payload.zoom_inicial,
                zoom_minimo=payload.zoom_minimo,
                zoom_maximo=payload.zoom_maximo,
                lat_min=payload.lat_min,
                lon_min=payload.lon_min,
                lat_max=payload.lat_max,
                lon_max=payload.lon_max,
                autor_id=payload.created_by,
            )
        )
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_mapa(mapa)


@router.delete("/mapas/{mapa_id}")
def excluir_mapa(
    mapa_id: str,
    repo: Annotated[RepositorioMapaSig, Depends(get_mapa_repo)],
    vinculos: Annotated[RepositorioMapaCamada, Depends(get_vinculo_repo)],
) -> MapaResponse:
    try:
        return to_mapa(ExcluirMapaUseCase(repo, vinculos).execute(mapa_id))
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/mapas/{mapa_id}/publicar")
def publicar_mapa(
    mapa_id: str,
    repo: Annotated[RepositorioMapaSig, Depends(get_mapa_repo)],
    vinculos: Annotated[RepositorioMapaCamada, Depends(get_vinculo_repo)],
    camadas: Annotated[RepositorioCamadaMapa, Depends(get_camada_repo)],
    created_by: str = "",
) -> MapaResponse:
    try:
        return to_mapa(PublicarMapaUseCase(repo, vinculos, camadas).execute(mapa_id, created_by))
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/mapas/{mapa_id}/arquivar")
def arquivar_mapa(
    mapa_id: str,
    repo: Annotated[RepositorioMapaSig, Depends(get_mapa_repo)],
    created_by: str = "",
) -> MapaResponse:
    try:
        return to_mapa(ArquivarMapaUseCase(repo).execute(mapa_id, created_by))
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.get("/mapas/{mapa_id}/composicao")
def listar_composicao(
    mapa_id: str,
    repo: Annotated[RepositorioMapaCamada, Depends(get_vinculo_repo)],
) -> list[MapaCamadaResponse]:
    """Lista as camadas que compõem um mapa (RN-GEO-004)."""
    return [to_vinculo(v) for v in repo.list_by_mapa(mapa_id)]


@router.post("/mapas/{mapa_id}/composicao", status_code=201)
def compor_camada(
    mapa_id: str,
    payload: MapaComposicaoRequest,
    vinculos: Annotated[RepositorioMapaCamada, Depends(get_vinculo_repo)],
    mapas: Annotated[RepositorioMapaSig, Depends(get_mapa_repo)],
    camadas: Annotated[RepositorioCamadaMapa, Depends(get_camada_repo)],
) -> MapaCamadaResponse:
    try:
        vinculo = ComporCamadaUseCase(vinculos, mapas, camadas).execute(
            ComporCamadaInput(
                mapa_id=mapa_id,
                camada_id=payload.camada_id,
                ordem=payload.ordem,
                opacidade=payload.opacidade,
                visivel=payload.visivel,
                rotulo=payload.rotulo,
                autor_id=payload.created_by,
            )
        )
    except DomGeoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_vinculo(vinculo)


@router.delete("/mapas/{mapa_id}/composicao/{vinculo_id}")
def remover_composicao(
    mapa_id: str,
    vinculo_id: str,
    vinculos: Annotated[RepositorioMapaCamada, Depends(get_vinculo_repo)],
    mapas: Annotated[RepositorioMapaSig, Depends(get_mapa_repo)],
) -> MapaCamadaResponse:
    vinculo = RemoverComposicaoUseCase(vinculos, mapas).execute(vinculo_id)
    if vinculo.mapa_id != mapa_id:
        raise HTTPException(404, "Vínculo de composição não pertence ao mapa informado")
    return to_vinculo(vinculo)
