"""Implementação SQLAlchemy do repositório de Unidades Administrativas.

Implementa o contrato ``UnidadeAdministrativaRepository`` sobre a tabela
``core.unidades_administrativas`` (migration 20260820_01).

Observações de projeto:
  - O repositório executa ``flush`` (não ``commit``); a transação é
    controlada pela sessão da requisição (ver core get_db).
  - RN-CUM-008: a verificação de ciclos de hierarquia percorre a
    cadeia de ancestrais (profundidade limitada).
  - RN-CUM-009: a unicidade de sigla/códigos considera também registros
    logicamente excluídos, espelhando as constraints UNIQUE da tabela.
"""

from __future__ import annotations

import builtins
import logging
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.sigmun_cadastro.domain.entities.unidade_administrativa import (
    UnidadeAdministrativa,
)
from src.modules.sigmun_cadastro.domain.exceptions import CicloHierarquiaError
from src.modules.sigmun_cadastro.domain.repositories.unidade_administrativa_repository import (
    UnidadeAdministrativaRepository,
)
from src.modules.sigmun_cadastro.infrastructure.database.models import (
    UnidadeAdministrativaModel,
)

logger = logging.getLogger(__name__)


def _to_entity(model: UnidadeAdministrativaModel) -> UnidadeAdministrativa:
    """Converte um registro ORM em entidade de domínio."""
    return UnidadeAdministrativa(
        id=model.id,
        nome=model.nome,
        unidade_pai_id=model.unidade_pai_id,
        codigo_ibge=model.codigo_ibge,
        codigo_siafi=model.codigo_siafi,
        sigla=model.sigla,
        created_at=model.created_at,
        created_by=model.created_by,
        updated_at=model.updated_at,
        updated_by=model.updated_by,
        deleted_at=model.deleted_at,
        deleted_by=model.deleted_by,
    )


class SqlAlchemyUnidadeAdministrativaRepository(UnidadeAdministrativaRepository):
    """Repositório de unidades administrativas persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    # -- Helpers -----------------------------------------------------------------

    def _get_model(
        self, unidade_id: UUID, *, include_deleted: bool = False
    ) -> UnidadeAdministrativaModel | None:
        model = self._session.get(UnidadeAdministrativaModel, unidade_id)
        if model is None:
            return None
        if not include_deleted and model.deleted_at is not None:
            return None
        return model

    def _garantir_sem_ciclo(self, unidade: UnidadeAdministrativa) -> None:
        """Valida que a unidade não cria ciclo na hierarquia (RN-CUM-008)."""
        if unidade.unidade_pai_id is None:
            return
        if unidade.unidade_pai_id == unidade.id:
            raise CicloHierarquiaError(
                "Unidade não pode ser pai de si mesma (RN-CUM-008)"
            )
        ancestrais = self.get_ancestral_ids(unidade.unidade_pai_id)
        if unidade.id in ancestrais:
            raise CicloHierarquiaError(
                f"Alteração criaria ciclo na hierarquia de unidades (RN-CUM-008): "
                f"{unidade.id} é ancestral do pai informado"
            )

    # -- Contrato do domínio -------------------------------------------------------

    def save(self, unidade: UnidadeAdministrativa) -> UnidadeAdministrativa:
        self._garantir_sem_ciclo(unidade)
        model = self._get_model(unidade.id, include_deleted=True)
        if model is None:
            model = UnidadeAdministrativaModel(
                id=unidade.id,
                nome=unidade.nome,
                unidade_pai_id=unidade.unidade_pai_id,
                codigo_ibge=unidade.codigo_ibge,
                codigo_siafi=unidade.codigo_siafi,
                sigla=unidade.sigla,
                created_at=unidade.created_at,
                created_by=unidade.created_by,
                updated_at=unidade.updated_at,
                updated_by=unidade.updated_by,
                deleted_at=unidade.deleted_at,
                deleted_by=unidade.deleted_by,
            )
            self._session.add(model)
            logger.info("Unidade administrativa inserida: %s", unidade.id)
        else:
            model.nome = unidade.nome
            model.unidade_pai_id = unidade.unidade_pai_id
            model.codigo_ibge = unidade.codigo_ibge
            model.codigo_siafi = unidade.codigo_siafi
            model.sigla = unidade.sigla
            model.updated_at = unidade.updated_at
            model.updated_by = unidade.updated_by
            model.deleted_at = unidade.deleted_at
            model.deleted_by = unidade.deleted_by
            logger.info("Unidade administrativa atualizada: %s", unidade.id)
        self._session.flush()
        self._session.refresh(model)
        return _to_entity(model)

    def get_by_id(
        self, unidade_id: UUID, *, include_deleted: bool = False
    ) -> UnidadeAdministrativa | None:
        model = self._get_model(unidade_id, include_deleted=include_deleted)
        return _to_entity(model) if model else None

    def get_by_sigla(self, sigla: str) -> UnidadeAdministrativa | None:
        model = self._session.scalars(
            select(UnidadeAdministrativaModel).where(
                UnidadeAdministrativaModel.sigla == sigla,
                UnidadeAdministrativaModel.deleted_at.is_(None),
            )
        ).first()
        return _to_entity(model) if model else None

    def list(
        self,
        *,
        include_deleted: bool = False,
        limit: int | None = None,
        offset: int = 0,
    ) -> builtins.list[UnidadeAdministrativa]:
        stmt = select(UnidadeAdministrativaModel).order_by(UnidadeAdministrativaModel.nome)
        if not include_deleted:
            stmt = stmt.where(UnidadeAdministrativaModel.deleted_at.is_(None))
        if limit is not None:
            stmt = stmt.limit(limit)
        if offset:
            stmt = stmt.offset(offset)
        models = self._session.scalars(stmt).all()
        return [_to_entity(m) for m in models]

    def delete(self, unidade_id: UUID, usuario_id: UUID) -> None:
        """Soft-delete da unidade (RN-CUM-007).

        ``deleted_at`` é gerado pelo servidor do banco (``NOW()``) para
        satisfazer a constraint ``ck_unidades_administrativas_deleted``.
        """
        model = self._get_model(unidade_id, include_deleted=True)
        if model is None or model.deleted_at is not None:
            return
        model.deleted_at = func.now()
        model.deleted_by = usuario_id
        self._session.flush()
        logger.info("Unidade administrativa marcada como excluída: %s", unidade_id)

    def exists_sigla(self, sigla: str, *, exclude_id: UUID | None = None) -> bool:
        """RN-CUM-009: espelha a UNIQUE da tabela (inclui excluídos)."""
        stmt = select(UnidadeAdministrativaModel.id).where(
            UnidadeAdministrativaModel.sigla == sigla
        )
        if exclude_id is not None:
            stmt = stmt.where(UnidadeAdministrativaModel.id != exclude_id)
        return self._session.scalars(stmt.limit(1)).first() is not None

    def exists_codigo_ibge(self, codigo_ibge: str, *, exclude_id: UUID | None = None) -> bool:
        """RN-CUM-009: espelha a UNIQUE da tabela (inclui excluídos)."""
        stmt = select(UnidadeAdministrativaModel.id).where(
            UnidadeAdministrativaModel.codigo_ibge == codigo_ibge
        )
        if exclude_id is not None:
            stmt = stmt.where(UnidadeAdministrativaModel.id != exclude_id)
        return self._session.scalars(stmt.limit(1)).first() is not None

    def exists_codigo_siafi(self, codigo_siafi: str, *, exclude_id: UUID | None = None) -> bool:
        """RN-CUM-009: espelha a UNIQUE da tabela (inclui excluídos)."""
        stmt = select(UnidadeAdministrativaModel.id).where(
            UnidadeAdministrativaModel.codigo_siafi == codigo_siafi
        )
        if exclude_id is not None:
            stmt = stmt.where(UnidadeAdministrativaModel.id != exclude_id)
        return self._session.scalars(stmt.limit(1)).first() is not None

    def get_ancestral_ids(self, unidade_id: UUID, *, max_depth: int = 32) -> list[UUID]:
        """Cadeia de ancestrais (do pai até a raiz), com profundidade limitada.

        Proteção adicional contra ciclos já persistidos: interrompe a
        subida quando um ancestral se repete.
        """
        ancestrais: list[UUID] = []
        atual = self._get_model(unidade_id, include_deleted=True)
        while (
            atual is not None
            and atual.unidade_pai_id is not None
            and len(ancestrais) < max_depth
        ):
            pai_id = atual.unidade_pai_id
            if pai_id in ancestrais:
                break
            ancestrais.append(pai_id)
            atual = self._session.get(UnidadeAdministrativaModel, pai_id)
        return ancestrais

    def tem_filhas_ativas(self, unidade_id: UUID) -> bool:
        """Indica se a unidade possui unidades filhas não excluídas."""
        stmt = (
            select(UnidadeAdministrativaModel.id)
            .where(
                UnidadeAdministrativaModel.unidade_pai_id == unidade_id,
                UnidadeAdministrativaModel.deleted_at.is_(None),
            )
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None


__all__ = ["SqlAlchemyUnidadeAdministrativaRepository"]
