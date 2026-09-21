"""Repositório SQLAlchemy de contribuintes (DOM-TRI)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioContribuinte
from ...domain.entities.contribuinte import (
    Contribuinte,
    StatusContribuinte,
    TipoContribuinte,
)
from ..database.models import ContribuinteModel


class SQLAlchemyContribuinteRepository(RepositorioContribuinte):
    """Persistência de contribuintes."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, contribuinte: Contribuinte) -> Contribuinte:
        """Insere ou atualiza um contribuinte."""
        existente = self._session.get(ContribuinteModel, uuid.UUID(contribuinte.id))
        if existente is not None:
            existente.tipo = contribuinte.tipo.value
            existente.nome = contribuinte.nome
            existente.cpf_cnpj = contribuinte.cpf_cnpj
            existente.inscricao_municipal = contribuinte.inscricao_municipal
            existente.email = contribuinte.email
            existente.telefone = contribuinte.telefone
            existente.endereco = contribuinte.endereco
            existente.status = contribuinte.status.value
            existente.updated_at = contribuinte.updated_at
            existente.is_deleted = contribuinte.is_deleted
        else:
            self._session.add(
                ContribuinteModel(
                    id=uuid.UUID(contribuinte.id),
                    tipo=contribuinte.tipo.value,
                    nome=contribuinte.nome,
                    cpf_cnpj=contribuinte.cpf_cnpj,
                    inscricao_municipal=contribuinte.inscricao_municipal,
                    email=contribuinte.email,
                    telefone=contribuinte.telefone,
                    endereco=contribuinte.endereco,
                    status=contribuinte.status.value,
                    created_at=contribuinte.created_at,
                    updated_at=contribuinte.updated_at,
                    created_by=contribuinte.created_by,
                    is_deleted=contribuinte.is_deleted,
                )
            )
        self._session.flush()
        return contribuinte

    def get_by_id(self, contribuinte_id: str) -> Contribuinte | None:
        """Busca contribuinte por id."""
        model = self._session.get(ContribuinteModel, uuid.UUID(contribuinte_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_cpf_cnpj(self, documento: str) -> Contribuinte | None:
        """Busca contribuinte por CPF/CNPJ."""
        model = (
            self._session.query(ContribuinteModel)
            .filter(
                ContribuinteModel.cpf_cnpj == documento,
                ContribuinteModel.is_deleted == False,  # noqa: E712
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista contribuintes paginados."""
        models = (
            self._session.query(ContribuinteModel)
            .filter(ContribuinteModel.is_deleted == False)  # noqa: E712
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: ContribuinteModel) -> Contribuinte:
        return Contribuinte(
            id=str(model.id),
            tipo=TipoContribuinte(model.tipo or "pf"),
            nome=model.nome or "",
            cpf_cnpj=model.cpf_cnpj or "",
            inscricao_municipal=model.inscricao_municipal or "",
            email=model.email or "",
            telefone=model.telefone or "",
            endereco=model.endereco or "",
            status=StatusContribuinte(model.status or "ativo"),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyContribuinteRepository"]