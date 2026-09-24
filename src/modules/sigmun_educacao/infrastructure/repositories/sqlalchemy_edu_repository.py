"""Repositorios SQLAlchemy de matricula/diario/transporte/merenda (DOM-EDU)."""
from __future__ import annotations
import uuid
from sqlalchemy.orm import Session
from ...domain.entities.diario import LancamentoDiario
from ...domain.entities.matricula import Matricula, StatusMatricula
from ...domain.entities.merenda import DistribuicaoMerenda, ItemMerenda
from ...domain.entities.transporte import PassagemTransporte, RotaTransporte, StatusRota
from ..database.models import DistribuicaoMerendaModel, ItemMerendaModel, LancamentoDiarioModel, MatriculaModel, PassagemTransporteModel, RotaTransporteModel

class SQLAlchemyMatriculaRepository:
    def __init__(self, session: Session) -> None:
        self._session = session
    def save(self, matricula: Matricula) -> Matricula:
        ex = self._session.get(MatriculaModel, uuid.UUID(matricula.id))
        if ex is not None:
            ex.aluno_id = matricula.aluno_id; ex.escola = matricula.escola; ex.serie = matricula.serie; ex.turno = matricula.turno; ex.ano_letivo = matricula.ano_letivo; ex.data_matricula = matricula.data_matricula; ex.status = matricula.status.value; ex.escola_destino = matricula.escola_destino; ex.motivo = matricula.motivo; ex.updated_at = matricula.updated_at
        else:
            self._session.add(MatriculaModel(id=uuid.UUID(matricula.id), aluno_id=matricula.aluno_id, escola=matricula.escola, serie=matricula.serie, turno=matricula.turno, ano_letivo=matricula.ano_letivo, data_matricula=matricula.data_matricula, status=matricula.status.value, escola_destino=matricula.escola_destino, motivo=matricula.motivo, created_at=matricula.created_at, updated_at=matricula.updated_at, created_by=matricula.created_by))
        self._session.flush()
        return matricula
    def get_by_id(self, matricula_id: str):
        m = self._session.get(MatriculaModel, uuid.UUID(matricula_id))
        return self._to_entity(m) if m else None
    def get_ativa_by_aluno(self, aluno_id: str):
        m = (self._session.query(MatriculaModel).filter(MatriculaModel.aluno_id == aluno_id, MatriculaModel.status == "ativa").first())
        return self._to_entity(m) if m else None
    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        ms = (self._session.query(MatriculaModel).offset((page - 1) * page_size).limit(page_size).all())
        return [self._to_entity(m) for m in ms]
    def _to_entity(self, m: MatriculaModel) -> Matricula:
        return Matricula(id=str(m.id), aluno_id=m.aluno_id or "", escola=m.escola or "", serie=m.serie or "", turno=m.turno or "manha", ano_letivo=int(m.ano_letivo or 0), data_matricula=m.data_matricula, status=StatusMatricula(m.status or "ativa"), escola_destino=m.escola_destino or "", motivo=m.motivo or "", created_at=m.created_at, updated_at=m.updated_at, created_by=m.created_by or "")

class SQLAlchemyLancamentoDiarioRepository:
    def __init__(self, session: Session) -> None:
        self._session = session
    def save(self, lancamento: LancamentoDiario) -> LancamentoDiario:
        ex = self._session.get(LancamentoDiarioModel, uuid.UUID(lancamento.id))
        if ex is not None:
            ex.matricula_id = lancamento.matricula_id; ex.data = lancamento.data; ex.presente = lancamento.presente; ex.nota = lancamento.nota; ex.observacao = lancamento.observacao
        else:
            self._session.add(LancamentoDiarioModel(id=uuid.UUID(lancamento.id), matricula_id=lancamento.matricula_id, data=lancamento.data, presente=lancamento.presente, nota=lancamento.nota, observacao=lancamento.observacao, created_at=lancamento.created_at, created_by=lancamento.created_by))
        self._session.flush()
        return lancamento
    def get_by_id(self, lancamento_id: str):
        m = self._session.get(LancamentoDiarioModel, uuid.UUID(lancamento_id))
        return self._to_entity(m) if m else None
    def list_by_matricula(self, matricula_id: str) -> list:
        ms = (self._session.query(LancamentoDiarioModel).filter(LancamentoDiarioModel.matricula_id == matricula_id).order_by(LancamentoDiarioModel.data).all())
        return [self._to_entity(m) for m in ms]
    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        ms = (self._session.query(LancamentoDiarioModel).offset((page - 1) * page_size).limit(page_size).all())
        return [self._to_entity(m) for m in ms]
    def _to_entity(self, m: LancamentoDiarioModel) -> LancamentoDiario:
        return LancamentoDiario(id=str(m.id), matricula_id=m.matricula_id or "", data=m.data, presente=bool(m.presente), nota=float(m.nota) if m.nota is not None else None, observacao=m.observacao or "", created_at=m.created_at, created_by=m.created_by or "")

class SQLAlchemyRotaTransporteRepository:
    def __init__(self, session: Session) -> None:
        self._session = session
    def save(self, rota: RotaTransporte) -> RotaTransporte:
        ex = self._session.get(RotaTransporteModel, uuid.UUID(rota.id))
        if ex is not None:
            ex.identificacao = rota.identificacao; ex.veiculo = rota.veiculo; ex.motorista = rota.motorista; ex.vagas = rota.vagas; ex.turno = rota.turno; ex.status = rota.status.value; ex.updated_at = rota.updated_at
        else:
            self._session.add(RotaTransporteModel(id=uuid.UUID(rota.id), identificacao=rota.identificacao, veiculo=rota.veiculo, motorista=rota.motorista, vagas=rota.vagas, turno=rota.turno, status=rota.status.value, created_at=rota.created_at, updated_at=rota.updated_at, created_by=rota.created_by))
        self._session.flush()
        return rota
    def get_by_id(self, rota_id: str):
        m = self._session.get(RotaTransporteModel, uuid.UUID(rota_id))
        return self._to_entity(m) if m else None
    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        ms = (self._session.query(RotaTransporteModel).offset((page - 1) * page_size).limit(page_size).all())
        return [self._to_entity(m) for m in ms]
    def _to_entity(self, m: RotaTransporteModel) -> RotaTransporte:
        return RotaTransporte(id=str(m.id), identificacao=m.identificacao or "", veiculo=m.veiculo or "", motorista=m.motorista or "", vagas=int(m.vagas or 0), turno=m.turno or "manha", status=StatusRota(m.status or "ativa"), created_at=m.created_at, updated_at=m.updated_at, created_by=m.created_by or "")

class SQLAlchemyPassagemTransporteRepository:
    def __init__(self, session: Session) -> None:
        self._session = session
    def save(self, passagem: PassagemTransporte) -> PassagemTransporte:
        self._session.add(PassagemTransporteModel(id=uuid.UUID(passagem.id), rota_id=passagem.rota_id, matricula_id=passagem.matricula_id, data=passagem.data, created_at=passagem.created_at, created_by=passagem.created_by))
        self._session.flush()
        return passagem
    def get_by_id(self, passagem_id: str):
        m = self._session.get(PassagemTransporteModel, uuid.UUID(passagem_id))
        return self._to_entity(m) if m else None
    def count_by_rota_data(self, rota_id: str, data) -> int:
        from sqlalchemy import func as _func
        total = self._session.query(_func.count(PassagemTransporteModel.id)).filter(PassagemTransporteModel.rota_id == rota_id, PassagemTransporteModel.data == data).scalar()
        return int(total or 0)
    def list_by_rota(self, rota_id: str) -> list:
        ms = (self._session.query(PassagemTransporteModel).filter(PassagemTransporteModel.rota_id == rota_id).order_by(PassagemTransporteModel.data).all())
        return [self._to_entity(m) for m in ms]
    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        ms = (self._session.query(PassagemTransporteModel).offset((page - 1) * page_size).limit(page_size).all())
        return [self._to_entity(m) for m in ms]
    def _to_entity(self, m: PassagemTransporteModel) -> PassagemTransporte:
        return PassagemTransporte(id=str(m.id), rota_id=m.rota_id or "", matricula_id=m.matricula_id or "", data=m.data, created_at=m.created_at, created_by=m.created_by or "")


class SQLAlchemyItemMerendaRepository:
    def __init__(self, session: Session) -> None:
        self._session = session
    def save(self, item: ItemMerenda) -> ItemMerenda:
        ex = self._session.get(ItemMerendaModel, uuid.UUID(item.id))
        if ex is not None:
            ex.nome = item.nome; ex.tipo = item.tipo; ex.estoque = item.estoque; ex.estoque_minimo = item.estoque_minimo; ex.updated_at = item.updated_at; ex.is_deleted = item.is_deleted
        else:
            self._session.add(ItemMerendaModel(id=uuid.UUID(item.id), nome=item.nome, tipo=item.tipo, estoque=item.estoque, estoque_minimo=item.estoque_minimo, created_at=item.created_at, updated_at=item.updated_at, created_by=item.created_by, is_deleted=item.is_deleted))
        self._session.flush()
        return item
    def get_by_id(self, item_id: str):
        m = self._session.get(ItemMerendaModel, uuid.UUID(item_id))
        if m is None or m.is_deleted:
            return None
        return self._to_entity(m)
    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        ms = (self._session.query(ItemMerendaModel).filter(ItemMerendaModel.is_deleted == False).offset((page - 1) * page_size).limit(page_size).all())  # noqa: E712
        return [self._to_entity(m) for m in ms]
    def _to_entity(self, m: ItemMerendaModel) -> ItemMerenda:
        return ItemMerenda(id=str(m.id), nome=m.nome or "", tipo=m.tipo or "refeicao", estoque=float(m.estoque or 0), estoque_minimo=float(m.estoque_minimo or 0), created_at=m.created_at, updated_at=m.updated_at, created_by=m.created_by or "", is_deleted=bool(m.is_deleted))

class SQLAlchemyDistribuicaoMerendaRepository:
    def __init__(self, session: Session) -> None:
        self._session = session
    def save(self, distribuicao: DistribuicaoMerenda) -> DistribuicaoMerenda:
        self._session.add(DistribuicaoMerendaModel(id=uuid.UUID(distribuicao.id), matricula_id=distribuicao.matricula_id, item_id=distribuicao.item_id, quantidade=distribuicao.quantidade, data=distribuicao.data, refeicao=distribuicao.refeicao, created_at=distribuicao.created_at, created_by=distribuicao.created_by))
        self._session.flush()
        return distribuicao
    def get_by_id(self, distribuicao_id: str):
        m = self._session.get(DistribuicaoMerendaModel, uuid.UUID(distribuicao_id))
        return self._to_entity(m) if m else None
    def list_by_matricula(self, matricula_id: str) -> list:
        ms = (self._session.query(DistribuicaoMerendaModel).filter(DistribuicaoMerendaModel.matricula_id == matricula_id).order_by(DistribuicaoMerendaModel.data).all())
        return [self._to_entity(m) for m in ms]
    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        ms = (self._session.query(DistribuicaoMerendaModel).offset((page - 1) * page_size).limit(page_size).all())
        return [self._to_entity(m) for m in ms]
    def _to_entity(self, m: DistribuicaoMerendaModel) -> DistribuicaoMerenda:
        return DistribuicaoMerenda(id=str(m.id), matricula_id=m.matricula_id or "", item_id=m.item_id or "", quantidade=float(m.quantidade or 0), data=m.data, refeicao=m.refeicao or "almoco", created_at=m.created_at, created_by=m.created_by or "")

