"""Repositorio SQLAlchemy de servidores (DOM-PES)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioServidor
from ...domain.entities.servidor import Servidor, StatusServidor, TipoVinculo
from ..database.models import ServidorModel


class SQLAlchemyServidorRepository(RepositorioServidor):
    """Persistencia de servidores."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, servidor: Servidor) -> Servidor:
        """Insere ou atualiza um servidor."""
        existente = self._session.get(ServidorModel, uuid.UUID(servidor.id))
        if existente is not None:
            existente.matricula = servidor.matricula
            existente.cpf = servidor.cpf
            existente.nome = servidor.nome
            existente.cargo_id = servidor.cargo_id
            existente.tipo_vinculo = servidor.tipo_vinculo.value
            existente.status = servidor.status.value
            existente.data_admissao = servidor.data_admissao
            existente.data_desligamento = servidor.data_desligamento
            existente.salario = servidor.salario
            existente.email = servidor.email
            existente.telefone = servidor.telefone
            existente.updated_at = servidor.updated_at
            existente.updated_by = servidor.updated_by
            existente.is_deleted = servidor.is_deleted
        else:
            self._session.add(
                ServidorModel(
                    id=uuid.UUID(servidor.id),
                    matricula=servidor.matricula,
                    cpf=servidor.cpf,
                    nome=servidor.nome,
                    cargo_id=servidor.cargo_id,
                    tipo_vinculo=servidor.tipo_vinculo.value,
                    status=servidor.status.value,
                    data_admissao=servidor.data_admissao,
                    data_desligamento=servidor.data_desligamento,
                    salario=servidor.salario,
                    email=servidor.email,
                    telefone=servidor.telefone,
                    created_at=servidor.created_at,
                    updated_at=servidor.updated_at,
                    created_by=servidor.created_by,
                    updated_by=servidor.updated_by,
                    is_deleted=servidor.is_deleted,
                )
            )
        self._session.flush()
        return servidor

    def get_by_id(self, servidor_id: str) -> Servidor | None:
        """Busca servidor por id."""
        model = self._session.get(ServidorModel, uuid.UUID(servidor_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_matricula(self, matricula: str) -> Servidor | None:
        """Busca servidor por matricula."""
        model = (
            self._session.query(ServidorModel)
            .filter(
                ServidorModel.matricula == matricula,
                ServidorModel.is_deleted == False,  # noqa: E712
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def get_by_cpf(self, cpf: str) -> Servidor | None:
        """Busca servidor por CPF."""
        model = (
            self._session.query(ServidorModel)
            .filter(
                ServidorModel.cpf == cpf,
                ServidorModel.is_deleted == False,  # noqa: E712
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def _to_entity(self, model: ServidorModel) -> Servidor:
        return Servidor(
            id=str(model.id),
            matricula=model.matricula or "",
            cpf=model.cpf or "",
            nome=model.nome or "",
            cargo_id=model.cargo_id or "",
            tipo_vinculo=TipoVinculo(model.tipo_vinculo or "efetivo"),
            status=StatusServidor(model.status or "ativo"),
            data_admissao=model.data_admissao,
            data_desligamento=model.data_desligamento,
            salario=float(model.salario or 0),
            email=model.email or "",
            telefone=model.telefone or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            updated_by=model.updated_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyServidorRepository"]
