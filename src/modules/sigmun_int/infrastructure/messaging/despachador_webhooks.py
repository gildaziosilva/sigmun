"""Transporte HTTP de entrega de mensagens a webhooks (DOM-INT).

``TransporteWebhookHTTP`` implementa ``TransporteWebhook`` com um cliente
``httpx`` síncrono. Considera sucesso todo código HTTP 2xx; os erros de
transporte (timeout, conexão, HTTP 4xx/5xx) são retornados como ``ResultadoEnvio``
falhado para que o despachador programe o retry (backoff/DLQ).
"""

from __future__ import annotations

import time

import httpx

from ...application.interfaces import ResultadoEnvio, TransporteWebhook

__all__ = ["TransporteWebhookHTTP"]


class TransporteWebhookHTTP(TransporteWebhook):
    """Entrega mensagens a webhooks via POST JSON sobre HTTP/HTTPS."""

    def __init__(self, timeout_seg: int = 30) -> None:
        self._timeout_seg = timeout_seg
        self._client = httpx.Client(timeout=timeout_seg)

    def enviar(
        self,
        url: str,
        payload: dict,
        cabecalhos: dict | None = None,
        timeout_seg: int = 30,
    ) -> ResultadoEnvio:
        inicio = time.monotonic()
        try:
            resposta = self._client.post(
                url,
                json=payload,
                headers=cabecalhos or {},
                timeout=timeout_seg or self._timeout_seg,
            )
        except httpx.HTTPError as exc:  # tempo de espera, conexão, etc.
            return ResultadoEnvio(
                http_status=None,
                ok=False,
                erro=str(exc)[:500],
                duracao_seg=round(time.monotonic() - inicio, 4),
            )
        duracao = round(time.monotonic() - inicio, 4)
        ok = 200 <= resposta.status_code < 300
        erro = "" if ok else f"HTTP {resposta.status_code}: {resposta.text[:200]}"
        return ResultadoEnvio(
            http_status=resposta.status_code,
            ok=ok,
            erro=erro,
            duracao_seg=duracao,
        )