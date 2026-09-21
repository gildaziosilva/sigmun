"""Repositório SQLAlchemy de veículos (DOM-FRO)."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import RepositorioVeiculo
from ...domain.entities.veiculo import (
    Combustivel,
    StatusVeiculo,
    TipoVeiculo,
    Veiculo,
)
from ..database.models import VeiculoModel


class SQLAlchemyVeiculoRepository(RepositorioVeiculo):
    """Persistência de veículos."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, veiculo: Veiculo) -> Veiculo:
        """Insere ou atualiza um veículo."""
        existente = self._session.get(VeiculoModel, uuid.UUID(veiculo.id))
        if existente is not None:
            existente.placa = veiculo.placa
            existente.chassi = veiculo.chassi
            existente.renavam = veiculo.renavam
            existente.marca = veiculo.marca
            existente.modelo = veiculo.modelo
            existente.ano_fabricacao = veiculo.ano_fabricacao
            existente.ano_modelo = veiculo.ano_modelo
            existente.tipo = veiculo.tipo.value
            existente.combustivel = veiculo.combustivel.value
            existente.capacidade = veiculo.capacidade
            existente.odometro_atual = veiculo.odometro_atual
            existente.status = veiculo.status.value
            existente.unidade_id = veiculo.unidade_id
            existente.updated_at = veiculo.updated_at
            existente.is_deleted = veiculo.is_deleted
        else:
            self._session.add(
                VeiculoModel(
                    id=uuid.UUID(veiculo.id),
                    placa=veiculo.placa,
                    chassi=veiculo.chassi,
                    renavam=veiculo.renavam,
                    marca=veiculo.marca,
                    modelo=veiculo.modelo,
                    ano_fabricacao=veiculo.ano_fabricacao,
                    ano_modelo=veiculo.ano_modelo,
                    tipo=veiculo.tipo.value,
                    combustivel=veiculo.combustivel.value,
                    capacidade=veiculo.capacidade,
                    odometro_atual=veiculo.odometro_atual,
                    status=veiculo.status.value,
                    unidade_id=veiculo.unidade_id,
                    created_at=veiculo.created_at,
                    updated_at=veiculo.updated_at,
                    created_by=veiculo.created_by,
                    is_deleted=veiculo.is_deleted,
                )
            )
        self._session.flush()
        return veiculo

    def get_by_id(self, veiculo_id: str) -> Veiculo | None:
        """Busca veículo por id."""
        model = self._session.get(VeiculoModel, uuid.UUID(veiculo_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_placa(self, placa: str) -> Veiculo | None:
        """Busca veículo pela placa."""
        model = (
            self._session.query(VeiculoModel)
            .filter(
                VeiculoModel.placa == placa,
                VeiculoModel.is_deleted == False,  # noqa: E712
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista veículos paginados."""
        models = (
            self._session.query(VeiculoModel)
            .filter(VeiculoModel.is_deleted == False)  # noqa: E712
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: VeiculoModel) -> Veiculo:
        return Veiculo(
            id=str(model.id),
            placa=model.placa or "",
            chassi=model.chassi or "",
            renavam=model.renavam or "",
            marca=model.marca or "",
            modelo=model.modelo or "",
            ano_fabricacao=model.ano_fabricacao or 0,
            ano_modelo=model.ano_modelo or 0,
            tipo=TipoVeiculo(model.tipo or "leve"),
            combustivel=Combustivel(model.combustivel or "flex"),
            capacidade=float(model.capacidade or 0),
            odometro_atual=float(model.odometro_atual or 0),
            status=StatusVeiculo(model.status or "ativo"),
            unidade_id=model.unidade_id or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = ["SQLAlchemyVeiculoRepository"]