"""Casos de uso de webhooks inscritos no barramento (DOM-INT).

Gerenciam o registro, inscrição em tópicos, configuração de retries e
ativação/desativação dos webhooks que recebem os eventos do barramento.
"""

from datetime import datetime

from ...application.interfaces import RepositorioWebhook
from ...domain.entities import EstadoInscricao, Webhook
from ...domain.exceptions import (
    UrlWebhookInvalidaError,
    WebhookJaExisteError,
    WebhookNaoEncontradoError,
)
from ...domain.value_objects import validar_topicos, validar_url_http

__all__ = [
    "RegistrarWebhookUseCase",
    "BuscarWebhookUseCase",
    "AtualizarWebhookUseCase",
    "MudarEstadoWebhookUseCase",
    "DeletarWebhookUseCase",
]


class RegistrarWebhookUseCase:
    """Registra um webhook inscrito para receber eventos do barramento."""

    def __init__(self, repo: RepositorioWebhook) -> None:
        self._repo = repo

    def execute(
        self,
        nome: str,
        url_destino: str,
        topicos: list[str],
        segredo_ref: str = "",
        cabecalhos: dict | None = None,
        max_tentativas: int = 5,
        backoff_base_seg: int = 60,
    ) -> Webhook:
        """Registra o webhook validando URL, tópicos e unicidade de nome."""
        if not nome or len(nome) < 3:
            raise ValueError("O nome do webhook deve ter pelo menos 3 caracteres")
        valido, msg = validar_url_http(url_destino)
        if not valido:
            raise UrlWebhookInvalidaError(msg)
        valido, msg = validar_topicos(topicos)
        if not valido:
            raise ValueError(msg)
        if max_tentativas < 1:
            raise ValueError("max_tentativas deve ser pelo menos 1")
        if backoff_base_seg < 0:
            raise ValueError("backoff_base_seg não pode ser negativo")
        if self._repo.exists_by_nome(nome):
            raise WebhookJaExisteError(f"Já existe um webhook chamado '{nome}'")

        webhook = Webhook(
            nome=nome,
            url_destino=url_destino.strip(),
            segredo_ref=segredo_ref,
            topicos=list(topicos),
            cabecalhos=cabecalhos or {},
            estado=EstadoInscricao.ATIVA,
            max_tentativas=max_tentativas,
            backoff_base_seg=backoff_base_seg,
        )
        return self._repo.save(webhook)


class BuscarWebhookUseCase:
    """Consulta de webhooks."""

    def __init__(self, repo: RepositorioWebhook) -> None:
        self._repo = repo

    def get_by_id(self, webhook_id: str) -> Webhook:
        webhook = self._repo.get_by_id(webhook_id)
        if webhook is None:
            raise WebhookNaoEncontradoError(f"Webhook '{webhook_id}' nao encontrado")
        return webhook

    def get_by_nome(self, nome: str) -> Webhook | None:
        return self._repo.get_by_nome(nome)

    def list_all(
        self, page: int = 0, page_size: int = 50, estado: str | None = None
    ) -> tuple[list[Webhook], int]:
        return self._repo.list_all(page, page_size, estado)


class AtualizarWebhookUseCase:
    """Atualiza os dados de um webhook (atualizacao parcial)."""

    def __init__(self, repo: RepositorioWebhook) -> None:
        self._repo = repo

    def execute(
        self,
        webhook_id: str,
        url_destino: str | None = None,
        segredo_ref: str | None = None,
        topicos: list[str] | None = None,
        cabecalhos: dict | None = None,
        max_tentativas: int | None = None,
        backoff_base_seg: int | None = None,
    ) -> Webhook:
        webhook = self._repo.get_by_id(webhook_id)
        if webhook is None:
            raise WebhookNaoEncontradoError(f"Webhook '{webhook_id}' nao encontrado")

        if url_destino is not None:
            valido, msg = validar_url_http(url_destino)
            if not valido:
                raise UrlWebhookInvalidaError(msg)
            webhook.url_destino = url_destino.strip()
        if segredo_ref is not None:
            webhook.segredo_ref = segredo_ref
        if topicos is not None:
            valido, msg = validar_topicos(topicos)
            if not valido:
                raise ValueError(msg)
            webhook.topicos = list(topicos)
        if cabecalhos is not None:
            webhook.cabecalhos = {**webhook.cabecalhos, **cabecalhos}
        if max_tentativas is not None:
            if max_tentativas < 1:
                raise ValueError("max_tentativas deve ser pelo menos 1")
            webhook.max_tentativas = max_tentativas
        if backoff_base_seg is not None:
            if backoff_base_seg < 0:
                raise ValueError("backoff_base_seg nao pode ser negativo")
            webhook.backoff_base_seg = backoff_base_seg

        webhook.atualizado_em = datetime.utcnow()
        return self._repo.save(webhook)


class MudarEstadoWebhookUseCase:
    """Ativa ou desativa a recepcao de eventos de um webhook."""

    def __init__(self, repo: RepositorioWebhook) -> None:
        self._repo = repo

    def execute(self, webhook_id: str, estado: str) -> Webhook:
        webhook = self._repo.get_by_id(webhook_id)
        if webhook is None:
            raise WebhookNaoEncontradoError(f"Webhook '{webhook_id}' nao encontrado")
        webhook.estado = EstadoInscricao(estado)
        webhook.atualizado_em = datetime.utcnow()
        return self._repo.save(webhook)


class DeletarWebhookUseCase:
    """Exclui (exclusao logica) um webhook."""

    def __init__(self, repo: RepositorioWebhook) -> None:
        self._repo = repo

    def execute(self, webhook_id: str) -> bool:
        webhook = self._repo.get_by_id(webhook_id)
        if webhook is None:
            raise WebhookNaoEncontradoError(f"Webhook '{webhook_id}' nao encontrado")
        return self._repo.delete(webhook_id)
