"""Módulo de Domínio do SIGMUN - Dados Corporativos.

Este módulo contém as entidades, value objects, serviços e eventos
relacionados ao domínio de Dados Corporativos.
"""

from src.modules.sigmun_dad.domain.entities import (
    AtivoDado,
    Catalogo,
    LinhagemDado,
    PoliticaDado,
    QualidadeDado,
    QualidadeNivel,
    StatusAtivo,
    TipoAtivoDado,
)
from src.modules.sigmun_dad.domain.events import (
    AtivoArquivadoEvent,
    AtivoAtivadoEvent,
    AtivoAtualizadoEvent,
    AtivoCriadoEvent,
    AtivoDesativadoEvent,
    CatalogoAtualizadoEvent,
    CatalogoCriadoEvent,
    DomainEvent,
    LinhagemCriadaEvent,
    PoliticaCriadaEvent,
    QualidadeAvaliadaEvent,
)
from src.modules.sigmun_dad.domain.exceptions import (
    AtivoJaExisteError,
    AtivoNaoEncontradoError,
    CatalogoJaExisteError,
    CatalogoNaoEncontradoError,
    ClassificacaoInvalidaError,
    DomainException,
    LinhagemJaExisteError,
    LinhagemNaoEncontradaError,
    NomeAtivoInvalidoError,
    PoliticaJaExisteError,
    PoliticaNaoEncontradaError,
    QualidadeNaoEncontradaError,
)
from src.modules.sigmun_dad.domain.services import (
    CatalogoService,
    GovernançaService,
    LinhagemService,
)
from src.modules.sigmun_dad.domain.value_objects import (
    ClassificacaoDado,
    NomeAtivo,
    Tag,
)

__all__ = [
    # Entities
    "AtivoDado",
    "TipoAtivoDado",
    "StatusAtivo",
    "QualidadeNivel",
    "Catalogo",
    "LinhagemDado",
    "PoliticaDado",
    "QualidadeDado",
    # Value Objects
    "NomeAtivo",
    "ClassificacaoDado",
    "Tag",
    # Services
    "CatalogoService",
    "LinhagemService",
    "GovernançaService",
    "DomainEvent",
    "AtivoCriadoEvent",
    "AtivoAtualizadoEvent",
    "AtivoAtivadoEvent",
    "AtivoDesativadoEvent",
    "AtivoArquivadoEvent",
    "CatalogoCriadoEvent",
    "CatalogoAtualizadoEvent",
    "LinhagemCriadaEvent",
    "PoliticaCriadaEvent",
    "QualidadeAvaliadaEvent",
    "DomainException",
    "AtivoNaoEncontradoError",
    "AtivoJaExisteError",
    "CatalogoNaoEncontradoError",
    "CatalogoJaExisteError",
    "LinhagemNaoEncontradaError",
    "LinhagemJaExisteError",
    "PoliticaNaoEncontradaError",
    "PoliticaJaExisteError",
    "QualidadeNaoEncontradaError",
    "ClassificacaoInvalidaError",
    "NomeAtivoInvalidoError",
]
