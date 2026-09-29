"""Repositórios SQLAlchemy de acompanhamento da obra (DOM-OBR).

Reúne medições, etapas, despesas e vistorias, que compartilham a mesma
convenção de leitura/escrita e a busca tolerante a identificador malformado.
"""

from __future__ import annotations

from datetime import date

from sqlalchemy.orm import Session

from ...application.interfaces import (
    RepositorioDespesa,
    RepositorioEtapa,
    RepositorioMedicao,
    RepositorioVistoria,
)
from ...domain.entities import (
    DespesaObra,
    EtapaObra,
    MedicaoObra,
    ParecerVistoria,
    SituacaoEtapa,
    SituacaoMedicao,
    TipoDespesa,
    TipoEtapa,
    TipoMedicao,
    TipoVistoria,
    VistoriaObra,
)
from ..database.models import (
    DespesaObraModel,
    EtapaObraModel,
    MedicaoObraModel,
    VistoriaObraModel,
)
from .obra import buscar_ou_um, to_uuid


class SQLAlchemyMedicaoRepository(RepositorioMedicao):
    """Persistência de medições físico-financeiras (RN-OBR-005)."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, medicao: MedicaoObra) -> MedicaoObra:
        """Insere ou atualiza uma medição."""
        existente = buscar_ou_um(self._session, MedicaoObraModel, medicao.id)
        if existente is not None:
            existente.obra_id = medicao.obra_id
            existente.numero = medicao.numero
            existente.tipo = medicao.tipo.value
            existente.situacao = medicao.situacao.value
            existente.data = medicao.data
            existente.percentual_fisico = medicao.percentual_fisico
            existente.valor_medido = medicao.valor_medido
            existente.responsavel_tecnico = medicao.responsavel_tecnico
            existente.observacao = medicao.observacao or None
            existente.updated_at = medicao.updated_at
            existente.is_deleted = medicao.is_deleted
        else:
            self._session.add(
                MedicaoObraModel(
                    id=to_uuid(medicao.id),
                    obra_id=medicao.obra_id,
                    numero=medicao.numero,
                    tipo=medicao.tipo.value,
                    situacao=medicao.situacao.value,
                    data=medicao.data,
                    percentual_fisico=medicao.percentual_fisico,
                    valor_medido=medicao.valor_medido,
                    responsavel_tecnico=medicao.responsavel_tecnico,
                    observacao=medicao.observacao or None,
                    created_at=medicao.created_at,
                    updated_at=medicao.updated_at,
                    created_by=medicao.created_by or None,
                    is_deleted=medicao.is_deleted,
                )
            )
        self._session.flush()
        return medicao

    def get_by_id(self, medicao_id: str) -> MedicaoObra | None:
        """Busca medição por id."""
        model = buscar_ou_um(self._session, MedicaoObraModel, medicao_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_numero_obra(self, numero: str, obra_id: str) -> MedicaoObra | None:
        """Busca medição pelo número dentro da obra."""
        model = (
            self._session.query(MedicaoObraModel)
            .filter(
                MedicaoObraModel.numero == numero,
                MedicaoObraModel.obra_id == obra_id,
                MedicaoObraModel.is_deleted.is_(False),
            )
            .first()
        )
        return self._to_entity(model) if model else None

    def list_by_obra(self, obra_id: str) -> list[MedicaoObra]:
        """Lista as medições de uma obra."""
        models = (
            self._session.query(MedicaoObraModel)
            .filter(
                MedicaoObraModel.obra_id == obra_id, MedicaoObraModel.is_deleted.is_(False)
            )
            .order_by(MedicaoObraModel.data, MedicaoObraModel.numero)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: MedicaoObraModel) -> MedicaoObra:
        return MedicaoObra(
            id=str(model.id),
            obra_id=model.obra_id or "",
            numero=model.numero,
            tipo=TipoMedicao(model.tipo or "avanco"),
            situacao=SituacaoMedicao(model.situacao or "registrada"),
            data=model.data or date.today(),
            percentual_fisico=float(model.percentual_fisico or 0),
            valor_medido=float(model.valor_medido or 0),
            responsavel_tecnico=model.responsavel_tecnico or "",
            observacao=model.observacao or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


class SQLAlchemyEtapaRepository(RepositorioEtapa):
    """Persistência de etapas de execução da obra (RN-OBR-007)."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, etapa: EtapaObra) -> EtapaObra:
        """Insere ou atualiza uma etapa."""
        existente = buscar_ou_um(self._session, EtapaObraModel, etapa.id)
        if existente is not None:
            existente.obra_id = etapa.obra_id
            existente.numero = etapa.numero
            existente.descricao = etapa.descricao
            existente.tipo = etapa.tipo.value
            existente.situacao = etapa.situacao.value
            existente.percentual_previsto = etapa.percentual_previsto
            existente.percentual_realizado = etapa.percentual_realizado
            existente.data_inicio_prevista = etapa.data_inicio_prevista
            existente.data_fim_prevista = etapa.data_fim_prevista
            existente.data_conclusao = etapa.data_conclusao
            existente.responsavel = etapa.responsavel
            existente.updated_at = etapa.updated_at
            existente.is_deleted = etapa.is_deleted
        else:
            self._session.add(
                EtapaObraModel(
                    id=to_uuid(etapa.id),
                    obra_id=etapa.obra_id,
                    numero=etapa.numero,
                    descricao=etapa.descricao,
                    tipo=etapa.tipo.value,
                    situacao=etapa.situacao.value,
                    percentual_previsto=etapa.percentual_previsto,
                    percentual_realizado=etapa.percentual_realizado,
                    data_inicio_prevista=etapa.data_inicio_prevista,
                    data_fim_prevista=etapa.data_fim_prevista,
                    data_conclusao=etapa.data_conclusao,
                    responsavel=etapa.responsavel,
                    created_at=etapa.created_at,
                    updated_at=etapa.updated_at,
                    created_by=etapa.created_by or None,
                    is_deleted=etapa.is_deleted,
                )
            )
        self._session.flush()
        return etapa

    def get_by_id(self, etapa_id: str) -> EtapaObra | None:
        """Busca etapa por id."""
        model = buscar_ou_um(self._session, EtapaObraModel, etapa_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def list_by_obra(self, obra_id: str) -> list[EtapaObra]:
        """Lista as etapas de uma obra."""
        models = (
            self._session.query(EtapaObraModel)
            .filter(EtapaObraModel.obra_id == obra_id, EtapaObraModel.is_deleted.is_(False))
            .order_by(EtapaObraModel.numero)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: EtapaObraModel) -> EtapaObra:
        return EtapaObra(
            id=str(model.id),
            obra_id=model.obra_id or "",
            numero=model.numero,
            descricao=model.descricao,
            tipo=TipoEtapa(model.tipo or "estrutura"),
            situacao=SituacaoEtapa(model.situacao or "pendente"),
            percentual_previsto=float(model.percentual_previsto or 0),
            percentual_realizado=float(model.percentual_realizado or 0),
            data_inicio_prevista=model.data_inicio_prevista,
            data_fim_prevista=model.data_fim_prevista,
            data_conclusao=model.data_conclusao,
            responsavel=model.responsavel or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


class SQLAlchemyDespesaRepository(RepositorioDespesa):
    """Persistência de despesas financeiras da obra (RN-OBR-006)."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, despesa: DespesaObra) -> DespesaObra:
        """Insere ou atualiza uma despesa."""
        existente = buscar_ou_um(self._session, DespesaObraModel, despesa.id)
        if existente is not None:
            existente.obra_id = despesa.obra_id
            existente.medicao_id = despesa.medicao_id or None
            existente.descricao = despesa.descricao
            existente.tipo = despesa.tipo.value
            existente.valor = despesa.valor
            existente.data = despesa.data
            existente.documento = despesa.documento or None
            existente.credor = despesa.credor or None
            existente.observacao = despesa.observacao or None
            existente.is_deleted = despesa.is_deleted
        else:
            self._session.add(
                DespesaObraModel(
                    id=to_uuid(despesa.id),
                    obra_id=despesa.obra_id,
                    medicao_id=despesa.medicao_id or None,
                    descricao=despesa.descricao,
                    tipo=despesa.tipo.value,
                    valor=despesa.valor,
                    data=despesa.data,
                    documento=despesa.documento or None,
                    credor=despesa.credor or None,
                    observacao=despesa.observacao or None,
                    created_at=despesa.created_at,
                    created_by=despesa.created_by or None,
                    is_deleted=despesa.is_deleted,
                )
            )
        self._session.flush()
        return despesa

    def get_by_id(self, despesa_id: str) -> DespesaObra | None:
        """Busca despesa por id."""
        model = buscar_ou_um(self._session, DespesaObraModel, despesa_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def list_by_obra(self, obra_id: str) -> list[DespesaObra]:
        """Lista as despesas de uma obra."""
        models = (
            self._session.query(DespesaObraModel)
            .filter(DespesaObraModel.obra_id == obra_id, DespesaObraModel.is_deleted.is_(False))
            .order_by(DespesaObraModel.data)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: DespesaObraModel) -> DespesaObra:
        return DespesaObra(
            id=str(model.id),
            obra_id=model.obra_id or "",
            medicao_id=model.medicao_id or "",
            descricao=model.descricao,
            tipo=TipoDespesa(model.tipo or "medicao"),
            valor=float(model.valor or 0),
            data=model.data or date.today(),
            documento=model.documento or "",
            credor=model.credor or "",
            observacao=model.observacao or "",
            created_at=model.created_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


class SQLAlchemyVistoriaRepository(RepositorioVistoria):
    """Persistência de vistorias fiscalizadoras da obra (RN-OBR-008)."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, vistoria: VistoriaObra) -> VistoriaObra:
        """Insere uma vistoria (vistoriar é evento imutável)."""
        existente = buscar_ou_um(self._session, VistoriaObraModel, vistoria.id)
        if existente is not None:
            existente.data = vistoria.data
            existente.tipo = vistoria.tipo.value
            existente.parecer = vistoria.parecer.value
            existente.percentual_fisico_verificado = vistoria.percentual_fisico_verificado
            existente.fiscal = vistoria.fiscal
            existente.observacao = vistoria.observacao or None
            existente.is_deleted = vistoria.is_deleted
        else:
            self._session.add(
                VistoriaObraModel(
                    id=to_uuid(vistoria.id),
                    obra_id=vistoria.obra_id,
                    data=vistoria.data,
                    tipo=vistoria.tipo.value,
                    parecer=vistoria.parecer.value,
                    percentual_fisico_verificado=vistoria.percentual_fisico_verificado,
                    fiscal=vistoria.fiscal,
                    observacao=vistoria.observacao or None,
                    created_at=vistoria.created_at,
                    created_by=vistoria.created_by or None,
                    is_deleted=vistoria.is_deleted,
                )
            )
        self._session.flush()
        return vistoria

    def get_by_id(self, vistoria_id: str) -> VistoriaObra | None:
        """Busca vistoria por id."""
        model = buscar_ou_um(self._session, VistoriaObraModel, vistoria_id)
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def list_by_obra(self, obra_id: str) -> list[VistoriaObra]:
        """Lista as vistorias de uma obra."""
        models = (
            self._session.query(VistoriaObraModel)
            .filter(VistoriaObraModel.obra_id == obra_id, VistoriaObraModel.is_deleted.is_(False))
            .order_by(VistoriaObraModel.data)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: VistoriaObraModel) -> VistoriaObra:
        return VistoriaObra(
            id=str(model.id),
            obra_id=model.obra_id or "",
            data=model.data or date.today(),
            tipo=TipoVistoria(model.tipo or "periodica"),
            parecer=ParecerVistoria(model.parecer or "aprovado"),
            percentual_fisico_verificado=float(model.percentual_fisico_verificado or 0),
            fiscal=model.fiscal or "",
            observacao=model.observacao or "",
            created_at=model.created_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


__all__ = [
    "SQLAlchemyMedicaoRepository",
    "SQLAlchemyEtapaRepository",
    "SQLAlchemyDespesaRepository",
    "SQLAlchemyVistoriaRepository",
]
