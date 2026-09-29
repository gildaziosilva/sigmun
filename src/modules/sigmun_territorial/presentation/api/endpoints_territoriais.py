"""Endpoints do DOM-TEL — bairros e logradouros (prefixo /api/v1/tel)."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError

from ...application.interfaces import RepositorioBairro, RepositorioLogradouro
from ...application.use_cases import (
    AtualizarBairroInput,
    AtualizarBairroUseCase,
    AtualizarLogradouroInput,
    AtualizarLogradouroUseCase,
    CadastrarBairroInput,
    CadastrarBairroUseCase,
    CadastrarLogradouroInput,
    CadastrarLogradouroUseCase,
    ExcluirBairroUseCase,
    ExcluirLogradouroUseCase,
)
from ...domain.exceptions import (
    BairroNaoEncontradoError,
    DomTelDomainError,
    LogradouroNaoEncontradoError,
)
from ..schemas import (
    BairroCreateRequest,
    BairroResponse,
    BairroUpdateRequest,
    LogradouroCreateRequest,
    LogradouroResponse,
    LogradouroUpdateRequest,
)
from .deps import get_bairro_repo, get_logradouro_repo, obter, to_bairro, to_logradouro
from .router import router

_CONFLITO_CODIGO_BAIRRO = "Código de bairro já cadastrado para outra divisão (RN-TEL-001)"
_CONFLITO_CODIGO_LOGRADOURO = "Código de logradouro já cadastrado (RN-TEL-002)"


@router.post("/bairros", status_code=201)
def cadastrar_bairro(
    payload: BairroCreateRequest,
    repo: Annotated[RepositorioBairro, Depends(get_bairro_repo)],
) -> BairroResponse:
    try:
        bairro = CadastrarBairroUseCase(repo).execute(
            CadastrarBairroInput(
                codigo=payload.codigo,
                nome=payload.nome,
                tipo=payload.tipo,
                populacao_estimada=payload.populacao_estimada,
                area_km2=payload.area_km2,
                autor_id=payload.created_by,
            )
        )
    except IntegrityError as exc:
        raise HTTPException(409, _CONFLITO_CODIGO_BAIRRO) from exc
    except DomTelDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_bairro(bairro)


@router.get("/bairros")
def listar_bairros(
    repo: Annotated[RepositorioBairro, Depends(get_bairro_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> list[BairroResponse]:
    return [to_bairro(b) for b in repo.list_all(page=page, page_size=page_size)]


@router.get("/bairros/codigo/{codigo}")
def obter_bairro_por_codigo(
    codigo: str, repo: Annotated[RepositorioBairro, Depends(get_bairro_repo)]
) -> BairroResponse:
    bairro = repo.get_by_codigo(codigo)
    if bairro is None:
        raise HTTPException(404, "Bairro não encontrado")
    return to_bairro(bairro)


@router.get("/bairros/{bairro_id}")
def obter_bairro(
    bairro_id: str, repo: Annotated[RepositorioBairro, Depends(get_bairro_repo)]
) -> BairroResponse:
    bairro = obter(repo, bairro_id)
    if bairro is None:
        raise HTTPException(404, "Bairro não encontrado")
    return to_bairro(bairro)


@router.get("/bairros/{bairro_id}/logradouros")
def listar_logradouros_do_bairro(
    bairro_id: str,
    bairros: Annotated[RepositorioBairro, Depends(get_bairro_repo)],
    logradouros: Annotated[RepositorioLogradouro, Depends(get_logradouro_repo)],
) -> list[LogradouroResponse]:
    if obter(bairros, bairro_id) is None:
        raise HTTPException(404, "Bairro não encontrado")
    return [to_logradouro(lg) for lg in logradouros.list_by_bairro(bairro_id)]


@router.patch("/bairros/{bairro_id}")
def atualizar_bairro(
    bairro_id: str,
    payload: BairroUpdateRequest,
    repo: Annotated[RepositorioBairro, Depends(get_bairro_repo)],
) -> BairroResponse:
    try:
        bairro = AtualizarBairroUseCase(repo).execute(
            AtualizarBairroInput(
                bairro_id=bairro_id,
                codigo=payload.codigo,
                nome=payload.nome,
                tipo=payload.tipo,
                populacao_estimada=payload.populacao_estimada,
                area_km2=payload.area_km2,
                situacao=payload.situacao,
                autor_id=payload.created_by,
            )
        )
    except BairroNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except IntegrityError as exc:
        raise HTTPException(409, _CONFLITO_CODIGO_BAIRRO) from exc
    except DomTelDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_bairro(bairro)


@router.delete("/bairros/{bairro_id}")
def excluir_bairro(
    bairro_id: str,
    repo: Annotated[RepositorioBairro, Depends(get_bairro_repo)],
    logradouros: Annotated[RepositorioLogradouro, Depends(get_logradouro_repo)],
) -> BairroResponse:
    try:
        return to_bairro(ExcluirBairroUseCase(repo, logradouros).execute(bairro_id))
    except BairroNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomTelDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/logradouros", status_code=201)
def cadastrar_logradouro(
    payload: LogradouroCreateRequest,
    repo: Annotated[RepositorioLogradouro, Depends(get_logradouro_repo)],
    bairros: Annotated[RepositorioBairro, Depends(get_bairro_repo)],
) -> LogradouroResponse:
    try:
        logradouro = CadastrarLogradouroUseCase(repo, bairros).execute(
            CadastrarLogradouroInput(
                codigo=payload.codigo,
                nome=payload.nome,
                bairro_id=payload.bairro_id,
                tipo=payload.tipo,
                cep=payload.cep,
                numero_inicial=payload.numero_inicial,
                numero_final=payload.numero_final,
                autor_id=payload.created_by,
            )
        )
    except IntegrityError as exc:
        raise HTTPException(409, _CONFLITO_CODIGO_LOGRADOURO) from exc
    except BairroNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomTelDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_logradouro(logradouro)


@router.get("/logradouros")
def listar_logradouros(
    repo: Annotated[RepositorioLogradouro, Depends(get_logradouro_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> list[LogradouroResponse]:
    return [to_logradouro(lg) for lg in repo.list_all(page=page, page_size=page_size)]


@router.get("/logradouros/codigo/{codigo}")
def obter_logradouro_por_codigo(
    codigo: str, repo: Annotated[RepositorioLogradouro, Depends(get_logradouro_repo)]
) -> LogradouroResponse:
    logradouro = repo.get_by_codigo(codigo)
    if logradouro is None:
        raise HTTPException(404, "Logradouro não encontrado")
    return to_logradouro(logradouro)


@router.get("/logradouros/{logradouro_id}")
def obter_logradouro(
    logradouro_id: str, repo: Annotated[RepositorioLogradouro, Depends(get_logradouro_repo)]
) -> LogradouroResponse:
    logradouro = obter(repo, logradouro_id)
    if logradouro is None:
        raise HTTPException(404, "Logradouro não encontrado")
    return to_logradouro(logradouro)



@router.patch("/logradouros/{logradouro_id}")
def atualizar_logradouro(
    logradouro_id: str,
    payload: LogradouroUpdateRequest,
    repo: Annotated[RepositorioLogradouro, Depends(get_logradouro_repo)],
    bairros: Annotated[RepositorioBairro, Depends(get_bairro_repo)],
) -> LogradouroResponse:
    try:
        logradouro = AtualizarLogradouroUseCase(repo, bairros).execute(
            AtualizarLogradouroInput(
                logradouro_id=logradouro_id,
                codigo=payload.codigo,
                nome=payload.nome,
                tipo=payload.tipo,
                bairro_id=payload.bairro_id,
                cep=payload.cep,
                numero_inicial=payload.numero_inicial,
                numero_final=payload.numero_final,
                situacao=payload.situacao,
                autor_id=payload.created_by,
            )
        )
    except LogradouroNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except IntegrityError as exc:
        raise HTTPException(409, _CONFLITO_CODIGO_LOGRADOURO) from exc
    except DomTelDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_logradouro(logradouro)


@router.delete("/logradouros/{logradouro_id}")
def excluir_logradouro(
    logradouro_id: str, repo: Annotated[RepositorioLogradouro, Depends(get_logradouro_repo)]
) -> LogradouroResponse:
    try:
        return to_logradouro(ExcluirLogradouroUseCase(repo).execute(logradouro_id))
    except LogradouroNaoEncontradoError as exc:
        raise HTTPException(404, str(exc)) from exc
    except DomTelDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc

