"""Endpoints do DOM-OBR — obras e ciclo de vida (prefixo /api/v1/obr)."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, Query, status

from ...application.interfaces import RepositorioDespesa, RepositorioMedicao, RepositorioObra
from ...application.use_cases import (
    AtualizarObraInput,
    AtualizarObraUseCase,
    CadastrarObraInput,
    CadastrarObraUseCase,
    CancelarObraUseCase,
    ConcluirObraUseCase,
    ExcluirObraUseCase,
    IniciarExecucaoObraUseCase,
    SuspenderObraUseCase,
)
from ...domain.exceptions import DomObrDomainError
from ..schemas import ObraAcaoRequest, ObraCreateRequest, ObraResponse, ObraUpdateRequest
from .deps import get_despesa_repo, get_medicao_repo, get_obra_repo, obter, to_obra
from .router import router


@router.post("/obras", status_code=201)
def cadastrar_obra(
    payload: ObraCreateRequest,
    repo: Annotated[RepositorioObra, Depends(get_obra_repo)],
) -> ObraResponse:
    try:
        obra = CadastrarObraUseCase(repo).execute(
            CadastrarObraInput(
                numero=payload.numero,
                nome=payload.nome,
                descricao=payload.descricao,
                tipo=payload.tipo,
                tipo_contratacao=payload.tipo_contratacao,
                fonte_recurso=payload.fonte_recurso,
                valor_orcado=payload.valor_orcado,
                valor_contratado=payload.valor_contratado,
                empresa_contratada=payload.empresa_contratada,
                numero_contrato=payload.numero_contrato,
                responsavel_tecnico=payload.responsavel_tecnico,
                endereco=payload.endereco,
                bairro=payload.bairro,
                data_inicio_prevista=payload.data_inicio_prevista,
                data_fim_prevista=payload.data_fim_prevista,
                autor_id=payload.created_by,
            )
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_obra(obra)


@router.get("/obras")
def listar_obras(
    repo: Annotated[RepositorioObra, Depends(get_obra_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    situacao: str | None = None,
) -> list[ObraResponse]:
    return [to_obra(o) for o in repo.list_all(page=page, page_size=page_size, situacao=situacao)]


@router.get("/obras/{obra_id}")
def obter_obra(
    obra_id: str,
    repo: Annotated[RepositorioObra, Depends(get_obra_repo)],
) -> ObraResponse:
    obra = obter(repo, obra_id)
    if obra is None:
        raise HTTPException(404, "Obra não encontrada")
    return to_obra(obra)


@router.patch("/obras/{obra_id}")
def atualizar_obra(
    obra_id: str,
    payload: ObraUpdateRequest,
    repo: Annotated[RepositorioObra, Depends(get_obra_repo)],
) -> ObraResponse:
    try:
        obra = AtualizarObraUseCase(repo).execute(
            AtualizarObraInput(
                obra_id=obra_id,
                nome=payload.nome,
                descricao=payload.descricao,
                tipo=payload.tipo,
                tipo_contratacao=payload.tipo_contratacao,
                fonte_recurso=payload.fonte_recurso,
                valor_orcado=payload.valor_orcado,
                valor_contratado=payload.valor_contratado,
                empresa_contratada=payload.empresa_contratada,
                numero_contrato=payload.numero_contrato,
                responsavel_tecnico=payload.responsavel_tecnico,
                endereco=payload.endereco,
                bairro=payload.bairro,
                data_inicio_prevista=payload.data_inicio_prevista,
                data_fim_prevista=payload.data_fim_prevista,
                observacao=payload.observacao,
                autor_id=payload.created_by,
            )
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_obra(obra)


@router.post("/obras/{obra_id}/iniciar-execucao")
def iniciar_execucao_obra(
    obra_id: str,
    payload: ObraAcaoRequest,
    repo: Annotated[RepositorioObra, Depends(get_obra_repo)],
) -> ObraResponse:
    try:
        return to_obra(
            IniciarExecucaoObraUseCase(repo).execute(
                obra_id, payload.data, payload.created_by
            )
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/obras/{obra_id}/suspender")
def suspender_obra(
    obra_id: str,
    payload: ObraAcaoRequest,
    repo: Annotated[RepositorioObra, Depends(get_obra_repo)],
) -> ObraResponse:
    try:
        return to_obra(
            SuspenderObraUseCase(repo).execute(obra_id, payload.motivo, payload.created_by)
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/obras/{obra_id}/concluir")
def concluir_obra(
    obra_id: str,
    payload: ObraAcaoRequest,
    repo: Annotated[RepositorioObra, Depends(get_obra_repo)],
) -> ObraResponse:
    try:
        return to_obra(
            ConcluirObraUseCase(repo).execute(obra_id, payload.data, payload.created_by)
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/obras/{obra_id}/cancelar")
def cancelar_obra(
    obra_id: str,
    payload: ObraAcaoRequest,
    repo: Annotated[RepositorioObra, Depends(get_obra_repo)],
) -> ObraResponse:
    try:
        return to_obra(
            CancelarObraUseCase(repo).execute(obra_id, payload.motivo, payload.created_by)
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.delete("/obras/{obra_id}")
def excluir_obra(
    obra_id: str,
    repo: Annotated[RepositorioObra, Depends(get_obra_repo)],
    medicoes: Annotated[RepositorioMedicao, Depends(get_medicao_repo)],
    despesas: Annotated[RepositorioDespesa, Depends(get_despesa_repo)],
) -> ObraResponse:
    try:
        return to_obra(ExcluirObraUseCase(repo, medicoes, despesas).execute(obra_id))
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
