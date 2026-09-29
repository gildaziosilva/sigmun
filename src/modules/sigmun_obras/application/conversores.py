"""Conversores de enumeração textual compartilhados pelos casos de uso do DOM-OBR.

Centralizados para que todos os use cases convertam e validem enums do mesmo
jeito, com a mesma mensagem de erro.
"""

from __future__ import annotations

from typing import TypeVar

from ..domain.entities import (
    FonteRecurso,
    ParecerVistoria,
    SituacaoEtapa,
    SituacaoMedicao,
    SituacaoObra,
    TipoContratacao,
    TipoDespesa,
    TipoEtapa,
    TipoMedicao,
    TipoObra,
    TipoVistoria,
)

E = TypeVar("E")


def _converter(enum_cls: type[E], valor: str, rotulo: str) -> E:
    """Converte um valor textual no enum correspondente, rejeitando desconhecidos."""
    from ..domain.exceptions import RegraNegocioError

    try:
        return enum_cls(valor)  # type: ignore[call-arg]
    except ValueError as exc:
        raise RegraNegocioError(f"{rotulo} inválido: {valor}") from exc


def tipo_obra(valor: str) -> TipoObra:
    """Converte o tipo de obra textual."""
    return _converter(TipoObra, valor, "Tipo de obra")


def situacao_obra(valor: str) -> SituacaoObra:
    """Converte a situação da obra textual."""
    return _converter(SituacaoObra, valor, "Situação da obra")


def tipo_contratacao(valor: str) -> TipoContratacao:
    """Converte o tipo de contratação textual."""
    return _converter(TipoContratacao, valor, "Tipo de contratação")


def fonte_recurso(valor: str) -> FonteRecurso:
    """Converte a fonte de recurso textual."""
    return _converter(FonteRecurso, valor, "Fonte de recurso")


def tipo_medicao(valor: str) -> TipoMedicao:
    """Converte o tipo de medição textual."""
    return _converter(TipoMedicao, valor, "Tipo de medição")


def situacao_medicao(valor: str) -> SituacaoMedicao:
    """Converte a situação da medição textual."""
    return _converter(SituacaoMedicao, valor, "Situação da medição")


def tipo_despesa(valor: str) -> TipoDespesa:
    """Converte o tipo de despesa textual."""
    return _converter(TipoDespesa, valor, "Tipo de despesa")


def tipo_etapa(valor: str) -> TipoEtapa:
    """Converte o tipo de etapa textual."""
    return _converter(TipoEtapa, valor, "Tipo de etapa")


def situacao_etapa(valor: str) -> SituacaoEtapa:
    """Converte a situação da etapa textual."""
    return _converter(SituacaoEtapa, valor, "Situação da etapa")


def tipo_vistoria(valor: str) -> TipoVistoria:
    """Converte o tipo de vistoria textual."""
    return _converter(TipoVistoria, valor, "Tipo de vistoria")


def parecer_vistoria(valor: str) -> ParecerVistoria:
    """Converte o parecer da vistoria textual."""
    return _converter(ParecerVistoria, valor, "Parecer da vistoria")


__all__ = [
    "tipo_obra",
    "situacao_obra",
    "tipo_contratacao",
    "fonte_recurso",
    "tipo_medicao",
    "situacao_medicao",
    "tipo_despesa",
    "tipo_etapa",
    "situacao_etapa",
    "tipo_vistoria",
    "parecer_vistoria",
]
