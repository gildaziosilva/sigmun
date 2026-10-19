"""Rate limiting e limite de payload (Fase 0 - TODO2 T-0.4).

Token bucket em memoria por (IP, rota), com limite mais baixo para
`/auth/*` (forca bruta) e para a consulta publica de protocolo.
Evolucao prevista: trocar o dicionario por Redis (ja disponivel).

O middleware e inerte quando `RATE_LIMIT_ENABLED=False`, quando
`APP_ENV` e `test`/`testing` ou sob `PYTEST_CURRENT_TEST` (suite).
"""

from __future__ import annotations

import os
import time
from collections import defaultdict

from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from src.shared.config.settings import settings

_JANELA_SEGUNDOS = 60.0

_baldes: dict[tuple[str, str], list[float]] = defaultdict(list)


def reset_rate_limit_state() -> None:
    """Limpa os baldes (uso em testes)."""

    _baldes.clear()


def _bypass_ativo() -> bool:
    if not settings.RATE_LIMIT_ENABLED:
        return True
    if settings.APP_ENV.lower() in {"test", "testing"}:
        return True
    return "PYTEST_CURRENT_TEST" in os.environ


def _limite_para_rota(path: str) -> int:
    if "/auth/" in path:
        return settings.RATE_LIMIT_AUTH_PER_MINUTE
    return settings.RATE_LIMIT_PER_MINUTE


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Limita requisicoes por IP+rota (429) e corpo gigante (413)."""

    async def dispatch(self, request: Request, call_next) -> Response:
        if not _bypass_ativo():
            try:
                tamanho = int(request.headers.get("content-length", "0"))
            except ValueError:
                tamanho = 0
            if tamanho > settings.MAX_REQUEST_BODY_BYTES:
                return JSONResponse(
                    status_code=413,
                    content={"detail": "Corpo da requisicao excede o limite."},
                )
            limite = _limite_para_rota(request.url.path)
            ip = request.client.host if request.client else "unknown"
            chave = (ip, request.url.path)
            agora = time.monotonic()
            janela = [t for t in _baldes[chave] if agora - t < _JANELA_SEGUNDOS]
            if len(janela) >= limite:
                return JSONResponse(
                    status_code=429,
                    content={"detail": "Rate limit excedido. Tente em instantes."},
                )
            janela.append(agora)
            _baldes[chave] = janela
        return await call_next(request)
