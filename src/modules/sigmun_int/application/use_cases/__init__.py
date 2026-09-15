"""Casos de uso da aplicação de Integração e Interoperabilidade (DOM-INT)."""

from .api_use_cases import (
    AtualizarApiExternaUseCase,
    BuscarApiExternaUseCase,
    MudarEstadoApiUseCase,
    CriarApiExternaUseCase,
    DeletarApiExternaUseCase,
)
from .bus_use_cases import ConsumirOutboxUseCase, DespacharWebhooksUseCase
from .conector_use_cases import (
    CODIGOS_CONECTORES_OFICIAIS,
    CONECTORES_OFICIAIS,
    AtualizarConectorUseCase,
    BuscarConectorUseCase,
    MudarEstadoConectorUseCase,
    CriarConectorUseCase,
    DeletarConectorUseCase,
)
from .contrato_use_cases import (
    AprovarContratoIntegracaoUseCase,
    AtualizarContratoIntegracaoUseCase,
    BuscarContratoIntegracaoUseCase,
    CriarContratoIntegracaoUseCase,
    DeletarContratoIntegracaoUseCase,
    RetirarContratoIntegracaoUseCase,
)
from .entrega_use_cases import (
    BuscarEntregaWebhookUseCase,
    CancelarEntregaWebhookUseCase,
    RetryEntregaWebhookUseCase,
)
from .webhook_use_cases import (
    AtualizarWebhookUseCase,
    BuscarWebhookUseCase,
    MudarEstadoWebhookUseCase,
    DeletarWebhookUseCase,
    RegistrarWebhookUseCase,
)

__all__ = [
    "CriarApiExternaUseCase",
    "BuscarApiExternaUseCase",
    "AtualizarApiExternaUseCase",
    "MudarEstadoApiUseCase",
    "DeletarApiExternaUseCase",
    "CriarContratoIntegracaoUseCase",
    "BuscarContratoIntegracaoUseCase",
    "AtualizarContratoIntegracaoUseCase",
    "AprovarContratoIntegracaoUseCase",
    "RetirarContratoIntegracaoUseCase",
    "DeletarContratoIntegracaoUseCase",
    "CONECTORES_OFICIAIS",
    "CODIGOS_CONECTORES_OFICIAIS",
    "CriarConectorUseCase",
    "BuscarConectorUseCase",
    "AtualizarConectorUseCase",
    "MudarEstadoConectorUseCase",
    "DeletarConectorUseCase",
    "RegistrarWebhookUseCase",
    "BuscarWebhookUseCase",
    "AtualizarWebhookUseCase",
    "MudarEstadoWebhookUseCase",
    "DeletarWebhookUseCase",
    "BuscarEntregaWebhookUseCase",
    "RetryEntregaWebhookUseCase",
    "CancelarEntregaWebhookUseCase",
    "ConsumirOutboxUseCase",
    "DespacharWebhooksUseCase",
]
