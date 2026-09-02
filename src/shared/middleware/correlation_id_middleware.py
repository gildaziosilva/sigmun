"""
Middleware de Correlation ID para requisições HTTP.

Adiciona automaticamente um correlation ID a cada requisição
para rastreabilidade distribuída.

Referência: Pendência P-002 (Seção 41 do Checklist de Prontidão)
"""

import logging

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from src.shared.config.logging_config import (
    clear_correlation_id,
    get_correlation_id,
    set_correlation_id,
)

logger = logging.getLogger(__name__)


class CorrelationIDMiddleware(BaseHTTPMiddleware):
    """
    Middleware que gerencia o correlation ID das requisições.

    - Se a requisição já contém um X-Correlation-ID, reutiliza-o
    - Caso contrário, gera um novo UUID v4
    - Adiciona o correlation ID à resposta (header X-Correlation-ID)
    - Limpa o contexto ao final da requisição
    """

    HEADER_NAME = "X-Correlation-ID"

    async def dispatch(self, request: Request, call_next) -> Response:
        # Obtém correlation ID do header ou gera novo
        corr_id = request.headers.get(self.HEADER_NAME)
        if corr_id:
            set_correlation_id(corr_id)
        else:
            set_correlation_id()

        current_corr_id = get_correlation_id()

        # Log da requisição recebida
        logger.info(
            "Requisição recebida",
            extra={"extra_data": {
                "method": request.method,
                "path": str(request.url.path),
                "client_ip": request.client.host if request.client else "unknown",
                "correlation_id": current_corr_id,
            }},
        )

        try:
            response = await call_next(request)

            # Adiciona correlation ID à resposta
            response.headers[self.HEADER_NAME] = current_corr_id

            # Log da resposta
            logger.info(
                "Resposta enviada",
                extra={"extra_data": {
                    "method": request.method,
                    "path": str(request.url.path),
                    "status_code": response.status_code,
                    "correlation_id": current_corr_id,
                }},
            )

            return response
        except Exception as exc:
            logger.error(
                "Erro não tratado na requisição",
                exc_info=True,
                extra={"extra_data": {
                    "method": request.method,
                    "path": str(request.url.path),
                    "error": str(exc),
                    "correlation_id": current_corr_id,
                }},
            )
            raise
        finally:
            clear_correlation_id()
