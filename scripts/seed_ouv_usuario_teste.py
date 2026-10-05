#!/usr/bin/env python
"""Cria usuário de teste da Ouvidoria vinculado à ROLE_OUVIDOR.

Uso:
    .venv/bin/python scripts/seed_ouv_usuario_teste.py
    .venv/bin/python scripts/seed_ouv_usuario_teste.py --dry-run

Contexto:
    Os papéis funcionais do DOM-OUV foram criados em 2026-10-03
    (ADR-0008 §5.2), mas nenhum servidor real está vinculado a eles.
    Este script cria um usuário DEMONSTRATIVO para destravar a validação
    da Onda 1 (tarefas 1.1 a 1.6) enquanto a Ouvidoria não define
    quais servidores ocupam cada função.

    Quando os servidores reais forem definidos, este usuário deve ser
    desativado (status='inativo') e removido.

O que cria:
    - idn.usuarios: demo.ouvidoria.ouvidor (status ativo)
    - idn.usuario_roles: vínculo com ROLE_OUVIDOR

Não cria sessões nem auditoria de login.
A senha é gerada com PBKDF2-SHA256, o mesmo algoritmo de
AutenticacaoService.criar_hash_senha. É idempotente: reexecutar não
altera o usuário nem a senha já existentes.

Segurança:
    A senha é exibida apenas na criação. Subsequentemente, apenas o
    hash é exibido. O usuário é de demonstração e NÃO deve ser usado
    em ambiente de produção.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Permite execução direta a partir da raiz do projeto.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sqlalchemy import select  # noqa: E402
from sqlalchemy.orm import Session  # noqa: E402

from src.core.infrastructure.database.session import SessionLocal  # noqa: E402
from src.modules.sigmun_idn.domain.services.auth_service import (  # noqa: E402
    AutenticacaoService,
)
from src.modules.sigmun_idn.domain.value_objects.senha import Senha  # noqa: E402
from src.modules.sigmun_idn.infrastructure.database.models import (  # noqa: E402
    RoleModel,
    UsuarioModel,
    UsuarioRoleModel,
)

LOGIN = "demo.ouvidoria.ouvidor"
EMAIL = "demo.ouvidoria.ouvidor@sigmun.local"
NOME = "Ouvidor — Demo"
SENHA_PADRAO = "Ouvidoria2026"
ROLE_CODIGO = "ROLE_OUVIDOR"


def _obter_usuario(session: Session) -> UsuarioModel | None:
    """Obtém o usuário de teste ativo pelo login."""
    return session.scalar(
        select(UsuarioModel).where(
            UsuarioModel.login == LOGIN,
            UsuarioModel.deleted_at.is_(None),
        )
    )


def _obter_role(session: Session) -> RoleModel | None:
    """Obtém o papel da Ouvidoria ativo pelo código."""
    return session.scalar(
        select(RoleModel).where(
            RoleModel.codigo == ROLE_CODIGO,
            RoleModel.deleted_at.is_(None),
        )
    )
def criar_usuario_teste(session: Session) -> dict[str, object]:
    """
    Cria o usuário de teste e vincula-o à ROLE_OUVIDOR.

    Não realiza commit; o controle transacional pertence ao chamador.

    Retorna um resumo com:
        usuario_criado      bool
        vinculo_criado      bool
        senha_gerada        str (apenas se o usuário foi criado)
        usuario_id          str
        senha_hash          str
    """
    role = _obter_role(session)

    if role is None:
        raise SystemExit(
            f"Papel {ROLE_CODIGO} não encontrado. "
            "Execute antes: .venv/bin/python scripts/seed_idn.py"
        )

    usuario = _obter_usuario(session)
    senha_gerada = ""

    if usuario is None:
        # Valida o formato antes de gerar o hash.
        Senha(SENHA_PADRAO)

        senha_gerada = SENHA_PADRAO
        usuario = UsuarioModel(
            login=LOGIN,
            email=EMAIL,
            nome=NOME,
            status="ativo",
            senha_hash=AutenticacaoService.criar_hash_senha(SENHA_PADRAO),
            unidades_ids="",
        )
        session.add(usuario)
        session.flush()

    usuario_criado = senha_gerada != ""

    # Verifica se o vínculo já existe.
    vinculo_existente = session.scalar(
        select(UsuarioRoleModel).where(
            UsuarioRoleModel.usuario_id == usuario.id,
            UsuarioRoleModel.role_id == role.id,
        )
    )

    vinculo_criado = False

    if vinculo_existente is None:
        session.add(UsuarioRoleModel(usuario_id=usuario.id, role_id=role.id))
        session.flush()
        vinculo_criado = True

    return {
        "usuario_criado": usuario_criado,
        "vinculo_criado": vinculo_criado,
        "senha_gerada": senha_gerada,
        "usuario_id": str(usuario.id),
        "senha_hash": usuario.senha_hash,
    }
def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cria usuário de teste da Ouvidoria (ROLE_OUVIDOR)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Executa sem confirmar alterações (rollback ao final).",
    )
    args = parser.parse_args()

    with SessionLocal() as session:
        try:
            resultado = criar_usuario_teste(session)

            if args.dry_run:
                session.rollback()
                print("[dry-run] Alterações revertidas (nenhum dado gravado).")
            else:
                session.commit()
                print("Usuário de teste da Ouvidoria aplicado com sucesso.")

            print(f"  Login:                  {LOGIN}")
            print(f"  Nome:                   {NOME}")
            print(f"  Papel vinculado:        {ROLE_CODIGO}")
            print(f"  Usuário criado:         {resultado['usuario_criado']}")
            print(f"  Vínculo criado:         {resultado['vinculo_criado']}")

            if resultado["senha_gerada"]:
                print()
                print("  SENHA (exibida apenas nesta criacao):")
                print(f"    {resultado['senha_gerada']}")
            else:
                print(f"  Senha (hash):           {resultado['senha_hash']}")

            if not resultado["usuario_criado"] and not resultado["vinculo_criado"]:
                print()
                print("  Nada a fazer — usuario e vinculo ja existiam.")

            return 0

        except Exception as exc:  # noqa: BLE001
            session.rollback()
            print(f"Erro ao criar usuario de teste: {exc}", file=sys.stderr)
            return 1


if __name__ == "__main__":
    raise SystemExit(main())
