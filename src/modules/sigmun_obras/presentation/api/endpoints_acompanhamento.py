"""Endpoints do DOM-OBR — acompanhamento físico-financeiro (prefixo /api/v1/obr)."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, status

from ...application.interfaces import (
    RepositorioDespesa,
    RepositorioEtapa,
    RepositorioMedicao,
    RepositorioObra,
    RepositorioVistoria,
)
from ...application.use_cases import (
    AprovarMedicaoUseCase,
    AtualizarEtapaUseCase,
    CadastrarEtapaInput,
    CadastrarEtapaUseCase,
    CancelarMedicaoUseCase,
    ConcluirEtapaUseCase,
    ExcluirDespesaUseCase,
    GlosarMedicaoUseCase,
    RegistrarDespesaInput,
    RegistrarDespesaUseCase,
    RegistrarMedicaoInput,
    RegistrarMedicaoUseCase,
    RegistrarVistoriaInput,
    RegistrarVistoriaUseCase,
)
from ...domain.exceptions import DomObrDomainError
from ..schemas import (
    DespesaCreateRequest,
    DespesaResponse,
    EtapaCreateRequest,
    EtapaResponse,
    EtapaUpdateRequest,
    MedicaoCreateRequest,
    MedicaoGlosaRequest,
    MedicaoResponse,
    ObraDetalheResponse,
    VistoriaCreateRequest,
    VistoriaResponse,
)
from .deps import (
    get_despesa_repo,
    get_etapa_repo,
    get_medicao_repo,
    get_obra_repo,
    get_vistoria_repo,
    obter,
    to_despesa,
    to_etapa,
    to_medicao,
    to_obra,
    to_vistoria,
)
from .router import router

# Repositórios injetados na visão consolidada do acompanhamento.
_DetalheDeps = Annotated[
    RepositorioObra,
    RepositorioMedicao,
    RepositorioDespesa,
    RepositorioEtapa,
    RepositorioVistoria,
]


@router.get("/obras/{obra_id}/acompanhamento")
def obter_acompanhamento_obra(
    obra_id: str,
    obras: Annotated[RepositorioObra, Depends(get_obra_repo)],
    medicoes: Annotated[RepositorioMedicao, Depends(get_medicao_repo)],
    despesas: Annotated[RepositorioDespesa, Depends(get_despesa_repo)],
    etapas: Annotated[RepositorioEtapa, Depends(get_etapa_repo)],
    vistorias: Annotated[RepositorioVistoria, Depends(get_vistoria_repo)],
) -> ObraDetalheResponse:
    """Visão consolidada físico-financeira de uma obra (RN-OBR-005, RN-OBR-006)."""
    obra = obter(obras, obra_id)
    if obra is None:
        raise HTTPException(404, "Obra não encontrada")
    return ObraDetalheResponse(
        obra=to_obra(obra),
        medicoes=[to_medicao(m) for m in medicoes.list_by_obra(obra_id)],
        despesas=[to_despesa(d) for d in despesas.list_by_obra(obra_id)],
        etapas=[to_etapa(e) for e in etapas.list_by_obra(obra_id)],
        vistorias=[to_vistoria(v) for v in vistorias.list_by_obra(obra_id)],
    )


@router.post("/medicoes", status_code=201)
def registrar_medicao(
    payload: MedicaoCreateRequest,
    repo: Annotated[RepositorioMedicao, Depends(get_medicao_repo)],
    obras: Annotated[RepositorioObra, Depends(get_obra_repo)],
    despesas: Annotated[RepositorioDespesa, Depends(get_despesa_repo)],
) -> MedicaoResponse:
    try:
        medicao = RegistrarMedicaoUseCase(repo, obras, despesas).execute(
            RegistrarMedicaoInput(
                obra_id=payload.obra_id,
                numero=payload.numero,
                tipo=payload.tipo,
                data=payload.data,
                percentual_fisico=payload.percentual_fisico,
                valor_medido=payload.valor_medido,
                responsavel_tecnico=payload.responsavel_tecnico,
                observacao=payload.observacao,
                autor_id=payload.created_by,
            )
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_medicao(medicao)


@router.get("/obras/{obra_id}/medicoes")
def listar_medicoes_da_obra(
    obra_id: str,
    repo: Annotated[RepositorioMedicao, Depends(get_medicao_repo)],
) -> list[MedicaoResponse]:
    """Lista as medições físico-financeiras de uma obra (RN-OBR-005)."""
    return [to_medicao(m) for m in repo.list_by_obra(obra_id)]


@router.post("/medicoes/{medicao_id}/aprovar")
def aprovar_medicao(
    medicao_id: str,
    repo: Annotated[RepositorioMedicao, Depends(get_medicao_repo)],
    obras: Annotated[RepositorioObra, Depends(get_obra_repo)],
    despesas: Annotated[RepositorioDespesa, Depends(get_despesa_repo)],
) -> MedicaoResponse:
    try:
        return to_medicao(
            AprovarMedicaoUseCase(repo, obras, despesas).execute(medicao_id)
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/medicoes/{medicao_id}/glosar")
def glosar_medicao(
    medicao_id: str,
    payload: MedicaoGlosaRequest,
    repo: Annotated[RepositorioMedicao, Depends(get_medicao_repo)],
) -> MedicaoResponse:
    try:
        return to_medicao(
            GlosarMedicaoUseCase(repo).execute(medicao_id, payload.motivo, payload.created_by)
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/medicoes/{medicao_id}/cancelar")
def cancelar_medicao(
    medicao_id: str,
    repo: Annotated[RepositorioMedicao, Depends(get_medicao_repo)],
) -> MedicaoResponse:
    try:
        return to_medicao(CancelarMedicaoUseCase(repo).execute(medicao_id))
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/despesas", status_code=201)
def registrar_despesa(
    payload: DespesaCreateRequest,
    repo: Annotated[RepositorioDespesa, Depends(get_despesa_repo)],
    obras: Annotated[RepositorioObra, Depends(get_obra_repo)],
    medicoes: Annotated[RepositorioMedicao, Depends(get_medicao_repo)],
) -> DespesaResponse:
    try:
        despesa = RegistrarDespesaUseCase(repo, obras, medicoes).execute(
            RegistrarDespesaInput(
                obra_id=payload.obra_id,
                medicao_id=payload.medicao_id,
                descricao=payload.descricao,
                tipo=payload.tipo,
                valor=payload.valor,
                data=payload.data,
                documento=payload.documento,
                credor=payload.credor,
                observacao=payload.observacao,
                autor_id=payload.created_by,
            )
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_despesa(despesa)


@router.get("/obras/{obra_id}/despesas")
def listar_despesas_da_obra(
    obra_id: str,
    repo: Annotated[RepositorioDespesa, Depends(get_despesa_repo)],
) -> list[DespesaResponse]:
    """Lista as despesas financeiras de uma obra (RN-OBR-006)."""
    return [to_despesa(d) for d in repo.list_by_obra(obra_id)]


@router.delete("/despesas/{despesa_id}")
def excluir_despesa(
    despesa_id: str,
    repo: Annotated[RepositorioDespesa, Depends(get_despesa_repo)],
    obras: Annotated[RepositorioObra, Depends(get_obra_repo)],
    medicoes: Annotated[RepositorioMedicao, Depends(get_medicao_repo)],
) -> DespesaResponse:
    try:
        return to_despesa(
            ExcluirDespesaUseCase(repo, obras, medicoes).execute(despesa_id)
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/etapas", status_code=201)
def cadastrar_etapa(
    payload: EtapaCreateRequest,
    repo: Annotated[RepositorioEtapa, Depends(get_etapa_repo)],
    obras: Annotated[RepositorioObra, Depends(get_obra_repo)],
) -> EtapaResponse:
    try:
        etapa = CadastrarEtapaUseCase(repo, obras).execute(
            CadastrarEtapaInput(
                obra_id=payload.obra_id,
                numero=payload.numero,
                descricao=payload.descricao,
                tipo=payload.tipo,
                percentual_previsto=payload.percentual_previsto,
                data_inicio_prevista=payload.data_inicio_prevista,
                data_fim_prevista=payload.data_fim_prevista,
                responsavel=payload.responsavel,
                autor_id=payload.created_by,
            )
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_etapa(etapa)


@router.get("/obras/{obra_id}/etapas")
def listar_etapas_da_obra(
    obra_id: str,
    repo: Annotated[RepositorioEtapa, Depends(get_etapa_repo)],
) -> list[EtapaResponse]:
    """Lista as etapas de execução de uma obra (RN-OBR-007)."""
    return [to_etapa(e) for e in repo.list_by_obra(obra_id)]


@router.patch("/etapas/{etapa_id}")
def atualizar_etapa(
    etapa_id: str,
    payload: EtapaUpdateRequest,
    repo: Annotated[RepositorioEtapa, Depends(get_etapa_repo)],
) -> EtapaResponse:
    try:
        return to_etapa(
            AtualizarEtapaUseCase(repo).execute(
                etapa_id, payload.percentual_realizado, payload.situacao, payload.created_by
            )
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/etapas/{etapa_id}/concluir")
def concluir_etapa(
    etapa_id: str,
    repo: Annotated[RepositorioEtapa, Depends(get_etapa_repo)],
) -> EtapaResponse:
    try:
        return to_etapa(ConcluirEtapaUseCase(repo).execute(etapa_id))
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.post("/vistorias", status_code=201)
def registrar_vistoria(
    payload: VistoriaCreateRequest,
    repo: Annotated[RepositorioVistoria, Depends(get_vistoria_repo)],
    obras: Annotated[RepositorioObra, Depends(get_obra_repo)],
) -> VistoriaResponse:
    try:
        vistoria = RegistrarVistoriaUseCase(repo, obras).execute(
            RegistrarVistoriaInput(
                obra_id=payload.obra_id,
                data=payload.data,
                tipo=payload.tipo,
                parecer=payload.parecer,
                percentual_fisico_verificado=payload.percentual_fisico_verificado,
                fiscal=payload.fiscal,
                observacao=payload.observacao,
                autor_id=payload.created_by,
            )
        )
    except DomObrDomainError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc
    return to_vistoria(vistoria)


@router.get("/obras/{obra_id}/vistorias")
def listar_vistorias_da_obra(
    obra_id: str,
    repo: Annotated[RepositorioVistoria, Depends(get_vistoria_repo)],
) -> list[VistoriaResponse]:
    """Lista as vistorias fiscalizadoras de uma obra (RN-OBR-008)."""
    return [to_vistoria(v) for v in repo.list_by_obra(obra_id)]
