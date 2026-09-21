"""Repositório SQLAlchemy de imóveis (DOM-TRI)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioImovel
from ...domain.entities.imovel import Imovel, StatusImovel
from ..database.models import ImovelModel


class SQLAlchemyImovelRepository(RepositorioImovel):
    """Persistência de imóveis."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, imovel: Imovel) -> Imovel:
        """Insere ou atualiza um imóvel."""
        existente = self._session.get(ImovelModel, uuid.UUID(imovel.id))
        if existente is not None:
            existente.contribuinte_id = imovel.contribuinte_id
            existente.inscricao_imobiliaria = imovel.inscricao_imobiliaria
            existente.logradouro = imovel.logradouro
            existente.numero = imovel.numero
            existente.bairro = imovel.bairro
            existente.cidade = imovel.cidade
            existente.uf = imovel.uf
            existente.cep = imovel.cep
            existente.area_terreno = imovel.area_terreno
            existente.area_construida = imovel.area_construida
            existente.valor_venal = imovel.valor_venal
            existente.aliquota = imovel.aliquota
            existente.status = imovel.status.value
            existente.updated_at = imovel.updated_at
            existente.is_deleted = imovel.is_deleted
        else:
            self._session.add(
                ImovelModel(
                    id=uuid.UUID(imovel.id),
                    contribuinte_id=imovel.contribuinte_id,
                    inscricao_imobiliaria=imovel.inscricao_imobiliaria,
                    logradouro=imovel.logradouro,
                    numero=imovel.numero,
                    bairro=imovel.bairro,
                    cidade=imovel.cidade,
                    uf=imovel.uf,
                    cep=imovel.cep,
                    area_terreno=imovel.area_terreno,
                    area_construida=imovel.area_construida,
                    valor_venal=imovel.valor_venal,
                    aliquota=imovel.aliquota,
                    created_at=imovel.created_at,
                    updated_at=imovel.updated_at,
                    created_by=imovel.created_by,
                    is_deleted=imovel.is_deleted,
                )
            )
        self._session.flush()
        return imovel

    def get_by_id(self, imovel_id: str) -> Imovel | None:
        """Busca imóvel por id."""
        model = self._session.get(ImovelModel, uuid.UUID(imovel_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_inscricao(self, inscricao: str) -> Imovel | None:
        """Busca imóvel por inscrição imobiliária."""
        model = (
            self._session.query(ImovelModel)
            .filter(
                ImovelModel.inscricao_imobiliaria == inscricao,
                ImovelModel.is_deleted == False,  # noqa: E712
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista imóveis paginados."""
        models = (
            self._session.query(ImovelModel)
            .filter(ImovelModel.is_deleted == False)  # noqa: E712
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: ImovelModel) -> Imovel:
        return Imovel(
            id=str(model.id),
            contribuinte_id=model.contribuinte_id or "",
            inscricao_imobiliaria=model.inscricao_imobiliaria or "",
            logradouro=model.logradouro or "",
            numero=model.numero or "",
            bairro=model.bairro or "",
            cidade=model.cidade or "",
            uf=model.uf or "",
            cep=model.cep or "",
            area_terreno=float(model.area_terreno or 0),
            area_construida=float(model.area_construida or 0),
            valor_venal=float(model.valor_venal or 0),
            aliquota=float(model.aliquota or 0),
            status=StatusImovel(model.status or "ativo"),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyImovelRepository"]