"""Repositorios SQLAlchemy de atendimento/agendamento/regulacao/farmacia (DOM-SAU)."""
from __future__ import annotations
import uuid
from sqlalchemy.orm import Session
from ...domain.entities.atendimento import Agendamento, Atendimento, StatusAgendamento, TipoAtendimento
from ...domain.entities.farmacia_regulacao import Dispensacao, Medicamento, PrioridadeRegulacao, Regulacao, StatusRegulacao
from ..database.models import AgendamentoModel, AtendimentoModel, DispensacaoModel, MedicamentoModel, RegulacaoModel

class SQLAlchemyAtendimentoRepository:
    def __init__(self, session: Session) -> None:
        self._session = session
    def save(self, atendimento: Atendimento) -> Atendimento:
        ex = self._session.get(AtendimentoModel, uuid.UUID(atendimento.id))
        if ex is not None:
            ex.paciente_id = atendimento.paciente_id; ex.data = atendimento.data; ex.tipo = atendimento.tipo.value; ex.profissional = atendimento.profissional; ex.estabelecimento = atendimento.estabelecimento; ex.queixa = atendimento.queixa; ex.conduta = atendimento.conduta; ex.cid10 = atendimento.cid10
        else:
            self._session.add(AtendimentoModel(id=uuid.UUID(atendimento.id), paciente_id=atendimento.paciente_id, data=atendimento.data, tipo=atendimento.tipo.value, profissional=atendimento.profissional, estabelecimento=atendimento.estabelecimento, queixa=atendimento.queixa, conduta=atendimento.conduta, cid10=atendimento.cid10, created_at=atendimento.created_at, created_by=atendimento.created_by))
        self._session.flush()
        return atendimento
    def get_by_id(self, atendimento_id: str):
        m = self._session.get(AtendimentoModel, uuid.UUID(atendimento_id))
        return self._to_entity(m) if m else None
    def list_by_paciente(self, paciente_id: str) -> list:
        ms = (self._session.query(AtendimentoModel).filter(AtendimentoModel.paciente_id == paciente_id).order_by(AtendimentoModel.data).all())
        return [self._to_entity(m) for m in ms]
    def _to_entity(self, m: AtendimentoModel) -> Atendimento:
        return Atendimento(id=str(m.id), paciente_id=m.paciente_id or "", data=m.data, tipo=TipoAtendimento(m.tipo or "consulta"), profissional=m.profissional or "", estabelecimento=m.estabelecimento or "", queixa=m.queixa or "", conduta=m.conduta or "", cid10=m.cid10 or "", created_at=m.created_at, created_by=m.created_by or "")

class SQLAlchemyAgendamentoRepository:
    def __init__(self, session: Session) -> None:
        self._session = session
    def save(self, ag: Agendamento) -> Agendamento:
        ex = self._session.get(AgendamentoModel, uuid.UUID(ag.id))
        if ex is not None:
            ex.paciente_id = ag.paciente_id; ex.especialidade = ag.especialidade; ex.data = ag.data; ex.hora = ag.hora; ex.estabelecimento = ag.estabelecimento; ex.status = ag.status.value; ex.motivo_cancelamento = ag.motivo_cancelamento; ex.updated_at = ag.updated_at
        else:
            self._session.add(AgendamentoModel(id=uuid.UUID(ag.id), paciente_id=ag.paciente_id, especialidade=ag.especialidade, data=ag.data, hora=ag.hora, estabelecimento=ag.estabelecimento, status=ag.status.value, motivo_cancelamento=ag.motivo_cancelamento, created_at=ag.created_at, updated_at=ag.updated_at, created_by=ag.created_by))
        self._session.flush()
        return ag
    def get_by_id(self, agendamento_id: str):
        m = self._session.get(AgendamentoModel, uuid.UUID(agendamento_id))
        return self._to_entity(m) if m else None
    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        ms = (self._session.query(AgendamentoModel).offset((page - 1) * page_size).limit(page_size).all())
        return [self._to_entity(m) for m in ms]
    def _to_entity(self, m: AgendamentoModel) -> Agendamento:
        return Agendamento(id=str(m.id), paciente_id=m.paciente_id or "", especialidade=m.especialidade or "", data=m.data, hora=m.hora or "", estabelecimento=m.estabelecimento or "", status=StatusAgendamento(m.status or "agendado"), motivo_cancelamento=m.motivo_cancelamento or "", created_at=m.created_at, updated_at=m.updated_at, created_by=m.created_by or "")

class SQLAlchemyRegulacaoRepository:
    def __init__(self, session: Session) -> None:
        self._session = session
    def save(self, reg: Regulacao) -> Regulacao:
        ex = self._session.get(RegulacaoModel, uuid.UUID(reg.id))
        if ex is not None:
            ex.paciente_id = reg.paciente_id; ex.procedimento = reg.procedimento; ex.prioridade = reg.prioridade.value; ex.solicitante = reg.solicitante; ex.data_solicitacao = reg.data_solicitacao; ex.status = reg.status.value; ex.justificativa = reg.justificativa; ex.updated_at = reg.updated_at
        else:
            self._session.add(RegulacaoModel(id=uuid.UUID(reg.id), paciente_id=reg.paciente_id, procedimento=reg.procedimento, prioridade=reg.prioridade.value, solicitante=reg.solicitante, data_solicitacao=reg.data_solicitacao, status=reg.status.value, justificativa=reg.justificativa, created_at=reg.created_at, updated_at=reg.updated_at, created_by=reg.created_by))
        self._session.flush()
        return reg
    def get_by_id(self, regulacao_id: str):
        m = self._session.get(RegulacaoModel, uuid.UUID(regulacao_id))
        return self._to_entity(m) if m else None
    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        ms = (self._session.query(RegulacaoModel).offset((page - 1) * page_size).limit(page_size).all())
        return [self._to_entity(m) for m in ms]
    def _to_entity(self, m: RegulacaoModel) -> Regulacao:
        return Regulacao(id=str(m.id), paciente_id=m.paciente_id or "", procedimento=m.procedimento or "", prioridade=PrioridadeRegulacao(m.prioridade or "rotina"), solicitante=m.solicitante or "", data_solicitacao=m.data_solicitacao, status=StatusRegulacao(m.status or "solicitada"), justificativa=m.justificativa or "", created_at=m.created_at, updated_at=m.updated_at, created_by=m.created_by or "")

class SQLAlchemyMedicamentoRepository:
    def __init__(self, session: Session) -> None:
        self._session = session
    def save(self, med: Medicamento) -> Medicamento:
        ex = self._session.get(MedicamentoModel, uuid.UUID(med.id))
        if ex is not None:
            ex.nome = med.nome; ex.apresentacao = med.apresentacao; ex.estoque = med.estoque; ex.estoque_minimo = med.estoque_minimo; ex.updated_at = med.updated_at
        else:
            self._session.add(MedicamentoModel(id=uuid.UUID(med.id), nome=med.nome, apresentacao=med.apresentacao, estoque=med.estoque, estoque_minimo=med.estoque_minimo, created_at=med.created_at, updated_at=med.updated_at, created_by=med.created_by))
        self._session.flush()
        return med
    def get_by_id(self, medicamento_id: str):
        m = self._session.get(MedicamentoModel, uuid.UUID(medicamento_id))
        return self._to_entity(m) if m else None
    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        ms = (self._session.query(MedicamentoModel).offset((page - 1) * page_size).limit(page_size).all())
        return [self._to_entity(m) for m in ms]
    def _to_entity(self, m: MedicamentoModel) -> Medicamento:
        return Medicamento(id=str(m.id), nome=m.nome or "", apresentacao=m.apresentacao or "", estoque=float(m.estoque or 0), estoque_minimo=float(m.estoque_minimo or 0), created_at=m.created_at, updated_at=m.updated_at, created_by=m.created_by or "")

class SQLAlchemyDispensacaoRepository:
    def __init__(self, session: Session) -> None:
        self._session = session
    def save(self, disp: Dispensacao) -> Dispensacao:
        self._session.add(DispensacaoModel(id=uuid.UUID(disp.id), paciente_id=disp.paciente_id, medicamento_id=disp.medicamento_id, quantidade=disp.quantidade, data=disp.data, receita=disp.receita, created_at=disp.created_at, created_by=disp.created_by))
        self._session.flush()
        return disp
    def get_by_id(self, dispensacao_id: str):
        m = self._session.get(DispensacaoModel, uuid.UUID(dispensacao_id))
        return self._to_entity(m) if m else None
    def list_by_paciente(self, paciente_id: str) -> list:
        ms = (self._session.query(DispensacaoModel).filter(DispensacaoModel.paciente_id == paciente_id).all())
        return [self._to_entity(m) for m in ms]
    def _to_entity(self, m: DispensacaoModel) -> Dispensacao:
        return Dispensacao(id=str(m.id), paciente_id=m.paciente_id or "", medicamento_id=m.medicamento_id or "", quantidade=float(m.quantidade or 0), data=m.data, receita=m.receita or "", created_at=m.created_at, created_by=m.created_by or "")
