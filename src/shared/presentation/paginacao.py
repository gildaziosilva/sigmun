"""Schemas de paginação unificados para toda a API — T-3.1.

Decisão (ADR-0011): base 1 (page=1 = primeira página), page_size padrão 20.
Isso alinha com a convenção mais comum em APIs REST públicas e com a
expectativa de clientes humanos (não programáticos).

Migração: substituir todos os usos de:
  - `page: int = 0` + `page_size: int = 50`  (92 ocorrências)
  - `offset: int = 0`                        (19 ocorrências)
por `ParametrosPaginacao` (ou `PaginaRequest`).
"""
from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class ParametrosPaginacao(BaseModel):
    """Parâmetros de entrada para paginação (query params).

    - `page`: base 1 (1 = primeira página). Default = 1.
    - `page_size`: itens por página. Default = 20, máx = 100.
    """
    page: int = Field(default=1, ge=1, description="Número da página (base 1)")
    page_size: int = Field(default=20, ge=1, le=100, description="Itens por página (máx 100)")

    def offset(self) -> int:
        """Converte para offset 0-based para uso em SQL (LIMIT/OFFSET)."""
        return (self.page - 1) * self.page_size

    def limit(self) -> int:
        """Retorna o limit para SQL."""
        return self.page_size


class Pagina(BaseModel, Generic[T]):
    """Resposta padronizada de lista paginada.

    Exemplo:
    ```json
    {
      "items": [...],
      "page": 1,
      "page_size": 20,
      "total": 150,
      "total_pages": 8,
      "has_next": true,
      "has_prev": false
    }
    ```
    """
    items: list[T]
    page: int = Field(ge=1, description="Página atual (base 1)")
    page_size: int = Field(ge=1, description="Itens por página")
    total: int = Field(ge=0, description="Total de itens (sem paginação)")
    total_pages: int = Field(ge=0, description="Total de páginas")
    has_next: bool = Field(description="Existe próxima página")
    has_prev: bool = Field(description="Existe página anterior")


def criar_pagina(
    items: list[T],
    params: ParametrosPaginacao,
    total: int,
) -> Pagina[T]:
    """Constrói uma resposta `Pagina` a partir dos itens e total."""
    total_pages = (total + params.page_size - 1) // params.page_size if total > 0 else 0
    return Pagina[T](
        items=items,
        page=params.page,
        page_size=params.page_size,
        total=total,
        total_pages=total_pages,
        has_next=params.page < total_pages,
        has_prev=params.page > 1,
    )


# Alias semântico para uso em endpoints (query params)
PaginaRequest = ParametrosPaginacao

__all__ = [
    "ParametrosPaginacao",
    "Pagina",
    "criar_pagina",
    "PaginaRequest",
]