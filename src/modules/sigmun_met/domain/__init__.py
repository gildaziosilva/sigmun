"""Módulo de Domínio do SIGMUN - Metadados Corporativos.

Este módulo contém as entidades, value objects, serviços e eventos
relacionados ao domínio de Metadados Corporativos.
"""

from src.modules.sigmun_met.domain.entities import (
    Classificacao,
    Metadado,
    StatusMetadado,
    Taxonomia,
    TermoTaxonomia,
    TipoClassificacao,
    TipoDadoMetadado,
    ValorMetadado,
)
from src.modules.sigmun_met.domain.events import (
    ClassificacaoCriadaEvent,
    DomainEvent,
    MetadadoAtivadoEvent,
    MetadadoAtualizadoEvent,
    MetadadoCriadoEvent,
    MetadadoDesativadoEvent,
    TaxonomiaCriadaEvent,
    TermoCriadoEvent,
    ValorMetadadoAtribuidoEvent,
    ValorMetadadoRemovidoEvent,
)
from src.modules.sigmun_met.domain.exceptions import (
    ClassificacaoJaExisteError,
    ClassificacaoNaoEncontradaError,
    CodigoInvalidoError,
    DomainException,
    HierarquiaCiclicaError,
    MetadadoJaExisteError,
    MetadadoNaoEncontradoError,
    TaxonomiaJaExisteError,
    TaxonomiaNaoEncontradaError,
    TermoJaExisteError,
    TermoNaoEncontradoError,
    ValorMetadadoInvalidoError,
    ValorMetadadoNaoEncontradoError,
)
from src.modules.sigmun_met.domain.services import (
    ClassificacaoService,
    MetadadoService,
    TaxonomiaService,
)
from src.modules.sigmun_met.domain.value_objects import (
    CodigoMetadado,
    EntidadeAlvo,
    NomeEntidade,
    ValorAtributo,
)

__all__ = [
    # Entities
    "Metadado",
    "TipoDadoMetadado",
    "StatusMetadado",
    "ValorMetadado",
    "Classificacao",
    "TipoClassificacao",
    "Taxonomia",
    "TermoTaxonomia",
    # Value Objects
    "CodigoMetadado",
    "NomeEntidade",
    "ValorAtributo",
    "EntidadeAlvo",
    # Services
    "MetadadoService",
    "TaxonomiaService",
    "ClassificacaoService",
    # Events
    "DomainEvent",
    "MetadadoCriadoEvent",
    "MetadadoAtualizadoEvent",
    "MetadadoAtivadoEvent",
    "MetadadoDesativadoEvent",
    "ValorMetadadoAtribuidoEvent",
    "ValorMetadadoRemovidoEvent",
    "ClassificacaoCriadaEvent",
    "TaxonomiaCriadaEvent",
    "TermoCriadoEvent",
    # Exceptions
    "DomainException",
    "MetadadoNaoEncontradoError",
    "MetadadoJaExisteError",
    "ValorMetadadoNaoEncontradoError",
    "ValorMetadadoInvalidoError",
    "ClassificacaoNaoEncontradaError",
    "ClassificacaoJaExisteError",
    "TaxonomiaNaoEncontradaError",
    "TaxonomiaJaExisteError",
    "TermoNaoEncontradoError",
    "TermoJaExisteError",
    "HierarquiaCiclicaError",
    "CodigoInvalidoError",
]
