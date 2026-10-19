"""
Testes unitários para dependências centralizadas de autenticação (T-2.1).
"""

from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from src.shared.presentation.dependencies import (
    JWTUsuarioContexto,
    UsuarioObrigatorio,
    UsuarioOpcional,
    exigir_papeis,
    require_roles_hybrid,
)
from src.shared.security.jwt import create_access_token


def _make_ctx(roles: tuple[str, ...] = ()) -> JWTUsuarioContexto:
    """Cria contexto de usuário de teste."""
    return JWTUsuarioContexto(
        usuario_id="11111111-1111-1111-1111-111111111111",
        login="teste",
        roles=roles,
        unidades_ids=(),
    )


def _make_token(ctx: JWTUsuarioContexto) -> str:
    """Cria token JWT de teste a partir do contexto."""
    return create_access_token(
        usuario_id=ctx.usuario_id,
        login=ctx.login,
        roles=list(ctx.roles),
        unidades_ids=list(ctx.unidades_ids),
    )


class TestDependencies:
    """Testes das dependências centralizadas."""

    def test_usuario_obrigatorio_retorna_401_sem_token(self):
        """Rota com UsuarioObrigatorio retorna 401 sem token."""
        app = FastAPI()

        @app.get("/protegida")
        def rota(usuario: UsuarioObrigatorio):
            return {"usuario": str(usuario.usuario_id)}

        with TestClient(app, raise_server_exceptions=False) as client:
            resp = client.get("/protegida")
            assert resp.status_code == 401

    def test_usuario_obrigatorio_funciona_com_token_valido(self):
        """Rota com UsuarioObrigatorio aceita token válido."""
        app = FastAPI()

        @app.get("/protegida")
        def rota(usuario: UsuarioObrigatorio):
            return {"usuario": str(usuario.usuario_id)}

        ctx = _make_ctx()
        token = _make_token(ctx)

        with TestClient(app, raise_server_exceptions=False) as client:
            resp = client.get("/protegida", headers={"Authorization": f"Bearer {token}"})
            assert resp.status_code == 200
            assert resp.json()["usuario"] == str(ctx.usuario_id)

    def test_usuario_opcional_permite_anonimo(self):
        """Rota com UsuarioOpcional permite acesso anônimo."""
        app = FastAPI()

        @app.get("/publica")
        def rota(usuario: UsuarioOpcional):
            return {"autenticado": usuario is not None}

        with TestClient(app, raise_server_exceptions=False) as client:
            resp = client.get("/publica")
            assert resp.status_code == 200
            assert resp.json()["autenticado"] is False

    def test_usuario_opcional_funciona_com_token(self):
        """Rota com UsuarioOpcional aceita token válido."""
        app = FastAPI()

        @app.get("/publica")
        def rota(usuario: UsuarioOpcional):
            return {"autenticado": usuario is not None, "roles": usuario.roles if usuario else ()}

        ctx = _make_ctx(("gestor",))
        token = _make_token(ctx)

        with TestClient(app, raise_server_exceptions=False) as client:
            resp = client.get("/publica", headers={"Authorization": f"Bearer {token}"})
            assert resp.status_code == 200
            assert resp.json()["autenticado"] is True
            assert "gestor" in resp.json()["roles"]

    def test_exigir_papeis_alias_funciona(self):
        """exigir_papeis é alias de require_roles_hybrid."""
        assert exigir_papeis is require_roles_hybrid

    def test_exigir_papeis_retorna_403_sem_papel(self):
        """Factory exigir_papeis retorna 403 quando papel não presente."""
        app = FastAPI()

        @app.get("/admin")
        def rota_admin(usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("admin"))]):
            return {"ok": True}

        ctx = _make_ctx(("gestor",))  # não tem papel "admin"
        token = _make_token(ctx)

        with TestClient(app, raise_server_exceptions=False) as client:
            resp = client.get("/admin", headers={"Authorization": f"Bearer {token}"})
            assert resp.status_code == 403

    def test_exigir_papeis_retorna_200_com_papel(self):
        """Factory exigir_papeis retorna 200 quando papel presente."""
        app = FastAPI()

        @app.get("/admin")
        def rota_admin(usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("admin"))]):
            return {"ok": True}

        ctx = _make_ctx(("admin", "gestor"))
        token = _make_token(ctx)

        with TestClient(app, raise_server_exceptions=False) as client:
            resp = client.get("/admin", headers={"Authorization": f"Bearer {token}"})
            assert resp.status_code == 200
            assert resp.json()["ok"] is True

    def test_exigir_papeis_multiplos_papeis(self):
        """Factory exigir_papeis aceita qualquer um dos papéis listados."""
        app = FastAPI()

        @app.get("/gestor-ou-admin")
        def rota(usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("admin", "gestor"))]):
            return {"ok": True}

        # Usuário com apenas "gestor" deve passar
        ctx = _make_ctx(("gestor",))
        token = _make_token(ctx)

        with TestClient(app, raise_server_exceptions=False) as client:
            resp = client.get("/gestor-ou-admin", headers={"Authorization": f"Bearer {token}"})
            assert resp.status_code == 200
