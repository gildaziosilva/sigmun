"""Auxiliares compartilhados pelos repositórios do DOM-GEO."""

from __future__ import annotations

import uuid
from typing import TypeVar

from sqlalchemy.orm import Session


def to_uuid(valor: str) -> uuid.UUID | None:
    """Converte o identificador textual em UUID.

    Retorna `None` quando o valor não é um UUID válido. O identificador é opaco
    na borda HTTP, então um valor malformado equivale a um recurso inexistente:
    propagar `ValueError` aqui produziria HTTP 500 nas operações de escrita.
    """
    try:
        return uuid.UUID(valor)
    except (ValueError, AttributeError, TypeError):
        return None


T = TypeVar("T")


def buscar_ou_um(session: Session, model: type[T], valor: str) -> T | None:
    """Busca a linha pelo identificador, tolerando valor malformado."""
    chave = to_uuid(valor)
    if chave is None:
        return None
    return session.get(model, chave)


__all__ = ["to_uuid", "buscar_ou_um"]
