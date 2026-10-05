"""Utilitários compartilhados pelos repositórios do DOM-IDN."""

from __future__ import annotations

from uuid import UUID


def as_uuid(valor: str) -> UUID | None:
    """Converte a string em UUID, tolerando identificador malformado.

    As rotas recebem o identificador como `str`. Um valor inválido
    (``/usuarios/abc``) faria ``UUID("abc")`` levantar ``ValueError`` e a
    requisição terminaria em HTTP 500. Retornando ``None``, o repositório
    responde "não encontrado" e a rota devolve 404 — a semântica correta,
    já que um identificador malformado não pode corresponder a nenhum
    registro.
    """
    try:
        return UUID(str(valor))
    except (ValueError, AttributeError, TypeError):
        return None
