"""Dependências e conversores compartilhados pelos endpoints do DOM-OBR."""

from __future__ import annotations

from typing import Annotated, Any, Protocol

from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db

from ...application.interfaces import (
    RepositorioDespesa,
    RepositorioEtapa,
    RepositorioMedicao,
    RepositorioObra,
    RepositorioVistoria,
)
from ...domain.entities import DespesaObra, EtapaObra, MedicaoObra, Obra, VistoriaObra
from ...infrastructure.repositories import (
    SQLAlchemyDespesaRepository,
    SQLAlchemyEtapaRepository,
    SQLAlchemyMedicaoRepository,
    SQLAlchemyObraRepository,
    SQLAlchemyVistoriaRepository,
)
from ..schemas import (
    DespesaResponse,
    EtapaResponse,
    MedicaoResponse,
    ObraResponse,
    VistoriaResponse,
)


class RepoComId(Protocol):
    """Port mínimo com busca por identificador."""

    def get_by_id(self, entidade_id: str) -> Any:
        """Busca a entidade pelo identificador."""
        ...


def get_obra_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioObra:
    """Fornece o port de obras."""
    return SQLAlchemyObraRepository(session)


def get_medicao_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioMedicao:
    """Fornece o port de medições."""
    return SQLAlchemyMedicaoRepository(session)


def get_despesa_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioDespesa:
    """Fornece o port de despesas."""
    return SQLAlchemyDespesaRepository(session)


def get_etapa_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioEtapa:
    """Fornece o port de etapas."""
    return SQLAlchemyEtapaRepository(session)


def get_vistoria_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioVistoria:
    """Fornece o port de vistorias."""
    return SQLAlchemyVistoriaRepository(session)


def obter(repo: RepoComId, entidade_id: str) -> Any:
    """Busca por id tolerando UUID malformado (evita 500 em input inválido)."""
    try:
        return repo.get_by_id(entidade_id)
    except (ValueError, AttributeError):
        return None


def to_obra(o: Obra) -> ObraResponse:
    """Converte a entidade de obra na resposta da API."""
    return ObraResponse(
        id=o.id,
        numero=o.numero,
        nome=o.nome,
        descricao=o.descricao,
        tipo=o.tipo.value,
        situacao=o.situacao.value,
        tipo_contratacao=o.tipo_contratacao.value,
        fonte_recurso=o.fonte_recurso.value,
        valor_orcado=o.valor_orcado,
        valor_contratado=o.valor_contratado,
        valor_mediado=o.valor_mediado,
        valor_pago=o.valor_pago,
        percentual_fisico=o.percentual_fisico,
        percentual_financeiro=o.percentual_financeiro,
        empresa_contratada=o.empresa_contratada,
        numero_contrato=o.numero_contrato,
        responsavel_tecnico=o.responsavel_tecnico,
        endereco=o.endereco,
        bairro=o.bairro,
        data_inicio_prevista=o.data_inicio_prevista,
        data_fim_prevista=o.data_fim_prevista,
        data_inicio_real=o.data_inicio_real,
        data_fim_real=o.data_fim_real,
        observacao=o.observacao,
        created_at=o.created_at,
        updated_at=o.updated_at,
    )


def to_medicao(m: MedicaoObra) -> MedicaoResponse:
    """Converte a entidade de medição na resposta da API."""
    return MedicaoResponse(
        id=m.id,
        obra_id=m.obra_id,
        numero=m.numero,
        tipo=m.tipo.value,
        situacao=m.situacao.value,
        data=m.data,
        percentual_fisico=m.percentual_fisico,
        valor_medido=m.valor_medido,
        responsavel_tecnico=m.responsavel_tecnico,
        observacao=m.observacao,
        created_at=m.created_at,
        updated_at=m.updated_at,
    )


def to_despesa(d: DespesaObra) -> DespesaResponse:
    """Converte a entidade de despesa na resposta da API."""
    return DespesaResponse(
        id=d.id,
        obra_id=d.obra_id,
        medicao_id=d.medicao_id,
        descricao=d.descricao,
        tipo=d.tipo.value,
        valor=d.valor,
        data=d.data,
        documento=d.documento,
        credor=d.credor,
        observacao=d.observacao,
        created_at=d.created_at,
    )


def to_etapa(e: EtapaObra) -> EtapaResponse:
    """Converte a entidade de etapa na resposta da API."""
    return EtapaResponse(
        id=e.id,
        obra_id=e.obra_id,
        numero=e.numero,
        descricao=e.descricao,
        tipo=e.tipo.value,
        situacao=e.situacao.value,
        percentual_previsto=e.percentual_previsto,
        percentual_realizado=e.percentual_realizado,
        data_inicio_prevista=e.data_inicio_prevista,
        data_fim_prevista=e.data_fim_prevista,
        data_conclusao=e.data_conclusao,
        responsavel=e.responsavel,
        created_at=e.created_at,
        updated_at=e.updated_at,
    )


def to_vistoria(v: VistoriaObra) -> VistoriaResponse:
    """Converte a entidade de vistoria na resposta da API."""
    return VistoriaResponse(
        id=v.id,
        obra_id=v.obra_id,
        data=v.data,
        tipo=v.tipo.value,
        parecer=v.parecer.value,
        percentual_fisico_verificado=v.percentual_fisico_verificado,
        fiscal=v.fiscal,
        observacao=v.observacao,
        created_at=v.created_at,
    )


__all__ = [
    "get_obra_repo",
    "get_medicao_repo",
    "get_despesa_repo",
    "get_etapa_repo",
    "get_vistoria_repo",
    "obter",
    "to_obra",
    "to_medicao",
    "to_despesa",
    "to_etapa",
    "to_vistoria",
]
