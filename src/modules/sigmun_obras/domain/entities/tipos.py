"""Enumerations e validações do DOM-OBR — Obras e Infraestrutura.

Concentradas em módulo próprio para evitar duplicação entre as entidades
`Obra`, `EtapaObra`, `MedicaoObra`, `DespesaObra` e `VistoriaObra`.
"""

from __future__ import annotations

from enum import Enum

# Tolerância (em pontos percentuais) entre o avanço físico e o financeiro.
# O físico pode adiantar o financeiro em obras com medição por etapa, mas não
# o contrário: não se mede financeiramente o que ainda não foi executado.
TOLERANCIA_AVANCO_PERCENT = 0.01


class TipoObra(Enum):
    """Natureza da obra pública municipal."""

    PAVIMENTACAO = "pavimentacao"
    DRENAGEM = "drenagem"
    CONSTRUCAO = "construcao"
    REFORMA = "reforma"
    ILUMINACAO = "iluminacao"
    SANEAMENTO = "saneamento"
    PONTE = "ponte"
    PRACA = "praca"
    QUADRA = "quadra"
    OUTRO = "outro"


class SituacaoObra(Enum):
    """Ciclo de vida da obra pública (RN-OBR-002)."""

    PLANEJADA = "planejada"
    EM_LICITACAO = "em_licitacao"
    CONTRATADA = "contratada"
    EM_EXECUCAO = "em_execucao"
    SUSPENSA = "suspensa"
    CONCLUIDA = "concluida"
    CANCELADA = "cancelada"


class FonteRecurso(Enum):
    """Origem do recurso financeiro da obra (RN-OBR-004)."""

    ORCAMENTO_PROPRIO = "orcamento_proprio"
    CONVENIO = "convenio"
    CONVENIO_ESTADUAL = "convenio_estadual"
    CONVENIO_FEDERAL = "convenio_federal"
    TRANSFERENCIA = "transferencia"
    OPERACAO_CREDITO = "operacao_credito"
    OUTRO = "outro"


class TipoContratacao(Enum):
    """Modalidade de contratação da obra (RN-OBR-003)."""

    LICITACAO = "licitacao"
    DISPENSA = "dispensa"
    INEXIGIBILIDADE = "inexigibilidade"
    CONVENIO = "convenio"
    CONTRATO_DIRETO = "contrato_direto"


class TipoMedicao(Enum):
    """Tipo de medição física-financeira da obra (RN-OBR-005)."""

    AVANCO = "avanco"
    ETAPA = "etapa"
    FINAL = "final"
    REVISIONAL = "revisional"


class SituacaoMedicao(Enum):
    """Ciclo de vida da medição de obra (RN-OBR-005)."""

    REGISTRADA = "registrada"
    CONFERIDA = "conferida"
    APROVADA = "aprovada"
    GLOSADA = "glosada"
    CANCELADA = "cancelada"


class TipoDespesa(Enum):
    """Natureza do desembolso financeiro da obra (RN-OBR-006)."""

    MEDICAO = "medicao"
    REPASSE = "repasse"
    MATERIAL = "material"
    MAO_DE_OBRA = "mao_de_obra"
    TRIBUTOS = "tributos"
    CUSTOS = "custos"
    OUTRO = "outro"


class TipoEtapa(Enum):
    """Fase da obra fisikicamente verificável (RN-OBR-007)."""

    PROJETO = "projeto"
    TERRAPLANAGEM = "terraplanagem"
    FUNDACAO = "fundacao"
    ESTRUTURA = "estrutura"
    ACABAMENTO = "acabamento"
    INSTALACAO = "instalacao"
    PAVIMENTACAO = "pavimentacao"
    PAISAGISMO = "paisagismo"
    RECEPCAO = "recepcao"


class SituacaoEtapa(Enum):
    """Ciclo de vida da etapa de obra (RN-OBR-007)."""

    PENDENTE = "pendente"
    EM_EXECUCAO = "em_execucao"
    CONCLUIDA = "concluida"
    ATRASADA = "atrasada"
    CANCELADA = "cancelada"


class TipoVistoria(Enum):
    """Modalidade de vistoria fiscalizadora da obra (RN-OBR-008)."""

    PERIODICA = "periodica"
    PARCIAL = "parcial"
    FINAL = "final"
    RECEPCAO = "recepcao"


class ParecerVistoria(Enum):
    """Parecer do fiscal de obra sobre a vistoria (RN-OBR-008)."""

    APROVADO = "aprovado"
    APROVADO_COM_RESSALVAS = "aprovado_com_ressalvas"
    REPROVADO = "reprovado"


def validar_percentual(valor: float, rotulo: str) -> None:
    """Valida um percentual no intervalo 0..100."""
    from ..exceptions import RegraNegocioError

    if not 0.0 <= valor <= 100.0:
        raise RegraNegocioError(f"{rotulo} deve estar entre 0 e 100 (RN-OBR-005)")


def validar_valor(valor: float, rotulo: str) -> None:
    """Valida um valor monetário não negativo."""
    from ..exceptions import RegraNegocioError

    if valor < 0:
        raise RegraNegocioError(f"{rotulo} não pode ser negativo (RN-OBR-004)")


__all__ = [
    "TOLERANCIA_AVANCO_PERCENT",
    "TipoObra",
    "SituacaoObra",
    "FonteRecurso",
    "TipoContratacao",
    "TipoMedicao",
    "SituacaoMedicao",
    "TipoDespesa",
    "TipoEtapa",
    "SituacaoEtapa",
    "TipoVistoria",
    "ParecerVistoria",
    "validar_percentual",
    "validar_valor",
]
