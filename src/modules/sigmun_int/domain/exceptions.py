"""Exceções de domínio do módulo de Integração e Interoperabilidade (DOM-INT)."""

__all__ = [
    "IntegracaoError",
    "ApiExternaNaoEncontradaError",
    "ApiExternaJaExisteError",
    "ContratoIntegracaoNaoEncontradoError",
    "ContratoIntegracaoJaExisteError",
    "ConectorNaoEncontradoError",
    "ConectorJaExisteError",
    "WebhookNaoEncontradoError",
    "WebhookJaExisteError",
    "UrlWebhookInvalidaError",
    "EntregaNaoEncontradaError",
    "EntregaEstadoInvalidoError",
    "LimiteRetriesExcedidoError",
    "EventoOutboxDuplicadoError",
    "FonteOutboxInvalidaError",
    "OperacaoNaoPermitidaError",
]


class IntegracaoError(Exception):
    """Exceção base do domínio de Integração e Interoperabilidade."""


class ApiExternaNaoEncontradaError(IntegracaoError):
    """API externa não encontrada no catálogo."""


class ApiExternaJaExisteError(IntegracaoError):
    """Já existe uma API externa com esse código no catálogo."""


class ContratoIntegracaoNaoEncontradoError(IntegracaoError):
    """Contrato de integração não encontrado."""


class ContratoIntegracaoJaExisteError(IntegracaoError):
    """Já existe um contrato de integração com esse código."""


class ConectorNaoEncontradoError(IntegracaoError):
    """Conector oficial não encontrado."""


class ConectorJaExisteError(IntegracaoError):
    """Já existe um conector com esse código."""


class WebhookNaoEncontradoError(IntegracaoError):
    """Webhook não encontrado."""


class WebhookJaExisteError(IntegracaoError):
    """Já existe um webhook com esse nome."""


class UrlWebhookInvalidaError(IntegracaoError):
    """URL destino do webhook inválida (deve ser http/https absoluta)."""


class EntregaNaoEncontradaError(IntegracaoError):
    """Entrega de mensagem não encontrada."""


class EntregaEstadoInvalidoError(IntegracaoError):
    """A operação não é válida para o estado atual da entrega."""


class LimiteRetriesExcedidoError(IntegracaoError):
    """A entrega atingiu o limite de retries (fila de mensagens mortas)."""


class EventoOutboxDuplicadoError(IntegracaoError):
    """O evento do outbox já foi processado pelo barramento (idempotência)."""


class FonteOutboxInvalidaError(IntegracaoError):
    """A fonte de outbox indicada não é um produtor válido (gdo|compras)."""


class OperacaoNaoPermitidaError(IntegracaoError):
    """Operação não permitida no estado atual do agregado."""
