"""Enumerações do DOM-IMO — Cadastro Imobiliário."""

from __future__ import annotations

from enum import Enum


class TipoImovel(Enum):
    """Natureza da unidade imobiliária (lote, casa, apartamento, ponto comercial)."""

    LOTE = "lote"
    CASA = "casa"
    APARTAMENTO = "apartamento"
    LOJA = "loja"
    GALPAO = "galpao"
    TERRENO = "terreno"
    OUTRO = "outro"


class SituacaoImovel(Enum):
    """Situação cadastral do imóvel."""

    ATIVO = "ativo"
    INATIVO = "inativo"
    EM_OBRA = "em_obra"
    DESOCUPADO = "desocupado"
    DEMOLIDO = "demolido"


class TipoPropriedade(Enum):
    """Forma de titularidade registrada no cadastro."""

    PROPRIO = "proprio"
    ALUGADO = "alugado"
    CEDIDO = "cedido"
    INVENCIONADO = "invencionado"


class TipoVinculo(Enum):
    """Natureza do vínculo entre pessoa e imóvel."""

    TITULAR = "titular"
    COMODATO = "comodato"
    ARRENDAMENTO = "arrendamento"
    USUFRUTO = "usufruto"
    PARCEIRO = "parceiro"


class TipoObra(Enum):
    """Natureza da construção declarada para o imóvel."""

    RESIDENCIAL = "residencial"
    COMERCIAL = "comercial"
    INDUSTRIAL = "industrial"
    INSTITUCIONAL = "institucional"
    MISTA = "mista"
    NAO_APLICAVEL = "nao_aplicavel"


class SituacaoAvaliacao(Enum):
    """Ciclo de vida da avaliação de valor venal do imóvel (RN-IMO-005)."""

    RASCUNHO = "rascunho"
    CONCLUIDA = "concluida"
    CANCELADA = "cancelada"


# Transições permitidas na situação do imóvel (RN-IMO-004).
_TRANSICOES_SITUACAO: dict[SituacaoImovel, set[SituacaoImovel]] = {
    SituacaoImovel.ATIVO: {
        SituacaoImovel.INATIVO,
        SituacaoImovel.EM_OBRA,
        SituacaoImovel.DESOCUPADO,
        SituacaoImovel.DEMOLIDO,
    },
    SituacaoImovel.INATIVO: {SituacaoImovel.ATIVO},
    SituacaoImovel.EM_OBRA: {SituacaoImovel.ATIVO, SituacaoImovel.DEMOLIDO},
    SituacaoImovel.DESOCUPADO: {SituacaoImovel.ATIVO, SituacaoImovel.INATIVO},
    SituacaoImovel.DEMOLIDO: set(),
}


def transicao_permitida(
    origem: SituacaoImovel, destino: SituacaoImovel
) -> bool:
    """Indica se a mudança de situação do imóvel é admitida (RN-IMO-004)."""
    return destino in _TRANSICOES_SITUACAO[origem]


__all__ = [
    "TipoImovel",
    "SituacaoImovel",
    "TipoPropriedade",
    "TipoVinculo",
    "TipoObra",
    "SituacaoAvaliacao",
    "transicao_permitida",
]
