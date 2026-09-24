"""Repositorio SQLAlchemy de pacientes (DOM-SAU)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioPaciente
from ...domain.entities.paciente import Paciente, Sexo, StatusPaciente
from ..database.models import PacienteModel


class SQLAlchemyPacienteRepository(RepositorioPaciente):
    """Persistencia de pacientes."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, paciente: Paciente) -> Paciente:
        """Insere ou atualiza um paciente."""
        existente = self._session.get(PacienteModel, uuid.UUID(paciente.id))
        if existente is not None:
            existente.nome = paciente.nome
            existente.cns = paciente.cns
            existente.cpf = paciente.cpf
            existente.data_nascimento = paciente.data_nascimento
            existente.sexo = paciente.sexo.value
            existente.nome_mae = paciente.nome_mae
            existente.telefone = paciente.telefone
            existente.endereco = paciente.endereco
            existente.ubs_referencia = paciente.ubs_referencia
            existente.status = paciente.status.value
            existente.updated_at = paciente.updated_at
            existente.is_deleted = paciente.is_deleted
        else:
            self._session.add(PacienteModel(id=uuid.UUID(paciente.id), nome=paciente.nome, cns=paciente.cns, cpf=paciente.cpf, data_nascimento=paciente.data_nascimento, sexo=paciente.sexo.value, nome_mae=paciente.nome_mae, telefone=paciente.telefone, endereco=paciente.endereco, ubs_referencia=paciente.ubs_referencia, status=paciente.status.value, created_at=paciente.created_at, updated_at=paciente.updated_at, created_by=paciente.created_by, is_deleted=paciente.is_deleted))
        self._session.flush()
        return paciente

    def get_by_id(self, paciente_id: str) -> Paciente | None:
        """Busca paciente por id."""
        model = self._session.get(PacienteModel, uuid.UUID(paciente_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_cns(self, cns: str) -> Paciente | None:
        """Busca paciente pelo CNS."""
        model = (self._session.query(PacienteModel).filter(PacienteModel.cns == cns, PacienteModel.is_deleted == False).first())  # noqa: E712
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista pacientes paginados."""
        models = (self._session.query(PacienteModel).filter(PacienteModel.is_deleted == False).offset((page - 1) * page_size).limit(page_size).all())  # noqa: E712
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: PacienteModel) -> Paciente:
        return Paciente(id=str(model.id), nome=model.nome or "", cns=model.cns or "", cpf=model.cpf or "", data_nascimento=model.data_nascimento or "", sexo=Sexo(model.sexo or "ignorado"), nome_mae=model.nome_mae or "", telefone=model.telefone or "", endereco=model.endereco or "", ubs_referencia=model.ubs_referencia or "", status=StatusPaciente(model.status or "ativo"), created_at=model.created_at, updated_at=model.updated_at, created_by=model.created_by or "", is_deleted=bool(model.is_deleted))


__all__ = ["SQLAlchemyPacienteRepository"]
