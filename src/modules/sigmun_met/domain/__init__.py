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
    EventoMetadados,
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
    CicloHierarquiaError,
    ClassificacaoDuplicadaError,
    ClassificacaoJaExisteError,
    ClassificacaoNaoEncontradaError,
    CodigoInvalidoError,
    DomainException,
    HierarquiaCiclicaError,
    MetadadoJaCadastradoError,
    MetadadoJaExisteError,
    MetadadoNaoEncontradoError,
    MetadadosDomainError,
    TaxonomiaDuplicadaError,
    TaxonomiaJaExisteError,
    TaxonomiaNaoEncontradaError,
    TermoDuplicadoError,
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
    "EventoMetadados",
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
    "MetadadosDomainError",
    "DomainException",
    "MetadadoNaoEncontradoError",
    "MetadadoJaCadastradoError",
    "MetadadoJaExisteError",
    "ValorMetadadoNaoEncontradoError",
    "ValorMetadadoInvalidoError",
    "ClassificacaoNaoEncontradaError",
    "ClassificacaoDuplicadaError",
    "ClassificacaoJaExisteError",
    "TaxonomiaNaoEncontradaError",
    "TaxonomiaDuplicadaError",
    "TaxonomiaJaExisteError",
    "TermoNaoEncontradoError",
    "TermoDuplicadoError",
    "TermoJaExisteError",
    "CicloHierarquiaError",
    "HierarquiaCiclicaError",
    "CodigoInvalidoError",
]
