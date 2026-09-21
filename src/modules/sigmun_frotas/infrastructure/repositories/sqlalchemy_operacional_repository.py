"""Repositórios SQLAlchemy de abastecimentos e manutenções (DOM-FRO)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioAbastecimento, RepositorioManutencao
from ...domain.entities.operacional import (
    Abastecimento,
    Manutencao,
    StatusManutencao,
    TipoManutencao,
)
from ...domain.entities.veiculo import Combustivel
from ..database.models import AbastecimentoModel, ManutencaoModel


class SQLAlchemyAbastecimentoRepository(RepositorioAbastecimento):
    """Persistência de abastecimentos."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, abastecimento: Abastecimento) -> Abastecimento:
        """Persiste um abastecimento."""
        self._session.add(
            AbastecimentoModel(
                id=uuid.UUID(abastecimento.id),
                veiculo_id=abastecimento.veiculo_id,
                data=abastecimento.data,
                quantidade_litros=abastecimento.quantidade_litros,
                valor_unitario=abastecimento.valor_unitario,
                valor_total=abastecimento.valor_total,
                odometro=abastecimento.odometro,
                posto=abastecimento.posto,
                tipo_combustivel=abastecimento.tipo_combustivel.value,
                created_at=abastecimento.created_at,
                created_by=abastecimento.created_by,
            )
        )
        self._session.flush()
        return abastecimento

    def get_by_id(self, abastecimento_id: str) -> Abastecimento | None:
        """Busca abastecimento por id."""
        model = self._session.get(
            AbastecimentoModel, uuid.UUID(abastecimento_id)
        )
        return self._to_entity(model) if model else None

    def list_by_veiculo(self, veiculo_id: str) -> list:
        """Lista abastecimentos de um veículo."""
        models = (
            self._session.query(AbastecimentoModel)
            .filter(AbastecimentoModel.veiculo_id == veiculo_id)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista abastecimentos paginados."""
        models = (
            self._session.query(AbastecimentoModel)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: AbastecimentoModel) -> Abastecimento:
        return Abastecimento(
            id=str(model.id),
            veiculo_id=model.veiculo_id or "",
            data=model.data,
            quantidade_litros=float(model.quantidade_litros or 0),
            valor_unitario=float(model.valor_unitario or 0),
            valor_total=float(model.valor_total or 0),
            odometro=float(model.odometro or 0),
            posto=model.posto or "",
            tipo_combustivel=Combustivel(model.tipo_combustivel or "flex"),
            created_at=model.created_at,
            created_by=model.created_by or "",
        )


class SQLAlchemyManutencaoRepository(RepositorioManutencao):
    """Persistência de manutenções."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, manutencao: Manutencao) -> Manutencao:
        """Persiste uma manutenção."""
        existente = self._session.get(ManutencaoModel, uuid.UUID(manutencao.id))
        if existente is not None:
            existente.status = manutencao.status.value
            existente.data_saida = manutencao.data_saida
        else:
            self._session.add(
                ManutencaoModel(
                    id=uuid.UUID(manutencao.id),
                    veiculo_id=manutencao.veiculo_id,
                    data_entrada=manutencao.data_entrada,
                    data_saida=manutencao.data_saida,
                    tipo=manutencao.tipo.value,
                    descricao=manutencao.descricao,
                    oficina=manutencao.oficina,
                    valor=manutencao.valor,
                    status=manutencao.status.value,
                    created_at=manutencao.created_at,
                    created_by=manutencao.created_by,
                )
            )
        self._session.flush()
        return manutencao

    def get_by_id(self, manutencao_id: str) -> Manutencao | None:
        """Busca manutenção por id."""
        model = self._session.get(ManutencaoModel, uuid.UUID(manutencao_id))
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista manutenções paginadas."""
        models = (
            self._session.query(ManutencaoModel)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: ManutencaoModel) -> Manutencao:
        return Manutencao(
            id=str(model.id),
            veiculo_id=model.veiculo_id or "",
            data_entrada=model.data_entrada,
            data_saida=model.data_saida,
            tipo=TipoManutencao(model.tipo or "preventiva"),
            descricao=model.descricao or "",
            oficina=model.oficina or "",
            valor=float(model.valor or 0),
            status=StatusManutencao(model.status or "aberta"),
            created_at=model.created_at,
            created_by=model.created_by or "",
        )


__all__ = [
    "SQLAlchemyAbastecimentoRepository",
    "SQLAlchemyManutencaoRepository",
]