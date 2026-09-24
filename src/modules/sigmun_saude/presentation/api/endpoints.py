"""Endpoints do DOM-SAU (prefixo /api/v1/sau)."""
from __future__ import annotations
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from src.core.infrastructure.database.session import get_db
from ...application.interfaces import RepositorioAgendamento, RepositorioAtendimento, RepositorioDispensacao, RepositorioMedicamento, RepositorioPaciente, RepositorioRegulacao
from ...application.use_cases import (AgendarConsultaInput, AgendarConsultaUseCase, AutorizarRegulacaoUseCase, CadastrarMedicamentoInput, CadastrarMedicamentoUseCase, CadastrarPacienteInput, CadastrarPacienteUseCase, CancelarAgendamentoUseCase, ConfirmarAgendamentoUseCase, DispensarMedicamentoInput, DispensarMedicamentoUseCase, NegarRegulacaoUseCase, RealizarAgendamentoUseCase, RegistrarAtendimentoInput, RegistrarAtendimentoUseCase, ReporEstoqueUseCase, SolicitarRegulacaoInput, SolicitarRegulacaoUseCase)
from ...domain.exceptions import AgendamentoNaoEncontradoError, DomSauDomainError, MedicamentoNaoEncontradoError, PacienteNaoEncontradoError, RegulacaoNaoEncontradaError
from ...infrastructure.repositories.sqlalchemy_atendimento_repository import (SQLAlchemyAgendamentoRepository, SQLAlchemyAtendimentoRepository, SQLAlchemyDispensacaoRepository, SQLAlchemyMedicamentoRepository, SQLAlchemyRegulacaoRepository)
from ...infrastructure.repositories.sqlalchemy_paciente_repository import SQLAlchemyPacienteRepository
from ..schemas.sau_schemas import (AgendamentoCreateRequest, AgendamentoResponse, AtendimentoCreateRequest, AtendimentoResponse, DispensacaoCreateRequest, DispensacaoResponse, MedicamentoCreateRequest, MedicamentoResponse, PacienteCreateRequest, PacienteResponse, RegulacaoCreateRequest, RegulacaoResponse)
router = APIRouter(prefix="/api/v1/sau", tags=["Saude Municipal"])

def get_paciente_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioPaciente:
    return SQLAlchemyPacienteRepository(session)

def get_atendimento_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioAtendimento:
    return SQLAlchemyAtendimentoRepository(session)

def get_agendamento_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioAgendamento:
    return SQLAlchemyAgendamentoRepository(session)

def get_regulacao_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioRegulacao:
    return SQLAlchemyRegulacaoRepository(session)

def get_medicamento_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioMedicamento:
    return SQLAlchemyMedicamentoRepository(session)

def get_dispensacao_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioDispensacao:
    return SQLAlchemyDispensacaoRepository(session)

def _to_paciente(p) -> PacienteResponse:
    return PacienteResponse(id=p.id, nome=p.nome, cns=p.cns, cpf=p.cpf, data_nascimento=p.data_nascimento, sexo=p.sexo.value, nome_mae=p.nome_mae, telefone=p.telefone, endereco=p.endereco, ubs_referencia=p.ubs_referencia, status=p.status.value, created_at=p.created_at, updated_at=p.updated_at)

def _to_atendimento(a) -> AtendimentoResponse:
    return AtendimentoResponse(id=a.id, paciente_id=a.paciente_id, data=a.data, tipo=a.tipo.value, profissional=a.profissional, estabelecimento=a.estabelecimento, queixa=a.queixa, conduta=a.conduta, cid10=a.cid10, created_at=a.created_at)

def _to_agendamento(a) -> AgendamentoResponse:
    return AgendamentoResponse(id=a.id, paciente_id=a.paciente_id, especialidade=a.especialidade, data=a.data, hora=a.hora, estabelecimento=a.estabelecimento, status=a.status.value, created_at=a.created_at)

def _to_regulacao(r) -> RegulacaoResponse:
    return RegulacaoResponse(id=r.id, paciente_id=r.paciente_id, procedimento=r.procedimento, prioridade=r.prioridade.value, solicitante=r.solicitante, data_solicitacao=r.data_solicitacao, status=r.status.value, justificativa=r.justificativa, created_at=r.created_at)

def _to_medicamento(m) -> MedicamentoResponse:
    return MedicamentoResponse(id=m.id, nome=m.nome, apresentacao=m.apresentacao, estoque=m.estoque, estoque_minimo=m.estoque_minimo, created_at=m.created_at)

def _to_dispensacao(d) -> DispensacaoResponse:
    return DispensacaoResponse(id=d.id, paciente_id=d.paciente_id, medicamento_id=d.medicamento_id, quantidade=d.quantidade, data=d.data, receita=d.receita, created_at=d.created_at)

@router.post("/pacientes", status_code=201)
def cadastrar_paciente(payload: PacienteCreateRequest, repo: Annotated[RepositorioPaciente, Depends(get_paciente_repo)]):
    try:
        p = CadastrarPacienteUseCase(repo).execute(CadastrarPacienteInput(nome=payload.nome, cns=payload.cns, cpf=payload.cpf, data_nascimento=payload.data_nascimento, sexo=payload.sexo, nome_mae=payload.nome_mae, telefone=payload.telefone, endereco=payload.endereco, ubs_referencia=payload.ubs_referencia, autor_id=payload.created_by))
    except DomSauDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_paciente(p)

@router.get("/pacientes")
def listar_pacientes(repo: Annotated[RepositorioPaciente, Depends(get_paciente_repo)], page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100)):
    return [_to_paciente(p) for p in repo.list_all(page=page, page_size=page_size)]

@router.get("/pacientes/{paciente_id}")
def obter_paciente(paciente_id: str, repo: Annotated[RepositorioPaciente, Depends(get_paciente_repo)]):
    p = repo.get_by_id(paciente_id)
    if p is None:
        raise HTTPException(status_code=404, detail="Paciente nao encontrado")
    return _to_paciente(p)

@router.post("/atendimentos", status_code=201)
def registrar_atendimento(payload: AtendimentoCreateRequest, repo: Annotated[RepositorioAtendimento, Depends(get_atendimento_repo)], pacientes: Annotated[RepositorioPaciente, Depends(get_paciente_repo)]):
    try:
        a = RegistrarAtendimentoUseCase(repo, pacientes).execute(RegistrarAtendimentoInput(paciente_id=payload.paciente_id, profissional=payload.profissional, estabelecimento=payload.estabelecimento, tipo=payload.tipo, data=payload.data, queixa=payload.queixa, conduta=payload.conduta, cid10=payload.cid10, autor_id=payload.created_by))
    except PacienteNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomSauDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_atendimento(a)

@router.get("/pacientes/{paciente_id}/prontuario")
def obter_prontuario(paciente_id: str, repo: Annotated[RepositorioAtendimento, Depends(get_atendimento_repo)], pacientes: Annotated[RepositorioPaciente, Depends(get_paciente_repo)]):
    if pacientes.get_by_id(paciente_id) is None:
        raise HTTPException(status_code=404, detail="Paciente nao encontrado")
    return [_to_atendimento(a) for a in repo.list_by_paciente(paciente_id)]

@router.post("/agendamentos", status_code=201)
def agendar(payload: AgendamentoCreateRequest, repo: Annotated[RepositorioAgendamento, Depends(get_agendamento_repo)], pacientes: Annotated[RepositorioPaciente, Depends(get_paciente_repo)]):
    try:
        a = AgendarConsultaUseCase(repo, pacientes).execute(AgendarConsultaInput(paciente_id=payload.paciente_id, especialidade=payload.especialidade, data=payload.data, hora=payload.hora, estabelecimento=payload.estabelecimento, autor_id=payload.created_by))
    except PacienteNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomSauDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_agendamento(a)

@router.get("/agendamentos")
def listar_agendamentos(repo: Annotated[RepositorioAgendamento, Depends(get_agendamento_repo)], page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100)):
    return [_to_agendamento(a) for a in repo.list_all(page=page, page_size=page_size)]

@router.post("/agendamentos/{agendamento_id}/confirmar")
def confirmar(agendamento_id: str, repo: Annotated[RepositorioAgendamento, Depends(get_agendamento_repo)]):
    try:
        return _to_agendamento(ConfirmarAgendamentoUseCase(repo).execute(agendamento_id))
    except AgendamentoNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomSauDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))

@router.post("/agendamentos/{agendamento_id}/cancelar")
def cancelar(agendamento_id: str, repo: Annotated[RepositorioAgendamento, Depends(get_agendamento_repo)], motivo: str = Query("")):
    try:
        return _to_agendamento(CancelarAgendamentoUseCase(repo).execute(agendamento_id, motivo))
    except AgendamentoNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomSauDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))

@router.post("/agendamentos/{agendamento_id}/realizar")
def realizar(agendamento_id: str, repo: Annotated[RepositorioAgendamento, Depends(get_agendamento_repo)]):
    try:
        return _to_agendamento(RealizarAgendamentoUseCase(repo).execute(agendamento_id))
    except AgendamentoNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomSauDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))

@router.post("/regulacoes", status_code=201)
def solicitar(payload: RegulacaoCreateRequest, repo: Annotated[RepositorioRegulacao, Depends(get_regulacao_repo)], pacientes: Annotated[RepositorioPaciente, Depends(get_paciente_repo)]):
    try:
        r = SolicitarRegulacaoUseCase(repo, pacientes).execute(SolicitarRegulacaoInput(paciente_id=payload.paciente_id, procedimento=payload.procedimento, prioridade=payload.prioridade, solicitante=payload.solicitante, autor_id=payload.created_by))
    except PacienteNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomSauDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_regulacao(r)

@router.get("/regulacoes")
def listar_regulacoes(repo: Annotated[RepositorioRegulacao, Depends(get_regulacao_repo)], page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100)):
    return [_to_regulacao(r) for r in repo.list_all(page=page, page_size=page_size)]

@router.post("/regulacoes/{regulacao_id}/autorizar")
def autorizar(regulacao_id: str, repo: Annotated[RepositorioRegulacao, Depends(get_regulacao_repo)]):
    try:
        return _to_regulacao(AutorizarRegulacaoUseCase(repo).execute(regulacao_id))
    except RegulacaoNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomSauDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))

@router.post("/regulacoes/{regulacao_id}/negar")
def negar(regulacao_id: str, repo: Annotated[RepositorioRegulacao, Depends(get_regulacao_repo)], justificativa: str = Query("")):
    try:
        return _to_regulacao(NegarRegulacaoUseCase(repo).execute(regulacao_id, justificativa))
    except RegulacaoNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomSauDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))

@router.post("/medicamentos", status_code=201)
def cadastrar_medicamento(payload: MedicamentoCreateRequest, repo: Annotated[RepositorioMedicamento, Depends(get_medicamento_repo)]):
    try:
        m = CadastrarMedicamentoUseCase(repo).execute(CadastrarMedicamentoInput(nome=payload.nome, apresentacao=payload.apresentacao, estoque=payload.estoque, estoque_minimo=payload.estoque_minimo, autor_id=payload.created_by))
    except DomSauDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_medicamento(m)

@router.get("/medicamentos")
def listar_medicamentos(repo: Annotated[RepositorioMedicamento, Depends(get_medicamento_repo)], page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100)):
    return [_to_medicamento(m) for m in repo.list_all(page=page, page_size=page_size)]

@router.post("/medicamentos/{medicamento_id}/repor")
def repor(medicamento_id: str, repo: Annotated[RepositorioMedicamento, Depends(get_medicamento_repo)], quantidade: float = Query(0)):
    try:
        return _to_medicamento(ReporEstoqueUseCase(repo).execute(medicamento_id, quantidade))
    except MedicamentoNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomSauDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))

@router.post("/dispensacoes", status_code=201)
def dispensar(payload: DispensacaoCreateRequest, dispensacoes: Annotated[RepositorioDispensacao, Depends(get_dispensacao_repo)], medicamentos: Annotated[RepositorioMedicamento, Depends(get_medicamento_repo)], pacientes: Annotated[RepositorioPaciente, Depends(get_paciente_repo)]):
    try:
        d = DispensarMedicamentoUseCase(dispensacoes, medicamentos, pacientes).execute(DispensarMedicamentoInput(paciente_id=payload.paciente_id, medicamento_id=payload.medicamento_id, quantidade=payload.quantidade, receita=payload.receita, autor_id=payload.created_by))
    except (PacienteNaoEncontradoError, MedicamentoNaoEncontradoError) as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomSauDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_dispensacao(d)
