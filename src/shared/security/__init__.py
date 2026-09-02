"""Autorização compartilhada (camada shared/security).

Padrão corporativo provisório até o DOM-IDN (Identidade e Acesso) ser
implementado. Nesta fase a autenticação é feita por headers:

  - ``X-Usuario-Id``: UUID do usuário autenticado (obrigatório nas operações
    que exigem autenticação).
  - ``X-Usuario-Papel``: papel(is) do usuário, separados por vírgula
    (ex.: ``gestor_contratos,compras``).

A substituição por tokens JWT/OpenID ocorrerá com o DOM-IDN sem alterar a
assinatura dos endpoints (a dependência troca de implementação interna).
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Annotated
from uuid import UUID

from fastapi import Depends, Header, HTTPException, status

__all__ = [
    "UsuarioContexto",
    "extrair_usuario_id_header",
    "obter_usuario_contexto",
    "exigir_autenticacao",
    "exigir_papeis",
]


@dataclass(frozen=True)
class UsuarioContexto:
    """Contexto de autorização do usuário autenticado."""

    usuario_id: UUID
    papeis: tuple[str, ...] = ()

    def possui_papel(self, papel: str) -> bool:
        return papel in self.papeis

    def possui_algum_papel(self, *papeis: str) -> bool:
        return bool(set(papeis) & set(self.papeis))


def extrair_usuario_id_header(
    x_usuario_id: Annotated[
        UUID | None,
        Header(
            alias="X-Usuario-Id",
            description="Identificador do usuário autenticado (provisório até DOM-IDN).",
        ),
    ] = None,
) -> UUID | None:
    """Extrai o UUID do usuário do header provisório (ou None)."""
    return x_usuario_id


def obter_usuario_contexto(
    usuario_id: Annotated[UUID | None, Depends(extrair_usuario_id_header)],
    x_usuario_papel: Annotated[
        str | None,
        Header(
            alias="X-Usuario-Papel",
            description="Papel(is) do usuário separados por vírgula (opcional).",
        ),
    ] = None,
) -> UsuarioContexto | None:
    """Monta o contexto de autorização; retorna None quando não autenticado."""
    if usuario_id is None:
        return None
    papeis: tuple[str, ...] = ()
    if x_usuario_papel:
        papeis = tuple(p.strip() for p in x_usuario_papel.split(",") if p.strip())
    return UsuarioContexto(usuario_id=usuario_id, papeis=papeis)


def exigir_autenticacao(
    contexto: Annotated[UsuarioContexto | None, Depends(obter_usuario_contexto)],
) -> UsuarioContexto:
    """Dependency que exige usuário autenticado (401 quando ausente)."""
    if contexto is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticação obrigatória. Informe o header X-Usuario-Id.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return contexto


def exigir_papeis(*papeis_permitidos: str) -> Callable:
    """Factory de dependency que exige autenticação e um dos papéis (403)."""

    def dependency(
        contexto: Annotated[UsuarioContexto, Depends(exigir_autenticacao)],
    ) -> UsuarioContexto:
        if not contexto.papeis or not contexto.possui_algum_papel(*papeis_permitidos):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=(
                    f"Acesso negado. Requer um dos papéis: {', '.join(papeis_permitidos)}"
                ),
            )
        return contexto

    return dependency
