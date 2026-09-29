"""Repositório SQLAlchemy dos vínculos de propriedade (DOM-IMO)."""

from __future__ import annotations

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioProprietario
from ...domain.entities import ProprietarioImovel, TipoVinculo
from ..database.models import ProprietarioImovelModel
from .imovel import buscar_ou_um
from .imovel import to_uuid


class SQLAlchemyProprietarioRepository(RepositorioProprietario):
    """Persistência dos vínculos pessoa-imóvel."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, proprietario: ProprietarioImovel) -> ProprietarioImovel:
        """Insere ou atualiza um vínculo de propriedade."""
        existente = self._session.get(ProprietarioImovelModel, to_uuid(proprietario.id))
        if existente is not None:
            existente.imovel_id = proprietario.imovel_id
            existente.pessoa_id = proprietario.pessoa_id
            existente.nome = proprietario.nome
            existente.cpf = proprietario.cpf
            existente.vinculo = proprietario.vinculo.value
            existente.principal = proprietario.principal
            existente.updated_at = proprietario.updated_at
            existente.is_deleted = proprietario.is_deleted
        else:
            self._session.add(
                ProprietarioImovelModel(
                    id=to_uuid(proprietario.id),
                    imovel_id=proprietario.imovel_id,
                    pessoa_id=proprietario.pessoa_id,
                    nome=proprietario.nome,
                    cpf=proprietario.cpf,
                    vinculo=proprietario.vinculo.value,
                    principal=proprietario.principal,
                    created_at=proprietario.created_at,
                    updated_at=proprietario.updated_at,
                    created_by=proprietario.created_by,
                    is_deleted=proprietario.is_deleted,
                )
            )
        self._session.flush()
        return proprietario

    def get_by_id(self, vinculo_id: str) -> ProprietarioImovel | None:
        """Busca vínculo por id."""
        model = buscar_ou_um(self._session, ProprietarioImovelModel, vinculo_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_imovel_e_cpf(self, imovel_id: str, cpf: str) -> ProprietarioImovel | None:
        """Busca vínculo pelo imóvel e pelo CPF (RN-IMO-006)."""
        model = (
            self._session.query(ProprietarioImovelModel)
            .filter(
                ProprietarioImovelModel.imovel_id == imovel_id,
                ProprietarioImovelModel.cpf == cpf,
                ProprietarioImovelModel.is_deleted.is_(False),
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def get_principal(self, imovel_id: str) -> ProprietarioImovel | None:
        """Busca o proprietário titular principal do imóvel (RN-IMO-006)."""
        model = (
            self._session.query(ProprietarioImovelModel)
            .filter(
                ProprietarioImovelModel.imovel_id == imovel_id,
                ProprietarioImovelModel.principal.is_(True),
                ProprietarioImovelModel.vinculo == TipoVinculo.TITULAR.value,
                ProprietarioImovelModel.is_deleted.is_(False),
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_by_imovel(self, imovel_id: str) -> list[ProprietarioImovel]:
        """Lista vínculos de um imóvel."""
        models = (
            self._session.query(ProprietarioImovelModel)
            .filter(
                ProprietarioImovelModel.imovel_id == imovel_id,
                ProprietarioImovelModel.is_deleted.is_(False),
            )
            .order_by(ProprietarioImovelModel.nome)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def list_all(self, page: int = 1, page_size: int = 20) -> list[ProprietarioImovel]:
        """Lista vínculos paginados."""
        models = (
            self._session.query(ProprietarioImovelModel)
            .filter(ProprietarioImovelModel.is_deleted.is_(False))
            .order_by(ProprietarioImovelModel.nome)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: ProprietarioImovelModel) -> ProprietarioImovel:
        return ProprietarioImovel(
            id=str(model.id),
            imovel_id=model.imovel_id or "",
            pessoa_id=model.pessoa_id or "",
            nome=model.nome or "",
            cpf=model.cpf or "",
            vinculo=TipoVinculo(model.vinculo or "titular"),
            principal=bool(model.principal),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyProprietarioRepository"]
