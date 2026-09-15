"""Casos de uso do registro de entregas de webhooks (DOM-INT).

Consulta, cancelamento e reenfileiramento (retry) das entregas de mensagens.
O reenfileiramento permite recuperar mensagens da fila de mensagens mortas
(DLQ) reiniciando o contador de tentativas.
"""

from datetime import datetime

from ...application.interfaces import RepositorioEntregaWebhook
from ...domain.entities import EstadoEntrega, EntregaWebhook
from ...domain.exceptions import (
    EntregaEstadoInvalidoError,
    EntregaNaoEncontradaError,
    LimiteRetriesExcedidoError,
)

__all__ = [
    "BuscarEntregaWebhookUseCase",
    "RetryEntregaWebhookUseCase",
    "CancelarEntregaWebhookUseCase",
]


class BuscarEntregaWebhookUseCase:
    """Consulta de entregas de mensagens."""

    def __init__(self, repo: RepositorioEntregaWebhook) -> None:
        self._repo = repo

    def get_by_id(self, entrega_id: str) -> EntregaWebhook:
        entrega = self._repo.get_by_id(entrega_id)
        if entrega is None:
            raise EntregaNaoEncontradaError(f"Entrega '{entrega_id}' não encontrada")
        return entrega

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        estado: str | None = None,
    ) -> tuple[list[EntregaWebhook], int]:
        return self._repo.list_all(page, page_size, estado)

    def list_by_webhook(
        self, webhook_id: str, page: int = 0, page_size: int = 50
    ) -> tuple[list[EntregaWebhook], int]:
        return self._repo.list_by_webhook(webhook_id, page, page_size)


class RetryEntregaWebhookUseCase:
    """Reenfileira uma entrega falhada ou na fila de mensagens mortas.

    Só é válido para estados terminais de erro (falhou, fila_morta,
    cancelado). Ao reenfileirar são reiniciadas as tentativas para dar à mensagem
    uma nova oportunidade de entrega.
    """

    def __init__(self, repo: RepositorioEntregaWebhook) -> None:
        self._repo = repo

    def execute(self, entrega_id: str) -> EntregaWebhook:
        entrega = self._repo.get_by_id(entrega_id)
        if entrega is None:
            raise EntregaNaoEncontradaError(f"Entrega '{entrega_id}' não encontrada")

        if entrega.estado is EstadoEntrega.SUCESSO:
            raise EntregaEstadoInvalidoError(
                "Não pode reenfileirar uma entrega já entregada com sucesso"
            )
        if entrega.estado is EstadoEntrega.PENDENTE:
            raise EntregaEstadoInvalidoError("A entrega já se encontra pendente")

        entrega.estado = EstadoEntrega.PENDENTE
        entrega.tentativas = 0
        entrega.proximo_retry = None
        entrega.ultimo_erro = ""
        entrega.atualizado_em = datetime.utcnow()
        return self._repo.save(entrega)


class CancelarEntregaWebhookUseCase:
    """Cancela uma entrega pendente (não será reentregue)."""

    def __init__(self, repo: RepositorioEntregaWebhook) -> None:
        self._repo = repo

    def execute(self, entrega_id: str) -> EntregaWebhook:
        entrega = self._repo.get_by_id(entrega_id)
        if entrega is None:
            raise EntregaNaoEncontradaError(f"Entrega '{entrega_id}' não encontrada")
        if entrega.estado not in (EstadoEntrega.PENDENTE, EstadoEntrega.FALHOU):
            raise EntregaEstadoInvalidoError(
                "Só podem ser canceladas entregas pendentes ou falhadas"
            )
        entrega.estado = EstadoEntrega.CANCELADO
        entrega.atualizado_em = datetime.utcnow()
        return self._repo.save(entrega)
