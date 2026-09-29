"""Entidades do DOM-OBR — Obras e Infraestrutura.

Regras de negócio implementadas (ver também o docstring de cada entidade):
- RN-OBR-001: o número da obra é único no cadastro municipal de obras públicas.
- RN-OBR-002: a obra obedece ao ciclo PLANEJADA -> EM_LICITACAO -> CONTRATADA ->
    EM_EXECUCAO -> CONCLUIDA, com SUSPENSA e CANCELADA disponíveis; obra
    concluída é terminal.
- RN-OBR-003: a contratação exige empresa, tipo de contratação e data de início
    prevista antes do início da execução.
- RN-OBR-004: valores e percentuais de avanço são não negativos; o valor
    contratado não supera o orçado e o avanço financeiro não ultrapassa o físico.
- RN-OBR-005: a medição exige percentual físico entre 0 e 100 e obedece ao
    ciclo REGISTRADA -> CONFERIDA -> APROVADA, com GLOSADA e CANCELADA.
- RN-OBR-006: a despesa exige valor positivo e não pode superar o valor medido.
- RN-OBR-007: a etapa exige responsável, percentual previsto não inferior ao
    realizado e obedece ao ciclo PENDENTE -> EM_EXECUCAO -> CONCLUIDA.
- RN-OBR-008: a vistoria exige fiscal e registra o parecer sobre o avanço físico.
"""

from .despesa import DespesaObra
from .etapa import EtapaObra
from .medicao import MedicaoObra
from .obra import Obra
from .tipos import (
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
    validar_percentual,
    validar_valor,
)
from .vistoria import VistoriaObra

__all__ = [
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
    "Obra",
    "EtapaObra",
    "MedicaoObra",
    "DespesaObra",
    "VistoriaObra",
    "validar_percentual",
    "validar_valor",
]
