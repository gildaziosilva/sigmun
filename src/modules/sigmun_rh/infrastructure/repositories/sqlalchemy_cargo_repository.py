"""Repositorio SQLAlchemy de cargos (DOM-PES)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioCargo
from ...domain.entities.cargo import Cargo
from ..database.models import CargoModel


class SQLAlchemyCargoRepository(RepositorioCargo):
    """Persistencia de cargos."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, cargo: Cargo) -> Cargo:
        """Insere ou atualiza um cargo."""
        existente = self._session.get(CargoModel, uuid.UUID(cargo.id))
        if existente is not None:
            existente.codigo = cargo.codigo
            existente.nome = cargo.nome
            existente.descricao = cargo.descricao
            existente.nivel = cargo.nivel
            existente.salario_base = cargo.salario_base
            existente.carga_horaria_semanal = cargo.carga_horaria_semanal
            existente.ativo = cargo.ativo
            existente.updated_at = cargo.updated_at
            existente.is_deleted = cargo.is_deleted
        else:
            self._session.add(
                CargoModel(
                    id=uuid.UUID(cargo.id),
                    codigo=cargo.codigo,
                    nome=cargo.nome,
                    descricao=cargo.descricao,
                    nivel=cargo.nivel,
                    salario_base=cargo.salario_base,
                    carga_horaria_semanal=cargo.carga_horaria_semanal,
                    ativo=cargo.ativo,
                    created_at=cargo.created_at,
                    updated_at=cargo.updated_at,
                    created_by=cargo.created_by,
                    is_deleted=cargo.is_deleted,
                )
            )
        self._session.flush()
        return cargo

    def get_by_id(self, cargo_id: str) -> Cargo | None:
        """Busca cargo por id."""
        model = self._session.get(CargoModel, uuid.UUID(cargo_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_codigo(self, codigo: str) -> Cargo | None:
        """Busca cargo por codigo."""
        model = (
            self._session.query(CargoModel)
            .filter(CargoModel.codigo == codigo, CargoModel.is_deleted == False)  # noqa: E712
            .first()
        )
        if model is None:
            return None
        return self._to_entity(model)

    def _to_entity(self, model: CargoModel) -> Cargo:
        return Cargo(
            id=str(model.id),
            codigo=model.codigo or "",
            nome=model.nome or "",
            descricao=model.descricao or "",
            nivel=model.nivel or "basico",
            salario_base=float(model.salario_base or 0),
            carga_horaria_semanal=int(model.carga_horaria_semanal or 40),
            ativo=bool(model.ativo),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyCargoRepository"]
