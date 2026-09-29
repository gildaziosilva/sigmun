"""Repositório SQLAlchemy das unidades imobiliárias (DOM-IMO)."""

from __future__ import annotations

import uuid
from typing import TypeVar

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioImovel
from ...domain.entities import Imovel, SituacaoImovel, TipoImovel, TipoPropriedade
from ..database.models import ImovelModel


def to_uuid(valor: str) -> uuid.UUID | None:
    """Converte o identificador textual em UUID.

    Retorna `None` quando o valor não é um UUID válido. O identificador é opaco
    na borda HTTP, então um valor malformado equivale a um recurso inexistente:
    propagar `ValueError` aqui produziria HTTP 500 nas operações de escrita,
    que não traduzem essa exceção. Com `None`, os repositórios seguem o mesmo
    caminho de "não encontrado" e a API responde 404.
    """
    try:
        return uuid.UUID(valor)
    except (ValueError, AttributeError, TypeError):
        return None


T = TypeVar("T")


def buscar_ou_um(session: Session, model: type[T], valor: str) -> T | None:
    """Busca a linha pelo identificador, tolerando valor malformado.

    `session.get` exige uma chave primária válida; um identificador opaco que
    não é UUID equivale a registro inexistente e devolve `None`.
    """
    chave = to_uuid(valor)
    if chave is None:
        return None
    return session.get(model, chave)


class SQLAlchemyImovelRepository(RepositorioImovel):
    """Persistência das unidades imobiliárias."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, imovel: Imovel) -> Imovel:
        """Insere ou atualiza uma unidade imobiliária."""
        existente = self._session.get(ImovelModel, to_uuid(imovel.id))
        if existente is not None:
            existente.inscricao_imobiliaria = imovel.inscricao_imobiliaria
            existente.logradouro_id = imovel.logradouro_id
            existente.bairro_id = imovel.bairro_id
            existente.numero = imovel.numero
            existente.complemento = imovel.complemento
            existente.tipo = imovel.tipo.value
            existente.situacao = imovel.situacao.value
            existente.tipo_propriedade = imovel.tipo_propriedade.value
            existente.area_terreno_m2 = imovel.area_terreno_m2
            existente.area_construida_m2 = imovel.area_construida_m2
            existente.ano_construcao = imovel.ano_construcao
            existente.updated_at = imovel.updated_at
            existente.is_deleted = imovel.is_deleted
        else:
            self._session.add(
                ImovelModel(
                    id=to_uuid(imovel.id),
                    inscricao_imobiliaria=imovel.inscricao_imobiliaria,
                    logradouro_id=imovel.logradouro_id,
                    bairro_id=imovel.bairro_id,
                    numero=imovel.numero,
                    complemento=imovel.complemento,
                    tipo=imovel.tipo.value,
                    situacao=imovel.situacao.value,
                    tipo_propriedade=imovel.tipo_propriedade.value,
                    area_terreno_m2=imovel.area_terreno_m2,
                    area_construida_m2=imovel.area_construida_m2,
                    ano_construcao=imovel.ano_construcao,
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
        model = buscar_ou_um(self._session, ImovelModel, imovel_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_inscricao(self, inscricao: str) -> Imovel | None:
        """Busca imóvel pela inscrição imobiliária (RN-IMO-001)."""
        model = (
            self._session.query(ImovelModel)
            .filter(
                ImovelModel.inscricao_imobiliaria == inscricao,
                ImovelModel.is_deleted.is_(False),
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_by_logradouro(self, logradouro_id: str) -> list[Imovel]:
        """Lista imóveis de um logradouro."""
        models = (
            self._session.query(ImovelModel)
            .filter(
                ImovelModel.logradouro_id == logradouro_id,
                ImovelModel.is_deleted.is_(False),
            )
            .order_by(ImovelModel.inscricao_imobiliaria)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def list_by_bairro(self, bairro_id: str) -> list[Imovel]:
        """Lista imóveis de um bairro."""
        models = (
            self._session.query(ImovelModel)
            .filter(
                ImovelModel.bairro_id == bairro_id,
                ImovelModel.is_deleted.is_(False),
            )
            .order_by(ImovelModel.inscricao_imobiliaria)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def list_all(
        self, page: int = 1, page_size: int = 20, situacao: str | None = None
    ) -> list[Imovel]:
        """Lista imóveis paginados, opcionalmente por situação."""
        query = self._session.query(ImovelModel).filter(ImovelModel.is_deleted.is_(False))
        if situacao:
            query = query.filter(ImovelModel.situacao == situacao)
        models = (
            query.order_by(ImovelModel.inscricao_imobiliaria)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: ImovelModel) -> Imovel:
        return Imovel(
            id=str(model.id),
            inscricao_imobiliaria=model.inscricao_imobiliaria or "",
            logradouro_id=model.logradouro_id or "",
            bairro_id=model.bairro_id or "",
            numero=model.numero or "",
            complemento=model.complemento or "",
            tipo=TipoImovel(model.tipo or "lote"),
            situacao=SituacaoImovel(model.situacao or "ativo"),
            tipo_propriedade=TipoPropriedade(model.tipo_propriedade or "proprio"),
            area_terreno_m2=float(model.area_terreno_m2 or 0),
            area_construida_m2=float(model.area_construida_m2 or 0),
            ano_construcao=model.ano_construcao,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyImovelRepository", "to_uuid"]
