"""Compatibilidade entre versões do Python.

``datetime.UTC`` foi introduzido em Python 3.11. Como o SIGMUN suporta
Python 3.10 (ver ``requires-python`` em pyproject.toml), este módulo
fornece ``UTC`` de forma compatível, permitindo ``from datetime import UTC``
ser substituído por ``from src.shared.compat import UTC``.
"""

from __future__ import annotations

from datetime import timezone

# ``datetime.UTC`` só existe em Python 3.11+; o alias abaixo é equivalente e
# funciona em todas as versões suportadas (3.10+).
UTC = timezone.utc

__all__ = ["UTC"]
