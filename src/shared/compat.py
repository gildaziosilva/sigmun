"""Compatibilidade entre versões do Python.

``datetime.UTC`` foi introduzido em Python 3.11. Como o SIGMUN suporta
Python 3.10 (ver ``requires-python`` em pyproject.toml), este módulo
fornece ``UTC`` de forma compatível, permitindo ``from datetime import UTC``
ser substituído por ``from src.shared.compat import UTC``.
"""

from __future__ import annotations

try:
    from datetime import UTC  # Python 3.11+
except ImportError:  # Python 3.10
    from datetime import timezone
    UTC = timezone.utc  # type: ignore[assignment, misc]

__all__ = ["UTC"]