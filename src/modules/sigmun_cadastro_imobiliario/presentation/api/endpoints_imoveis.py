"""Endpoints do DOM-IMO — imóveis e proprietários (prefixo /api/v1/imo)."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError

from ...application.interfaces import RepositorioImovel, RepositorioProprietario
from ...application.use_cases import (
    AlterarSituacaoImovelUseCase,
    AtualizarImovelInput,
    AtualizarImovelUseCase,
    CadastrarImovelInput,
    CadastrarImovelUseCase,
    ExcluirImovelUseCase,
    RemoverProprietarioUseCase,
    VincularProprietarioInput,
    VincularProprietarioUseCase,
)
from ...domain.exceptions import (
    DomImoDomainError,
    ImovelNaoEncontradoError,
    ProprietarioNaoEncontradoError,
)
from ..schemas import (
    ImovelCreateRequest,
    ImovelResponse,
    ImovelSituacaoRequest,
    ImovelUpdateRequest,
    ProprietarioCreateRequest,
    ProprietarioResponse,
)
from .deps import get_imovel_repo, get_proprietario_repo, obter, to_imovel, to_proprietario
from .router import router

_CONFLITO_INSCRICAO = "Inscrição imobiliária já cadastrada para outro imóvel (RN-IMO-001)"


@router.post("/imoveis", status_code=201)
def cadastrar_imovel(
    payload: ImovelCreateRequest,
    repo: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
) -> ImovelResponse:
    try:
        imovel = CadastrarImovelUseCase(repo).execute(
            CadastrarImovelInput(
                inscricao_imobiliaria=payload.inscricao_imobiliaria,
                logradouro_id=payload.logradouro_id,
                bairro_id=payload.bairro_id,
                numero=payload.numero,
                complemento=payload.complemento,
                tipo=payload.tipo,
                tipo_propriedade=payload.tipo_propriedade,
                area_terreno_m2=payload.area_terreno_m2,
                area_construida_m2=payload.area_construida_m2,
                ano_construcao=payload.ano_construcao,
                autor_id=payload.created_by,
            )
        )
    except IntegrityError as exc:
        raise HTTPException(409, _CONFLITO_INSCRICAO) from exc
    except DomImoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_imovel(imovel)


@router.get("/imoveis")
def listar_imoveis(
    repo: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    situacao: str | None = None,
) -> list[ImovelResponse]:
    return [to_imovel(i) for i in repo.list_all(page=page, page_size=page_size, situacao=situacao)]


@router.get("/imoveis/inscricao/{inscricao}")
def obter_imovel_por_inscricao(
    inscricao: str, repo: Annotated[RepositorioImovel, Depends(get_imovel_repo)]
) -> ImovelResponse:
    imovel = repo.get_by_inscricao(inscricao)
    if imovel is None:
        raise HTTPException(404, "Imóvel não encontrado")
    return to_imovel(imovel)


@router.get("/imoveis/logradouro/{logradouro_id}")
def listar_imoveis_do_logradouro(
    logradouro_id: str, repo: Annotated[RepositorioImovel, Depends(get_imovel_repo)]
) -> list[ImovelResponse]:
    return [to_imovel(i) for i in repo.list_by_logradouro(logradouro_id)]


@router.get("/imoveis/bairro/{bairro_id}")
def listar_imoveis_do_bairro(
    bairro_id: str, repo: Annotated[RepositorioImovel, Depends(get_imovel_repo)]
) -> list[ImovelResponse]:
    return [to_imovel(i) for i in repo.list_by_bairro(bairro_id)]


@router.get("/imoveis/{imovel_id}")
def obter_imovel(
    imovel_id: str, repo: Annotated[RepositorioImovel, Depends(get_imovel_repo)]
) -> ImovelResponse:
    imovel = obter(repo, imovel_id)
    if imovel is None:
        raise HTTPException(404, "Imóvel não encontrado")
    return to_imovel(imovel)


@router.patch("/imoveis/{imovel_id}")
def atualizar_imovel(
    imovel_id: str,
    payload: ImovelUpdateRequest,
    repo: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
) -> ImovelResponse:
    try:
        imovel = AtualizarImovelUseCase(repo).execute(
            AtualizarImovelInput(
                imovel_id=imovel_id,
                numero=payload.numero,
                complemento=payload.complemento,
                tipo=payload.tipo,
                tipo_propriedade=payload.tipo_propriedade,
                area_terreno_m2=payload.area_terreno_m2,
                area_construida_m2=payload.area_construida_m2,
                ano_construcao=payload.ano_construcao,
                autor_id=payload.created_by,
            )
        )
    except ImovelNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomImoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_imovel(imovel)


@router.post("/imoveis/{imovel_id}/situacao")
def alterar_situacao_imovel(
    imovel_id: str,
    payload: ImovelSituacaoRequest,
    repo: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
) -> ImovelResponse:
    try:
        return to_imovel(AlterarSituacaoImovelUseCase(repo).execute(imovel_id, payload.situacao))
    except ImovelNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomImoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.delete("/imoveis/{imovel_id}")
def excluir_imovel(
    imovel_id: str, repo: Annotated[RepositorioImovel, Depends(get_imovel_repo)]
) -> ImovelResponse:
    try:
        return to_imovel(ExcluirImovelUseCase(repo).execute(imovel_id))
    except ImovelNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomImoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.get("/imoveis/{imovel_id}/proprietarios")
def listar_proprietarios_do_imovel(
    imovel_id: str,
    imoveis: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
    proprietarios: Annotated[RepositorioProprietario, Depends(get_proprietario_repo)],
) -> list[ProprietarioResponse]:
    if obter(imoveis, imovel_id) is None:
        raise HTTPException(404, "Imóvel não encontrado")
    return [to_proprietario(p) for p in proprietarios.list_by_imovel(imovel_id)]


@router.post("/proprietarios", status_code=201)
def vincular_proprietario(
    payload: ProprietarioCreateRequest,
    repo: Annotated[RepositorioProprietario, Depends(get_proprietario_repo)],
    imoveis: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
) -> ProprietarioResponse:
    try:
        proprietario = VincularProprietarioUseCase(repo, imoveis).execute(
            VincularProprietarioInput(
                imovel_id=payload.imovel_id,
                nome=payload.nome,
                cpf=payload.cpf,
                pessoa_id=payload.pessoa_id,
                vinculo=payload.vinculo,
                principal=payload.principal,
                autor_id=payload.created_by,
            )
        )
    except ImovelNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomImoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_proprietario(proprietario)


@router.get("/proprietarios")
def listar_proprietarios(
    repo: Annotated[RepositorioProprietario, Depends(get_proprietario_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> list[ProprietarioResponse]:
    return [to_proprietario(p) for p in repo.list_all(page=page, page_size=page_size)]


@router.delete("/proprietarios/{vinculo_id}")
def remover_proprietario(
    vinculo_id: str, repo: Annotated[RepositorioProprietario, Depends(get_proprietario_repo)]
) -> ProprietarioResponse:
    try:
        return to_proprietario(RemoverProprietarioUseCase(repo).execute(vinculo_id))
    except ProprietarioNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomImoDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc

