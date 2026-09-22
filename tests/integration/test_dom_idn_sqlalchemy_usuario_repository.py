"""Testes de integração do repositório de usuários do DOM-IDN."""

from __future__ import annotations

from uuid import UUID, uuid4

import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import engine
from src.modules.sigmun_idn.domain.entities import (
    Permissao,
    PermissaoEscopo,
    Role,
    Usuario,
    UsuarioStatus,
)
from src.modules.sigmun_idn.domain.services.auth_service import AutorizacaoService
from src.modules.sigmun_idn.infrastructure.database.models import (
    PermissaoModel,
    RoleModel,
    RolePermissaoModel,
)
from src.modules.sigmun_idn.infrastructure.repositories.sqlalchemy_usuario_repository import (
    SqlAlchemyUsuarioRepository,
)


@pytest.fixture
def session() -> Session:
    """Sessão PostgreSQL isolada por rollback."""
    connection = engine.connect()
    transaction = connection.begin()

    session = Session(bind=connection, expire_on_commit=False)

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


def _criar_role(session: Session) -> str:
    """Cria uma role mínima para o teste e retorna seu ID."""
    role_id = uuid4()

    session.execute(
        text(
            """
            INSERT INTO idn.roles (
                id,
                codigo,
                nome,
                descricao
            )
            VALUES (
                :id,
                :codigo,
                :nome,
                :descricao
            )
            """
        ),
        {
            "id": role_id,
            "codigo": f"ROLE_TESTE_{uuid4().hex[:8].upper()}",
            "nome": "Role de Teste DOM-IDN",
            "descricao": "Role criada exclusivamente para teste de integração.",
        },
    )

    return str(role_id)


class TestSqlAlchemyUsuarioRepository:
    def test_save_sincroniza_associacoes_de_roles_na_atualizacao(
        self,
        session: Session,
    ) -> None:
        """Sincroniza as relações N:N quando as roles do usuário mudam."""
        role_a = _criar_role(session)
        role_b = _criar_role(session)
        role_c = _criar_role(session)

        usuario = Usuario(
            login=f"teste.idn.{uuid4().hex[:8]}",
            email=f"teste.idn.{uuid4().hex[:8]}@sigmun.local",
            nome="Usuário Teste Atualização Roles",
            status=UsuarioStatus.ATIVO,
            senha_hash="TESTE",
            roles_ids=[role_a, role_b],
        )

        repo = SqlAlchemyUsuarioRepository(session)

        repo.save(usuario)

        usuario.roles_ids = [role_a, role_c]
        repo.save(usuario)

        rows = session.execute(
            text(
                """
                SELECT role_id
                FROM idn.usuario_roles
                WHERE usuario_id = :usuario_id
                ORDER BY role_id
                """
            ),
            {"usuario_id": usuario.id},
        ).scalars().all()

        assert {str(role_id) for role_id in rows} == {
            role_a,
            role_c,
        }

        assert role_b not in {str(role_id) for role_id in rows}

        total = session.execute(
            text(
                """
                SELECT COUNT(*)
                FROM idn.usuario_roles
                WHERE usuario_id = :usuario_id
                """
            ),
            {"usuario_id": usuario.id},
        ).scalar_one()

        assert total == 2


    def test_get_by_id_reconstroi_roles_a_partir_da_relacao_normalizada(
        self,
        session: Session,
    ) -> None:
        """Reconstrói as roles do usuário usando a relação N:N."""
        role_a = _criar_role(session)
        role_b = _criar_role(session)

        usuario = Usuario(
            login=f"teste.idn.{uuid4().hex[:8]}",
            email=f"teste.idn.{uuid4().hex[:8]}@sigmun.local",
            nome="Usuário Teste Leitura Roles",
            status=UsuarioStatus.ATIVO,
            senha_hash="TESTE",
            roles_ids=[],
        )

        repo = SqlAlchemyUsuarioRepository(session)

        repo.save(usuario)

        # As associações válidas existem exclusivamente na tabela N:N.
        session.execute(
            text(
                """
                INSERT INTO idn.usuario_roles (
                    id,
                    usuario_id,
                    role_id
                )
                VALUES
                    (:id_a, :usuario_id, :role_a),
                    (:id_b, :usuario_id, :role_b)
                """
            ),
            {
                "id_a": uuid4(),
                "id_b": uuid4(),
                "usuario_id": usuario.id,
                "role_a": UUID(role_a),
                "role_b": UUID(role_b),
            },
        )

        session.flush()

        recuperado = repo.get_by_id(usuario.id)

        assert recuperado is not None
        assert set(recuperado.roles_ids) == {role_a, role_b}


    def test_save_persiste_usuario_e_associacoes_de_roles(
        self,
        session: Session,
    ) -> None:
        """Persiste o usuário e suas associações na tabela N:N."""
        role_id = _criar_role(session)

        usuario = Usuario(
            login=f"teste.idn.{uuid4().hex[:8]}",
            email=f"teste.idn.{uuid4().hex[:8]}@sigmun.local",
            nome="Usuário Teste DOM-IDN",
            status=UsuarioStatus.ATIVO,
            senha_hash="TESTE",
            roles_ids=[role_id],
        )

        repo = SqlAlchemyUsuarioRepository(session)

        salvo = repo.save(usuario)

        assert salvo.id == usuario.id
        assert salvo.roles_ids == [role_id]

        row_usuario = session.execute(
            text(
                """
                SELECT id
                FROM idn.usuarios
                WHERE id = :usuario_id
                """
            ),
            {"usuario_id": usuario.id},
        ).mappings().one()

        assert str(row_usuario["id"]) == usuario.id

        row_relacao = session.execute(
            text(
                """
                SELECT usuario_id, role_id
                FROM idn.usuario_roles
                WHERE usuario_id = :usuario_id
                  AND role_id = :role_id
                """
            ),
            {
                "usuario_id": usuario.id,
                "role_id": role_id,
            },
        ).mappings().one()

        assert str(row_relacao["usuario_id"]) == usuario.id
        assert str(row_relacao["role_id"]) == role_id


def test_usuario_recarregado_da_relacao_normalizada_mantem_autorizacao(
    session: Session,
) -> None:
    """A autorização deve funcionar após reconstruir o usuário via usuario_roles."""
    role_id = str(uuid4())
    permissao = Permissao(
        codigo=f"TESTE.IDN.AUTORIZACAO.{uuid4().hex[:8].upper()}",
        nome="Consultar demanda",
        descricao="Permissão de teste do fluxo normalizado.",
        escopo=PermissaoEscopo.DOMINIO,
        modulo="compras",
    )

    role = RoleModel(
        id=UUID(role_id),
        codigo=f"ROLE_TESTE_{uuid4().hex[:8].upper()}",
        nome="Role Teste Autorização",
        descricao="Role utilizada exclusivamente no teste.",
    )
    session.add(role)

    permissao_model = PermissaoModel(
        id=UUID(permissao.id),
        codigo=permissao.codigo,
        nome=permissao.nome,
        descricao=permissao.descricao,
        escopo="DOMINIO",
        modulo=permissao.modulo,
    )
    session.add(permissao_model)

    session.flush()

    session.add(
        RolePermissaoModel(
            role_id=UUID(role_id),
            permissao_id=UUID(permissao.id),
            created_by=None,
        )
    )

    usuario = Usuario(
        login=f"teste.idn.{uuid4().hex[:8]}",
        email=f"teste.idn.{uuid4().hex[:8]}@sigmun.local",
        nome="Usuário Teste Autorização Normalizada",
        status=UsuarioStatus.ATIVO,
        senha_hash="TESTE",
        roles_ids=[role_id],
    )

    repo = SqlAlchemyUsuarioRepository(session)
    repo.save(usuario)

    recuperado = repo.get_by_id(usuario.id)

    assert recuperado is not None
    assert recuperado.roles_ids == [role_id]

    permissao_recarregada = Permissao(
        id=permissao.id,
        codigo=permissao_model.codigo,
        nome=permissao_model.nome,
        descricao=permissao_model.descricao,
        escopo=PermissaoEscopo.DOMINIO,
        modulo=permissao_model.modulo,
    )

    role_recarregada = Role(
        id=role_id,
        codigo=role.codigo,
        nome=role.nome,
        descricao=role.descricao,
        permissoes=[permissao_recarregada],
    )

    assert AutorizacaoService.verificar_permissao(
        recuperado,
        permissao.codigo,
        [role_recarregada],
    ) is True
