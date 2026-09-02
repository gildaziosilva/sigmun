"""
Configuração de Logging Estruturado do SIGMUN.

Implementa logging estruturado com correlation ID para rastreabilidade
de requisições em ambiente de produção.

Referência: Pendência P-002 (Seção 41 do Checklist de Prontidão)
"""

import logging
import logging.handlers
import os
import sys
import uuid
from contextvars import ContextVar
from datetime import datetime, timezone
from typing import Any, Optional

import json

# ContextVar para armazenar o correlation ID por requisição
correlation_id_var: ContextVar[Optional[str]] = ContextVar("correlation_id", default=None)


class JSONFormatter(logging.Formatter):
    """Formatter para saída de logs em formato JSON estruturado."""

    def format(self, record: logging.LogRecord) -> str:
        log_data: dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        # Adiciona correlation ID se disponível
        corr_id = correlation_id_var.get()
        if corr_id:
            log_data["correlation_id"] = corr_id

        # Adiciona informações de exceção se presente
        if record.exc_info and record.exc_info[0] is not None:
            log_data["exception"] = {
                "type": record.exc_info[0].__name__,
                "message": str(record.exc_info[1]),
                "traceback": self.formatException(record.exc_info),
            }

        # Adiciona campos extras do record
        if hasattr(record, "extra_data"):
            log_data["data"] = record.extra_data

        return json.dumps(log_data, default=str, ensure_ascii=False)


class CorrelationIDFilter(logging.Filter):
    """Filter que adiciona correlation ID ao record de log."""

    def filter(self, record: logging.LogRecord) -> bool:
        record.correlation_id = correlation_id_var.get() or "N/A"
        return True


def get_correlation_id() -> str:
    """Retorna o correlation ID atual ou gera um novo."""
    current = correlation_id_var.get()
    if current is None:
        current = str(uuid.uuid4())
        correlation_id_var.set(current)
    return current


def set_correlation_id(corr_id: Optional[str] = None) -> str:
    """Define o correlation ID. Se não fornecido, gera um novo."""
    new_id = corr_id or str(uuid.uuid4())
    correlation_id_var.set(new_id)
    return new_id


def clear_correlation_id() -> None:
    """Limpa o correlation ID do contexto atual."""
    correlation_id_var.set(None)


def setup_logging(
    log_level: Optional[str] = None,
    log_file: Optional[str] = None,
    retention_days: int = 30,
) -> None:
    """
    Configura o logging estruturado da aplicação.

    Args:
        log_level: Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Caminho para o arquivo de log
        retention_days: Número de dias para retenção dos logs
    """
    level = getattr(logging, (log_level or os.getenv("LOG_LEVEL", "INFO")).upper())

    # Configura logger raiz
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Remove handlers existentes
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Formatter JSON
    json_formatter = JSONFormatter()
    corr_filter = CorrelationIDFilter()

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(json_formatter)
    console_handler.addFilter(corr_filter)
    root_logger.addHandler(console_handler)

    # File handler com rotação se log_file especificado
    if log_file:
        log_dir = os.path.dirname(log_file)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

        file_handler = logging.handlers.TimedRotatingFileHandler(
            filename=log_file,
            when="midnight",
            backupCount=retention_days,
            encoding="utf-8",
        )
        file_handler.setFormatter(json_formatter)
        file_handler.addFilter(corr_filter)
        root_logger.addHandler(file_handler)

    # Suprime logs muito verbosos de bibliotecas
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)


def get_logger(name: str) -> logging.Logger:
    """Retorna um logger configurado com o nome especificado."""
    return logging.getLogger(name)
