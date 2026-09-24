"""Repositorio SQLAlchemy de alunos (DOM-EDU)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioAluno
from ...domain.entities.aluno import Aluno, Sexo, StatusAluno
from ..database.models import AlunoModel


class SQLAlchemyAlunoRepository(RepositorioAluno):
    """Persistencia de alunos."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, aluno: Aluno) -> Aluno:
        """Insere ou atualiza um aluno."""
        existente = self._session.get(AlunoModel, uuid.UUID(aluno.id))
        if existente is not None:
            existente.nome = aluno.nome
            existente.cpf = aluno.cpf
            existente.data_nascimento = aluno.data_nascimento
            existente.sexo = aluno.sexo.value
            existente.nome_mae = aluno.nome_mae
            existente.telefone = aluno.telefone
            existente.endereco = aluno.endereco
            existente.status = aluno.status.value
            existente.updated_at = aluno.updated_at
            existente.is_deleted = aluno.is_deleted
        else:
            self._session.add(AlunoModel(id=uuid.UUID(aluno.id), nome=aluno.nome, cpf=aluno.cpf, data_nascimento=aluno.data_nascimento, sexo=aluno.sexo.value, nome_mae=aluno.nome_mae, telefone=aluno.telefone, endereco=aluno.endereco, status=aluno.status.value, created_at=aluno.created_at, updated_at=aluno.updated_at, created_by=aluno.created_by, is_deleted=aluno.is_deleted))
        self._session.flush()
        return aluno

    def get_by_id(self, aluno_id: str) -> Aluno | None:
        """Busca aluno por id."""
        model = self._session.get(AlunoModel, uuid.UUID(aluno_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_cpf(self, cpf: str) -> Aluno | None:
        """Busca aluno pelo CPF."""
        model = (self._session.query(AlunoModel).filter(AlunoModel.cpf == cpf, AlunoModel.is_deleted == False).first())  # noqa: E712
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista alunos paginados."""
        models = (self._session.query(AlunoModel).filter(AlunoModel.is_deleted == False).offset((page - 1) * page_size).limit(page_size).all())  # noqa: E712
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: AlunoModel) -> Aluno:
        return Aluno(id=str(model.id), nome=model.nome or "", cpf=model.cpf or "", data_nascimento=model.data_nascimento or "", sexo=Sexo(model.sexo or "ignorado"), nome_mae=model.nome_mae or "", telefone=model.telefone or "", endereco=model.endereco or "", status=StatusAluno(model.status or "ativo"), created_at=model.created_at, updated_at=model.updated_at, created_by=model.created_by or "", is_deleted=bool(model.is_deleted))


__all__ = ["SQLAlchemyAlunoRepository"]
