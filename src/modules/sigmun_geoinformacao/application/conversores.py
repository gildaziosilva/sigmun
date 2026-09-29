"""Conversores de enumeração textual shared pelos casos de uso do DOM-GEO.

Centralizados para que todos os use cases convertam e validem enums do mesmo
jeito, com a mesma mensagem de erro.
"""

from __future__ import annotations

from typing import TypeVar

from ..domain.entities import (
    DatumGeografico,
    FormatoCamada,
    SituacaoCamadaMapa,
    SituacaoMapaSig,
    SituacaoServicoGeo,
    TipoCamadaMapa,
    TipoGeometria,
    TipoMapaSig,
    TipoServicoGeo,
)

E = TypeVar("E")


def _converter(enum_cls: type[E], valor: str, rotulo: str) -> E:
    """Converte um valor textual no enum correspondente, rejeitando desconhecidos."""
    from ..domain.exceptions import RegraNegocioError

    try:
        return enum_cls(valor)  # type: ignore[call-arg]
    except ValueError as exc:
        raise RegraNegocioError(f"{rotulo} inválido: {valor}") from exc


def tipo_camada(valor: str) -> TipoCamadaMapa:
    """Converte o tipo de camada textual."""
    return _converter(TipoCamadaMapa, valor, "Tipo de camada")


def formato_camada(valor: str) -> FormatoCamada:
    """Converte o formato de camada textual."""
    return _converter(FormatoCamada, valor, "Formato de camada")


def situacao_camada(valor: str) -> SituacaoCamadaMapa:
    """Converte a situação de camada textual."""
    return _converter(SituacaoCamadaMapa, valor, "Situação da camada")


def tipo_mapa(valor: str) -> TipoMapaSig:
    """Converte o tipo de mapa textual."""
    return _converter(TipoMapaSig, valor, "Tipo de mapa")


def situacao_mapa(valor: str) -> SituacaoMapaSig:
    """Converte a situação de mapa textual."""
    return _converter(SituacaoMapaSig, valor, "Situação do mapa")


def geometria(valor: str) -> TipoGeometria:
    """Converte o tipo de geometria textual."""
    return _converter(TipoGeometria, valor, "Tipo de geometria")


def datum(valor: str) -> DatumGeografico:
    """Converte o datum geodésico textual."""
    return _converter(DatumGeografico, valor, "Datum geodésico")


def tipo_servico(valor: str) -> TipoServicoGeo:
    """Converte o tipo de serviço geoespacial textual."""
    return _converter(TipoServicoGeo, valor, "Tipo de serviço geoespacial")


def situacao_servico(valor: str) -> SituacaoServicoGeo:
    """Converte a situação do serviço geoespacial textual."""
    return _converter(SituacaoServicoGeo, valor, "Situação do serviço geoespacial")


__all__ = [
    "tipo_camada",
    "formato_camada",
    "situacao_camada",
    "tipo_mapa",
    "situacao_mapa",
    "geometria",
    "datum",
    "tipo_servico",
    "situacao_servico",
]
