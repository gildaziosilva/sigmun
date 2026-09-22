"""
Testes unitários do contrato de autorização do DOM-IDN.

Os dados utilizados aqui são exclusivamente de teste.
Nenhum Role ou Permissão deste arquivo constitui catálogo institucional.
"""

from src.modules.sigmun_idn.domain.entities import (
    Permissao,
    PermissaoEscopo,
    Role,
    Usuario,
    UsuarioStatus,
)
from src.modules.sigmun_idn.domain.services.auth_service import (
    AutorizacaoService,
)


PERMISSAO_CONSULTAR = "COMPRAS.DEMANDA.CONSULTAR"


def criar_permissao(codigo: str = PERMISSAO_CONSULTAR) -> Permissao:
    return Permissao(
        codigo=codigo,
        nome="Consultar demanda de compras",
        descricao="Permissão utilizada exclusivamente nos testes do DOM-IDN.",
        escopo=PermissaoEscopo.DOMINIO,
        modulo="compras",
    )


def criar_role(
    role_id: str | None = None,
    codigo: str = "ROLE_TESTE_COMPRAS",
    permissao: Permissao | None = None,
) -> Role:
    role = Role(
        id=role_id or "role-teste-compras",
        codigo=codigo,
        nome="Role de Teste Compras",
        descricao="Role fictícia utilizada exclusivamente nos testes.",
    )

    if permissao is not None:
        role.adicionar_permissao(permissao)

    return role


def criar_usuario(
    role_ids: list[str] | None = None,
    status: UsuarioStatus = UsuarioStatus.ATIVO,
    is_deleted: bool = False,
    unidades_ids: list[str] | None = None,
) -> Usuario:
    return Usuario(
        login="usuario.teste",
        email="usuario.teste@example.invalid",
        nome="Usuário de Teste",
        status=status,
        roles_ids=role_ids or [],
        unidades_ids=unidades_ids or [],
        is_deleted=is_deleted,
    )


def test_usuario_com_role_e_permissao_deve_ser_autorizado():
    permissao = criar_permissao()
    role = criar_role(permissao=permissao)
    usuario = criar_usuario(role_ids=[role.id])

    assert AutorizacaoService.verificar_permissao(
        usuario,
        PERMISSAO_CONSULTAR,
        [role],
    ) is True


def test_usuario_sem_role_deve_ser_negado():
    permissao = criar_permissao()
    role = criar_role(permissao=permissao)
    usuario = criar_usuario(role_ids=[])

    assert AutorizacaoService.verificar_permissao(
        usuario,
        PERMISSAO_CONSULTAR,
        [role],
    ) is False


def test_role_sem_permissao_deve_ser_negada():
    role = criar_role()
    usuario = criar_usuario(role_ids=[role.id])

    assert AutorizacaoService.verificar_permissao(
        usuario,
        PERMISSAO_CONSULTAR,
        [role],
    ) is False


def test_role_excluida_nao_deve_conceder_permissao():
    permissao = criar_permissao()
    role = criar_role(permissao=permissao)
    role.is_deleted = True

    usuario = criar_usuario(role_ids=[role.id])

    assert AutorizacaoService.verificar_permissao(
        usuario,
        PERMISSAO_CONSULTAR,
        [role],
    ) is False


def test_usuario_inativo_nao_deve_ser_autorizado():
    permissao = criar_permissao()
    role = criar_role(permissao=permissao)
    usuario = criar_usuario(
        role_ids=[role.id],
        status=UsuarioStatus.INATIVO,
    )

    assert AutorizacaoService.verificar_permissao(
        usuario,
        PERMISSAO_CONSULTAR,
        [role],
    ) is False


def test_usuario_bloqueado_nao_deve_ser_autorizado():
    permissao = criar_permissao()
    role = criar_role(permissao=permissao)
    usuario = criar_usuario(
        role_ids=[role.id],
        status=UsuarioStatus.BLOQUEADO,
    )

    assert AutorizacaoService.verificar_permissao(
        usuario,
        PERMISSAO_CONSULTAR,
        [role],
    ) is False


def test_usuario_pendente_nao_deve_ser_autorizado():
    permissao = criar_permissao()
    role = criar_role(permissao=permissao)
    usuario = criar_usuario(
        role_ids=[role.id],
        status=UsuarioStatus.PENDENTE,
    )

    assert AutorizacaoService.verificar_permissao(
        usuario,
        PERMISSAO_CONSULTAR,
        [role],
    ) is False


def test_usuario_excluido_nao_deve_ser_autorizado():
    permissao = criar_permissao()
    role = criar_role(permissao=permissao)
    usuario = criar_usuario(
        role_ids=[role.id],
        is_deleted=True,
    )

    assert AutorizacaoService.verificar_permissao(
        usuario,
        PERMISSAO_CONSULTAR,
        [role],
    ) is False


def test_verificar_role_deve_reconhecer_role_do_usuario():
    role = criar_role()
    usuario = criar_usuario(role_ids=[role.id])

    assert AutorizacaoService.verificar_role(
        usuario,
        "ROLE_TESTE_COMPRAS",
        [role],
    ) is True


def test_verificar_role_deve_negar_role_que_usuario_nao_possui():
    role = criar_role()
    usuario = criar_usuario(role_ids=[])

    assert AutorizacaoService.verificar_role(
        usuario,
        "ROLE_TESTE_COMPRAS",
        [role],
    ) is False


def test_verificar_role_deve_negar_role_excluida():
    role = criar_role()
    role.is_deleted = True

    usuario = criar_usuario(role_ids=[role.id])

    assert AutorizacaoService.verificar_role(
        usuario,
        "ROLE_TESTE_COMPRAS",
        [role],
    ) is False


def test_usuario_sem_unidades_deve_ter_acesso_global():
    usuario = criar_usuario(unidades_ids=[])

    assert AutorizacaoService.pode_acessar_unidade(
        usuario,
        "unidade-qualquer",
    ) is True


def test_usuario_deve_acessar_unidade_explicitamente_associada():
    usuario = criar_usuario(
        unidades_ids=["unidade-01", "unidade-02"],
    )

    assert AutorizacaoService.pode_acessar_unidade(
        usuario,
        "unidade-02",
    ) is True


def test_usuario_nao_deve_acessar_unidade_nao_associada():
    usuario = criar_usuario(
        unidades_ids=["unidade-01"],
    )

    assert AutorizacaoService.pode_acessar_unidade(
        usuario,
        "unidade-02",
    ) is False


def test_usuario_inativo_nao_deve_acessar_unidade():
    usuario = criar_usuario(
        status=UsuarioStatus.INATIVO,
        unidades_ids=[],
    )

    assert AutorizacaoService.pode_acessar_unidade(
        usuario,
        "unidade-01",
    ) is False


def test_usuario_excluido_nao_deve_acessar_unidade():
    usuario = criar_usuario(
        is_deleted=True,
        unidades_ids=[],
    )

    assert AutorizacaoService.pode_acessar_unidade(
        usuario,
        "unidade-01",
    ) is False
