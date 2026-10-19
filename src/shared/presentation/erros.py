"""Envelope de erro padronizado para toda a API — T-3.2.

Define o formato único de resposta de erro que todos os endpoints devem retornar,
incluindo o correlation_id para rastreabilidade distribuída.

Exemplo de resposta:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dados de entrada inválidos",
    "details": [
      {"field": "email", "issue": "formato inválido"}
    ],
    "correlation_id": "550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2026-10-08T15:30:00.123456Z"
  }
}
```
"""
from __future__ import annotations

from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ErrorDetail(BaseModel):
    """Detalhe de um erro específico (ex: campo inválido)."""

    field: str | None = Field(default=None, description="Campo relacionado ao erro")
    issue: str = Field(description="Descrição do problema")
    code: str | None = Field(default=None, description="Código específico do erro")


class ErrorEnvelope(BaseModel):
    """Envelope de erro padronizado."""

    model_config = ConfigDict(populate_by_name=True)

    code: str = Field(description="Código de erro categorizado (ex: VALIDATION_ERROR, NOT_FOUND)")
    message: str = Field(description="Mensagem legível para humanos")
    details: list[ErrorDetail] | None = Field(
        default=None, description="Lista de detalhes específicos (opcional)"
    )
    correlation_id: str = Field(description="ID de correlação da requisição (X-Correlation-ID)")
    timestamp: datetime = Field(
        default_factory=datetime.utcnow, description="Timestamp UTC do erro"
    )


class ErrorResponse(BaseModel):
    """Resposta completa de erro."""

    model_config = ConfigDict(populate_by_name=True)

    error: ErrorEnvelope


# Códigos de erro padrão
class ErrorCodes:
    """Códigos de erro padronizados."""

    # Erros de validação (4xx)
    VALIDATION_ERROR = "VALIDATION_ERROR"
    INVALID_INPUT = "INVALID_INPUT"
    MISSING_REQUIRED_FIELD = "MISSING_REQUIRED_FIELD"
    INVALID_FORMAT = "INVALID_FORMAT"

    # Erros de autenticação/autorização (4xx)
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    TOKEN_EXPIRED = "TOKEN_EXPIRED"
    INVALID_TOKEN = "INVALID_TOKEN"
    INSUFFICIENT_PERMISSIONS = "INSUFFICIENT_PERMISSIONS"

    # Erros de recurso (4xx)
    NOT_FOUND = "NOT_FOUND"
    ALREADY_EXISTS = "ALREADY_EXISTS"
    CONFLICT = "CONFLICT"
    GONE = "GONE"

    # Erros de regra de negócio (4xx)
    BUSINESS_RULE_VIOLATION = "BUSINESS_RULE_VIOLATION"
    INVALID_STATE_TRANSITION = "INVALID_STATE_TRANSITION"
    OPERATION_NOT_ALLOWED = "OPERATION_NOT_ALLOWED"

    # Erros de servidor (5xx)
    INTERNAL_ERROR = "INTERNAL_ERROR"
    DATABASE_ERROR = "DATABASE_ERROR"
    EXTERNAL_SERVICE_ERROR = "EXTERNAL_SERVICE_ERROR"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"


def criar_error_response(
    code: str,
    message: str,
    correlation_id: str,
    details: list[ErrorDetail] | None = None,
    status_code: int = 400,
) -> tuple[ErrorResponse, int]:
    """Factory para criar resposta de erro padronizada com status code."""
    envelope = ErrorEnvelope(
        code=code,
        message=message,
        details=details,
        correlation_id=correlation_id,
    )
    return ErrorResponse(error=envelope), status_code


__all__ = [
    "ErrorDetail",
    "ErrorEnvelope",
    "ErrorResponse",
    "ErrorCodes",
    "criar_error_response",
]