"""Eventos de domínio do Cadastro Único Municipal (DOM-CUM).

Seguem o padrão dos eventos de COMPRAS (dataclasses congeladas).
"""

from src.modules.sigmun_cadastro.domain.events.pessoa_events import (
    ContatoAdicionadoEvent,
    DocumentoAdicionadoEvent,
    EnderecoAdicionadoEvent,
    PessoaAtualizadaEvent,
    PessoaExcluidaEvent,
    PessoaRegistradaEvent,
)
from src.modules.sigmun_cadastro.domain.events.unidade_events import (
    UnidadeAtualizadaEvent,
    UnidadeExcluidaEvent,
    UnidadeRegistradaEvent,
)

__all__ = [
    "PessoaRegistradaEvent",
    "PessoaAtualizadaEvent",
    "PessoaExcluidaEvent",
    "EnderecoAdicionadoEvent",
    "DocumentoAdicionadoEvent",
    "ContatoAdicionadoEvent",
    "UnidadeRegistradaEvent",
    "UnidadeAtualizadaEvent",
    "UnidadeExcluidaEvent",
]
