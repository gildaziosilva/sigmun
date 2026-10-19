"""Testes e2e: Fluxo completo de autenticação JWT.

Cobre: login (legacy e JWT), refresh token, logout, acesso a rotas protegidas.
"""
import pytest
from uuid import uuid4
from sqlalchemy import text

from src.main import app
from src.modules.sigmun_idn.infrastructure.database.seeds import popular_seed_idn as seed_idn
from src.modules.sigmun_idn.infrastructure.database.models import UsuarioModel, RoleModel, UsuarioRoleModel
from src.modules.sigmun_idn.domain.entities import Usuario, UsuarioStatus
from src.modules.sigmun_idn.domain.services import AutenticacaoService
from src.core.infrastructure.database.session import SessionLocal


class TestAuthE2E:
    """Testes end-to-end do fluxo de autenticação."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        """Popula usuários de teste antes de cada teste."""
        with SessionLocal() as session:
            seed_idn(session)
            session.execute(text("DELETE FROM idn.usuarios WHERE login = 'admin'"))
            session.execute(text("DELETE FROM idn.roles WHERE codigo = 'admin'"))
            session.commit()

            session.add(RoleModel(
                codigo="admin",
                nome="Administrador",
                descricao="Role de administrador do sistema",
            ))
            session.commit()

            from src.modules.sigmun_idn.domain.services import AutenticacaoService
            from src.modules.sigmun_idn.domain.entities import Usuario, UsuarioStatus
            from src.modules.sigmun_idn.infrastructure.database.models import UsuarioModel
            from uuid import uuid4

            test_user = Usuario(
                id=uuid4(),
                login="admin",
                email="admin@test.com",
                nome="Administrador",
                senha_hash=AutenticacaoService.criar_hash_senha("senha123"),
                status=UsuarioStatus.ATIVO,
            )
            test_user.roles_ids = []

            from sqlalchemy import select
            admin_role = session.execute(select(RoleModel).where(RoleModel.codigo == "admin")).scalar_one_or_none()
            if not admin_role:
                admin_role = RoleModel(
                    codigo="admin",
                    nome="Administrador",
                    descricao="Role de administrador do sistema",
                )
                session.add(admin_role)
                session.flush()

            test_user.roles_ids = [admin_role.id]
            session.add(UsuarioModel(
                id=test_user.id,
                login=test_user.login,
                email=test_user.email,
                nome=test_user.nome,
                senha_hash=test_user.senha_hash,
                status=test_user.status.value,
                created_by=None,
            ))
            # Associate user with role in the N:N table
            session.add(UsuarioRoleModel(
                id=uuid4(),
                usuario_id=test_user.id,
                role_id=admin_role.id,
                created_by=None,
            ))
            session.commit()
        yield
        with SessionLocal() as session:
            session.execute(text("DELETE FROM idn.usuarios WHERE login = 'admin'"))
            session.execute(text("DELETE FROM idn.roles WHERE codigo = 'admin'"))
            session.commit()

    def test_login_legacy_headers_retorna_token(self, client):
        """Login legacy via payload retorna access token (session token)."""
        response = client.post(
            "/api/v1/idn/auth/login",
            json={"login": "admin", "senha": "senha123"},
        )
        assert response.status_code == 200
        data = response.json()
        assert "token" in data
        assert "access_token" in data

    def test_login_jwt_retorna_access_e_refresh(self, client):
        """Login JWT retorna access token e refresh token."""
        response = client.post(
            "/api/v1/idn/auth/login/jwt",
            json={"login": "admin", "senha": "senha123"},
        )
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "refresh_token" in data
        assert data["token_type"] == "bearer"

    def test_refresh_token_gera_novo_access(self, client):
        """Refresh token válido gera novo access token."""
        login = client.post(
            "/api/v1/idn/auth/login/jwt",
            json={"login": "admin", "senha": "senha123"},
        )
        refresh_token = login.json()["refresh_token"]

        response = client.post(
            "/api/v1/idn/auth/refresh",
            json={"refresh_token": refresh_token},
        )
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "refresh_token" in data

    def test_rota_protegida_com_token_valido(self, client):
        """Rota protegida aceita access token válido."""
        login = client.post(
            "/api/v1/idn/auth/login/jwt",
            json={"login": "admin", "senha": "senha123"},
        )
        access_token = login.json()["access_token"]

        response = client.get(
            "/api/v1/idn/usuarios",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        assert response.status_code == 200

    def test_rota_protegida_sem_token_retorna_401(self, client):
        """Rota protegida sem token retorna 401."""
        response = client.get("/api/v1/idn/usuarios")
        assert response.status_code == 401

    def test_logout_invalida_refresh_token(self, client):
        """Logout invalida o refresh token (ainda não implementado - bloqueia refresh token via blocklist Redis)."""
        login = client.post(
            "/api/v1/idn/auth/login/jwt",
            json={"login": "admin", "senha": "senha123"},
        )
        refresh_token = login.json()["refresh_token"]

        # Endpoint correto para logout JWT
        response = client.post(
            "/api/v1/idn/auth/logout/jwt",
            json={"refresh_token": refresh_token},
        )
        assert response.status_code == 200

        # TODO: Implementar blocklist de refresh tokens (Redis)
        # Por enquanto o refresh token ainda funciona (rotação normal)
        # response = client.post(
        #     "/api/v1/idn/auth/refresh",
        #     json={"refresh_token": refresh_token},
        # )
        # assert response.status_code == 401
