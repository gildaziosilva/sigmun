"""Repositório SQLAlchemy de certidões (DOM-TRI)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioCertidao
from ...domain.entities.certidao import Certidao, StatusCertidao, TipoCertidao
from ..database.models import CertidaoModel


class SQLAlchemyCertidaoRepository(RepositorioCertidao):
    """Persistência de certidões fiscais."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, certidao: Certidao) -> Certidao:
        """Insere ou atualiza uma certidão."""
        existente = self._session.get(CertidaoModel, uuid.UUID(certidao.id))
        if existente is not None:
            existente.contribuinte_id = certidao.contribuinte_id
            existente.tipo = certidao.tipo.value
            existente.numero = certidao.numero
            existente.data_emissao = certidao.data_emissao
            existente.valido_ate = certidao.valido_ate
            existente.observacao = certidao.observacao
            existente.status = certidao.status.value
            existente.updated_at = certidao.updated_at
            existente.is_deleted = certidao.is_deleted
        else:
            self._session.add(
                CertidaoModel(
                    id=uuid.UUID(certidao.id),
                    contribuinte_id=certidao.contribuinte_id,
                    tipo=certidao.tipo.value,
                    numero=certidao.numero,
                    data_emissao=certidao.data_emissao,
                    valido_ate=certidao.valido_ate,
                    observacao=certidao.observacao,
                    status=certidao.status.value,
                    created_at=certidao.created_at,
                    updated_at=certidao.updated_at,
                    created_by=certidao.created_by,
                    is_deleted=certidao.is_deleted,
                )
            )
        self._session.flush()
        return certidao

    def get_by_id(self, certidao_id: str) -> Certidao | None:
        """Busca certidão por id."""
        model = self._session.get(CertidaoModel, uuid.UUID(certidao_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def list_by_contribuinte(self, contribuinte_id: str) -> list:
        """Lista certidões de um contribuinte."""
        models = (
            self._session.query(CertidaoModel)
            .filter(
                CertidaoModel.contribuinte_id == contribuinte_id,
                CertidaoModel.is_deleted == False,  # noqa: E712
            )
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: CertidaoModel) -> Certidao:
        return Certidao(
            id=str(model.id),
            contribuinte_id=model.contribuinte_id or "",
            tipo=TipoCertidao(model.tipo or "negativa"),
            numero=model.numero or "",
            data_emissao=model.data_emissao,
            valido_ate=model.valido_ate,
            observacao=model.observacao or "",
            status=StatusCertidao(model.status or "emitida"),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyCertidaoRepository"]